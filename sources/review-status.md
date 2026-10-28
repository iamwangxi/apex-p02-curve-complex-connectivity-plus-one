# Review status and immutable identifiers

## All-bound theorem

The fresh-context adversarial review dated 28 October 2026 accepted the reviewed all-bound manuscript. It reported zero fatal issues, zero repairable mathematical issues and zero presentation issues. Its accepted scope is finite vertex-relative replacement for every integer $`g\geq2,d\geq1,k\geq1`$ with $`d\binom{k}{2}\leq2g-2`$; the resulting $`k`$-connectivity for $`g\geq3`$; and simple connectivity for every $`g\geq2,d\geq1`$.

The genus-two cases $`k=2,d=1,2`$ additionally use the target paper's Theorem 1.1 on contractibility of $`C_1(S_2)`$. The review did not independently establish that external theorem. The same dependency is explicit in the incorporated proof and theorem entry. Corollary B's genus-two 3-connectivity at intersection bound one also uses that external theorem.

The report concerns the reviewed source identified below. Incorporation into this repository is not a new independent review of the rewritten theorem entry, submission text or packaging. All 319 mathematical expressions in Sections 1–8 of the source and incorporated proof agree in order and content, with only the equivalent GitHub-safe spelling of a less-than sign normalized for comparison. The safe-image lemma is reproduced as mathematical content, with no dependency on another proof package.

## SHA-256 ledger

Reviewed all-bound source manuscript:

`556fae7de785e00eeb6ed17d3c5e1a1a991678be4c3e3859ca7b741e0ee9b7a5`

Adversarial review report:

`cec424df9918f723b414e8437136eaad68690e8fa57ba8d929f96eb742a7c32d`

Author self-check report:

`489c8c45308afd8b2fc75ea6796cab4493768cdba99f31c5b09783bf077f2926`

Incorporated complete proof: [proof/06-bounded-intersection.md](../proof/06-bounded-intersection.md):

`e4df80b759e93c863c0094cbda0c6b624cae52404449463913bb0cbbba9fd354`

Main theorem entry: [proof/03-connectivity.md](../proof/03-connectivity.md):

`e7de17ba6fe59949271229b21f3c3813ac4408e2cf31a55869e67e3503fcc248`

Website submission manuscript, held outside this repository:

`8cfacf643abd824615a7954a347a363ec751406edf05d101e50df53805947c1d`

Adapted primary finite checker: [verify_bounded_intersection.py](../scripts/verify_bounded_intersection.py):

`ff123be65329dcf75d6723f463e248c48f189fb5785670a2a14d02b6b609890f`

Adapted independent finite checker: [verify_bounded_independent.py](../scripts/verify_bounded_independent.py):

`327c181762d8a163d5bac4853b92f46b7c72214f86e8e6cf1f8b566abce437d8`

## Computational scope

The primary and independent checkers retain respectively all 45 and 61 assertion statements of the reviewed programs, with identical abstract syntax trees. Their reproduced statistics agree with the retained review outputs; the independent surface witnesses also agree exactly. Adaptation changes documentation and deterministic stdout packaging, removes timing fields and file writes, and embeds witness objects in the output. It does not reduce test ranges, capacities, seeds or assertions. See the [finite-check ledger](../checks/README.md).

Finite computation does not certify arbitrary curve isotopy classes, the infinite matroid selection theorem, compatible relative homotopies, or infinite parameter ranges. These are established by the written arguments and their stated classical inputs. The reviews are not formal verification, exhaustive novelty assessment or a prize-eligibility decision.
