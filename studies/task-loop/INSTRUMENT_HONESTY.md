# Instrument honesty: repeated refusal at an unhealthy seam

> **Artifact class:** `PUBLIC_RESULT_SUMMARY`
>
> **Status:** completed instrument-health arc
>
> **As of:** 2026-08-06
>
> **Authority:** private control rounds, seals, and measurement distributions
> remain authoritative.
>
> **Claim boundary:** fail-closed instrument behavior; no domain measurement
> or exclusion claim.

Repeated attempts to earn a domain observable refused to report it when the
control was unhealthy. A later self-calibration attempt was also rejected by
its held-out control rather than adopted because it looked plausible.

Each round inherited the prior lesson:

```text
control before claim
→ distributions before thresholds
→ unhealthy control means UNREADABLE
→ a rejected correction remains round-scoped evidence
```

The arc's result is not a domain read. It is an honest disposition and an
identified unblock that requires owner-controlled physical calibration. The
instrument did not convert unavailable evidence into a null or a conclusion.

All instrument values, tolerances, implementation details, and specimen
descriptions remain private.

## Limits

The retained evidence concerns one instrument context. No domain structure or
exclusion claim is made; a healthy control must precede any future read.
