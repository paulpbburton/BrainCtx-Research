# Finding — recurrence-ranked failure modes of an adversarial review corpus

> **Authority note:** The private record is authoritative; this repository is the legible surface.
> **Status:** descriptive corpus characterization · **As of:** 2026-08-27
> **Publication boundary:** the extraction receipt exists (frozen
> 2026-08-27, retained privately; its methods and denominators are
> projected below), so the top-mode counts are published — as approximate
> distillation measures whose ORDER is the trustworthy signal. This
> remains a characterization of one program's retained corpus, **not** a
> prevalence claim about agent failures in software engineering
> generally. (Anchors: `REVIEW-CORPUS-01`, `REVIEW-CORPUS-02`)

The program's PR process runs two fresh adversarial reviews on every
change. Mining the retained review documents yields seventeen recurring
failure modes, ranked by how many distinct changes each was caught in.

## The extraction receipt, projected

- **Source population (mechanically verified at the frozen boundary):**
  **172 review-class documents** (143 skeptic-seat, 29 founder-seat)
  across **144 distinct pull requests** of the predecessor domain
  program's dual-review corpus; 28 PRs carry both seat classes; at most
  two documents per PR inside the boundary. The retained table's own
  header states the same 172/144 — the denominators reproduce
  mechanically from filenames alone.
- **Unit of analysis:** the distinct PR. A mode caught in a PR counts
  once for that PR however many findings expressed it; one PR may count
  in several modes (multi-label). A "catch" is a finding that BLOCKED (a
  real defect surfaced and fixed) or CLEARED (a suspected defect chased
  and ruled out by a real check) — both load-bearing.
- **Procedure and its honest limit:** two independent signature passes
  clustered roughly a thousand findings into the seventeen modes and
  cross-validated the RANKING. The reviews carry no machine-readable
  finding tags, so per-mode counts are judgment-based distillation
  measures — approximate, order-trustworthy, and not mechanically
  reproducible; the source table says this of itself.
- **Known missing populations, quantified:** 438 further review documents
  of the same program (192 distinct PRs, later era) and the **entire**
  successor-program review corpus (738 documents) are retained and
  UNMINED. Nothing here extrapolates to them, and the top-mode ordering
  may differ there.

## The top modes, with counts

Approximate distinct-PR counts against the 144-PR denominator (order
trustworthy; counts approximate, per the receipt):

1. **Byte-identity claimed, not verified** (~67 PRs).
   "Faithful"/"byte-identical" trusted from the label, or proven only on
   the author's own shapes.
2. **Overclaim without a reproducing artifact** (~61). A decisive number
   in prose only; "validated" on a reconstructed case; enthusiasm dressed
   as a result.
3. **Vacuous tests** (~59). Green tests that prove nothing: asserting
   against the new wrapper, fixtures where the change is a no-op —
   countered by mutation-proofing (patch the bug back; the gate must
   fail).
4. **Stale citations and cross-page contradictions** (~50). Line-cites
   that drifted, counts never requeried, references that resolve to
   nothing, paraphrase presented inside quote marks.
5. **Signal turned off** (~46). A previously kept signal collapsed,
   dropped, or thresholded away under a mixed number — the program's rule
   is gate-off is not delete.

The long tail includes scope creep, per-frame determinations where a
session-level owner exists, re-trying recorded dead ends, import-purity
violations, wrong-tier gates, silent drops and collisions,
coordinate-space seams, eyeballs not actually performed, silent fallbacks
that clobber expensive artifacts, and clean aggregates masking bimodal
tails.

Two uses follow. **Author-side:** each mode carries a one-line
prophylaxis, so a competent author pre-satisfies the reviewer and the
clean pass is fast. **Instrument-side:** the recurring modes seed the
armed predicates and the mechanical gate — the lagging record made
leading. (Anchors: `REVIEW-CORPUS-01`, `LESSON-01`)
