# Related systems — overlap, adopted concepts, and explicit non-novelty

> **Status:** public projection of a completed concept-extraction research
> pass · **As of:** 2026-08-27 · **Citation audit:** the source list below
> names each system's public location; the audited VERSION PINS (commit
> hashes, retrieval dates, rights notes) remain in the private pass's
> pinned source ledger and are re-verified at release review.
> **Authority note:** The private record is authoritative; this repository is
> the legible surface. (Anchor: `ADJ-01`)

BrainCtx ran a structured extraction pass over the closest public systems —
concept-organized, not a feature matrix. The honest starting point is what
BrainCtx should **not** claim novelty for:

```text
Agent roles and orchestration:             common
Session recording and provenance:          increasingly common
Persistent typed records:                  established adjacent work
Trajectory monitoring and targeted nudges: an emerging demonstrated category
Pre-action policy guards:                  established
Replay, worktree isolation, deterministic
gates:                                     established
```

## The closest systems, and what each taught

- **The Recall Problem (Nou Collective).** The closest independent
  formulation of the activation thesis: `write ≠ load ≠ recall`, with query
  formulation as its own silent failure stage and memory naming as a
  retrieval parameter. Adopted: explicit `QUERY_FORMED` and
  `QUERY_MATCHED_REPRESENTATION` stages between opportunity recognition and
  retrieval. Not adopted: ambient filename injection as the recall solution
  (its own results degrade with memory depth), and its fixed-window "trigger
  rate" name, which is arithmetic coverage rather than observed behavior
  change.
- **Wink.** The closest public system to live course-correction: observes
  coding-agent trajectories and supplies asynchronous targeted guidance,
  with a production-scale evaluation. Adopted: independent timing events
  (`OBSERVER_SCHEDULED → RESULT_AVAILABLE → INTERVENTION_FIRED →
  INTERVENTION_NEEDED → DELIVERED` — an actor may self-recover before the
  result is ready), and burden as a first-class outcome. Its reported
  recovery numbers measure behavior-stopped plus forward progress, not task
  correctness or per-case causal help; BrainCtx keeps those axes separate.
- **10x (formerly Agent Loom).** The closest analogue to typed durable records: research,
  evidence, critique, accepted knowledge, and bounded worker packets as
  different objects, with placement rules and explicit promotion. Adopted in
  spirit throughout the ledger design; not adopted: automatic promotion from
  candidate to durable truth.
- **Sovereign Brain + Decision Notes.** Source-backed synthesis where a
  changed source makes linked synthesis visibly stale, and decisions carry
  evidence, alternatives, and revisit conditions. Adopted: currentness as
  dependency state, never elapsed time — a currentness receipt binds
  source-set identity, content hashes, synthesis version, and disposition
  state; an unchanged re-sync must not manufacture review debt.
- **Ward.** Session-aware mechanical guarding that parses intended command
  structure rather than regexing prose, and distinguishes intent from
  observed post-action effect. Adopted: the intent/effect split with a
  typed uncertainty state for what the aperture cannot see; and the
  boundary that loading retained session state is not evidence of fresh
  context or current authority. Mechanical policy is never epistemic truth.
- **Proof Loop / Ralph Review.** Fresh verifier identity, frozen acceptance
  criteria, stable finding identity, review separated from remediation.
  Adopted: finding-set novelty as the stop rule (`NET_NEW = 0` ends
  optional review; a hard round cap bounds it) and outcome-owner selection
  before any remediation. Not adopted: universal evidence gates around
  every task — that recreates certification churn.
- **AgentClash / Looplet / Entropy Loop.** Failure-to-regression promotion
  with provenance; captured-response replay as a narrow causal tool (valid
  for harness/tool changes, invalid for prompt/model comparisons, since
  holding the response fixed removes the treatment); comparison-state
  vocabulary (`NEW | PERSISTENT | FIXED | MISSING | SKIPPED`) kept separate
  from authority (`RECORD | WARN | BLOCK | EXIT`).
- **Memorix / Bernstein / Tutti.** Cross-agent memory portability and
  deterministic orchestration. Adopted: evidence kind, owner scope, and
  lifecycle state constrain where a memory may travel, with
  selection/omission receipts; and attestation as separate axes — stored,
  read, chain-consistent, semantically true, and actually consumed are
  five different claims. Not adopted: competing as an orchestration
  platform.

## Sources

Public locations, named for the audit; the pinned versions live in the
private source ledger. The 10x repository formerly published as Agent Loom
and redirects from that name.

| System | Public location |
|---|---|
| The Recall Problem (Nou Collective) | gist.github.com/noument/a2420dc52ff03f6bc8f540e1a90d57dd |
| Wink | arxiv.org/abs/2602.17037 |
| 10x (formerly Agent Loom) | github.com/z3z1ma/agent-loom |
| Sovereign Brain | github.com/LeoStehlik/decoupled-agent-memory |
| Decision Notes | gist.github.com/gururajl/a2e94896e4772a4e88833be31499bb47 |
| Ward | github.com/ctoth/ward |
| Proof Loop | github.com/LeoStehlik/proof-loop |
| Ralph Review | github.com/kenryu42/ralph-review |
| AgentClash | github.com/agentclash/agentclash |
| Memorix | github.com/AVIDS2/memorix |
| Tutti | github.com/nutthouse/tutti |
| Bernstein | github.com/sipyourdrink-ltd/bernstein |

## Concepts deliberately not adopted

Ambient context as the final recall solution; universal proof-loop task
wrappers; automatic remediation of reviewer findings; persistent reviewer
revival (retained findings may survive, review judgment comes from fresh
context); timestamp-only freshness; mechanical policy as epistemic truth;
generic orchestration and role proliferation; automatic promotion to
durable truth; longer synchronous-hook timeouts as a scaling fix.

## The differentiation, honestly bounded

The distinct research surface is the connected lifecycle:

```text
recognize possible bearing
  -> form and match a query
  -> retrieve/research with evidence lineage
  -> judge present applicability and authority
  -> contact current reality
  -> retain actor disposition and observed effect
  -> measure causal contribution, later outcome, and burden
  -> promote/revisit through reviewed owners
  -> freshly recover the corrected state
```

No inspected adjacent system evaluates that full chain. This is a
synthesis-level differentiation claim, **not an efficacy claim**, and it
carries named open gaps: no matched BrainCtx assay yet measures every stage
with per-stage denominators and an independently owned task outcome; the
inspected repositories are primarily first-party design records, not
independent benefit studies; and several transfers (the currentness races,
finding-identity canonicalization) remain to be reproduced natively before
they are treated as measured. (Anchors: `ADJ-01`, `ADJ-GAP-01`)
