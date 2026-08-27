# BrainCtx Research

> **Status:** current public research surface
> **As of:** 2026-08-26
> **Authority note:** The private record is authoritative; this repository is the legible surface.

BrainCtx studies a practical gap in long-horizon AI work: knowledge can
exist, be delivered, and even be cited without changing what an agent
actually does. Agents often have the ability to check a source, inspect the
current system, or ask for expertise — and fail to recognize when doing so
is necessary. They continue from priors, stale readings, or a locally
coherent trajectory. (Anchor: `THESIS-01`)

The program's hypothesis: an external organizational layer can preserve or
restore a relevant possibility at the moment it bears, point the actor
toward current evidence, and let the actor verify, reject, qualify, defer,
or use it — without the actor's cooperation being assumed, and without
shoving a whole knowledge corpus into context.

## What exists now

Since the ablation era ([retained under `archive/`](archive/README.md)),
the program built and now operates an **attachable
supervision-and-memory instrument** on its own natural work:

- a per-session component attached through a coding-agent host's native
  hook surface, capturing a passive notebook of what each session does at a
  bounded per-event cost — observation cost is capped, not absent;
- a long-running hub that observes attached sessions each heartbeat,
  evaluates a small set of **armed predicates** — deterministic detectors
  for the operator's most recurrent failure classes — and on a fire routes
  a cited, non-blocking nudge to the session it concerns;
- an append-only custody chain under the fires: every fire, delivery,
  actor receipt, decision, and correction is journaled, and strict
  verifiers replay claimed results from exact byte ranges.

The authority ladder is deliberately shallow: a fire produces a reminder, a
single exact-action pause, a peer dialogue, or silence — never a hard
policy block. The design bet is that cited, well-timed possibility beats
enforced verdict. (Anchor: `COMP-01`)

## The measured chain

```text
observable moment where context may be incomplete
→ actor-recognized need, or externally inferred gap
→ current knowledge / historical precedent / new research
→ fresh bearing judgment
→ cited possibility, never a verdict
→ reminder, exact-action pause, peer dialogue, or silence
→ current-world contact
→ evidence reconciliation
→ actor acceptance, rejection, deferral, or hand raise
→ actual next action and artifact effect
→ later outcome and operator-attention burden
→ paired knowledge product + activation product
```

Individual public systems cover nearly every component of this chain; the
composition — especially pairing *what was learned* with *what the moment
before needing it looked like* — is the program's research object. See
[`RELATED_SYSTEMS.md`](RELATED_SYSTEMS.md) for the overlap and non-novelty
record.

## The current claim, plainly

BrainCtx has physically demonstrated several parts of this chain in natural
coding work: armed detectors firing on real workload with every fire
receipted by the actor it reached; false-fire classes becoming same-day
predicate fixes that held on re-exercise; typed research needs answered
into the asking session with line-cited sections at a fraction of the prior
reading cost; and honest nulls retained with equal standing.
(Anchors: `FLYWHEEL-01`, `NEED-01`, `NULL-02`)

**It has not established general causal benefit.** Mechanism and
descriptive claims are supportable; causal benefit, long-run
operator-burden reduction, detector precision at scale, and production
readiness are open. This is a research instrument, not a product. See
[`STATUS_AND_CLAIMS.md`](STATUS_AND_CLAIMS.md) for the full claim ladder
and its ceilings.

## Reading order

1. [`CORE.md`](CORE.md) — the research object and the vocabulary.
2. [`STATUS_AND_CLAIMS.md`](STATUS_AND_CLAIMS.md) — every material claim
   with its force and its ceiling.
3. [`RESEARCH_HIGHLIGHTS.md`](RESEARCH_HIGHLIGHTS.md) — the findings a
   reader should not leave without.
4. [`ARCHITECTURE.md`](ARCHITECTURE.md) and
   [`METHODOLOGY.md`](METHODOLOGY.md) — the instrument and the study
   discipline.
5. [`NATURAL_WORK.md`](NATURAL_WORK.md) — the workloads the instrument
   observed, by evidentiary role.
6. [`RELATED_SYSTEMS.md`](RELATED_SYSTEMS.md) — adjacent public systems,
   concepts adopted, concepts rejected, and explicit non-novelty.
7. [`findings/`](findings/) — the descriptive findings pages, including
   the nulls and corrections record.
8. [`archive/`](archive/README.md) — the ablation-era record, retained.

Claims on every page carry anchors resolving in
[`PRIVATE_ANCHORS.md`](PRIVATE_ANCHORS.md) — a claim-to-private-custody
ledger an authorized reviewer can resolve inside private custody. About the
program, collaboration, and funding: [`ABOUT.md`](ABOUT.md),
[`COLLABORATE.md`](COLLABORATE.md), [`FUNDING.md`](FUNDING.md).

---

Contact: paulpb.burton@gmail.com
