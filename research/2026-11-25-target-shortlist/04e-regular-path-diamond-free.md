# Diamond-free degree five: the second sweep

**Status: reviewed (independent referee: accept with fixes; fixes applied), computer-assisted; no Lean.** The referee's report is [04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md). Theorem B is not a resolution of Conjecture 1. Graphs that contain a diamond remain open.

**Theorem B.** Let \(G\) be a finite simple 5-regular graph with a perfect matching. Suppose \(G\) contains no diamond, that is, no two triangles share an edge. Then \(E(G)\) partitions into paths with exactly five edges.

**Scope.**

- Theorem B contains the Chu–Fan–Hong–Zhou 2024 theorem, whose hypothesis is that no triangle shares an edge with a 4-cycle. A diamond is a 4-cycle that shares edges with its two triangles, so those graphs are diamond-free.
- It also contains the Botler–Mota–Wakabayashi triangle-free theorem, and the **existence part** of the Favaron–Genest–Kouider (FGK) results for \(C_4\)-free graphs and for graphs in which no 4-cycle shares an edge with a triangle or with another 4-cycle, given a perfect matching. All these classes are diamond-free.
- FGK prove more for their classes: every 1-factor is *extendable*, that is, it is the middle-edge set of some decomposition. Theorem B gives only the existence of a decomposition. Its middle edges need not be the edges of \(M\). This is the same distinction as in 04d, Corollary 1.
- Theorem B is incomparable with the matching-relative Theorem A of [04d](04d-regular-path-matching-relative-theorem.md). Theorem A allows diamonds that avoid a suitable matching. Theorem B allows triangles that share edges with chordless 4-cycles through the matching.
- Every perfect matching \(M\) works. The proof is algorithmic.
- **Novelty (bounded search).** The FGK 2010 full text has been read; see [04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md) and 04d. None of the FGK results recorded there is the diamond-free case. Their Theorems 6–7 are matching-relative extendability results under FGK's own bad-pair hypothesis, and their graph-level classes are subclasses of the diamond-free graphs. The referee's bounded search of 2026-11-25 ([04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md), §5) found no source that states Theorem B. This is a bounded search, not a certificate.

**Structure of the proof.**

- The 04d construction and sweep, with Proposition B, leave only *G-configurations*.
- A *second sweep* repairs them using four local rules, chosen by a case split.
- Each repaired piece belongs to one of finitely many *windows*. A window lists named vertices, the incidences \(r(x)=y\), \(s(x)=y\), \(m(x)=y\) that hold among them, and some inequalities.
- An exhaustive engine enumerates **every** identification of the named vertices compatible with the axioms, and checks the window's pieces in each one. The axioms are injective \(r,s\), the involution \(m\), disjoint edge classes, (P2), (P3) and diamond-freeness of the known edges.
- A window's facts are true consequences of its case, but they need not be all the facts. The enumeration is therefore a superset of the realizable configurations, and a pass is sound.
- The only other computer step is an extension of Lemma 4 of 04d.

## 1. Setting

Notation is as in 04d. The maps \(r,s\) are fixed-point-free permutations with properties (P1)–(P3), and \(m\) is the mate map. The canonical trail is \(\tau(uv)=(s(r(u)),r(u),u,v,r(v),s(r(v)))\). A defective trail is labelled \((a,b,c,d,e,b)\), where \(cd\in M\), \(b=r(c)\), \(e=r(d)\), \(a=s(b)\) and \(s(e)=b\).

Only (P1)–(P3) are used; Lemma 1's pairing is never used. The first sweep is Section 2 of 04d, with sources, recipients and the odd-cycle replacement of Section 3. Below, the second sweep also changes which sources trade. Removing a source's trade never invalidates Lemma 3, whose cases are per end and per pendant.

**Proposition B (04d).** If \(G\) is diamond-free, then after the first sweep every piece is a simple path except the G-configurations.

A *G-configuration* has an apex \(c\) and comes from a source \(T=\tau(cd)\) with a type-0 link, where
\[
f=r^{-1}(c),\qquad b=r(c)=m(f),\qquad h=r(b).
\]
Its target \(Q_c=\tau(fb)=(s(c),c,f,b,h,s(h))\) is not defective, and after the trade it becomes
\[
Q'_c=(b,c,f,b,h,Y),\qquad Y\in\{s(h),\ r(h)\}.
\]
Here \(Y=r(h)\) exactly when a source with \(c\)-label \(h\) traded with \(Q_c\).

## 2. Partners

For a G-configuration \(c\), put \(p=r^{-1}(f)\) and \(q=m(p)\). Let \(W_0=\tau(pq)\) be the canonical trail in which \(f\) is a red head. The *partner edge* is \(\varepsilon_c=\{f,s(f)\}\in S\). Write \(g=s(f)\).

**Lemma 5.**

