# Architecture and maturity

> **Authority note:** The private record is authoritative; this repository is the legible surface.

> **Status:** public explanation of the research instrument
>
> **As of:** 2026-08-26
>
> **Authority:** public explanation. The private as-built and evidence records
> govern implementation state and measurements.
>
> **Claim boundary:** functional groups, authority separation, and maturity;
> not domain outcomes or full implementation disclosure.

## Two planes

**A per-session component.** Attached through a coding-agent host's native
hook surface — every hook event type the host exposes is wired. The hook
jobs: attach and register the session with the hub; capture a passive
notebook of what the session does (each capture hook is bounded to a few
seconds; summed across the several hooks an event carries, the declared
synchronous ceiling per event stays under half a minute — cost is capped,
not absent); deliver queued guidance at safe points; and join actor
receipts back to the deliveries they answer. A parallel adapter exists for
a second host family. (Anchor: `COMP-01`)

**A long-running hub.** A user-level service that self-refreshes in place.
Each heartbeat it tails attached sessions' ledgers into an append-only
observation stream, evaluates the armed predicates, runs independent
reader panels over recent windows, answers typed research needs from the
knowledge base into the asking session, and checks its own health with the
same suspicion it applies to actors — staleness keyed on the loaded
surface, tick silence as a signal, zero-suppression retained as a row.

## The authority ladder

```text
silence
→ reminder (cited possibility, non-directive)
→ single exact-action pause (once per exact act, then never again)
→ peer dialogue
        — and never a hard policy block
```

Hard denial was explicitly declined by the program's operator; the
component's pre-action plane refuses the host's permission-decision
mechanism by construction. Mechanical policy is treated as an action
boundary, never as epistemic truth.

## The custody chain

- Every terminal predicate evaluation journals `FIRES / NO_SIGNAL / SKIP /
  ERROR` with stable identities **before** any delivery.
- A projector joins fire-time sources, delivery, actor handling, and later
  correction into six-stage concern episodes
  (`EVENT → CANDIDATE → KNOWLEDGE → ADJUDICATION → DELIVERY/HANDLING →
  OUTCOME`), verified by exact byte ranges rather than trust.
- A denominator layer keeps population, provenance, validity, and cost as
  independent typed axes; evidence that was not retained is reported
  `UNAVAILABLE` and reduces the conclusion — it is never inferred.
- Lifetime identity custody (append-only registry) is separated from
  operational addressability (`ACTIVE / QUIESCENT_UNKNOWN / ENDED`), so
  silence means uncertainty rather than death and hot work iterates only
  the affirmatively active set.
  (Anchors: `EP-01`, `DEN-01`, `LIFE-01`)

## Knowledge and review

Knowledge lives in a versioned markdown corpus with indexed owners; every
enforced expectation must be actor-visible and machine-checkable. Paid-for
lessons become deterministic predicates on the hub's cadence
(`LESSON-01`). Changes to the instrument pass a two-seat adversarial
review — an independent skeptic and an independent founder-critic, both in
fresh contexts, seeded on the relevant set rather than the corpus — plus a
mechanical relapse-detector gate; findings are dispositioned by an outcome
owner rather than auto-remediated. (Anchor: `REVIEW-01`)

## Maturity, honestly

Built and operating on one operator's natural work across one primary host
family plus a second adapter. Known open gaps are stated rather than
omitted: the running process's loaded bytes are vouched at admission, not
continuously; semantic adjudication of raw predicate matches,
counterfactual delivery, causal benefit, and long-run interruption burden
are unbuilt; pre-cutover historical liveness is permanently unavailable;
retrieval lacks stemming/synonym bridging. See
[STATUS_AND_CLAIMS.md](STATUS_AND_CLAIMS.md) for the binding ceilings.
