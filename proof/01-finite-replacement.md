# 1. Finite replacement and the direct intersection-count bound

Let $`S_g`$ be closed, connected and orientable with $`g\geq2`$. Curves are unoriented isotopy classes of embedded essential circles; essential means not bounding a disk. Write $`i(a,b)`$ for geometric intersection and put $`i(a,a)=0`$. For an integer $`d\geq0`$, $`C_d(S_g)`$ is the flag complex whose distinct vertices are adjacent when $`i(a,b)\leq d`$. In particular $`C_0`$ is the disjointness complex. All realizations have the weak topology. Repeated image classes are identified.

For a simplex put

```math
I(\sigma)=\sum_{\{a,b\}\subset\sigma}i(a,b),\qquad B=2g-2.
```

Write $`J:|C_0(S_g)|\longrightarrow|C_d(S_g)|`$ for inclusion. A space is $`k`$-connected if it is path connected and its homotopy groups in degrees one through $`k`$ vanish.

## Lemma 1.1. Essential boundary and the neighborhood dichotomy

Here and below a regular neighborhood of an embedded finite graph means a compact subsurface containing the graph in its interior and deformation retracting onto it. Such neighborhoods can be taken inside any prescribed open neighborhood of the graph. For completeness, take small disks about the finitely many graph vertices and thin bands along its edges, add thin annuli about any isolated circle components, and round the corners. The disks and bands may all be chosen inside the prescribed open set. No extra components are added.

**Statement.** Let $`A`$ be a nonempty finite collection of essential embedded circles in $`S_g`$. Suppose intersections are transverse double points, with no triple points, and let $`I`$ be the total number of intersection points in their union $`G`$. If $`I\leq 2g-2`$, every sufficiently small regular neighborhood $`N`$ of $`G`$ has an essential boundary component. The collection and its union need not be connected; different members may be isotopic.

**Proof.** We first compute $`\chi(G)`$ without assuming connectedness or the existence of any intersections. Let $`z`$ be the number of isolated circle components of $`G`$. Give each of these one artificial vertex and one edge. Every intersection vertex has degree four. Consequently

```math
V=I+z,\qquad E=2I+z,\qquad \chi(G)=V-E=-I.
```

The formula also holds when $`I=0`$: the graph is then a disjoint union of circles. Since $`N`$ retracts onto $`G`$,

```math
\chi(N)=-I.
```

Let $`N`$ be any proper regular neighborhood as above. Properness can be ensured by taking the neighborhood sufficiently small, since $`G`$ is a finite embedded graph in a surface. Every connected component of $`N`$ contains at least one of the original essential circles: every component of $`G`$ contains a whole input circle, and the regular neighborhood introduces no new components.

Suppose, for a contradiction, that every component $`\beta`$ of $`\partial N`$ is inessential. On a closed surface of positive genus, $`\beta`$ bounds a unique embedded disk $`D_\beta`$. The interior of the component of $`N`$ incident to $`\beta`$ lies entirely on one side of $`\beta`$. It cannot lie on the disk side, since it contains a circle essential in $`S_g`$, and every embedded circle contained in a disk is inessential in $`S_g`$.

No other component of $`N`$ can lie inside $`D_\beta`$, for the same reason. A connected component of $`N`$ disjoint from $`\beta`$ cannot straddle its two sides. It follows that

```math
\mathrm{int}(D_\beta)\cap N=\varnothing.
```

Thus $`D_\beta`$ is a complementary disk, not merely a disk that may contain other components of the curve system. In particular the disks for different boundary components have disjoint interiors: a nested disk would place a boundary component of $`N`$ inside a disk whose interior misses $`N`$.

