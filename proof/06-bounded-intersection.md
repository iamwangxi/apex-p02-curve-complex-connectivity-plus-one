# One more degree for every bounded-intersection curve complex

For every positive integer intersection bound, finite vertex-relative replacement gives one more degree of connectivity than direct intersection counting. All selection, descent and homotopy arguments are given below; finite checks are supplementary.

## 1. Statements

Let $`S_g`$ be a closed connected orientable surface, $`g\geq2`$. A curve vertex is an unoriented isotopy class of an embedded essential circle. Essential means not bounding a disk. Write $`i(a,b)`$ for geometric intersection, including $`i(a,a)=0`$. For $`d\geq0`$, let $`C_d(S_g)`$ be the flag complex whose distinct vertices are adjacent exactly when $`i(a,b)\leq d`$. Realizations carry the weak topology. Put

```math
B=2g-2,\qquad I(A)=\sum_{\{a,b\}\subset A}i(a,b).
```

**Theorem A (relative finite replacement, every $`d`$).** Let $`d\geq1`$ and $`k\geq1`$ be integers such that

```math
d\binom{k}{2}\leq B.                                      \qquad (1)
```

For every finite subcomplex $`L\subset C_d(S_g)`$ of dimension at most $`k`$, its inclusion is homotopic, fixing every original vertex, to a map factoring through $`C_0(S_g)`$. The construction uses finitely many interior stellar subdivisions of maximal $`k`$-simplices, followed by barycentric subdivision of the finite endpoint image complex. No change is made on the boundary of any stellar replacement.

The same argument works for any simplicial map from a finite complex of dimension at most $`k`$, with all its original vertices fixed during the homotopy.

**Theorem B (connectivity).** For every $`g\geq3`$, $`d\geq1`$ and $`k\geq1`$ satisfying (1), $`C_d(S_g)`$ is $`k`$-connected. Also, $`C_d(S_2)`$ is simply connected for every $`d\geq1`$.

If the target paper's Theorem 1.1 on contractibility of $`C_1(S_2)`$ is included as an input, the connectivity conclusion under (1) holds for $`g=2`$ as well. The only extra cases are $`k=2`$, $`d=1,2`$. This genus-two input is not used in Theorem A, or in any conclusion for $`g\geq3`$.

Consequently, for $`g\geq3`$ and every $`d\geq1`$,

```math
\mathrm{conn}\,C_d(S_g)\geq
1+\left\lfloor\frac{\sqrt{1+8(2g-2)/d}-1}{2}\right\rfloor.   \qquad (2)
```

With the specified genus-two input, (2) holds for every $`g\geq2`$. This is precisely one degree above the direct-count bound $`d\binom{k+1}{2}\leq B`$, including the case in which that bound gives only connectivity in degree zero. In particular, simple connectivity is uniform in $`d`$; it is not inferred from monotonicity of connectivity under adding simplices.

The new ingredient is a capacitated selection of dual edges that cannot support a homologically trivial cycle. A cycle may cross the same input curve more than once, so parity of a single color is not a sufficient essentiality argument in the general case.

## 2. Surface preliminaries

### 2.1. Generic simultaneous minimum position

Any finite set of distinct essential curve classes has embedded representatives realizing all pairwise geometric intersection numbers, with transverse double intersections and no triple points. To obtain them, choose their simple closed geodesics in a hyperbolic metric. Distinct geodesics are in pairwise minimum position. At each multiple intersection, make a sufficiently small local perturbation separating the crossing points, keeping exactly one crossing for each incident pair. Finitely many disjoint coordinate disks and sufficiently small perturbations preserve embeddedness and all pairwise counts.

For example, in geodesic normal coordinates the incident geodesics are radial lines with distinct tangent directions. Translate these lines by small generic offsets in a smaller disk, then join to the unchanged arcs near the boundary of the larger disk. Avoid the finitely many concurrence conditions. Transversality preserves the existing pairwise crossings; compact separation away from them prevents new crossings. These modifications are isotopies of each individual curve.

We use one representative per distinct image class. A degenerate simplicial image is counted as its set of classes, without multiplicity.

### 2.2. Essential boundary or disk complement

