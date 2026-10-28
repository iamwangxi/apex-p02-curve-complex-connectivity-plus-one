# 5. Covering towers and the cost of a new curve

## Proposition C. No universal constant intersection cost

There are filling 1-systems $`\mathcal A_h`$ on surfaces of genera $`g_h\to\infty`$, with $`n_h=\#\mathcal A_h=o(g_h)`$, total intersections $`I_h`$, and disk-face counts $`F_h`$, such that

```math
I_h=3(g_h-1),\qquad F_h=g_h-1,
```

and, for every essential curve class $`c`$,

```math
\sum_{a\in\mathcal A_h}i(c,a)\geq2^{\lfloor h/2\rfloor}.
```

This is a lower bound on intersection cost, not an upper bound on connectivity. The family does not have $`n_h=O(\sqrt{g_h})`$.

## 5.1. A complete ribbon specification for the initial system

Use indices $`i\in\mathbb Z/3`$, $`j\in\mathbb Z/2`$, and $`\epsilon_j=(-1)^j`$. At each vertex $`v_{ij}`$ introduce outgoing darts $`A_{ij}^{\pm}`$, $`B_{ij}^{\pm}`$. For signs $`s=\pm1`$, specify the edge involution and rotation by

```math
\alpha(A_{ij}^{s})=A_{i,j+s}^{-s},\qquad
 \alpha(B_{ij}^{s})=B_{i+s,j}^{-s},\qquad
 \rho=(A_{ij}^{+},B_{ij}^{\epsilon_j},A_{ij}^{-},B_{ij}^{-\epsilon_j}).
```

Take oriented vertex disks and untwisted edge bands in this cyclic order, then cap every boundary circle with a disk. The graph is connected. Joining opposite darts in each vertex disk gives embedded circles $`A_0,A_1,A_2,B_0,B_1`$; each $`A_i`$ visits its two vertices once, each $`B_j`$ its three vertices once. The groups are internally disjoint, and $`A_i`$ meets $`B_j`$ once, at $`v_{ij}`$. Parallel edges for $`j\in\mathbb Z/2`$ are retained as distinct bands.

For the face permutation $`\phi=\rho\alpha`$, direct calculation gives

```math
\phi^2(A_{ij}^{s})=A_{i+s\epsilon_j,j+s}^{-s},\qquad
 \phi^4(A_{ij}^{s})=A_{i+2s\epsilon_j,j}^{s}.
```

A return to an $`A`$-dart requires a multiple of four steps. The increment two has order three modulo three, so each face orbit has length twelve. All 24 darts therefore give exactly two faces. There are six vertices and twelve edges; capping yields Euler characteristic $`6-12+2=-4`$, hence genus three. The complement of a sufficiently small regular neighborhood consists of the two embedded disks; no assertion that a face closure in the graph is embedded is needed.

Every input has mod-two intersection one with an input of the other group. Thus it is essential and nonseparating, and the displayed single crossings realize geometric intersection one. Across the two groups, intersection one excludes equality of classes. Within a group, if two circles were parallel, choose consecutive parallel circles bounding an annulus containing no circle of that group. All arcs of the other group in this annulus span it: each of those circles crosses each boundary once. They cut the annulus into four-sided disk faces. There are no other graph arcs inside, contradicting the fact that every face has length twelve. This also excludes parallel circles in the other group. The five classes are distinct. Lemma 1.5 proves that their disk complements imply filling of the classes.

## 5.2. Intersection cost and the dual graph

For a cellular 1-system, let $`s(D)`$ be the minimum length of an edge walk in its embedded dual graph that is noncontractible in the surface. This is the dual systole used here. It is finite because the graph is cellular. A test curve minimized by Lemma 1.5 traces a homotopic dual closed walk through the complementary disks, with length its total geometric intersection. Therefore

```math
\sum_i i(c,a_i)\geq s(D)\qquad(c\text{ essential}). \qquad\text{(5.1)}
```

The walk need not be rainbow; the estimate applies to all essential classes.

## 5.3. Two successive homology covers

For a closed genus-$`g`$ surface, its full mod-two homology cover is the connected regular cover associated to

```math
\ker\bigl(\pi_1(S)\longrightarrow H_1(S;\mathbb F_2)\bigr),
```

of degree $`2^{2g}`$. A simple essential curve has a closed degree-one lift exactly when its mod-two homology class is zero, equivalently when it is separating.

**Lemma 5.2.** Every degree-one lift of an essential separating curve to this full homology cover is nonseparating.

**Proof.** Cut the base along the curve into surfaces of positive genera $`r,t`$, each with one boundary. Their homology images give a direct sum $`U\oplus V=H_1(S;\mathbb F_2)`$. Components over the first side are indexed by $`V`$, and components over the second by $`U`$. The boundary lift indexed by $`(u,v)`$ joins precisely those two components. Thus their gluing graph is the complete bipartite graph $`K_{|U|,|V|}`$, with $`|U|,|V|\geq4`$. No edge of this graph is a bridge. Cutting one boundary lift therefore leaves the covered surface connected. $`\square`$