Let $`M=\overline{S_g\setminus N}`$. Every component of $`M`$ has nonempty boundary, because $`S_g`$ is connected and $`N`$ is nonempty. For any boundary component $`\beta`$ of such a component, its disk $`D_\beta`$ is exactly that complementary component; one cannot leave its interior through $`\beta`$, which belongs to $`N`$. Hence all components of $`M`$ are disks. If their number is $`F`$, then $`F\geq1`$ because $`N`$ is proper. Additivity of Euler characteristic along boundary circles gives

```math
2-2g=\chi(S_g)=\chi(N)+\chi(M)=-I+F.
```

Therefore $`I=2g-2+F\geq2g-1`$, contradicting the hypothesis. At least one boundary component is essential. $`\square`$

The proof also gives the dichotomy: if no boundary circle is essential, every complementary component is a disk and $`F=I-B\geq1`$. The same count rules out filling: if the curve system filled the closed surface, its regular-neighborhood complement would consist of disks and the displayed equality would again force $`I\geq2g-1`$. The assertion about essential boundary is stronger than merely invoking a non-filling criterion and is proved directly above. The argument accommodates zero-intersection components and disconnected systems throughout.

There is no multiplicity issue in subsequent applications. A vertex denotes a class, and each class receives one representative. If a source map sends several vertices to the same class, that class appears only once in an image simplex. If instead one works with separate parallel representatives of a repeated class, the lemma still applies to their actual double-point count. Coincident copies of one geometric curve are first identified; they are not counted as distinct branches of a graph.

## Lemma 1.2. Simultaneous generic representatives

**Statement.** For a finite set $`V`$ of distinct vertices of the curve complex, representatives $`a_v`$, $`v\in V`$, can be chosen so that each is embedded, every two intersect in exactly $`i(v,w)`$ transverse points, and no point lies on three representatives.

**Proof.** Give $`S_g`$ a hyperbolic metric and choose the simple closed geodesic representing each class. Distinct simple closed geodesics are simultaneously in pairwise minimal position; see Farb–Margalit, Corollary 1.9 and the paragraph following it, printed p. 33. For essential simple curves, homotopy and isotopy agree by Proposition 1.10, printed p. 34.

Two distinct geodesics cannot have a tangency: equal position and tangent would determine the same geodesic. Their intersections are therefore transverse and finite. There may initially be points at which three or more geodesics pass.

Choose disjoint small disks about these finitely many multiple points. Each incident curve contributes one embedded arc in such a disk, with distinct tangent direction, and each pair of incident arcs has exactly one transverse crossing there. All other parts of the finite family can be kept unchanged.

Here is a concrete local perturbation. In geodesic normal coordinates centered at a multiple point, the incident geodesic arcs are straight lines through the origin. Write their equations as $`\ell_s(x)=0`$, with pairwise independent normal directions. In a smaller concentric disk replace them by $`\ell_s(x)=\varepsilon_s`$. Choose the offsets arbitrarily small and outside the finitely many hyperplanes in offset space which express concurrence of some three lines. Each pair still has exactly one intersection; its position tends to the origin as the offsets tend to zero, so all these intersections can be kept in the smaller disk. Join the shifted arcs smoothly to the original arcs using a cutoff supported in the larger disk, leaving them unchanged near its boundary. The joins can be made arbitrarily small in $`C^1`$. No triple intersection remains in the smaller disk, and sufficiently small joins introduce no intersections in the intervening region.

The pairwise counts remain unchanged. Each original pairwise crossing persists as a unique crossing under sufficiently small $`C^1`$ perturbation, by transversality. Outside small neighborhoods of these crossings, the two compact arcs are separated, so sufficiently small perturbations introduce no new crossing. Embeddedness of each individual arc and curve is preserved as well. Because the family is finite, the perturbations can be made small enough for all these requirements at once. These modifications are isotopies of the individual curves, so their classes remain unchanged. The number of crossings of each pair is still its original geometric intersection number, and hence the new representatives remain pairwise minimal. $`\square`$