Let $`G`$ be the union of a nonempty finite generic family of essential circles and let $`I`$ be its total number of double intersections. A sufficiently small proper regular neighborhood $`N`$ satisfies

```math
\chi(N)=\chi(G)=-I.                                      \qquad (3)
```

Indeed, if there are $`z`$ isolated circle components, add one artificial vertex and edge to each: $`V=I+z`$, $`E=2I+z`$.

Every component of $`N`$ contains an essential input circle. If a boundary circle of $`N`$ is inessential, its unique disk side cannot contain its incident component of $`N`$, or any other component of $`N`$: a component on that side would contain an essential circle in a disk. Thus its disk interior misses $`N`$. If all boundary circles are inessential, these disks are exactly all the complementary components, and have pairwise disjoint interiors. Writing their number as $`F\geq1`$, additivity gives

```math
2-2g=-I+F,\qquad F=I-B.                                 \qquad (4)
```

In this case $`G`$ is connected. Capping boundary components by individual disks cannot connect different components of $`N`$, whereas the capped surface is the connected surface $`S_g`$. In particular $`I\leq B`$ guarantees an essential boundary component. These assertions do not require a separate class-level filling criterion, for any value of $`d`$.

### 2.3. Dual cycles

In the disk-complement case, adjoining the collars between the spine and the neighborhood boundary to the complementary disks shows that $`S_g\setminus G`$ consists of open disks. Thus $`G`$ is cellularly embedded. Use its cellular dual graph $`D`$: its vertices are the $`F`$ complementary disks, and its edges cross the $`2I`$ primal edges once each. A dual edge is colored by the input curve containing the primal edge. Loops and parallel edges are retained.

A simple dual cycle with $`r`$ edges produces an embedded circle $`c`$ crossing those $`r`$ primal edges once each and missing all other primal edges. To see this directly, use the selected band co-cores and one properly embedded joining arc in each visited complementary disk. A simple cycle visits each disk once. A loop uses one such arc in one disk; a two-edge cycle uses one in each of two disks. Round the corners. This does not assume that a face boundary walk in $`G`$ is embedded.

If $`m_a`$ of its edges have color $`a`$, then

```math
\#(c\cap a)=m_a,\qquad i([c],a)\leq m_a,\qquad
\sum_a m_a=r.                                           \qquad (5)
```

When colors repeat, equality in the geometric intersection bound is not asserted. Essentiality will be proved separately. For a one-edge cycle, or a two-edge cycle of distinct colors, it follows at once from odd mod-two intersection with an input circle.

## 3. A finite selection lemma, with proof

We give the finite combinatorial input rather than assuming an unproved selection principle.

### 3.1. The deletion matroid of a connected graph

For a finite connected multigraph $`G=(V,E)`$, call $`X\subset E`$ independent when $`G-X`$ is connected, retaining all vertices. These independent sets form the cographic matroid. Its rank on $`A\subset E`$ is

```math
\rho(A)=\lvert A\rvert-c(G-A)+1,                         \qquad (6)
```

where $`c`$ counts components, including isolated vertices.

Here is a verification of the matroid assertions used below. Heredity is immediate. If $`X,Y`$ are independent and $`\lvert X\rvert<\lvert Y\rvert`$, not every edge of $`Y\setminus X`$ can be a bridge of $`G-X`$. Otherwise deleting those bridges produces $`\lvert Y\setminus X\rvert+1`$ components. Adding the $`\lvert X\setminus Y\rvert`$ edges cannot reconnect them, contradicting connectivity of $`G-Y`$. A non-bridge in $`Y\setminus X`$ gives the exchange axiom. For (6), contract the components of $`G-A`$. Exactly $`c(G-A)-1`$ edges of $`A`$ are needed in a spanning tree between them; deleting all other edges of $`A`$ is possible and optimal. This also handles primal loops and multiple edges.

### 3.2. Independent representatives

We use the following finite matroid version of the marriage lemma.

**Lemma 3.1.** For subsets $`A_1,\ldots,A_t`$ of a finite matroid with rank $`\rho`$, distinct independent representatives $`e_j\in A_j`$ exist if and only if

