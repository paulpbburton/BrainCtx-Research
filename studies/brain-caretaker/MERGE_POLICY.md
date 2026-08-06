# Knowledge-tier merge policy

> **Artifact class:** `PUBLIC_EXPLANATION`
>
> **Status:** standing owner-authorized governance design
>
> **As of:** 2026-08-05
>
> **Authority:** public projection. The private owner ruling, repository
> protections, review contracts, and merge records remain authoritative.
>
> **Claim boundary:** a narrow merge-policy description, not authorization to
> change governance, merge code, activate services, publish repositories, or
> bypass review.
>
> **Source basis:** the owner ruling recorded with the issue-#197 caretaker
> and the first controlled-ingest review and merge events under that ruling.
>
> **Supersedes:** an earlier per-PR, owner-word posture for the same narrow
> knowledge tier. Governance-tier work remains manual.

## Standing rule

Evidence-backed **knowledge-tier** brain PRs merge on a clean dual review.
**Governance-tier** changes remain delayed and manual.

Auto-merge is admitted only when every condition below holds:

1. **Knowledge-only path scope.** Changes are limited to knowledge pages and
   their index, currency, and append-only history surfaces. The guarded set is
   untouched.
2. **Evidence-backed claims.** Every added claim has a custody locator and an
   evidence class. Advisory classes cannot be promoted into owner rulings.
3. **Dual review is green.** The skeptic says safe to merge, and the
   goal/fidelity reviewer says faithful and advancing. Any finding, split, or
   ambiguity holds the PR until a corrected round is green; the latest round
   governs.
4. **Surface gates pass.** The complete proposed diff passes the repository's
   prohibited-token and protected-surface checks.

After merge, the ledger retains the diff summary, verdict history,
supersession relation, and a one-line revert command. Cheap, traceable revert
is the audit affordance; it does not loosen the pre-merge gates.

## Guarded tier: manual

Doctrine, core policy, governance, founder canon, code paths, service/timer
activation, public-repository pushes, and anything that fails or cannot prove
the gates above require explicit owner action. A reviewer flag also moves a
proposal into the manual or fix path.

The rule is standing authorization for a defined lane, not a transfer of
governance authority to the caretaker. Git history and explicit supersession
preserve correction paths without preventing newly reviewed knowledge from
becoming available to later work.
