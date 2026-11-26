// Rust port of check_03_conflict_free_colouring.js (same generator, same
// prefix-normalised labelled cover, same colouring search and verifier).
// Usage: pcf-census FIRST LAST [--cubic-matching [QUARTIC_COUNT ...]]
use std::collections::HashSet;

struct Gen<'a> {
    order: usize,
    target: Vec<u32>,
    residual: Vec<i32>,
    adj: Vec<u32>,
    cubic_mask: u32,
    req: bool,
    visit: &'a mut dyn FnMut(&[u32]),
}

fn has_clique_after_adding(adj: &[u32], a: usize, b: usize) -> bool {
    let mut common = adj[a] & adj[b];
    while common != 0 {
        let low = common & common.wrapping_neg();
        common ^= low;
        if adj[low.trailing_zeros() as usize] & common != 0 {
            return true;
        }
    }
    false
}

fn is_connected(adj: &[u32]) -> bool {
    let mut reached: u32 = 1;
    let mut frontier: u32 = 1;
    while frontier != 0 {
        let low = frontier & frontier.wrapping_neg();
        frontier ^= low;
        let nb = adj[low.trailing_zeros() as usize];
        frontier |= nb & !reached;
        reached |= nb;
    }
    reached == ((1u32 << adj.len()) - 1)
}

impl<'a> Gen<'a> {
    fn add(&mut self, a: usize, b: usize) {
        self.adj[a] |= 1 << b;
        self.adj[b] |= 1 << a;
        self.residual[a] -= 1;
        self.residual[b] -= 1;
    }
    fn remove(&mut self, a: usize, b: usize) {
        self.adj[a] ^= 1 << b;
        self.adj[b] ^= 1 << a;
        self.residual[a] += 1;
        self.residual[b] += 1;
    }
    fn complete_from(&mut self, mut vertex: usize) {
        while vertex < self.order && self.residual[vertex] == 0 {
            vertex += 1;
        }
        if vertex == self.order {
            if is_connected(&self.adj) {
                (self.visit)(&self.adj);
            }
            return;
        }
        let mut available: u32 = 0;
        for other in vertex + 1..self.order {
            if self.residual[other] > 0 {
                available |= 1 << other;
            }
        }
        let available_count = available.count_ones() as i32;
        if self.residual[vertex] > available_count {
            return;
        }
        let earlier: u32 = (1u32 << vertex) - 1;
        let mut groups: Vec<(u32, u32)> = Vec::new();
        let mut rest = available;
        while rest != 0 {
            let low = rest & rest.wrapping_neg();
            rest ^= low;
            let other = low.trailing_zeros() as usize;
            if self.residual[other] > available_count {
                return;
            }
            let key = (self.target[other] << self.order) | (self.adj[other] & earlier);
            match groups.iter_mut().find(|g| g.0 == key) {
                Some(g) => g.1 |= 1 << other,
                None => groups.push((key, 1 << other)),
            }
        }
        self.choose(vertex, available, available_count, &groups);
    }
    fn choose(&mut self, vertex: usize, mut available: u32, mut remaining: i32, groups: &[(u32, u32)]) {
        if self.residual[vertex] == 0 {
            self.complete_from(vertex + 1);
            return;
        }
        while remaining >= self.residual[vertex] {
            let low = available & available.wrapping_neg();
            let other = low.trailing_zeros() as usize;
            available ^= low;
            remaining -= 1;
            let valid_cubic_edge = !self.req
                || self.target[vertex] == 4
                || self.target[other] == 4
                || ((self.adj[vertex] | self.adj[other]) & self.cubic_mask) == 0;
            if valid_cubic_edge && !has_clique_after_adding(&self.adj, vertex, other) {
                self.add(vertex, other);
                self.choose(vertex, available, remaining, groups);
                self.remove(vertex, other);
            }
            let key = (self.target[other] << self.order) | (self.adj[other] & ((1u32 << vertex) - 1));
            let gmask = groups.iter().find(|g| g.0 == key).map(|g| g.1).unwrap_or(0);
            let equivalent = available & gmask;
            available ^= equivalent;
            remaining -= equivalent.count_ones() as i32;
        }
    }
}