```math
\rho\left(\bigcup_{j\in J}A_j\right)\geq\lvert J\rvert
\quad\text{for every }J\subseteq\{1,\ldots,t\}.           \qquad (7)
```

**Proof.** Necessity is immediate. For sufficiency induct on $`t`$. The case $`t=1`$ says there is a non-loop. If a nonempty proper index set $`J`$ is tight in (7), select its independent representatives by induction. They form a basis $`P`$ of $`\bigcup_{j\in J}A_j`$. Contract $`P`$. For any set $`K`$ of the remaining indices, the rank of its union in the contraction is

```math
\rho\left(P\cup\bigcup_{j\in K}A_j\right)-\lvert J\rvert
=\rho\left(\bigcup_{j\in J\cup K}A_j\right)-\lvert J\rvert
\geq\lvert K\rvert.
```

The equality holds because $`P`$ is a basis of the union indexed by $`J`$. Induction in the contraction supplies the remaining representatives. Together with $`P`$ they are independent and distinct. The contraction rank formula follows by extending $`P`$ to a basis of its union with the set in question, so no extra representability hypothesis is involved.

If there is no nonempty proper tight set, choose a non-loop $`e\in A_t`$ and contract it. Every nonempty index set $`K\subseteq\{1,\ldots,t-1\}`$ had union rank at least $`\lvert K\rvert+1`$. Contraction decreases rank by at most one. Thus (7) holds for the remaining sets in the contraction, and induction applies. Adjoin $`e`$. This proves the lemma. $`\square`$

**Lemma 3.2 (capacitated selection).** Suppose the ground set of a finite matroid is partitioned into $`E_1,\ldots,E_n`$. If $`q\leq dn`$ and

```math
\rho(E_A)+d(n-\lvert A\rvert)\geq q
\quad\text{for every }A\subseteq\{1,\ldots,n\},\qquad
E_A=\bigcup_{a\in A}E_a,                                 \qquad (8)
```

then there is an independent set of at least $`q`$ elements using at most $`d`$ elements from each part.

**Proof.** Add $`dn-q`$ new freely independent elements $`Z`$ by direct sum with a free matroid. Make $`d`$ slots for each part; each slot of part $`a`$ has candidate set $`E_a\cup Z`$. For any nonempty selection of slots whose represented parts are $`A`$, the rank of its union of candidates is $`\rho(E_A)+dn-q`$. By (8) this is at least $`d\lvert A\rvert`$, hence at least the number of selected slots. Lemma 3.1 gives independent representatives for all $`dn`$ slots. At most $`dn-q`$ of them belong to $`Z`$. Discarding those gives the required set. $`\square`$

## 4. Enough dual edges with bounded color multiplicity

Consider $`n\geq2`$ distinct input classes with $`i(a,b)\leq d`$ and

```math
I>B,\qquad d\binom{n-1}{2}\leq B.                        \qquad (9)
```

Use minimum-position representatives and suppose their neighborhood has no essential boundary. Thus (4) holds, and $`G`$ is connected. Set

```math
\delta_a=\sum_{b\neq a}i(a,b).
```

The total intersection of the facet omitting $`a`$ is at most $`d\binom{n-1}{2}\leq B`$, so

```math
\delta_a\geq I-B=F,\qquad
1\leq F\leq d(n-1)\lt dn.                                  \qquad (10)
```

**Proposition 4.1.** There is a set $`X`$ of at least $`F+1`$ primal edges such that $`G-X`$ is connected and $`X`$ contains at most $`d`$ edges of each input color.

**Proof.** Apply Lemma 3.2 to the deletion matroid, with $`q=F+1`$. We check (8). For a color set $`A`$ put $`U=\{1,\ldots,n\}\setminus A`$. If $`A`$ is empty, (10) gives $`dn\geq F+1`$. If $`U`$ is empty, (6) gives $`\rho(E)=2I-I+1=I+1\geq F+1`$.

Suppose both sets are nonempty. Write $`I_U`$ for the intersections between curves in $`U`$, $`I_A`$ for those between curves in $`A`$, and $`I_{A,U}`$ for the mixed intersections. Let $`h_U`$ be the number of components of the union of the $`U`$-curves; equivalently, the number of components of their intersection graph, counting an isolated input curve as one component. Deleting all edges colored in $`A`$ leaves that union, and exactly $`I_A`$ additional isolated vertices. Furthermore, $`\lvert E_A\rvert=2I_A+I_{A,U}`$. Hence

