# Bibliography and source-check scope

All locators are printed page numbers. Preparation used retained public-source copies and existing source comparisons from proof development and adversarial review; no new network request was made. No third-party full text or PDF is redistributed here. The retained target and Harer copies are identified by the hashes below; the source locators retain their original verification scope. A cited classical input is not claimed to have been formally verified.

## 1. Target paper

Apex Intelligence, [*The Complex of Curves Pairwise Intersecting at Most Once Is Contractible in Genus Two*](https://math.apexin.net/papers/curve-complex-genus-two.pdf), competition version dated 11 September 2026, 35 pages. Retained official public PDF; SHA-256:

`d1eadd01f94e9af17ee9f5fb2ee1b05b326430f37296309fd9417340ea366fd4`

Checked comparison points: definitions and flagness, §1.1, p. 1; genus-two contractibility, Theorem 1.1, p. 2; all-genus simple connectivity, Theorem 1.3, p. 2; scope, §1.4, p. 3; edge replacement, Lemma 7.5, p. 23; surjectivity on the fundamental group, Lemma 7.6, p. 24; Theorem 7.7, p. 24. The genus-two theorem is used for Corollary B and for the two exceptional parameters in the genus-two supplement to the all-bound connectivity statement. It is not an input to vertex-relative finite replacement or to any higher-genus conclusion. Section 7 is a comparison for the present higher-dimensional replacement, not a proof of Theorem A.

The target attributes the earlier question and simple-connectivity statement to Souto and gives a version of his inclusion argument in Proposition 7.8, p. 24. Souto's unpublished *A Remark About the Curve Complex*, dated approximately 2007 in the target's bibliography, was not read. No higher-connectivity claim is attributed to that uninspected note.

## 2. John L. Harer

John L. Harer, [*The Cohomology of the Moduli Space of Curves*](https://imag.umontpellier.fr/~calaque/GdT-CGEMC-Harer.pdf), expository chapter, printed pp. 138–221. The cited locators refer to this publicly circulated scan. SHA-256:

`190bbb154ab51d10d68e923a7a3615ad0537c9d6e975778f9f0cf94866d93514`

The checked chain is the definition of $`Z_g^s`$, p. 170; Lemma 3.6, p. 171; and Theorem 4.1, p. 176. The $`s=0`$ specialization concerns all essential closed-surface curve classes, including separating ones, and gives the homotopy type of a wedge of $`(2g-2)`$-spheres. This supplies the $`(2g-3)`$-connectivity input in proof/01, proof/03 and proof/06.

Lemma 4.3 and its proof, pp. 178–179, contain a close precedent for taking essential regular-neighborhood boundaries, removing trivial or repeated components, subdividing and constructing a compatible homotopy. Boundary replacement and subdivision homotopies are therefore not presented as new methods here. The inspected chapter is not the separate 1986 Inventiones article cited as [7] in the target; no inspection of that different publication is claimed.

## 3. Benson Farb and Dan Margalit

[*A Primer on Mapping Class Groups*](https://euclid.nmu.edu/~joshthom/teaching/ma589/farbmarg.pdf), Princeton Mathematical Series 49, Princeton University Press, 2012; retained public book PDF.

Checked inputs: bigon criterion, Proposition 1.7, pp. 30–33; Corollary 1.9 and the following simultaneous-minimal-position paragraph, p. 33; essential simple-curve homotopy versus isotopy, Proposition 1.10, p. 34. The local removal of multiple crossings and the minimization against a fixed 1-system are written out in proof/01.

## 4. Allen Hatcher

[*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Cambridge University Press, 2002; retained public author PDF.

Checked inputs: simplicial approximation to an arbitrary simplicial target, Theorem 2C.1, p. 177; the fixed-source-vertex observation, p. 179. These justify finite image complexes and preservation of the sphere-map basepoint without assuming target local finiteness.

For the covering construction: classification of connected covers, Theorem 1.38, p. 67; regular covers, Proposition 1.39, p. 71; cellular surface homology, Example 2.36, p. 141; and abelianization, Theorem 2A.1, p. 166. The separating-lift and two-cover systole assertions are proved in proof/05 rather than attributed to Hatcher.

## 5. James W. Anderson, Hugo Parlier and Alexandra Pettet

[*Small filling sets of curves on a surface*](https://arxiv.org/abs/0909.1966v2), retained arXiv:0909.1966v2, 8 October 2010; published in *Topology and its Applications* 158 (2011).

Checked Theorem 1 and Corollary 2, p. 1; filling conventions, §2, pp. 2–3; Euler lower bound, §3.1, p. 3; and the construction in §3.2, pp. 3–8, including the final cardinality argument in §3.2.5 on p. 8. For $`K=1`$, if $`N`$ is the least integer with $`N(N-1)\geq4g-2`$, their theorem gives $`N\leq f_1(g)\leq N+1`$ and hence $`f_1(g)\sim2\sqrt g`$.

Proposition 4.1 translates filling into failure of a precisely specified one-subdivision replacement map. Its leading square-root cutoff is an immediate consequence of the published filling-size result. Neither the sharp leading filling constant nor that consequence is claimed as a separate new extremal achievement here. No general choice between the two possible integer values is asserted.

## 6. Piotr Przytycki; maximal-system context

[*Arcs Intersecting at Most Once*](https://arxiv.org/abs/1402.1570v2), retained arXiv:1402.1570v2, 26 August 2014; journal publication 2015. Checked Theorems 1.2 and 1.4, p. 1, and the curve-complex discussion, p. 2. These concern maximum cardinalities of arc or curve systems, a different quantity from minimum filling size and from connectivity. They are not homotopy inputs.

Only the inspected Przytycki reference is used for this contextual comparison. No exhaustive novelty search is claimed.

## 7. Arguments supplied in this repository

The finite cone-carrier construction, rainbow-curve strict descent with its low-face-count exceptions, bounded-depth termination, the exact replacement-interface argument, and the homology-cover cost obstruction are proved in full in proof/01–06. The all-bound proof adds a self-contained independent-representatives lemma, capacitated cographic selection and mod-two essentiality for repeated-color cycles. Review scope and proof hashes are in [review-status.md](review-status.md). Numerical JSON files provide finite error checks only. All claims use these proofs and the classical inputs listed above; there is no dependency on a separate repository or unpublished proof package.
