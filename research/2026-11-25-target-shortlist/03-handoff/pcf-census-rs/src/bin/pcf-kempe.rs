// Rust port of 03-handoff/pcf-kempe-census.js on the 4-regular strata.
// For every labelled representative of a connected K4-free quartic graph of the
// given orders, enumerate every proper 5-colouring with at most two defective
// vertices (normalised by first appearance), and check by breadth-first search
// that every state with at most CAP defects (CAP = 1, 2) is joined to a PCF
// colouring by simultaneous Kempe swaps (any proper subset of the components
// of one colour pair) through states with at most CAP defects.
// Usage: pcf-kempe FIRST LAST
use std::collections::HashMap;

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


fn low_defect_states(nbrs: &[Vec<usize>]) -> HashMap<u64, (Vec<u8>, u8)> {
    let order = nbrs.len();
    let mut last_at: Vec<Vec<usize>> = vec![Vec::new(); order];
    for (c, row) in nbrs.iter().enumerate() {
        last_at[*row.iter().max().unwrap()].push(c);
    }
    let previous: Vec<Vec<usize>> = nbrs.iter().enumerate().map(|(v, r)| r.iter().cloned().filter(|&o| o < v).collect()).collect();
    let mut colours = vec![0u8; order];
    let mut states = HashMap::new();
    fn rec(v: usize, used: usize, defects: u8, code: u64, nbrs: &[Vec<usize>], prev: &[Vec<usize>], last_at: &[Vec<usize>], colours: &mut Vec<u8>, states: &mut HashMap<u64, (Vec<u8>, u8)>) {
        if v == nbrs.len() {
            states.insert(code, (colours.clone(), defects));
            return;
        }
        let mut excluded = 0u32;
        for &o in &prev[v] { excluded |= 1 << colours[o]; }
        for colour in 0..=used.min(4) {
            if excluded & (1 << colour) != 0 { continue; }
            colours[v] = colour as u8;
            let mut count = defects;
            for &c in &last_at[v] {
                let mut parity = 0u32;
                for &n in &nbrs[c] { parity ^= 1 << colours[n]; }
                if parity == 0 { count += 1; }
            }
            if count <= 2 {
                rec(v + 1, used.max(colour + 1), count, 5 * code + colour as u64, nbrs, prev, last_at, colours, states);
            }
        }
    }
    rec(0, 0, 0, 0, nbrs, &previous, &last_at, &mut colours, &mut states);
    states
}

fn normalize(colours: &[u8]) -> u64 {
    let mut renamed = [255u8; 5];
    let mut used = 0u8;
    let mut code = 0u64;
    for &c in colours {
        if renamed[c as usize] == 255 { renamed[c as usize] = used; used += 1; }
        code = 5 * code + renamed[c as usize] as u64;
    }
    code
}

fn kempe_moves(nbrs: &[Vec<usize>], colours: &[u8], out: &mut Vec<u64>) {
    out.clear();
    let order = colours.len();
    for a in 0u8..5 {
        for b in a + 1..5 {
            let mut comps: Vec<Vec<usize>> = Vec::new();
            let mut seen = vec![false; order];
            for v in 0..order {
                if seen[v] || (colours[v] != a && colours[v] != b) { continue; }
                let mut q = vec![v];
                seen[v] = true;
                let mut i = 0;
                while i < q.len() {
                    let x = q[i]; i += 1;
                    for &o in &nbrs[x] {
                        if !seen[o] && (colours[o] == a || colours[o] == b) { seen[o] = true; q.push(o); }
                    }
                }
                comps.push(q);
            }
            if comps.len() <= 1 { continue; }
            let k = comps.len() - 1;
            for mask in 1u64..(1u64 << k) {
                let mut next = colours.to_vec();
                for (i, comp) in comps.iter().enumerate() {
                    if i < 64 && mask & (1 << i) != 0 {
                        for &v in comp { next[v] = a + b - next[v]; }
                    }
                }
                out.push(normalize(&next));
            }
        }
    }
}

fn closure(nbrs: &[Vec<usize>], states: &HashMap<u64, (Vec<u8>, u8)>, cap: u8, report: u32) -> (u32, usize) {
    let mut reached: HashMap<u64, u32> = HashMap::new();
    let mut queue: Vec<u64> = Vec::new();
    for (k, s) in states { if s.1 == 0 { reached.insert(*k, 0); queue.push(*k); } }
    let mut maxd = 0;
    let mut i = 0;
    let mut moves = Vec::new();
    while i < queue.len() {
        let key = queue[i]; i += 1;
        let d = reached[&key] + 1;
        kempe_moves(nbrs, &states[&key].0, &mut moves);
        for &o in &moves {
            if reached.contains_key(&o) { continue; }
            if let Some(s) = states.get(&o) {
                if s.1 <= cap {
                    reached.insert(o, d); queue.push(o); maxd = maxd.max(d);
                    if report > 0 && d >= report {
                        println!("EXAMPLE cap {} distance {} defects {} nbrs {:?} colours {:?}", cap, d, s.1, nbrs, s.0);
                        std::process::exit(3);
                    }
                }
            }
        }
    }
    let missed = states.iter().filter(|(k, s)| s.1 <= cap && !reached.contains_key(k)).count();
    (maxd, missed)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let first: usize = args[1].parse().unwrap();
    let last: usize = args[2].parse().unwrap();
    for order in first..=last {
        let mut graphs = 0u64;
        let mut one = 0u64;
        let mut two = 0u64;
        let mut max1 = 0u32;
        let mut max2 = 0u32;
        enumerate(order, order, false, &mut |adj: &[u32]| {
            let nbrs: Vec<Vec<usize>> = adj.iter().map(|&m| bits(m)).collect();
            let states = low_defect_states(&nbrs);
            for s in states.values() { if s.1 == 1 { one += 1; } if s.1 == 2 { two += 1; } }
            for cap in [1u8, 2u8] {
                let report: u32 = std::env::var("PCF_REPORT_DISTANCE").ok().and_then(|v| v.parse().ok()).unwrap_or(0);
                let (maxd, missed) = closure(&nbrs, &states, cap, report);
                if missed > 0 {
                    let w = find_colouring(&nbrs, 5);
                    println!("MISSED order {} cap {} graph {} missed {} nbrs {:?} witness_ok {}", order, cap, graphs, missed, nbrs, verify_colouring(&nbrs, &w, 5));
                    std::process::exit(2);
                }
                if cap == 1 { max1 = max1.max(maxd); } else { max2 = max2.max(maxd); }
            }
            graphs += 1;
            if graphs % 10000 == 0 { eprintln!("order {} graphs {} max1 {} max2 {}", order, graphs, max1, max2); }
        });
        println!("{{\"complete\":true,\"order\":{},\"graphs\":{},\"oneDefectStates\":{},\"twoDefectStates\":{},\"maxDistanceAtOne\":{},\"maxDistanceAtTwo\":{}}}", order, graphs, one, two, max1, max2);
    }
}