```math
\rho(E_A)=I-I_U-h_U+1.                                  \qquad (11)
```

Since $`U`$ is proper, $`I_U\leq d\binom{n-1}{2}\leq B`$, and $`h_U\leq\lvert U\rvert\leq d\lvert U\rvert`$. Consequently

```math
\rho(E_A)+d\lvert U\rvert
=I-I_U-h_U+1+d\lvert U\rvert\geq I-B+1=F+1.
```

This proves (8), and Lemma 3.2 proves the proposition. $`\square`$

**Proposition 4.2 (essentiality of every selected cycle).** A nonempty mod-two cycle supported on the dual edges corresponding to $`X`$ is nonzero in $`H_1(S_g;\mathbb F_2)`$.

**Proof.** Use the cellular dual decomposition of the cellularly embedded graph $`G`$. Its 2-cells correspond to primal vertices. A homologically zero dual 1-cycle is the cellular boundary of a sum of dual 2-cells. Let $`W`$ be the corresponding set of primal vertices. Its boundary support consists exactly of the primal cut edges with one endpoint in $`W`$ and one outside, read as dual edges. If it is nonempty, $`W`$ is a nontrivial vertex subset. All cut edges would lie in $`X`$, contradicting connectivity of $`G-X`$. If the cut is empty, its dual chain is zero, contrary to the assumed nonempty cycle. Thus the cycle is homologically nonzero. Loops, repeated incidences and parallel edges are covered by this mod-two cellular boundary calculation. $`\square`$

In particular, any simple cycle in the selected dual subgraph gives an essential embedded curve by §2.3. This is the step that replaces the rainbow-only argument. The repeated-color crossings in (5) remain upper bounds on geometric intersections.

We also use a small graph fact: a multigraph on $`F`$ vertices with more than $`F`$ edges has a simple cycle of length at most $`F`$; if $`F\geq3`$, it has one of length at most $`F-1`$. It is not a forest. If its shortest cycle used all $`F`$ vertices, any extra edge would be a loop, a parallel edge or a chord giving a shorter cycle. For a triangle, an extra edge must be a loop or parallel edge. Disconnected graphs cause no exception.

## 5. Strict descent, including the small-face cases

**Lemma 5.1.** Under (9), there is a new essential class $`c`$ adjacent in $`C_d`$ to every input, such that each of the $`n`$ cone facets $`c*(A\setminus\{a\})`$ has total geometric intersection strictly less than $`I`$.

**Proof.** If there is an essential neighborhood boundary, take it for $`c`$. It is disjoint from every input and the cone facets have intersection at most $`d\binom{n-1}{2}\leq B\lt I`$. It cannot equal an input class, since (10)'s degree estimate, which does not require filling, gives positive degree for every input.

Otherwise the complement consists of $`F=I-B`$ disks. For a curve with the crossing multiplicities (5), the labelled cone-facet count omitting $`a`$ is bounded above by

```math
Q_a=I-\delta_a+r-m_a.                                   \qquad (12)
```

We construct a curve for which all these integers are less than $`I`$.

**If $`F\geq3`$:** choose $`X`$ as in Proposition 4.1. Its dual subgraph has more than $`F`$ edges. The graph fact gives a simple cycle with $`r\leq F-1`$. Proposition 4.2 makes it essential, and its multiplicities satisfy $`m_a\leq d`$. By (10),

```math
Q_a\leq I-F+(F-1)-m_a\leq I-1
```

for every input.

**If $`F=1`$:** every dual edge is a loop, giving an essential cost-one curve. If all degrees are at least two, any edge works. If $`\delta_v=1`$, then

```math
I-1=B=I(A\setminus\{v\})=d\binom{n-1}{2}.               \qquad (13)
```

