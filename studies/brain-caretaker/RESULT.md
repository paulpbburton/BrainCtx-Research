# Issue #197: one-shot brain caretaker

> **Artifact class:** `PUBLIC_RESULT_PROJECTION`
>
> **Status:** implemented MVP with retained acceptance and failure record
>
> **As of:** 2026-08-05
>
> **Authority:** public mechanism projection. Private source, cursors, delta
> packets, traces, seals, review receipts, and merge ledger remain authoritative.
>
> **Claim boundary:** ingest, fail-closed custody, and governance; not
> knowledge quality, cadence, downstream benefit, or host inventory.

## One bounded custody path

Each caretaker invocation validates receipt-linked cursors, rescans a bounded
overlap, emits a sourced `NOOP` when nothing changed, otherwise constructs a
typed delta packet, reconciles isolated knowledge-store worktrees, validates
declared dispositions against actual diffs, opens controlled-ingest proposals,
and writes a durable receipt before advancing any cursor.

Partial or failed phases seal `INVALID`, remain excluded, and do not advance
custody. A cursor means that material has a connected valid receipt, not merely
that a time range was scanned.

## Typed authority

The updater may propose knowledge prose only in isolated branches. Each input
and store receives a typed disposition such as `NOOP`, `PR_OPENED`, or
`GAP_RETAINED`; that declaration must agree with the actual diff. Governance,
canon, code, protected branches, service activation, and public pushes remain
outside its authority.

## Acceptance and recovery

Acceptance exercises covered idempotence, late-arriving material, corrupt
cursor refusal, and fresh index-to-owner recovery. A missing route surfaced
during recovery and was repaired before the exercise passed. These tests
establish custody mechanics and findability, not semantic quality or later use.

## Fail-closed seals are part of the result

A follow-on event-triggered tick refused several attempts before one valid
proposal. The seals caught:

- a disposition contradicting an actual diff;
- dirty isolated-worktree residue;
- legitimate locator forms outside an over-narrow verifier grammar; and
- a fabricated source path paired with the correct content hash.

The nonexistent locator was not laundered by a correct hash. The proposal was
refused and the cursor stayed unchanged, preserving retry rather than silently
skipping material. Apparatus errors were typed separately from updater errors.

## Ordinary governance after a valid tick

Valid output still travels through controlled ingest, independent skeptic and
goal/fidelity review, supersession records, and a traceable revert path. A
proposal merges only after both reviews are green. The standing
[merge policy](MERGE_POLICY.md) admits a narrow knowledge lane; governance
remains manual.

## Limits

The implemented inputs remain a subset and one updater route does not estimate
miss rate, judgment quality, or benefit. Raw inventory counts, knowledge
content, local paths, and machine custody remain private.
