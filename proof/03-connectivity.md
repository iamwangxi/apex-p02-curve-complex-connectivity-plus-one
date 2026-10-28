# 3. One more degree of connectivity for every intersection bound

## Theorem A. Vertex-relative finite replacement

Let $`g\geq2`$, $`d\geq1`$ and $`k\geq1`$ be integers, and put $`B=2g-2`$. Assume

```math
d\binom{k}{2}\leq B. \qquad\text{(3.1)}
```

For every finite subcomplex $`L\subset C_d(S_g)`$ of dimension at most $`k`$, its inclusion is homotopic, fixing every original vertex, to a map factoring through $`C_0(S_g)`$. The same holds for any simplicial map from a finite source complex of dimension at most $`k`$, even if image faces collapse. The construction uses finitely many interior stellar subdivisions of maximal $`k`$-simplices, followed by barycentric subdivision of the finite endpoint image.

Each stellar replacement fixes its entire source boundary. The final safe-image homotopy fixes all original vertices; it is not asserted to fix every original higher-dimensional face.

## Connectivity consequence

For $`g\geq3`$, condition (3.1) implies that $`C_d(S_g)`$ is $`k`$-connected. For every $`g\geq2`$ and $`d\geq1`$, it is simply connected. In particular,

```math
\mathrm{conn}\,C_d(S_g)\geq
1+\left\lfloor\frac{\sqrt{1+8(2g-2)/d}-1}{2}\right\rfloor
\qquad(g\geq3). \qquad\text{(3.2)}
```

The target paper's Theorem 1.1, stating that $`C_1(S_2)`$ is contractible, extends the consequence and (3.2) to $`g=2`$. The only extra parameters under (3.1) are $`k=2,d=1,2`$. This external input is not used in Theorem A, in simple connectivity, or in any conclusion for $`g\geq3`$.

## Proof and exact dependencies

A complete proof for every $`d`$ is given in [bounded-intersection replacement](06-bounded-intersection.md):

1. Section 2 proves simultaneous generic minimum position, the essential-boundary/disk-complement dichotomy and the embedded realization of simple dual cycles.
2. Sections 3–4 prove the cographic rank formula, the independent-representatives lemma and the capacitated edge choice. At least $`F+1`$ edges are selected with at most $`d`$ per color, while deleting them leaves the primal graph connected. Every nonzero dual cycle on these edges is nonzero in surface mod-two homology, even when colors repeat.
3. Section 5 constructs a fresh essential class with geometric intersection at most $`d`$ with each input. Every cone facet has a strictly smaller total, including the one-face degree-one and two-face degree-two cases. Actual repeated-color crossings are used only as geometric upper bounds.
4. Section 6 performs the compatible maximal-simplex replacements. Each bad descendant reduces its integer excess, initially at most $`dk`$; a tree has branching $`k+1`$ and bounded depth. All proper source faces remain safe at every stage. The endpoint complex includes only actual image simplices and their faces.
5. Section 7 proves the safe-image homotopy with nested neighborhoods and finite cone carriers, including the vertex-relative form for degenerate source maps. It supplies this input within the repository, as does [Proposition 1.3](01-finite-replacement.md).
6. Section 8 applies based simplicial approximation and Harer's $`(B-1)`$-connectivity for $`C_0`$. All parameters for $`g\geq3`$ satisfy $`k\leq B-1`$. For the two genus-two exceptions, a map moved into $`C_0(S_2)`$ is null-homotopic in $`C_1(S_2)\subset C_d(S_2)`$ using the explicitly stated external input.

For $`d=1`$, [rainbow descent](02-rainbow-descent.md) gives a separate specialized descent proof. For larger $`d`$, the selected cycle may repeat a color, and the homology argument of Section 4 is essential.

## Corollary B. Uniform 3-connectivity at intersection bound one

For every $`g\geq2`$, $`C_1(S_g)`$ is 3-connected.

**Proof.** For $`g\geq3`$, apply Theorem A and its connectivity consequence with $`d=1,k=3`$. For $`g=2`$, use the target paper's contractibility theorem, Theorem 1.1, p. 2. The genus-two part of this corollary is stronger than the numerical range (3.1) and has this separate dependency. $`\square`$

## Bounds and examples

If $`q_d(g)`$ is the largest nonnegative integer satisfying $`d\binom{q_d(g)+1}{2}\leq B`$, the largest integer allowed by (3.1) is exactly $`q_d(g)+1`$. Thus (3.2) is one degree above the [direct-count bound](01-finite-replacement.md), even when $`d>B`$ and that bound gives only degree zero. For fixed $`d`$, the leading term remains $`2\sqrt{g/d}`$.

Examples are 3-connectivity for $`(g,d)=(3,1)`$, 2-connectivity for $`(3,2)`$, 3-connectivity for $`(4,2)`$ and $`(6,3)`$, and 4-connectivity for $`(7,2)`$. At $`d=1`$ the bound is 4 in genera four and five, 5 in genus six, and $`2m`$ in genus $`m^2`$ for $`m\geq2`$. These are lower bounds, not assertions about a first nonzero homotopy group or optimality.

The [one-subdivision method cutoff](04-method-cutoff.md) and [covering cost obstruction](05-covering-tower.md) describe separate method interfaces. Neither gives a connectivity upper bound.
