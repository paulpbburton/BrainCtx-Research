# Finding — recurrence-ranked failure modes of an adversarial review corpus

> **Authority note:** The private record is authoritative; this repository is the legible surface.
> **Status:** descriptive corpus characterization · **As of:** 2026-08-26
> **Publication boundary:** headline counts await a public-safe extraction
> receipt (source population, unit of analysis, deduplication, multi-label
> handling). Until it lands, this page states the modes and their ordering
> qualitatively. This is a characterization of one program's retained
> corpus, **not** a prevalence claim about agent failures in software
> engineering generally. (Anchor: `REVIEW-CORPUS-01`)

The program's PR process runs two fresh adversarial reviews on every
change. Mining the retained review documents — on the order of 170
documents across ~140 pull requests, roughly a thousand findings — yields
seventeen recurring failure modes, ranked by how many distinct changes
each was caught in. The top of the table, in rank order:

1. **Byte-identity claimed, not verified.** "Faithful"/"byte-identical"
   trusted from the label, or proven only on the author's own shapes.
2. **Overclaim without a reproducing artifact.** A decisive number in
   prose only; "validated" on a reconstructed case; enthusiasm dressed as
   a result.
3. **Vacuous tests.** Green tests that prove nothing: asserting against
   the new wrapper, fixtures where the change is a no-op — countered by
   mutation-proofing (patch the bug back; the gate must fail).
4. **Stale citations and cross-page contradictions.** Line-cites that
   drifted, counts never requeried, references that resolve to nothing,
   paraphrase presented inside quote marks.
5. **Signal turned off.** A previously kept signal collapsed, dropped, or
   thresholded away under a mixed number — the program's rule is gate-off
   is not delete.

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