The removal of triple points is an elementary local argument supplied here; the cited Farb–Margalit passage supplies simultaneous minimal position, not a separate claim about triple points. At a point incident to $`m`$ distinct curves, the perturbation creates $`\binom m2`$ distinct double points in place of the multiple point, preserving the contribution to each pairwise count. It does not assert preservation of the number of distinct geometric points before the perturbation.

## Proposition 1.3. Relative finite replacement

**Statement.** Let $`L\subseteq C_d(S_g)`$ be a finite subcomplex. Choose the representatives of its vertex set as in Lemma 1.2. Assume that for every nonempty simplex $`\sigma\in L`$,

```math
I_\sigma:=\sum_{\{v,w\}\subseteq\sigma}i(v,w)\leq2g-2.
```

There exist a simplicial map

```math
r:\mathrm{sd}\,L\longrightarrow C_0(S_g)
```

and a homotopy, fixed on every vertex of $`L`$,

```math
u\simeq J\circ |r|\circ h_L^{-1},
```

where $`u:|L|\hookrightarrow |C_d(S_g)|`$ is the inclusion and $`h_L:|\mathrm{sd}\,L|\to |L|`$ is the canonical subdivision homeomorphism.

**Proof.** We construct all choices on the image subcomplex $`L`$ itself, so a shared face receives one choice regardless of which coface or source simplex contains it.

### 1.3.1. Nested neighborhoods

For a nonempty simplex $`\sigma`$, let

```math
G_\sigma=\bigcup_{v\in\sigma}a_v.
```

After Lemma 1.2 its actual double-point count is $`I_\sigma`$. For each such simplex choose a proper compact regular neighborhood $`N_\sigma`$ with $`G_\sigma\subset\mathrm{int}(N_\sigma)`$, requiring

```math
\tau\subsetneq\sigma\quad\Longrightarrow\quad
N_\tau\subset\mathrm{int}(N_\sigma).
```

These choices exist by descending induction on simplex dimension. After all strict cofaces of $`\tau`$ have been treated, the finite intersection

```math
U_\tau=\bigcap_{\substack{\sigma\in L\\\tau\subsetneq\sigma}}
\mathrm{int}(N_\sigma)
```

is an open neighborhood of $`G_\tau`$: the common representatives give $`G_\tau\subseteq G_\sigma\subset\mathrm{int}(N_\sigma)`$ for every coface. If there is no strict coface, take $`U_\tau=S_g`$. The elementary regular-neighborhood construction in Lemma 1.1 gives $`N_\tau\subset U_\tau`$. Only finitely many cofaces are involved. No compatibility between incomparable faces is required.

By Lemma 1.1 choose an essential boundary component $`c_\sigma\subset\partial N_\sigma`$ for each nonempty $`\sigma`$. For a singleton $`\sigma=\{v\}`$, $`N_\sigma`$ is an annulus about $`a_v`$, and either boundary component represents $`v`$. Thus

```math
[c_{\{v\}}]=v.
```

### 1.3.2. The subdivision map

A vertex of $`\mathrm{sd}\,L`$ is a nonempty simplex $`\sigma`$ of $`L`$. Define

```math
r(\sigma)=[c_\sigma].
```

A simplex of $`\mathrm{sd}\,L`$ is a strict inclusion chain $`\sigma_0\subsetneq\cdots\subsetneq\sigma_m`$. For $`a\lt b`$, the curve $`c_{\sigma_a}`$ lies in $`N_{\sigma_a}\subset\mathrm{int}(N_{\sigma_b})`$, whereas $`c_{\sigma_b}`$ lies on its boundary. These actual representatives are disjoint. Thus the distinct classes in the list $`[c_{\sigma_0}],\ldots,[c_{\sigma_m}]`$ span a simplex of $`C_0(S_g)`$. This defines a simplicial map, including when some of the classes coincide: a simplicial map may collapse a simplex to a lower-dimensional simplex.

### 1.3.3. Cone carriers