fn enumerate(order: usize, degree_four: usize, req: bool, visit: &mut dyn FnMut(&[u32])) {
    if (3 * order + degree_four) % 2 == 1 {
        return;
    }
    if req && order - degree_four > 2 * degree_four {
        return;
    }
    let target: Vec<u32> = (0..order).map(|v| if v < degree_four { 4 } else { 3 }).collect();
    let residual: Vec<i32> = target.iter().map(|&t| t as i32).collect();
    let cubic_mask = ((1u32 << order) - 1) ^ ((1u32 << degree_four) - 1);
    let mut g = Gen { order, target, residual, adj: vec![0; order], cubic_mask, req, visit };
    for nb4 in 0..=4usize {
        let nb3 = 4 - nb4;
        if nb4 >= degree_four || nb3 > order - degree_four {
            continue;
        }
        let mut nbrs = Vec::new();
        for v in 1..=nb4 {
            nbrs.push(v);
        }
        for v in degree_four..degree_four + nb3 {
            nbrs.push(v);
        }
        for &n in &nbrs {
            g.add(0, n);
        }
        g.complete_from(1);
        for &n in &nbrs {
            g.remove(0, n);
        }
    }
}

fn bits(mask: u32) -> Vec<usize> {
    let mut r = Vec::new();
    let mut m = mask;
    while m != 0 {
        let low = m & m.wrapping_neg();
        r.push(low.trailing_zeros() as usize);
        m ^= low;
    }
    r
}

fn find_colouring(nbrs: &[Vec<usize>], palette: usize) -> Option<Vec<i8>> {
    let order = nbrs.len();
    let mut colours = vec![-1i8; order];
    let mut checks: Vec<Vec<usize>> = vec![Vec::new(); order];
    for (v, nb) in nbrs.iter().enumerate() {
        if let Some(&last) = nb.last() {
            checks[last].push(v);
        }
    }
    fn visit(vertex: usize, used: usize, nbrs: &[Vec<usize>], checks: &[Vec<usize>], colours: &mut Vec<i8>, palette: usize) -> bool {
        let order = nbrs.len();
        if vertex == order {
            return true;
        }
        let mut forbidden: u32 = 0;
        for &o in &nbrs[vertex] {
            if o < vertex {
                forbidden |= 1 << colours[o];
            }
        }
        let choices: u32 = ((1u32 << (used + 1).min(palette)) - 1) & !forbidden;
        let mut rem = choices;
        while rem != 0 {
            let low = rem & rem.wrapping_neg();
            rem &= rem - 1;
            let colour = low.trailing_zeros() as usize;
            colours[vertex] = colour as i8;
            let mut valid = true;
            for &w in &checks[vertex] {
                let mut present: u32 = 0;
                let mut repeated: u32 = 0;
                for &o in &nbrs[w] {
                    let bit = 1u32 << colours[o];
                    repeated |= present & bit;
                    present |= bit;
                }
                if present & !repeated == 0 {
                    valid = false;
                    break;
                }
            }
            if valid && visit(vertex + 1, used.max(colour + 1), nbrs, checks, colours, palette) {
                return true;
            }
        }
        colours[vertex] = -1;
        false
    }
    if visit(0, 0, nbrs, &checks, &mut colours, palette) {
        Some(colours)
    } else {
        None
    }
}

fn verify_colouring(nbrs: &[Vec<usize>], colours: &Option<Vec<i8>>, palette: usize) -> bool {
    let colours = match colours {
        Some(c) => c,
        None => return false,
    };
    if colours.len() != nbrs.len() {
        return false;
    }
    for (v, nb) in nbrs.iter().enumerate() {
        let c = colours[v];
        if c < 0 || c as usize >= palette {
            return false;
        }
        let mut mult = vec![0u8; palette];
        for &o in nb {
            if colours[o] == c {
                return false;
            }
            mult[colours[o] as usize] += 1;
        }
        if !nb.is_empty() && !mult.contains(&1) {
            return false;
        }
    }
    true
}

fn check_examples() {
    let c5: Vec<Vec<usize>> = vec![vec![1, 4], vec![0, 2], vec![1, 3], vec![2, 4], vec![0, 3]];
    let k5: Vec<Vec<usize>> = (0..5).map(|i| (0..5).filter(|&j| j != i).collect()).collect();
    let oct: Vec<Vec<usize>> = (0..6).map(|i| (0..6).filter(|&j| (j >> 1) != (i >> 1)).collect()).collect();
    for g in [c5, k5, oct] {
        if find_colouring(&g, 4).is_some() || !verify_colouring(&g, &find_colouring(&g, 5), 5) {
            panic!("Example check failed");
        }
    }
}

