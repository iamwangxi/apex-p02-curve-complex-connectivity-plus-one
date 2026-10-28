# 4. The cutoff for one barycentric subdivision

The following comparison concerns specified replacement data. It gives no upper bound on the connectivity of the ambient curve complex.

Let $`f_1(g)`$ be the minimum cardinality of a filling 1-system, where filling has the class-level meaning in Lemma 1.5. Let $`\mathcal R_g(k)`$ mean that every finite subcomplex $`L\subset C_1(S_g)`$ of dimension at most $`k`$ admits a simplicial map

```math
r:\mathrm{sd}L\longrightarrow C_0(S_g)
```

fixing all original vertices, whose realization followed by inclusion is homotopic to the original inclusion, relative to those vertices. The source here is exactly one barycentric subdivision.

## Proposition 4.1. Exact interface in terms of the minimum filling size

```math
\mathcal R_g(k)\quad\Longleftrightarrow\quad k\leq f_1(g)-2.
```

**Proof.** If a simplex $`\sigma`$ fills, its subdivision vertex corresponding to the whole face is adjacent to the vertex for every singleton $`\{a\}`$. A simplicial map to $`C_0`$ fixing those singletons would therefore supply $`r(\sigma)`$ disjoint from every $`a\in\sigma`$, contradicting filling. Collapsed edges do not help, since $`i(a,a)=0`$. Taking a minimum filling simplex disproves $`\mathcal R_g(k)`$ whenever $`k\geq f_1(g)-1`$.

Conversely, when $`k\leq f_1(g)-2`$, each face of each allowed $`L`$ has fewer than $`f_1(g)`$ vertices and is non-filling. Fix simultaneous representatives by Lemma 1.2. Lemma 1.5 realizes a common disjoint class away from the fixed union for each face; that union cannot have only disk complements. The neighborhood dichotomy in Lemma 1.1 therefore gives an essential boundary. The nested-neighborhood, subdivision-map and cone-carrier proof of Proposition 1.3 applies verbatim: its numerical hypothesis was used only to obtain these essential boundary components. This proves the map and relative homotopy for every such $`L`$. ∎

## Published filling bounds and attribution

Anderson–Parlier–Pettet, *Small filling sets of curves on a surface*, Theorem 1 and Corollary 2, give the relevant extremal size. Put

```math
N(g)=\left\lceil\frac{1+\sqrt{16g-7}}2\right\rceil.
```

Their $`K=1`$ result gives

```math
N(g)\leq f_1(g)\leq N(g)+1,\qquad f_1(g)\sim2\sqrt g.
```

Consequently the exact cutoff $`b(g)=f_1(g)-2`$ satisfies

```math
N(g)-2\leq b(g)\leq N(g)-1,\qquad b(g)=2\sqrt g+O(1).
```

Thus the sharp leading square-root size of this method obstruction follows from their published construction and Euler lower bound. It is not an additional new filling-size theorem of this manuscript. The displayed bounds do not choose between the two possible integer cutoffs at every genus. Przytycki's maximal-system size estimates concern a different extremal quantity and are not homotopy inputs here.

## How Theorem A changes the source

Theorem A retains the original vertices but permits repeated interior stellar subdivisions before the final barycentric subdivision. After the first interior stellar subdivision of a top simplex, none of its child simplices contains all the old vertices. Subsequent interior stellar subdivisions do not restore such a simplex. The final barycentric subdivision therefore need not have a vertex joined to every original singleton of that top simplex. Proposition 4.1 does not apply to this different source interface.

The geometric reason the iteration closes is equally specific: under $`\binom k2\leq B`$, all proper faces remain within the intersection-count range throughout. Only maximal top faces need repair, so each local homotopy fixes its whole boundary. Outside that range, a bad proper face can occur. Replacing it requires the same new curve to be adjacent to every image vertex in every coface in its star. A curve constructed from one face alone does not supply that guarantee. Top-dimensional subdivisions alone leave a bad original proper-face map unchanged. No further uniform connectivity gain follows by simply repeating the theorem as a black box.

Neither an empty common-disjointness complex nor the covering obstruction in the next file produces a nonzero homotopy class in $`C_1`$. A filling simplex itself remains contractible.

[Next: covering towers and intersection cost](05-covering-tower.md).
