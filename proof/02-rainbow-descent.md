# 2. Rainbow curves and strict descent

Throughout this file, $`B=2g-2`$. In the disk-complement case of Lemma 1.1, form the embedded dual multigraph $`D`$. Its vertices are the complementary disks of a thin regular neighborhood. Every band along an input-graph edge gives a dual edge crossing the band once, colored by that input curve. Loops and parallel edges are retained.

**Lemma 2.1.** A simple dual cycle with $`r`$ edges of distinct colors gives an embedded essential curve $`c`$ with intersection one with exactly those $`r`$ input curves, and zero with all other inputs.

**Proof.** Use a transverse co-core in each selected band. In each visited complementary disk join the incoming and outgoing endpoints by one properly embedded arc. A simple cycle visits each disk once, so these arcs, together with the distinct band co-cores, give an embedded circle after smoothing. This includes a loop, using one disk, and a two-edge cycle, using two disks. No assertion that a face closure in $`S_g\setminus G`$ is embedded is needed: the complementary disks of $`N`$ really are embedded.

Each selected color occurs once, so the constructed curve has mod-two intersection one with that input circle. Hence it is essential, and its geometric intersection with that class cannot drop below one. All unselected classes have disjoint representatives. Thus the actual crossing pattern is the geometric one. $`\square`$

Call such a cycle *rainbow*. Any contractible circle has even intersection with every closed curve, so a nonempty rainbow cycle cannot represent a contractible loop.

**Lemma 2.2.** A multigraph with $`F`$ vertices and more than $`F`$ edges contains a cycle of length at most $`F`$. If $`F\geq3`$, it contains one of length at most $`F-1`$.

**Proof.** More than $`F-1`$ edges cannot form a forest. If a shortest cycle has length $`F`$, it uses every vertex. An extra edge is a loop, a parallel edge, or a chord, and gives a shorter cycle when $`F\geq3`$. A triangle has no unused simple chord, so its extra edge must be a loop or parallel edge. $`\square`$

Choosing one dual edge of each input color makes every cycle in the chosen multigraph rainbow.

## Lemma 2.3. Two-face parity

If the dual graph has two vertices and no loop, every primal graph edge has one side in each complementary disk. Retract the boundary of one disk onto $`G`$. Modulo two it uses every graph edge once, hence represents $`\sum_a[a]`$, while it bounds the disk in the surface. Thus

```math
\sum_a[a]=0\quad\text{in }H_1(S_g;\mathbb F_2).             \qquad\text{(2.2)}
```

If any input has odd intersection degree in the intersection graph, pairing with it contradicts (2.2). Therefore an odd-degree input forces a dual loop, which gives a cost-one curve by Lemma 2.1. This proves the parity test even when a face boundary revisits primal vertices.

## Lemma 2.4. Strict descent on every bad top simplex

Fix $`k\geq3`$ with $`\binom{k}{2}\leq B`$, and put

```math
n=k+1,\qquad T=\binom n2,\qquad s=T-B\leq n-1.
```

Call a simplex **safe** if its total geometric intersection is at most $`B`$, and **bad** otherwise. Every simplex with at most $`n-1`$ vertices automatically has total intersection at most $`\binom{n-1}{2}\leq B`$. A bad simplex in a complex of dimension at most $`k`$ must therefore be a maximal $`k`$-simplex with $`n`$ distinct image vertices and $`I>B`$.

Let $`d_v=\sum_{w\ne v}i(v,w)`$. Its proper facet has at most $`\binom{n-1}{2}`$ intersections, so

```math
d_v\geq I-\binom{n-1}{2}.
                                                               \qquad\text{(2.3)}
```

If an essential neighborhood boundary $`c`$ exists, it misses all inputs. Each cone facet $`c*(\sigma\setminus\{v\})`$ then has at most $`\binom{n-1}{2}\leq B`$ intersections and is already safe. Its class is new: otherwise an old input would be disjoint from every other input, contradicting (2.3) and $`I>B`$.

Otherwise the complement consists of $`F=I-B`$ disks. The degree estimate and $`\binom{k}{2}\leq B`$ give

```math
1\leq F\leq s\leq n-1,\qquad d_v\geq F\quad\text{for all }v.
                                                               \qquad\text{(2.4)}
```

We construct a rainbow curve $`c`$ of cost $`r`$ so that **every** new cone facet has fewer than $`I`$ intersections. If $`R`$ is its set of crossed input colors, define the labelled candidate count for the facet omitting $`v`$ by

```math
Q_v=I-d_v+r-\mathbf 1_{v\in R}.                            \qquad\text{(2.5)}
```

There are three cases.

**Case $`F\geq3`$.** Choose one dual edge of every color. There are $`n>F`$ chosen edges. Lemma 2.2 gives a rainbow cycle of length $`r\leq F-1`$. Equations (2.4)--(2.5) imply $`Q_v\leq I-1`$ for every $`v`$.

**Case $`F=2`$.** If every $`d_v\geq3`$, the same one-edge-per-color graph gives a cycle of length at most two, and again all facets decrease strictly. If some $`d_v=2`$, then

```math
I-2=B\leq\binom{n-1}{2}\leq B.
```

Equality holds throughout: the other $`k=n-1`$ input vertices form $`K_k`$, and $`v`$ is attached to precisely two of them. This graph has an odd-degree vertex. For odd $`k`$, either attached neighbor has odd degree $`k`$; for even $`k\geq4`$, an unattached vertex has odd degree $`k-1`$. The parity test of Lemma 2.3 forces a dual loop. Its cost is $`r=1\lt d_w`$ for every $`w`$, giving strict descent in (2.5).

**Case $`F=1`$.** If all input degrees are at least two, any dual loop has cost one and works. If $`d_v=1`$, then

```math
I-1=B=\binom{n-1}{2},
```

so all the other vertices form $`K_k`$. They have degree at least $`k-1\geq2`$; in particular $`v`$ is the unique leaf. Choose the dual loop on the graph edge belonging to this leaf curve. The resulting $`c`$ crosses $`v`$ once. For the facet omitting $`v`$, (2.5) gives $`Q_v=I-1`$; every other facet also has at most $`I-1`$ intersections.

This proves $`Q_v<I`$ in every case. To exclude a coincident class before interpreting these as all actual facet counts, suppose $`c=v`$ for some old input. Then $`v\notin R`$ and $`r=d_v`$, so $`Q_v=I`$, a contradiction. Thus $`c`$ is a new class, the candidate counts are the actual facet intersection counts, and all of them decrease strictly. The old $`n`$ vertices and $`c`$ form a genuine $`(n+1)`$-vertex simplex in $`C_1`$ by flagness.


∎

[Next: the main theorem](03-connectivity.md).