fn check_generator() {
    for order in [5usize, 6] {
        let mut edges = Vec::new();
        for a in 0..order {
            for b in a + 1..order {
                edges.push((a, b));
            }
        }
        let mut brute: HashSet<Vec<u32>> = HashSet::new();
        let mut brute_cm: HashSet<Vec<u32>> = HashSet::new();
        for subset in 0u32..(1u32 << edges.len()) {
            let mut adj = vec![0u32; order];
            for (e, &(a, b)) in edges.iter().enumerate() {
                if subset & (1 << e) != 0 {
                    adj[a] |= 1 << b;
                    adj[b] |= 1 << a;
                }
            }
            let deg: Vec<u32> = adj.iter().map(|m| m.count_ones()).collect();
            if deg[0] != 4 {
                continue;
            }
            if (0..order).any(|v| deg[v] < 3 || deg[v] > 4 || (v > 0 && deg[v] > deg[v - 1])) {
                continue;
            }
            if !is_connected(&adj) {
                continue;
            }
            let mut valid = true;
            'outer: for right in 1..order {
                for left in 0..right {
                    if deg[left] != deg[right] {
                        continue;
                    }
                    for row in 0..left {
                        let hl = adj[row] & (1 << left) != 0;
                        let hr = adj[row] & (1 << right) != 0;
                        if hl == hr {
                            continue;
                        }
                        valid = hl;
                        break;
                    }
                    if !valid {
                        break 'outer;
                    }
                }
            }
            if !valid {
                continue;
            }
            let mut clique = false;
            for a in 0..order {
                for b in a + 1..order {
                    if adj[a] & (1 << b) == 0 {
                        continue;
                    }
                    for c in b + 1..order {
                        if adj[a] & (1 << c) == 0 || adj[b] & (1 << c) == 0 {
                            continue;
                        }
                        for d in c + 1..order {
                            if [a, b, c].iter().all(|&v| adj[v] & (1 << d) != 0) {
                                clique = true;
                            }
                        }
                    }
                }
            }
            if !clique {
                brute.insert(adj.clone());
                let cm_ok = (0..order).all(|v| {
                    deg[v] == 4 || bits(adj[v]).iter().filter(|&&u| deg[u] == 3).count() <= 1
                });
                if cm_ok {
                    brute_cm.insert(adj.clone());
                }
            }
        }
        for d4 in 1..=order {
            enumerate(order, d4, false, &mut |adj: &[u32]| {
                if !brute.remove(adj) {
                    panic!("Unexpected or repeated representative");
                }
            });
            enumerate(order, d4, true, &mut |adj: &[u32]| {
                if !brute_cm.remove(adj) {
                    panic!("Unexpected or repeated filtered representative");
                }
            });
        }
        if !brute.is_empty() || !brute_cm.is_empty() {
            panic!("Generator omitted representatives");
        }
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let first: usize = args.get(1).map(|s| s.parse().unwrap()).unwrap_or(5);
    let last: usize = args.get(2).map(|s| s.parse().unwrap()).unwrap_or(11);
    let cubic_matching = args.get(3).map(|s| s == "--cubic-matching").unwrap_or(false);
    if args.len() > 3 && !cubic_matching {
        panic!("third argument must be --cubic-matching");
    }
    let requested: Vec<usize> = args.iter().skip(4).map(|s| s.parse().unwrap()).collect();
    assert!(first >= 5 && last >= first && last <= 15);
    check_examples();
    check_generator();
    eprintln!("examples and generator cross-check passed");
    for order in first..=last {
        let mut by = Vec::new();
        for d4 in 1..=order {
            if !requested.is_empty() && !requested.contains(&d4) {
                continue;
            }
            let mut checked: u64 = 0;
            enumerate(order, d4, cubic_matching, &mut |adj: &[u32]| {
                let nbrs: Vec<Vec<usize>> = adj.iter().map(|&m| bits(m)).collect();
                if cubic_matching
                    && nbrs.iter().any(|row| row.len() == 3 && row.iter().filter(|&&v| nbrs[v].len() == 3).count() > 1)
                {
                    panic!("Cubic filter accepted a restricted representative");
                }
                let col = find_colouring(&nbrs, 5);
                if !verify_colouring(&nbrs, &col, 5) {
                    panic!("No verified colouring for {:?}", nbrs);
                }
                checked += 1;
                if checked % 10_000_000 == 0 {
                    eprintln!("{{\"order\":{},\"degreeFour\":{},\"progress\":{}}}", order, d4, checked);
                }
            });
            if checked > 0 {
                by.push((d4, checked));
            }
        }
        let total: u64 = by.iter().map(|x| x.1).sum();
        println!("{{\"order\":{},\"total\":{},\"byDegreeFour\":{:?}}}", order, total, by);
    }
}