- (i) The first sweep never moves \(\varepsilon_c\).
- (ii) Exactly one of the following cases holds.
  - (α) \(W_0\) is not defective. Then \(\varepsilon_c\) is the terminal edge at the \(f\)-end of \(W_0\)'s piece \(P=(g,f,p,q,u,Z)\), where \(u=r(q)\).
  - (β) \(W_0\) is defective with \(b'=f\). Then \(W_0=(g,f,p,q,u,f)\), with \(u=r(q)\) and \(s(u)=f\). No type-1 trade changes its pendant.
  - (γ) \(W_0\) is defective with \(e'=f\). Then \(W_0=(s(g),g,q,p,f,g)\), with \(g=s(f)=r(q)\). Also \(W_0\) has no incoming type-2 link and lies on no type-2 cycle, so it is a source in the first sweep.
- (iii) \(W_0\ne T\), and \(c\ne q\).

*Proof.*

- (i) A source with \(c\)-label \(x\) takes \(\{x,s(x)\}\). Equality with \(\varepsilon_c\) needs \(x=f\) or \(x=g\) with \(s(g)=f\). If \(x=f\), the source is \(\tau(f\,m(f))=Q_c\), which is not defective. The case \(x=g\) with \(s(g)=f\) violates (P2).
- (ii) The red heads of \((a',b',c',d',e',b')\) are \(b'\) and \(e'\).
  - In case (α), only a source with \(c\)-label \(f\), namely \(Q_c\), could change the \(f\)-end.
  - In case (β), a type-1 trade into \(W_0\) needs a source with \(c\)-label \(b'=f\), again \(Q_c\).
  - In case (γ), an incoming type-2 link needs a source with \(c\)-label \(e'=f\), again \(Q_c\). Trails on type-2 cycles have incoming links.
  - Cases (β) and (γ) together would give \(s(u)=f\) and \(s(f)=u\), violating (P2).
- (iii) Suppose \(\{p,q\}=\{c,d\}\). If \(p=c\), then \(f=r(c)=b\). If \(p=d\), then \(f=r(d)=e\), so \(s(f)=s(e)=b=m(f)\). Both are impossible. Finally, \(c=q\) gives \(d=p\), the same case. \(\square\)

**Links.**

- *α-link \(c_3\to c\).* This holds when the α-partner piece of \(c_3\) is \(Q_c\). That happens exactly when \(h_c=f_{c_3}\). Then \(Y=s(h_c)\), since a received \(Y\) would mean the edge \(\{h,s(h)\}\) was taken by \(\tau(h\,m(h))=Q_{c_3}\), which is not defective.
  - The triangle end of \(Q_c\) has an \(R\)-edge terminal \(\{b,c\}\), so it is never a partner end.
  - Each piece therefore has at most two partner ends.
  - Pieces from defective trails are never α-partners, and \(Q_c\) is never a β- or γ-partner.
- *Gtarget edge \(c\to c^*\).* This holds when \(c\) is in case (γ), \(W_0\)'s link is type 0, and \(W_0=T_{c^*}\) is the source of a G-configuration \(c^*\) with apex \(q\). Both the in-degree and the out-degree are at most 1, because \(W_0\) determines \(f\) and hence \(c\).

## 3. The rules

- **G-rule (case α).** Replace \(Q'_c\) by \(Q^*_c=(g,f,c,b,h,Y^*)\). In \(P\), replace the terminal \(g\) by \(b\). This exchanges \(fb\in M\) with \(fg\in S\).
- **G-pendant (case β).** Before \(W_0\) is processed, exchange its pendant edge \(\{g,f\}\) with \(\{f,b\}\). Thus \(W_0=(b,f,p,q,u,f)\), with pendant \(b\), and \(Q_c\) becomes \(Q^*_c\).
  - The link structure is unchanged, since it does not involve pendants.
  - \(W_0\) is then processed as before, as a source, a recipient or a trail on an odd cycle.
- **Absorption (case γ).** \(W_0\) does not trade. It receives \(fb\) in place of its closing edge \(fg\), so \(W_0\) becomes \((A^*,g,q,p,f,b)\) and \(Q_c\) becomes \(Q^*_c\).
  - The target \(X\) of \(W_0\) simply does not receive \(W_0\)'s trade.
  - Absorption is used when \(W_0\)'s link is type 1, or type 0 with a target that is not a G-configuration. Neither case changes any type-2 alternation, and neither changes the set of G-configurations.
- **Γ-rule (case γ, \(W_0\) kept as a source).** The source piece is \(W=(A',g,f,p,q,s(q))\).
  - Replace \(Q'_c,W\) by \(N_1=(s(q),q,p,f,c,b)\) and \(N_2=(Y^*,h,b,f,g,A')\).
  - If \(A'=h\), use **Γ′** instead: \((Y^*,h,g,f,c,b)\) and \((h,b,f,p,q,s(q))\). Here the edge \(\{h,g\}\) is \(W\)'s pendant edge, and it becomes an interior edge.
  - Γ′ is used only with the plain pendant \(A'=s(g)=h\). For a changed pendant \(r(g)\) or a G-pendant \(m(g)\), the equality \(A'=h\) is impossible: windows W6 and W7 allow no alternative and no excluded case for these pendants, so their 0 failures mean that \(N_2=(Y^*,h,b,f,g,A')\) is simple, hence \(A'\ne h\), in every identification. (At a Gtarget node the pendant is always plain, by Lemma 8, Step 4.)
- **Gtarget resolution.** The Gtarget edges form a functional graph made of paths and cycles.
  - *Absorbing.* An existing configuration \(c\) may absorb \(W_0=T_{c^*}\). This cancels \(c^*\): \(T_{c^*}\) does not trade, and \(Q_{c^*}\) stays canonical at its \(c^*\)-end.
  - *Paths and even cycles.* On a path, the first configuration exists, and existing and cancelled configurations alternate. Even cycles alternate in the same way.
  - *Odd cycles.* Choose a node \(j\) at which the Γ-rules are valid, and apply Γ/Γ′ there. Absorption then alternates from \(j+1\) around the cycle.
  - *Validity criterion.* By window W7, the Γ-rules are valid at \(j\) unless both of the following hold:
    - (F1): \(s(q_j)=c_j\);
    - the pendant \(s(g_j)\) differs from \(h_j\).
  - *Rotation.* If every node fails, apply the **rotation**
    \[
    R_k=(b_k,c_k,f_k,p_k,c_{k+1},c_{k+2}),\qquad P_k=(Y^*_k,h_k,b_k,f_k,b_{k+1},A'_k).
    \]
    Under (F1) at every node, the pieces \(Q'_k\) and \(W_k=(A'_k,b_{k+1},f_k,p_k,c_{k+1},c_k)\) of the cycle are re-partitioned by \(\{R_k,P_k\}\). This holds around the whole cycle, not for each pair separately; see the telescoping argument in the proof of Theorem B.
- **The terminal \(Y^*\).** \(Y^*\) is \(b_{c_3}\) if an α-link \(c_3\to c\) exists, and \(Y\) otherwise.
- **Interfaces.**
  - The edge \(\{h,Y^*\}\) is terminal, with \(h\) next to the end, in every piece built from \(Q_c\): \(Q^*_c\), \(N_2\), the first Γ′ piece and \(P_k\). So the α-rule of \(c_3\), which acts only on that terminal, is compatible with every rule of \(c\).
  - The pendant edge \(\{g,A'\}\) of \(W\) is terminal in \(N_2\), with \(g\) next to the end. It is **not** terminal in Γ′, where it is the interior edge \(\{h,g\}\). This causes no conflict, because Γ′ is used only with the plain pendant \(A'=s(g)\) (see the Γ-rule). A plain pendant edge is moved by no other rule: a G-pendant at \(g\) would have replaced it, so \(A'\) would not be plain, and it is not the α-partner edge \(\{h,s(h)\}\) of a link at \(h\), since \(s(g)=h\) and \(s(h)=g\) would violate (P2).
  - The G-pendant is applied before \(W_0\) is processed, so \(A'\) and \(A^*\) already include it.
  - All rules are applied simultaneously. By Lemma 8, rules acting on the same piece act at different ends.
- **Odd type-2 cycles with G-pendants.**

  Let \(T_i\) on an odd type-2 cycle be the β-partner of a G-configuration \(c\). Then \(f=b_i\), the apex is \(c=r(b_i)\), and the G-pendant is \(b=r(c)=m(b_i)\).

  **Lemma 7.**
  - (a) A G-pendant \(m(b_i)\) on an odd cycle is not a local \(b\)-, \(c\)-, \(d\)- or \(e\)-label.
  - (b) A G-pendant \(m(b_i)\) never equals a changed pendant \(r(b_k)\).

  *Proof.*
  - (a), \(c\)-label. Suppose \(m(b_i)=c_j\), that is, \(b_i=d_j\). Then \(c=r(b_i)=r(d_j)=e_j=c_{j-1}\), and \(b=r(c)=b_{j-1}\). Also \(b=m(b_i)=m(d_j)=c_j\), so \(b_{j-1}=c_j\), contrary to (o2).
  - (a), \(d\)-label. The equality \(m(b_i)=d_j\) means \(b_i=c_j\), contrary to (o2).
  - (a), \(b\)-label. Suppose \(m(b_i)=b_j\). Then \(r(c)=b=b_j=r(c_j)\), so \(c=c_j\). Hence the source of the configuration is \(T_c=\tau(c\,m(c))=\tau(c_jd_j)=T_j\), which lies on the odd cycle. But \(T_c\) is a source, and trails on odd type-2 cycles are never sources.
  - (a), \(e\)-label. Since \(e_j=c_{j-1}\), an \(e\)-label is a \(c\)-label.
  - (b) Suppose \(m(b_i)=r(b_k)\), where the pendant of \(T_k\) was changed by an external type-1 source \(T''\) with \(c\)-label \(b_k\). Then \(r(c)=b=r(b_k)\), so \(c=b_k\). The trail with \(c\)-label \(b_k\) is unique, namely \(\tau(b_k\,m(b_k))\), so \(T_c=T''\). But \(T''\) has a type-1 link into the defective trail \(T_k\), while \(T_c\) has a type-0 link into the non-defective trail \(Q_c\). This is a contradiction. \(\square\)

  Hence a G-pendant is either a fresh vertex or equal to the unchanged pendant of another trail, and that unchanged pendant is itself fresh. By (a), it is not a local label, and by (b) it is not a changed pendant. Distinct G-pendants differ, since \(m\) is injective and the \(b_i\) are distinct. The label scheme of `odd_triples_with_g_pendants()` encodes exactly these facts. Pairs and rotations stay simple. Rotations never contain G-pendants, since in that case every pendant is a \(d\)-label.

  **Lemma 4′.** This is Lemma 4 with G-pendants allowed. Its computer check is `odd_triples_with_g_pendants()`. It finds 205 closed and 548 open simple covers, plus 12 open exceptions with \(d_1\in\{A_0,A_2\}\), and 243 cases are excluded by local diamonds. The completion argument of 04d is then unchanged.

## 4. Windows

By Lemma 8 below, every final piece is one of the following.

1. An unaffected first-sweep piece. Such a piece may have lost a trade through absorption or cancellation. It is simple by Lemma 3 and Proposition B, or by Lemma 4 on an odd type-2 cycle.
2. One of the windows below.

All windows are checked by [check_regular_path_gsweep.py](check_regular_path_gsweep.py).

| Window | Pieces | Options | Result |
|---|---|---|---|
| W1 | \(Q^*_c\), case α or β | \(Y^*\in\{s(h),r(h),b_{c_3}\}\) | 0 failures |
| W2 | \(Q^*_c\), case γ, absorbed | \(Y^*\) as in W1. When received or linked, the source is not \(W_0\) | 0 failures |
| W3 | \(P^*=(b,f,p,q,u,Z^*)\), case α | \(Z^*\in\{s(u),r(u),b_{c_2}\}\); a received \(r(u)\ne p\) (window facts) | 0 failures |
| W4 | β source piece \((b,f,u,q,p,s(p))\) and recipient piece \((b,f,p,q,u,r(u))\) | — | 0 failures |
| W5 | Absorbed \((A^*,g,q,p,f,b)\) | \(A^*\in\{s(g),r(g),m(g)\}\) | 0 failures |
| W6 | Γ/Γ′, link type 2 | \(Y^*\times A'\) | 0 failures |
| W7 | Γ/Γ′, Gtarget at an odd-cycle node | \(Y^*\times A'\) | Valid unless (F1) holds and \(A'\ne h\) |
| W8 | Rotation \(R_k\) and \(P_k\) | Three consecutive nodes for \(R_k\). Two nodes and \(Y^*\) options for \(P_k\) | 0 failures |
| L4′ | Odd-cycle triples with G-pendants | — | Exception only for an open block with \(d_1\in\{A_0,A_2\}\) |

**Window facts.** Each fact is a consequence of its case.

- **G-configuration.** \(m(c)=d\), \(r(c)=b\), \(r(d)=e\), \(s(e)=b\), \(s(b)=a\), \(r(f)=c\), \(m(f)=b\), \(r(b)=h\) and \(s(f)=g\). Also \(Q_c\) is not defective: \(s(c)\ne h\) and \(s(h)\ne c\).
- **Received end at \(x\).** A source with \(c\)-label \(x\) is defective: \(r(x)=b_*\), \(m(x)=d_*\), \(r(d_*)=e_*\) and \(s(e_*)=b_*\).
- **Linked configuration at \(x\).** \(r(x)=c'\), \(r(c')=b'=m(x)\), and the source \(\tau(c'm(c'))\) is defective.
- **Case α.** \(g\ne u\) and \(s(u)\ne f\).
- **Case α, received far end (W3).** If \(Z=r(u)\) is received, then \(Z\ne p\). Suppose \(Z=r(u)=p\). The source that gave \(Z\) is \(\tau(u\,m(u))\). Its \(f\)-vertex is \(r^{-1}(u)=q\), and \(m(q)=p=r(u)\). So that source is the source of a G-configuration with apex \(u\), \(f_u=q\), \(b_u=p\) and \(h_u=r(p)=f\), and it trades. Then \(W_0=\tau(qp)=Q_u\), and the \(f\)-end of \(W_0\) is the \(h\)-end of \(Q_u\). So \(c\to u\) is an α-link, and the piece is \(Q^*_u\) with \(Y^*=b_c\), which is checked by W1.
- **Case β.** \(s(u)=f\).
- **Case γ.** \(g=u\).
- **Type-2 link.** \(X=(a_X,b_X,c_X,d_X,q,b_X)\), so \(r(d_X)=q\), \(m(d_X)=c_X\) and \(r(c_X)=s(q)\). Moreover \(q\ne e\): otherwise \(X=T\) would be the recipient of the source \(W_0\), but \(T\) is a source.
- **Gtarget.** \(r(f_*)=q\), \(m(f_*)=g\), and \(\tau(f_*g)\) is not defective. At an odd-cycle node, \(c^*\) is in case γ, so the configuration linked at \(h\) is not \(c^*\).
  - In this case a changed or G-pendant \(A'\) is impossible: the engine finds 0 identifications. Lemma 8, Step 4, proves this by hand: the pendant of every \(T_{c^*}\) is plain.
- **Rotation.** Consecutive nodes satisfy \(e_{k+1}=f_k\), \(b_{k+1}=g_k\) and (F1) \(s(c_{k+1})=c_k\). Also \(A'_k\ne h_k\), since otherwise Γ′ applies.

**Lemma 8 (Classification of final pieces).** Call a G-configuration *surviving* if it is not cancelled. Only surviving configurations apply rules. After the second sweep, every piece is of one of the following kinds.

- (K1) A first-sweep piece that no second-sweep rule changes, except that it may have lost a received trade or a changed pendant through absorption or cancellation. It is simple by Lemma 3 and Proposition B, or by Lemma 4 on an odd type-2 cycle.
- (K2) The piece built from \(Q_c\) for a surviving configuration \(c\). It is \(Q^*_c\) in case α or β (W1), \(Q^*_c\) in case γ with absorption (W2), \(N_1\), \(N_2\) or a Γ′ piece (W6, W7), or \(R_k\), \(P_k\) (W8). Its \(h\)-end terminal is plain \(s(h)\), received \(r(h)\) or α-linked \(b_{c_3}\).
- (K3) A non-defective α-partner piece \(P^*=(b,f,p,q,u,Z^*)\) that is not \(Q_{c'}\) of a surviving configuration (W3). Its far end \(Z^*\) is plain \(s(u)\), received \(r(u)\) with \(r(u)\ne p\), or α-linked \(b_{c_2}\).
- (K4) The piece of a β-partner \(W_0\) that is not the γ-partner of a surviving configuration. It is a source or recipient piece (W4), or a piece of an odd type-2 cycle (Lemma 7 and Lemma 4′).
- (K5) The piece of the γ-partner \(W_0\) of a surviving configuration. It is absorbed (W5), a Γ or Γ′ piece (W6, W7), or a rotation piece (W8). Its pendant is plain \(s(g)\), changed \(r(g)\) or a G-pendant \(m(g)\). The G-pendant occurs exactly when \(W_0\) is also a β-partner.

*Proof.*

*Step 1: one configuration per \(T\), per \(f\) and per \(Q\).* The apex \(c\) is the \(c\)-label of \(T_c\), and \(c=r(f)\). So \(T_c\) and \(f\) each determine \(c\). The red heads of \(Q_c=\tau(fb)\) are \(c\) and \(h\). Suppose a configuration \(c'\ne c\) has \(Q_{c'}=Q_c\). Then \(c'=h\), \(f'=r^{-1}(h)=b\) and \(b'=m(b)=f=r(h)\). The triangles \(bcf\) and \(bhf\) share \(fb\), which is a diamond.

*Step 2: ends of non-defective trails.* Let \(N\) be a non-defective canonical trail and \(x\) one of its red heads, so its terminal edge at \(x\) is \(\{x,s(x)\}\). Put \(D_x=\tau(x\,m(x))\). Apart from the own rule of \(c\) when \(N=Q_c\), only two things can change the end \(x\).

- The trade of \(D_x\), when \(D_x\) is a defective source with \(c\)-label \(x\). Then \(x\) is a *received end*. The trade may later be removed by absorption or cancellation, which restores the plain terminal \(s(x)\).
- The α-rule of the configuration \(c'=r(x)\), when \(c'\) is surviving, in case α, and \(f'=x\). Then \(x\) is an *α-partner end*, and \(D_x=\tau(f'b')=Q_{c'}\) is not defective.

The trail \(D_x\) cannot be both defective and non-defective, so **no end is both received and an α-partner end.** This holds at every end, not only at the \(h\)-end of \(Q_c\), and it is the content of Lemma 5(i). Each end is an α-partner end of at most one configuration, namely \(r(x)\). Three consequences follow.

- The triangle end \(c\) of \(Q_c\) is received from \(T_c\), so it is never a partner end. Hence \(Q_c\) is an α-partner only at its \(h\)-end.
- In case α, the \(f\)-end of \(W_0\) is not received, so \(P\) has the terminal \(g\) there.
- For a cancelled \(c^*\), the \(c^*\)-end of \(Q_{c^*}\) is plain. It is not received, since \(T_{c^*}\) does not trade, and it is not a partner end, since \(D_{c^*}=T_{c^*}\) is defective.

The first sweep never moves a partner edge (Lemma 5(i)). In particular, the terminal edge \(\{q,s(q)\}\) of the Γ-rule source piece \(W\) was moved there by the trade of \(W_0\), so it is not a partner edge \(\varepsilon_{c'}=\{f',s(f')\}\), and \(W\) has no partner end other than its pendant end. Directly, there are two orientations.

- If \(f'=q\), then \(c'=r(q)=g\) and \(b'=m(q)=p=r(g)\). So \(gp\) is a chord of the 4-cycle \((g,q,p,f)\), whose edges \(gq,qp,pf,fg\) lie in \(R,M,R,S\). The triangles \(gqp\) and \(gpf\) share \(gp\), which is a diamond.
- If \(s(f')=q\) and \(f'=s(q)\), then \(s(s(q))=q\), contrary to (P2).

*Step 3: defective trails.* Let \(D=(a',b',c',d',e',b')\) be defective. Its red heads are \(b'\) and \(e'\).

- \(D\) is never an α-partner.
- \(D\) is the β-partner of at most one configuration, namely \(r(b')\) when \(f=b'\). It is the γ-partner of at most one, namely \(r(e')\) when \(f=e'\).
- If both hold, then \(D=(g,f,p,q,u,f)\) is β for \(c\) and γ for \(c_2\), with \(f_2=e'=u\) and \(g_2=s(u)=f\).
- Hence **one \(W_0\) serves at most two configurations, and the only combinations are (α,α) and (β,γ).** An (α,α) pair uses the two red heads of a non-defective \(W_0\). A (β,γ) pair uses the two red heads of a defective one.
- At most one rule changes the pendant of \(D\). Either the type-1 trade of the source with \(c\)-label \(b'\) gives \(r(b')\), or the G-pendant of the configuration with \(f=b'\) gives \(m(b')\). By Lemma 5(ii), these exclude each other. A removed type-1 trade leaves the plain pendant \(s(b')\).
- By Lemma 5(ii), a γ-partner is a source with no incoming type-2 link. So it is not a recipient, and it lies on no type-2 cycle.

*Step 4: sources of configurations.* Let \(T_c=(a,b,c,d,e,b)\) be the source of a configuration \(c\).

- **Its pendant is plain.**
  - A type-1 trade into \(T_c\) would come from the source \(\tau(b\,m(b))=\tau(bf)=Q_c\), which is not defective.
  - A G-pendant would make \(T_c\) the β-partner of a configuration \(c'\) with \(f'=b\). Then \(c'=r(b)=h\) and \(b'=m(b)=f=r(h)\). The triangles \(fhb\) and \(bcf\) share \(fb\), which is a diamond (Step 1).
- So \(T_c\) is never a β-partner.
- \(T_c\) is the γ-partner of a configuration \(c'\) exactly when \(e=f'\), that is, \(W_0(c')=T_c\). Its link is type 0 into the G-configuration \(Q_c\). So **this is exactly a Gtarget edge \(c'\to c\)**.
- \(T_c\) is a source, so it is not a recipient and lies on no type-2 cycle.

*Step 5: the Gtarget graph and removed trades.*

- The out-degree is at most 1, since \(c\) determines \(W_0=T_{c^*}\) and hence \(c^*\). The in-degree is at most 1, since \(c^*\) determines \(T_{c^*}=W_0\), whose \(e'\)-label is \(f\), and \(c=r(f)\). So the Gtarget graph is a disjoint union of directed paths and cycles, and the resolution of Section 3 is well defined.
- In that resolution, a surviving \(c\) with an edge \(c\to c^*\) does one of three things. It absorbs \(T_{c^*}\), and then \(c^*\) is cancelled. It uses Γ or Γ′ at the chosen node \(j\) of an odd cycle, and then \(c^*=c_{j+1}\) survives. Or it rotates, and then every node of its cycle survives.
- On an odd cycle with Γ at \(j\), the nodes \(j+1,j+3,\dots,j-2\) absorb and the nodes \(j+2,j+4,\dots,j-1\) are cancelled. So \(c_j\) and \(c_{j+1}\) both survive, as the Γ-rule requires. Every cancelled node has an absorbing predecessor.
- **No type-2 trade is ever removed.** Absorption removes the trade of \(W_0\) only when its link is type 0 or type 1. Cancellation removes the type-0 trade of \(T_{c^*}\). So every recipient keeps its source, the type-2 alternation is unchanged, and the odd type-2 cycles are unchanged.
- A removed type-0 trade leaves the target's terminal canonical at that end. A removed type-1 trade leaves the target's pendant plain. Lemma 3 is per end and per pendant, so the target is still a first-sweep piece of standard form.
- Removing a trade creates no G-configuration, since a G-configuration is the target of a trading source.

*Step 6: classification.* Take a final piece. Consider the first-sweep piece it comes from, or, for Γ, Γ′ and the rotation, the pieces they rebuild.

- **(a) A non-defective \(N=Q_c\), \(c\) surviving.**
  - By Steps 1 and 2, only the rule of \(c\) acts on the \(c\)-end.
  - At the \(h\)-end, the terminal is plain \(s(h)\) (also when a trade of \(D_h\) was removed), received \(r(h)\) from \(D_h\), or α-linked \(b_{c_3}\) by the α-rule of \(c_3=r(h)\). By Step 2, the last two exclude each other.
  - \(N\) is not defective, so it is not a β- or γ-partner.
  - So the piece is fixed by the case of \(c\) and its resolution: W1, W2, W6/W7 or W8. This is kind (K2).
  - The restrictions in the windows hold.
    - In W2, the source of a received \(Y\) is not \(W_0\), because an absorbed \(W_0\) does not trade.
    - In W2, the source of a linked \(c_3\) is not \(W_0\), because \(c_3\) survives and so its source trades.
    - In W7 and W8, the configuration linked at \(h\) is not the next node \(c^*\). That node has its own Gtarget edge, so it is in case γ and has no α-partner.
- **(b) A non-defective \(N\) that is not \(Q_c\) of a surviving configuration.** It may be the trail \(Q_{c^*}\) of a cancelled configuration.
  - By Step 2, each end is plain, received or an α-partner end.
  - If neither end is an α-partner end, then \(N\) is of kind (K1).
  - Otherwise, \(N\) is the α-partner piece \(P^*\) of some \(c\) at its \(f\)-end. Its far end is plain, received or α-linked. This is W3, kind (K3).
  - A received \(Z=r(u)=p\) would make \(N=Q_u\) with \(u\) surviving (W3 window fact), which is excluded here.
  - If \(N=Q_{c^*}\) with \(c^*\) cancelled, its \(c^*\)-end is plain (Step 2).
- **(c) A defective \(D=T_c\).** By Step 4, its pendant is plain, and its only possible second-sweep role is as the γ-partner on a Gtarget edge \(c'\to c\).
  - If \(c'\) survives, it absorbs \(D\) (W5), uses Γ or Γ′ at an odd-cycle node (W7), or rotates (W8). This is kind (K5).
  - Otherwise, \(D\) keeps its first-sweep source piece, which is kind (K1).
- **(d) A defective \(D\) that is no \(T_c\).** By Step 3 there are three cases.
  - *\(D\) is the γ-partner of a surviving \(c_2\).* Then \(D\) is a source.
    - Its link is type 1, or type 0 into a target that is not a G-configuration. Then \(D\) is absorbed (W5).
    - Or its link is type 2, and Γ or Γ′ applies (W6).
    - A type-0 link into a G-configuration would make \(D=T_{c^*}\), which is case (c).
    - Its pendant is plain, changed or the G-pendant \(m(g_2)\). The G-pendant occurs exactly when \(D\) is also the β-partner of a surviving configuration. This is kind (K5).
  - *\(D\) is only the β-partner of a surviving \(c\).* Then its pendant is \(m(f)=b\), and three cases remain.
    - \(D\) is a source, with source piece \((b,f,u,q,p,s(p))\) (W4).
    - \(D\) is a recipient, with piece \((b,f,p,q,u,r(u))\) (W4). Its incoming type-2 source has \(c\)-label \(u\).
    - \(D\) lies on an odd type-2 cycle (Lemma 7 and Lemma 4′).
    - This is kind (K4).
  - *Neither.* Then \(D\) is of kind (K1). Its pendant is plain, changed, or reverted to plain.

Every final piece arises in one of these cases. \(\square\)

The referee derived the same set of final pieces independently from the rules of Section 3 ([04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md), §2).

*Proof of Theorem B.* Apply Lemma 1 and the first sweep, with the absorption and cancellation decisions of Section 3. Then apply the second sweep.

- **Partition.** Every rule exchanges edges between pieces.
  - The G-rule, the G-pendant and absorption each exchange \(fb\in M\) with \(fg\in S\) between the piece of \(Q_c\) and the piece of \(W_0\).
  - Absorption and cancellation also undo a first-sweep trade. This returns \(\{b',c'\}\) to the source's trail and \(\{c',s(c')\}\) to its target.
  - The Γ-rule is checked by `symbolic_exchanges()`.
  - For Γ′, with \(A'=h\), the pair \(\{Q'_c,W\}\) and the two new pieces both have the edges \(hY^*,hg,gf,fc,cb,hb,bf,fp,pq,q\,s(q)\). Windows W6 and W7 also compare the edge multisets whenever Γ′ is used.
  - The rotation is checked by telescoping. On an odd Gtarget cycle \(c_0\to c_1\to\dots\to c_{L-1}\to c_0\), with indices mod \(L\), (F1) gives
    \[
    Q'_k=(b_k,c_k,f_k,b_k,h_k,Y^*_k),\qquad W_k=(A'_k,b_{k+1},f_k,p_k,c_{k+1},c_k).
    \]
    Here \(Y^*_k\) already includes an α-link at \(h_k\), whose exchange is counted with the α-rule of \(c_3\). Compare the edges of \(Q'_k\cup W_k\) with those of \(R_k\cup P_k\). Both contain \(b_kc_k\), \(c_kf_k\), \(f_kb_k\), \(b_kh_k\), \(h_kY^*_k\), \(A'_kb_{k+1}\), \(b_{k+1}f_k\), \(f_kp_k\) and \(p_kc_{k+1}\). The only difference is that \(Q'_k\cup W_k\) contains \(\{c_{k+1},c_k\}\), while \(R_k\cup P_k\) contains \(\{c_{k+1},c_{k+2}\}\). Summed over \(k\in\mathbb Z/L\), both families equal \(\{\{c_j,c_{j+1}\}:j\in\mathbb Z/L\}\), after the shift \(k\mapsto k+1\).
    So \(\bigcup_k(R_k\cup P_k)\) and \(\bigcup_k(Q'_k\cup W_k)\) have the same edge multiset. The rotation re-partitions the pieces of the whole cycle, but not each pair \(\{Q'_k,W_k\}\) on its own. The edge \(\{c_{k+1},c_{k+2}\}\) is the terminal edge \(\{c_{k+2},s(c_{k+2})\}\) of \(W_{k+1}\), by (F1) at node \(k+1\).
  - Distinct configurations exchange distinct edges, because \(fb\) and \(fg\) are determined by \(f\) and \(c=r(f)\).
  - By Lemma 8, rules acting on the same piece act at different ends.
  - Hence the pieces partition \(E(G)\).
- **Shape.** By Lemma 8, each piece is of one of the kinds (K1)–(K5). Each kind is a simple five-edge path, by Lemma 3, Proposition B, Lemma 4, Lemma 4′ or the windows W1–W8. \(\square\)

## 5. Verification

```powershell
Set-Location research/2026-11-25-target-shortlist
python -B check_regular_path_gsweep.py                         # all windows W1-W8 and Lemma 4' (proof step)
python -B check_regular_path_theoremB_independent.py --quick   # referee's independent checker (about 1 min)
python -B check_regular_path_theoremB_independent.py --seed 31 # referee's full run (seeds 31 and 77, about 25 min in total)
python -B check_regular_path_diamond_free.py --generic 1500    # author's end-to-end evidence
```

[check_regular_path_label_engine.py](check_regular_path_label_engine.py) enumerates restricted-growth set partitions. Its checks are incremental and are undone on backtracking. It prunes only when an axiom already fails. For a sanity check, it reproduced the earlier failure of the naive Γ-rule. It also found the realizable Gtarget case \(s(q)=c\), which was then confirmed on a real order-14 graph. The referee audited the engine and every window inequality and found them sound ([04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md), §2).

[check_regular_path_diamond_free.py](check_regular_path_diamond_free.py) implements the complete procedure, with Section 3 as written and its deterministic rule choice. It handles random diamond-free graphs and generic \((M,r,s)\) data satisfying (P1)–(P3), annealed toward many G-configurations. It verifies every output exactly. These runs are evidence only. Run counts are in 04-HANDOFF.md.

**Independent checker.** The referee's [check_regular_path_theoremB_independent.py](check_regular_path_theoremB_independent.py) was written from the text. It imports no code from this note; it reuses only the audited Lemma 1, (P1)–(P3) and path-cover code of the Theorem A referee. It asserts the intermediate claims of the text, including Lemma 5, Lemma 7, plain pendants at odd Gtarget nodes and the absence of pendant feedback. The referee's results (04-REVIEW-theorem-B.md, §3) were as follows.

- **Lemma 4′, own enumeration.** The counts match exactly. Triples with G-pendants gave 205 closed and 548 open covers and 12 exceptions. Triples without G-pendants gave 259 closed and 564 open covers and 24 exceptions.
- **Planted generic data.** Seeds 31 and 77, about 25 min in total, gave 5,916 verified decompositions with 0 failures. Planted structures exercised every rule: 10,140 G-pendants, 995 odd type-2 cycles with a G-pendant, 1,009 type-2 Γ uses, 119 Γ′ uses, and 1,935 Gtarget cycles of lengths 2–7. The odd Gtarget cycles were resolved by Γ at one node 575 times and by the rotation 442 times.
- **Graphs.** 5,760 verified decompositions came from 384 diamond-free graphs on 12–48 vertices. These Lemma 1 constructions contained no odd Gtarget cycle.
- **Cross-check.** The author's end-to-end code verified all 502 of the referee's planted instances, including 32 rotations and 53 odd-node Γ uses.

These runs are evidence only. The proof is the written argument with the exhaustive window checks.

## 6. Self-review and open points

- **Reviewed.** An independent referee ([04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md)) rechecked the case catalogue, the window facts and the resolution of the Gtarget graph. The verdict was accept with fixes, with no mathematical gap. The highest-risk point, that Section 4 lists every way a final piece can arise, is now proved as Lemma 8; the referee derived the same catalogue independently. The proof has no Lean formalization and has not been refereed externally.
- **Superset soundness.** Each engine fact is a true consequence of its case. Omitting facts only enlarges the enumeration. The inequality facts used to exclude configurations are each justified in the text (window facts, Lemma 8).
- **Rotation case.** Its validity rests on window W8 and on the telescoping argument in the proof of Theorem B. Odd Gtarget cycles occur in generic \((M,r,s)\) data satisfying (P1)–(P3); the referee's planted runs resolved 442 of them by the rotation. None has been observed in a Lemma 1 construction on a real graph. The proof uses only (P1)–(P3), so this does not matter.
- **Extension to all graphs.** Diamonds reintroduce the Lemma 3 exceptions \(A=d\) and \(s(c)=e\), the pair-replacement chords and further non-path pieces. They are not treated here.

## Change log (for the referee)

- **2026-11-25, after the first full run.**
  - W7's allowed-failure criterion in `window_Gamma_source` was tightened. It previously allowed any failure under (F1) \(s(q)=c\). It now allows failure only under (F1) **and** a plain pendant \(s(g)\ne h\), matching the text of §3.
  - The re-run gave 0 failures. The plain-pendant windows recorded 527, 16,365 and 18,467 excluded identifications for \(Y\) plain, received and linked, the same as before. So every (F1) failure already had \(A'\ne h\).
  - The full checker run took 14 min. Windows W1–W8 had 0 failures, and Lemma 4′ gave the counts stated in §3.
- **2026-11-25, end-to-end evidence.** These counts come from [check_regular_path_diamond_free.py](check_regular_path_diamond_free.py), using the deterministic rule choice of §3 with no search.
  - **Random diamond-free graphs.** There were 5,600 verified decompositions from seed 2 (40 graphs per order) and seed 7 (30 graphs per order). They included 53 γ-configurations, 11 Gtarget cancellations, 4 type-2 Γ uses, 2 Γ′ uses and 1 odd-cycle block cover.
  - **Generic \((M,r,s)\) instances (seed 23).** There were 193 verified decompositions, plus 7 instances where the annealing failed. They included 28 γ-configurations: 8 type-2 Γ, 8 Gtarget absorptions, 7 type-0 absorptions and 5 type-1 absorptions. There were also 34 β-configurations, 6 odd-cycle block covers and 1 Γ′ use.
  - No odd Gtarget cycle occurred, so the rotation is supported only by window W8.

## Change log after the independent review (2026-11-25)

The referee's issues are in [04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md), §4. No mathematical statement or rule was changed.

- **M1.** The list "Completeness of the catalogue" in §4 was replaced by **Lemma 8 (Classification of final pieces)** with a proof. It follows the referee's derivation and interaction analysis.
  - Step 1 gives one configuration per \(T\), \(f\) and \(Q\).
  - Step 2 gives received/α-partner exclusivity at every end.
  - Step 3 shows that the only same-\(W_0\) combinations are (α,α) and (β,γ).
  - Step 4 shows that \(T_c\) has a plain pendant and is never a β-partner (a diamond), but is a γ-partner exactly along a Gtarget edge.
  - Step 2 also shows that \(Q_c\) is an α-partner only at its \(h\)-end.
  - Step 5 shows that the Gtarget in- and out-degrees are at most 1, and that no type-2 trade is ever removed, so removing a trade never orphans a recipient.
  - Step 6 is the case split.
- **m1.** In Lemma 7 (§3), the \(b\)-label step was replaced by the referee's argument: \(m(b_i)=b_j\) gives \(c=c_j\), so \(T_c=T_j\) would be a source on the odd cycle. Part (b) was added: a G-pendant never equals a changed pendant \(r(b_k)\), since otherwise \(c=b_k\) and \(T_c\) would be the external type-1 source into \(T_k\).
- **m2.** In the proof of Theorem B, "checked by edge count in the windows" was replaced by an explicit partition argument. The rotation is proved by telescoping around the whole cycle. Γ′ is listed edge by edge.
- **m3.** The Γ-rule now states that Γ′ is used only with the plain pendant, and why. The Interfaces bullet no longer claims that \(\{g,A'\}\) is always terminal.
- **m4.** The justification of \(Z\ne p\) in W3 was moved from the code comment into the window facts (§4).
- **m5.** The partner-end argument for the Γ source piece, now in Lemma 8, Step 2, includes the orientation \(s(s(q))=q\), which (P2) excludes.
- **m6.** Scope now says that Theorem B contains only the existence part of the FGK results, not their extendability statement.
- **m7.** The Scope novelty bullet was updated: the FGK 2010 full text has been read (04-NOVELTY-fgk2010.md, 04d), and the referee's bounded search is cited.
- **m8.** In [check_regular_path_diamond_free.py](check_regular_path_diamond_free.py), the unreachable search code after `if True: raise` in `solve_one` was removed, together with the helper `_odd_gtarget_cycles`, the `_record` hook and the unused `choices` parameter. The docstrings now describe the deterministic rule. The behaviour is unchanged.
- **Also.** The status line, Verification (§5, now citing the referee's independent checker and its results) and Self-review (§6) were updated.

**Checks rerun after the fixes (2026-11-25, Python 3.12).**

- `python -B check_regular_path_gsweep.py` took 6 min 40 s, running alongside the other checks. It reported **total failures 0**, with 0 failures in every window W1–W8.
  - The Gtarget windows with a changed pendant or a G-pendant had 0 identifications, which agrees with Lemma 8, Step 4.
  - W7 excluded 527, 16,365 and 18,467 identifications for \(Y\) plain, received and linked, unchanged.
  - Lemma 4′ gave 205 closed and 548 open covers, 12 open exceptions with \(d_1\in\{A_0,A_2\}\), and 243 cases excluded by local diamonds.
- `python -B check_regular_path_theoremB_independent.py --quick` took 46 s and printed **ALL CHECKS PASSED**.
  - Its own Lemma 4′ counts matched: 205/548/12 with G-pendants, 259/564/24 without.
  - It verified 537 decompositions: 249 planted, 144 switch graphs and 144 line-cubic graphs. These included 14 rotations, 23 odd-node Γ uses and 5 Γ′ uses.
  - 51 planted instances failed in the instance generator ("repair failed") and were skipped. These are not decomposition failures.
- The edited end-to-end checker was run with `python -B check_regular_path_diamond_free.py --seed 5 --orders 12 14 16 20 24 --graphs 8 --constructions 5 --generic 150`. It took 1 min 21 s and verified **341 decompositions with 0 failures**: 200 on graphs and 141 generic, with 9 annealing failures skipped. They included 115 G-configurations (47 α, 35 β and 33 γ), 14 type-2 Γ uses, 1 Γ′ use, 1 cancellation and 4 odd-cycle block covers.
- The edited `solve_one` was also run on the referee's planted instances with `04-handoff/review-theoremB/cross_author_code_scratch.py 9 200`. It verified 171 of 171, including 9 rotations and 21 odd-node Γ uses.