For each nonempty $`\sigma\in L`$, form the finite vertex set

```math
W_\sigma=\sigma\ \cup\ 
\{[c_\tau]:\varnothing\neq\tau\subseteq\sigma\}
```

and let $`P_\sigma`$ be the full subcomplex of $`C_d(S_g)`$ spanned by $`W_\sigma`$. Let $`b_\sigma=[c_\sigma]`$.

The vertex $`b_\sigma`$ has intersection number zero with every vertex of $`W_\sigma`$. It is disjoint from all $`a_v`$ for $`v\in\sigma`$, since these curves lie in $`\mathrm{int}(N_\sigma)`$. For a proper face $`\tau`$ of $`\sigma`$, it is disjoint from $`c_\tau`$ by nesting. Equality of classes causes no problem because $`i(b_\sigma,b_\sigma)=0`$.

Since $`C_d(S_g)`$ is flag and $`P_\sigma`$ is full, every simplex $`\eta`$ of $`P_\sigma`$ extends to the simplex $`\eta\cup\{b_\sigma\}`$. Consequently $`P_\sigma`$ is a simplicial cone with apex $`b_\sigma`$. In particular its realization is contractible; its contraction is the linear contraction of each point to $`b_\sigma`$ inside the enlarged simplex.

This does **not** assert that all the other vertices of $`W_\sigma`$ span a simplex. Curves associated to incomparable faces may intersect more than $`d`$. The cone assertion needs only a universal adjacent apex and the flag property.

Also, if $`\tau\subseteq\sigma`$, then $`W_\tau\subseteq W_\sigma`$, and fullness gives

```math
P_\tau\subseteq P_\sigma.
```

Set $`q=J\circ |r|\circ h_L^{-1}`$. The map $`u`$ sends $`|\sigma|`$ into $`|P_\sigma|`$, because its vertices are in $`\sigma`$. The map $`q`$ sends $`|\sigma|`$ into $`|P_\sigma|`$, because the subdivision of $`\sigma`$ uses only vertices corresponding to its nonempty faces. For a vertex $`v`$, both maps take the value $`v`$, and $`P_{\{v\}}`$ is the single point $`v`$.

### 1.3.4. An explicit relative carrier argument

We construct $`H:|L|\times[0,1]\to |C_d(S_g)|`$ such that

```math
H(-,0)=u,\qquad H(-,1)=q,\qquad
H(|\sigma|\times[0,1])\subseteq |P_\sigma|.
```

On each vertex prism set $`H(v,t)=v`$ for all $`t`$. Suppose the homotopy has already been constructed on prisms over all proper faces of an $`m`$-simplex $`\sigma`$, with $`m\geq1`$. On

```math
B_\sigma=(|\sigma|\times\{0,1\})\ \cup\ 
(|\partial\sigma|\times[0,1])
```

we have a well-defined continuous map: use $`u`$ at the bottom, $`q`$ at the top, and the already constructed face homotopies on the sides. The maps agree on intersections because the face homotopies have those prescribed endpoints and were constructed once for each face. The whole boundary map lands in $`|P_\sigma|`$, since every proper-face carrier is a subcomplex of $`P_\sigma`$.

The prism $`|\sigma|\times[0,1]`$ is a closed $`(m+1)`$-ball with boundary $`B_\sigma`$. Its boundary map extends to this ball using the cone contraction of $`|P_\sigma|`$. More explicitly, identify the prism with the cone on its boundary by choosing an interior point and using radial segments. On a segment from a boundary point $`x`$ to this interior point, map the segment to the cone segment from the prescribed value $`H(x)`$ to $`b_\sigma`$. The apex condition guarantees that this segment lies in $`|P_\sigma|`$; the result is continuous, including at the interior point. It retains the previously assigned map on the entire boundary.