Thus all intersections among the other inputs equal $`d`$. Their degrees are at least $`d(n-2)`$. The possibility $`n=2`$ would force $`B=0`$ in (13), and $`n=3,d=1`$ would force $`B=1`$; both are excluded by $`B\geq2`$. Therefore the other degrees are at least two and $`v`$ is the unique degree-one input. Select an edge colored $`v`$. Its curve has $`r=m_v=1`$ and gives $`Q_v=I-1`$; for every other input, $`Q_a\leq I-1`$. Each color is used at most once.

**If $`F=2`$:** let $`T`$ be the set of degree-two inputs. We first show $`\lvert T\rvert\leq2`$. If $`T`$ is nonempty, choose $`v\in T`$. As above,

```math
I-2=B=I(A\setminus\{v\})=d\binom{n-1}{2}.               \qquad (14)
```

Every other degree is at least $`d(n-2)`$. If this is at least three, $`T=\{v\}`$. Values zero or one force $`B<2`$. The only remaining possibilities are $`(n,d)=(4,1)`$ or $`(3,2)`$. In the first, the other three inputs form a complete 1-system and $`v`$ meets two of them: only the third can also have degree two. In the second, the other pair has intersection two, and the two intersections contributed by $`v`$ can leave at most one of them of degree two. This proves the claim. (The first possibility is also excluded by the even value of $`B`$, but that exclusion is unnecessary.)

If the dual graph has a loop, its cost-one curve works because all degrees are at least two. If there is no loop, every dual edge joins the two distinct dual vertices. Choose two edges of distinct colors, covering every color in $`T`$. This is possible because $`\lvert T\rvert\leq2`$ and $`n\geq2`$, with every input having positive degree. They form a two-edge cycle. It is essential by odd intersection with either selected color. Here $`r=2`$, every degree-two input has $`m_a=1`$, and every remaining input has degree at least three. Thus (12) again gives $`Q_a\leq I-1`$ for all $`a`$. Its per-color cost is at most one, so it is admissible for every $`d\geq1`$.

Finally, (5) makes $`c`$ adjacent to every input. Its class is new: if $`c=v`$ for an old input, then for the facet omitting $`v`$,

```math
I=I-\delta_v+\sum_{a\neq v}i(c,a)
\leq I-\delta_v+r-m_v=Q_v\lt I,
```

a contradiction. All cone facets therefore have distinct image classes and their actual intersection totals are bounded by (12). The old inputs together with $`c`$ span a genuine simplex of $`C_d`$ by flagness. $`\square`$

The argument in this lemma does not promote actual crossing counts to geometric equality when a color repeats. It uses only their proved upper bounds.

## 6. Compatible replacement and termination

Let a finite source complex have dimension at most $`k`$, with a simplicial map into $`C_d`$. A source simplex is safe if the intersection total of its image set is at most $`B`$. Under (1), every source simplex of dimension at most $`k-1`$ is automatically safe, at every stage, because it has at most $`k`$ distinct image vertices.

Thus a bad simplex must be a maximal $`k`$-simplex with $`n=k+1`$ distinct image vertices. Apply Lemma 5.1 and perform an interior stellar subdivision, mapping its new interior source vertex to $`c`$ and keeping the boundary map unchanged. Every child top simplex has smaller actual intersection total. The old and new maps land in the single target simplex spanned by the old inputs and $`c`$. Their straight-line homotopy in its barycentric coordinates fixes the entire boundary of the source simplex. Extending constantly elsewhere is continuous and compatible with all neighboring simplices. All original source vertices are fixed.

There is genuine finite termination. For an initial bad top simplex of excess $`e=I-B`$, every descendant branch has at most $`e`$ bad subdivisions. Each subdivision has $`n`$ top children. Thus the descendant tree has bounded depth and finite branching, with at most $`n^e`$ leaves. Also

```math
e\leq d\binom{k+1}{2}-B\leq dk.                          \qquad (15)
```

There are finitely many initial top simplices. Replacements leave their original common faces fixed, so all their finite trees can be completed. Any child whose image has fewer than $`k+1`$ distinct classes is automatically safe. Curves introduced in different simplices need not be mutually adjacent unless they occur together in a source simplex.

At termination, let $`M`$ be the finite union of the actual endpoint image simplices and their faces. It is not the full complex on the endpoint vertex set. Every simplex of $`M`$ is safe. The higher-dimensional simplices used to carry the homotopies are not inserted into this endpoint image.