**Lemma 5.3.** For a cellular embedded graph $`D`$, lift it through two successive full homology covers to $`D''`$. Then

```math
s(D'')\geq2s(D).
```

**Proof.** Any shortest essential edge walk in any of these graphs is a simple cycle: a repeated vertex splits it into two shorter loops, at least one essential. Covering projection also gives $`s(D')\geq s(D)`$.

Suppose a shortest essential cycle in $`D''`$ has length $`L<2s(D)`$. Its projection to $`D'`$ cannot repeat a vertex. Such a repetition would split the projected walk into two loops, both noncontractible: a contractible subloop would lift with equal endpoints and contradict simplicity upstairs. Each would have length at least $`s(D')\geq s(D)`$, impossible. The projection is therefore an embedded essential circle $`\gamma'`$, mapped with degree one. It lifts closed to the homology cover, so it is separating in $`S'`$.

Apply the same argument to its projection to $`D`$. If that projection repeated a vertex, the two subloops would be essential in the base, again contradicting $`L<2s(D)`$. Thus it is an embedded essential circle $`\gamma`$, with a closed degree-one lift $`\gamma'`$. It is separating in the base. Lemma 5.2 says its lift $`\gamma'`$ is nonseparating, contradicting the preceding paragraph. $`\square`$

## 5.4. Proof of Proposition C

Start with the system of Section 5.1, of genus $`g_0=3`$, with five curves, six crossings, and two twelve-sided faces. Inductively take the full mod-two homology cover of $`S_h`$, and let $`\mathcal A_{h+1}`$ be all components of the preimages of the curves in $`\mathcal A_h`$. Put $`d_h=2^{2g_h}`$.

Every input is nonseparating and meets some other input once. It has nonzero homology and therefore $`d_h/2`$ lifts, each a double cover of that circle. For two inputs crossing once, their homology vectors are independent: their intersection pairing is one. Two corresponding cosets of their order-two monodromy subgroups meet in at most one element. Hence any pair of their lifts crosses at most once. Lifts of disjoint inputs remain disjoint. Each lifted curve meets another lift once and is essential and nonseparating.

The two original disjoint groups remain two disjoint groups upstairs. Their classes are distinct. Across groups, a hypothetical equality would contradict the existence of a crossing with a member of the other disjoint group. Within one group, choose consecutive hypothetical parallel curves, so their annulus contains no curve of that group. The annulus argument of Section 5.1 applies: every arc from the other group entering an annulus between consecutive parallel curves must span it. An arc with both endpoints on one boundary would cross that boundary curve twice, contrary to the 1-system property; an entire essential input cannot lie in the annulus without being parallel to its boundary and disjoint from the first group. The spanning arcs yield four-sided complementary faces, whereas every lifted face still has length twelve. This contradiction excludes parallel classes. Lemma 1.5 then certifies filling of the classes.

Covering multiplies Euler characteristic, crossings, and disk faces by $`d_h`$. Thus

```math
g_{h+1}-1=d_h(g_h-1),\quad
 n_{h+1}=\frac{d_h}{2}n_h,\quad
 I_h=3(g_h-1),\quad F_h=g_h-1,
```

and in particular

```math
\frac{n_h}{g_h-1}=\frac{5}{2^{h+1}}\longrightarrow0.
```

The dual graphs are exactly the corresponding graph lifts. Lemma 5.3 gives $`s(D_h)\geq2^{\lfloor h/2\rfloor}s(D_0)\geq2^{\lfloor h/2\rfloor}`$. Equation (5.1) proves Proposition C. $`\square`$

For any prescribed constants $`\varepsilon>0`$ and $`R`$, some system in this tower has $`n_h\leq\varepsilon g_h`$ and no essential curve of total intersection cost at most $`R`$. This refutes a universal constant-cost strategy in that range. It does not refute a growing-cost descent, and it does not obstruct a bound restricted to $`n\leq C\sqrt g`$ for fixed $`C`$.


For completeness the size restriction in Proposition C is strict. Since $`d_h\geq64`$, the recurrence gives $`g_h-1\geq2\cdot64^h`$. Combining this with $`n_h/(g_h-1)=5/2^{h+1}`$ yields $`n_h/\sqrt{g_h}\to\infty`$. Thus these systems cannot rule out a constant-cost assertion restricted to $`n\leq C\sqrt g`$ with fixed $`C`$.

The covering inputs are elementary classification of connected covers and cellular mod-two homology, as in Hatcher, Theorem 1.38, p. 67; Proposition 1.39, p. 71; Example 2.36, p. 141; and Theorem 2A.1, p. 166. Lemmas 5.2 and 5.3 supply the quantitative assertions, rather than invoking an unchecked systolic theorem.

[Repository overview](../README.md).