Do this for each $`m`$-simplex and continue in increasing dimension. Two same-dimensional simplex prisms intersect only in prisms over their common faces, where the map has already been fixed. The finite gluing produces a continuous homotopy on $`|L|\times[0,1]`$. Its vertex restrictions are the original constant homotopies. This proves the proposition. $`\square`$

Only the explicitly exhibited finite cones $`P_\sigma`$ were used to extend the homotopy. No assertion about contractibility or connectivity of a link in $`C_d(S_g)`$ is involved. Nor is the construction a global retraction of $`C_d`$ onto $`C_0`$: it depends on the chosen finite subcomplex.


## Corollary 1.4. Direct connectivity range

For integers $`d\geq1`$ and $`k\geq1`$,

```math
d\binom{k+1}{2}\leq B\quad\Longrightarrow\quad C_d(S_g)\text{ is }k\text{-connected}.
```

**Proof.** Harer's classical input is

```math
|C_0(S_g)|\simeq\bigvee S^{2g-2}.
```

The inspected source is Harer's expository chapter: $`Z_g^0`$ on p. 170, Lemma 3.6 on p. 171 and Theorem 4.1 on p. 176. It includes separating curves. Thus $`C_0(S_g)`$ is $`(2g-3)`$-connected. Harer's Lemma 4.3, pp. 178–179, is also a precedent for regular-neighborhood boundary replacement and subdivision homotopies. Those methods are not claimed as new here.

The proposed range lies within Harer's: for $`k=1`$, $`k\leq2g-3`$; for $`k\geq2`$, $`k+1\leq\binom{k+1}{2}\leq d\binom{k+1}{2}\leq B`$.

Take a based sphere map of dimension $`1\leq j\leq k`$, with a curve vertex as basepoint. Hatcher's Theorem 2C.1, p. 177, gives a simplicial approximation from a finite subdivision to an arbitrary simplicial target. The observation on p. 179 allows the basepoint vertex to stay fixed. Let $`L`$ be the finite union of the actual image simplices and their faces, of dimension at most $`j`$. Each image face has total intersection at most $`d\binom{j+1}{2}\leq B`$. Proposition 1.3 moves its inclusion into $`C_0`$, fixing the basepoint. Harer's connectivity supplies a based null-homotopy there, which remains a null-homotopy in $`C_d`$.

Finally $`C_0`$ is path connected and contains all vertices, and every point of $`C_d`$ joins a vertex inside its simplex. ∎

For $`d=1`$ this gives the baseline bound

```math
q(g)=\left\lfloor\frac{\sqrt{16g-15}-1}{2}\right\rfloor.
```

## Lemma 1.5. Minimal position against a fixed 1-system

If fixed generic essential circles $`a_1,\ldots,a_n`$ meet pairwise at most once, every essential class $`c`$ has a representative simultaneously realizing all $`i(c,a_i)`$.

**Proof.** Minimize the nonnegative integer $`\sum_i\#(\gamma\cap a_i)`$ over generic simple representatives of $`c`$, avoiding the fixed crossings. If $`\gamma,a_i`$ are not minimal, the bigon criterion gives an innermost bigon with sides $`u\subset\gamma`$, $`v\subset a_i`$. Every other $`a_j`$ meets $`v`$ at most once. If it meets $`v`$ once, parity of intersection with the disk boundary forces a crossing with $`u`$; if it misses $`v`$, the inequality is automatic. Thus $`\#(a_j\cap v)\leq\#(a_j\cap u)`$. Pushing $`u`$ across the bigon decreases the contribution from $`a_i`$ by two and increases no other contribution. This contradicts minimality. See Farb–Margalit, Proposition 1.7, pp. 30–33, for the bigon criterion. ∎

A 1-system **fills** if no essential class is disjoint from all its members. Lemma 1.5 shows that disk complementary regions of a fixed 1-system imply filling of its classes. Conversely a common disjoint class can be realized disjoint from the fixed union.

[Next: rainbow curves and strict descent](02-rainbow-descent.md).