## 7. Moving a safe finite image into the disjointness complex

The following finite replacement lemma supplies the entire safe-image homotopy. Its neighborhood and carrier argument is also given in [Proposition 1.3](01-finite-replacement.md); no separate proof package is required.

**Lemma 7.1.** If $`M\subset C_d(S_g)`$ is finite and $`I(\sigma)\leq B`$ for every simplex, there is a simplicial map $`r:\mathrm{sd}M\to C_0(S_g)`$ whose realization, followed by inclusion in $`C_d`$, is homotopic to the inclusion of $`M`$, fixing its original vertices.

**Proof.** Choose generic simultaneous minimum representatives for all vertices of $`M`$. For each nonempty face $`\sigma`$ choose a small proper regular neighborhood $`N_\sigma`$ of their union, with

```math
\tau\subsetneq\sigma\quad\Longrightarrow\quad
N_\tau\subset\mathrm{int}(N_\sigma).                    \qquad (16)
```

This is possible by descending induction: after its cofaces are chosen, choose the neighborhood of $`\tau`$ inside the finite intersection of their interiors, which is an open neighborhood of its fixed representative union. Regular neighborhoods can be chosen in any prescribed open neighborhood by small vertex disks, edge bands and annuli for isolated circles.

By §2.2 select an essential boundary component $`c_\sigma`$ of each $`N_\sigma`$. For a singleton it represents that same input vertex. Assign $`\sigma\mapsto[c_\sigma]`$ on the vertices of $`\mathrm{sd}M`$. Along an inclusion chain the boundary representatives are pairwise disjoint by (16), so this assignment is simplicial into $`C_0`$, allowing equal output classes.

To exhibit the relative homotopy, for each $`\sigma`$ let $`P_\sigma`$ be the full subcomplex of $`C_d`$ on the vertices of $`\sigma`$ together with all $`[c_\tau]`$, $`\varnothing\neq\tau\subseteq\sigma`$. The vertex $`[c_\sigma]`$ is disjoint from every one of these vertices, by (16) and the neighborhood definition. Flagness therefore makes $`P_\sigma`$ a cone. Incomparable face choices are not asserted to be adjacent to each other. Also $`P_\tau\subseteq P_\sigma`$ for $`\tau\subseteq\sigma`$.

The original map and the subdivided replacement of $`\lvert\sigma\rvert`$ both land in $`\lvert P_\sigma\rvert`$. Start with the constant homotopy on original vertices. Induct on the dimension of $`\sigma`$: its two endpoint maps and the already chosen homotopies on proper faces give a map from the boundary of $`\lvert\sigma\rvert\times[0,1]`$ into the cone $`\lvert P_\sigma\rvert`$. Extend over this ball by the cone contraction, keeping the boundary prescribed. The compatible finite gluing constructs the required homotopy. $`\square`$

Compose this homotopy with the finite endpoint source map from §6 and concatenate the previous stellar homotopies. Original vertices were unchanged in §6 and are fixed in Lemma 7.1. This proves Theorem A. A simplicial choice of the factor map on a subdivided source is also available: for the endpoint map $`f:K\to M`$, use $`r\circ\mathrm{sd}f`$. Under the subdivision homeomorphisms, $`f`$ and $`\mathrm{sd}f`$ are homotopic relative to vertices by straight-line homotopies in each image simplex, even when image faces collapse. Composing that homotopy with the continuous map from $`M`$ to $`C_0`$ gives the same required relative homotopy class; strict naturality of barycenters for degenerate maps is not assumed.

## 8. Connectivity and all parameter cases

The classical input used here is Harer's homotopy equivalence

```math
\lvert C_0(S_g)\rvert\simeq\bigvee S^{2g-2}.
```

Thus $`C_0(S_g)`$ is $`(B-1)`$-connected. This includes separating curve vertices. The precise source locators are listed in the [bibliography](../sources/bibliography.md).

Take a based map $`S^j\to\lvert C_d\rvert`$, $`1\leq j\leq k`$. Simplicial approximation for an arbitrary simplicial target gives a finite subdivided source, fixing a source basepoint vertex mapped to a curve vertex. Its finite image has dimension at most $`j`$. Theorem A moves this map into $`C_0`$ through a homotopy fixing the basepoint. No local finiteness assumption on the target is required.

