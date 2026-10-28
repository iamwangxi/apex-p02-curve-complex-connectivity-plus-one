# One more degree of connectivity for bounded-intersection curve complexes

Let $`C_d(S_g)`$ be the flag complex of essential simple closed curve classes on a closed connected orientable surface. Distinct vertices are adjacent when their geometric intersection is at most $`d`$. For every $`g\geq3,d\geq1,k\geq1`$,

```math
d\binom{k}{2}\leq2g-2\quad\Longrightarrow\quad C_d(S_g)\text{ is }k\text{-connected}.
```

Moreover, the same numerical condition gives finite replacement into $`C_0(S_g)`$, relative to all original vertices, for every $`g\geq2`$. Consequently,

```math
\mathrm{conn}\,C_d(S_g)\geq
1+\left\lfloor\frac{\sqrt{1+8(2g-2)/d}-1}{2}\right\rfloor
\qquad(g\geq3).
```

The bound is exactly one degree above direct intersection counting; for fixed $`d`$, its leading term remains $`2\sqrt{g/d}`$. Simple connectivity holds for every $`g\geq2,d\geq1`$. The target paper's Theorem 1.1 on contractibility of $`C_1(S_2)`$ extends the displayed bound to $`g=2`$; its only additional numerical cases are $`k=2,d=1,2`$. Together with the higher-genus bound above, this gives 3-connectivity for every genus at least two when $`d=1`$.

## Target and scope

Target: Apex Intelligence, [*The Complex of Curves Pairwise Intersecting at Most Once Is Contractible in Genus Two*](https://math.apexin.net/papers/curve-complex-genus-two.pdf), competition version dated 11 September 2026, 35 pages. SHA-256:

`d1eadd01f94e9af17ee9f5fb2ee1b05b326430f37296309fd9417340ea366fd4`

The target proves contractibility in genus two (Theorem 1.1, p. 2) and simple connectivity for every genus at least two (Theorem 1.3, p. 2; Theorem 7.7, p. 24). The contribution is a uniform one-degree improvement for every positive integer intersection bound, including higher-connectivity estimates in higher genus. Its proof is self-contained apart from explicitly cited classical surface topology, simplicial approximation and Harer's homotopy type for the disjointness complex.

All surfaces here are closed, connected and orientable. The complex uses all essential unoriented isotopy classes, including separating ones, and the usual weak topology. The finite replacement homotopies fix all original vertices. They do not define a global retraction or establish higher-genus contractibility.

## Proof guide

Start with [Theorem A and its connectivity consequence](proof/03-connectivity.md). The complete all-bound proof is [bounded-intersection replacement](proof/06-bounded-intersection.md): finite capacitated selection, essentiality with repeated colors, strict descent on every child facet, compatible finite termination, the safe-image homotopy and all parameter cases.

The [finite replacement page](proof/01-finite-replacement.md) also proves the neighborhood and cone-carrier input in full, with the direct-count bound. [Rainbow descent](proof/02-rainbow-descent.md) is the intersection-bound-one specialization. Neither is an external proof dependency.

The [one-subdivision cutoff](proof/04-method-cutoff.md) specifies the interface obstructed by filling systems. Its leading square-root size follows from Anderson–Parlier–Pettet's published construction. The [covering obstruction](proof/05-covering-tower.md) proves Proposition C, with a complete initial ribbon specification and homology-cover argument. See also the [source ledger](sources/bibliography.md), [finite-check scope](checks/README.md) and [review hashes](sources/review-status.md).

Proposition C gives filling systems with $`n_h=o(g_h)`$ for which every essential curve has total intersection at least $`2^{\lfloor h/2\rfloor}`$. Their curve counts grow faster than $`\sqrt{g_h}`$. This restricts a constant-cost strategy in the stated range; it supplies no connectivity upper bound.

## Reproduce the finite checks

Requires Python 3.9 or later and only its standard library. From the repository root:

```sh
python3 -B scripts/run_checks.py
```

The runner executes six checks and compares their parsed JSON with the recorded reference files under `checks/`. It writes no files. Do not use `-O`: the computations rely on assertions. Each individual `verify_*.py` also prints its JSON to standard output. `verify_long_cycles.py` loads two sibling source files without running their main routines or creating bytecode.

The checks include exhaustive weighted intersection graphs and short multigraphs, independent matroid tests, actual bounded-intersection surface models and repeated-color homology certificates. They also retain the genus-three enumerations, ribbon insertion/deletion, a length-three rainbow cycle with consecutive filling replacements and the first 64-sheet homology cover. Fixed seeds and omission of runtime fields make every reference JSON deterministic. See the scope ledger for counts and limitations. Finite checks detect implementation errors; the infinite and topological statements are proved in the proof files. No Lean or other formal verification is claimed.

To verify the package hashes:

```sh
shasum -a 256 -c MANIFEST.sha256
```

The manifest lists every repository file except itself, `.DS_Store` and `.git` contents. External source PDFs are linked or cited rather than bundled.

## Literature and review status

Boundary replacement and subdivision homotopies have a close precedent in Harer's Lemma 4.3, pp. 178–179. Anderson–Parlier–Pettet already established the $`2\sqrt g`$ leading size of minimum filling 1-systems. The contribution here is a technical strengthening through capacitated dual-edge selection and iterated top-dimensional descent. For each fixed intersection bound, the leading asymptotic constant is unchanged. No exhaustive literature search or prize-eligibility determination has been performed.

Fresh-context adversarial reviews found no fatal, repairable mathematical or presentation issues in the reviewed proof stages, including the extension to every positive intersection bound. The [review record](sources/review-status.md) binds the reviewed proof, report and incorporated proof by SHA-256 and distinguishes the scope of each. The genus-two supplement retains its stated external dependency. The covering proposition and method limitations are separate from the connectivity conclusion.

## AI disclosure

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; separate GPT-6.1 Sol sessions in fresh contexts performed adversarial reviews. GPT-6 Astra, also in OpenAI Codex, advised on research direction and submission scope. Claude contributed planning, source checks and editing to the intersection-bound-one material. No human expert has certified the work.

## License

Original prose is licensed under CC BY 4.0. Code in `scripts/` is licensed under the MIT License. See [LICENSE](LICENSE). External publications retain their own terms. No endorsement by Apex Intelligence or the cited authors is implied.