If $`k\leq B-1`$, Harer's input null-homotopes every such resulting based map. This covers all parameters of (1) for $`g\geq3`$: $`k=1,2`$ are immediate; for $`k=3`$, $`B\geq3d`$ and evenness of $`B`$ gives $`B\geq4`$; for $`k\geq4`$, $`\binom{k}{2}\geq k+1`$, hence $`B\geq k+1`$. It also covers $`k=1`$ for $`g=2`$, irrespective of $`d`$.

For $`g=2`$, (1) can exceed this Harer range only when $`k=2`$ and $`d=1`$ or $`2`$. The target competition paper's Theorem 1.1 says that $`C_1(S_2)`$ is contractible. In the first case this directly suffices. In the second, the endpoint map into $`C_0(S_2)`$ factors under inclusion as

```math
C_0(S_2)\longrightarrow C_1(S_2)\longrightarrow C_2(S_2),
```

so it has a based null-homotopy inside the middle complex. This proves the stated genus-two supplement without assuming that adding simplices preserves connectivity.

Finally, path connectivity follows because $`C_0`$ is path connected and contains every vertex, and any point joins a vertex in its simplex. This proves Theorem B and its supplement.

If $`q_d(g)`$ is the largest nonnegative integer with $`d\binom{q_d(g)+1}{2}\leq B`$, the largest integer satisfying (1) is exactly $`q_d(g)+1`$. Solving the quadratic gives (2), with no rounding loss.

Examples of the new uniform lower bounds are:

| genus | intersection bound | direct-count bound | new bound |
|---:|---:|---:|---:|
| 3 | 1 | 2 | 3 |
| 3 | 2 | 1 | 2 |
| 4 | 2 | 2 | 3 |
| 6 | 3 | 2 | 3 |
| 7 | 2 | 3 | 4 |
| 2 | 2 | 1 | 2, using the stated genus-two input |
| any genus at least 2 | any integer greater than 2g−2 | 0 | 1 |

## 9. Scope and the remaining interface

The result does not assert optimal connectivity, contractibility in higher genus, or any upper bound on homotopy groups. For fixed $`d`$, (2) is $`2\sqrt{g/d}+O(1)`$. Its improvement is one degree; no leading-constant improvement is claimed. An inclusion $`C_d\subset C_{d+1}`$ is not used to transfer connectivity automatically.

Outside (1), proper source faces can exceed $`B`$. A stellar subdivision at such a nonmaximal face requires one new class adjacent to every vertex in every coface of its entire star. Proposition 4.1 controls only the colors in the selected face. The proof supplies neither those external adjacency inequalities nor strict decrease for all affected cofaces. Repeated subdivisions of top-dimensional faces alone leave a bad original proper face unchanged. This is an unclosed method interface, not a topological obstruction or a connectivity upper bound.

The [one-subdivision cutoff](04-method-cutoff.md) obstructs a universal common disjoint curve on every original simplex of a filling 1-system. It does not obstruct the changed-source construction here. No fixed-position simultaneous-disjointness assertion for arbitrary bounded-intersection systems is imported from the 1-system case. The proof uses the explicit neighborhood dichotomy and geometric upper bounds for newly constructed curves.

Classical inputs are simultaneous geodesic minimum position and homotopy versus isotopy of essential simple curves (Farb–Margalit); Harer's homotopy type for the full disjointness complex, including separating vertices; and Hatcher's simplicial approximation theorem, including its fixed-vertex form. The genus-two supplement alone also uses the target paper's Theorem 1.1. See the [source ledger](../sources/bibliography.md) for versions and printed locators. The finite independent-representatives lemma and the capacitated selection argument are proved in §3, without an external matroid theorem as a black box.

The [finite-check ledger](../checks/README.md) specifies computational coverage and limitations. The [review record](../sources/review-status.md) identifies the reviewed proof, the review report and this proof page by SHA-256. No formal verification, exhaustive novelty search or prize-eligibility determination is claimed.

[Main theorem and examples](03-connectivity.md).
