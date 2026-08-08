# Publication policy

> **Authority note:** The private record is authoritative; this repository is the legible surface.

> **Status:** active policy for repository authoring; release review pending
>
> **As of:** 2026-08-06
>
> **Authority:** governs this public projection only. It does not change the
> private implementation, study contracts, evidence corpus, or publication
> rights.
>
> **Claim boundary:** publication and repository handling; not a study or
> implementation claim.
>
> **Source basis:** approved public-curation plan and private-corpus public
> projection rules.
>
> **Supersedes:** the 2026-07-28 policy surface by adding the owner-directed
> host-evidence boundary below; all earlier authority and release gates remain.

## Purpose

BrainCtx Research is a one-way, curated projection from private implementation
and evidence authorities into public research documentation.

```text
private implementation and evidence
→ private publication brief and source map
→ public-native draft
→ privacy, rights, claims, and chronology review
→ clean-room review
→ public commit and release
```

No automated process mirrors arbitrary private changes into this repository.
Every published byte is an explicit publication decision.

## Authority

The private BrainCtx project and its owning study records remain authoritative
for:

- implementation and design state;
- exact prompts and provider adapters;
- complete run and evaluation evidence;
- private knowledge stores;
- study construction, exposure, and contamination records;
- corpus custody;
- and private-to-public publication decisions.

If a public document conflicts with a later owning private record, the private
record is reconciled first. The public claim is then corrected through an
explicit update or erratum.

## Public artifact classes

Every substantive artifact is classified as one of:

| Class | Meaning |
|---|---|
| `PUBLIC_EXPLANATION` | Public-native explanation of a question, mechanism, or boundary. |
| `PUBLIC_PROTOCOL_PROJECTION` | Bounded protocol summary that cannot replace the private protocol. |
| `PUBLIC_EVIDENCE_PROJECTION` | Redacted, aggregated, or synthetic representation of private evidence. |
| `PUBLIC_RESULT_PROJECTION` | Public result account bound to a sealed private result. |
| `PUBLIC_RESEARCH_DIRECTION` | Proposed research direction, not current implementation or evidence. |

Private candidates also receive one handling class:

| Handling | Rule |
|---|---|
| `PUBLIC_AS_IS` | Already public-native and free of private dependencies. |
| `PUBLIC_REWRITE` | Finding may be public; source text must not be copied. |
| `PUBLIC_AGGREGATE_ONLY` | Only bounded counts or summaries may leave private custody. |
| `PUBLIC_SYNTHETIC_ONLY` | Only a clearly labeled invented example may be published. |
| `PRIVATE` | Must not enter this repository. |
| `PROHIBITED_UNTIL_RIGHTS_CLEAR` | Withhold until rights, privacy, or contract review passes. |

Internal BrainCtx documents are `PUBLIC_REWRITE` by default.

## Material that is private by default

This repository does not publish:

- full runtime source;
- raw owner or model transcripts;
- raw private-corpus rows;
- detailed role prompts or detector rules;
- private knowledge-store contents;
- raw run roots or unrestricted Git custody;
- exact actor packets or complete admitted-knowledge manifests;
- evaluation-only artifacts or unpublished review findings;
- provider sessions, request identifiers, billing records, or credentials;
- private filesystem paths, host details, or proprietary diffs;
- or third-party material with uncertain redistribution rights.

Role purposes, authority, input categories, and output types may be explained
without publishing exact prompts.

## Claims discipline

Major claims use the closed statuses defined in
[STATUS_AND_CLAIMS.md](STATUS_AND_CLAIMS.md). Mechanism evidence and benefit
evidence are reported separately.

The following outcomes remain legitimate and publishable:

```text
positive
null
negative
mixed
refused
unavailable
contaminated
failed
```

A result is not strengthened because the implementation was expensive, the
mechanism is elaborate, or a failed run produced useful diagnostics.

## Evidence mapping

Every material public claim must have:

- an exact private source pointer;
- the source state or version observed;
- a transformation and redaction record;
- a public evidence pointer appropriate to the claim;
- and privacy, rights, and claims-review dispositions.

Those mappings remain private. Public documents do not expose private paths,
commits, or source names merely to appear more evidentially complete.

## Study-integrity boundary

Publication must not become actor input.

Before a live study seals, public material is limited to what cannot reveal
task answers, evaluation-only information, private knowledge packets, or
future outcome-bearing evidence. If an actor can reach the public repository,
the repository is part of the discoverable input universe and must be treated
accordingly.

Detailed protocols, public seals, and results are published only after their
private prerequisites exist and a fresh leakage review passes.

## Release gates

A release requires:

1. **Story:** a technical reader can identify the question, evidence state,
   central unknown, current study, and next direction.
2. **Claims:** every major assertion is status-typed and scope-limited.
3. **Privacy:** no private person, transcript, path, credential, provider
   state, or host artifact is exposed unintentionally.
4. **Rights:** reproduced or quoted material has an acceptable publication
   basis.
5. **Study integrity:** publication does not expose actor or evaluation-only
   information.
6. **Evidence:** demonstrated and observed claims have private source maps and
   suitable public pointers.
7. **Projection:** redaction, rights, privacy, and claim reviews are retained
   privately.
8. **Clean clone:** an independent review is performed from a clone with no
   private-workspace access.
9. **Five-minute test:** the core research story is understandable without
   adopting BrainCtx's internal vocabulary.

The project owner is the final publication authority.

## Owner-directed host-evidence boundary (2026-08-06)

The owner directed (with the private-domain example generalized here):

> "I think the public repo may have drifted too deeply into host evidence exposure. If it
> was a domain-project public repo, depth of information about what was being worked on would
> be more appropriate. For BrainCtx, the more appropriate handling is to detail how the
> knowledge, governance, and framework allowed the domain-specific efforts to proceed. Not
> what the domain-specific outcome itself."

Operationally, public BrainCtx material centers evidence classes and their
force limits, rulings and measurement triggers, consultation and transfer
behavior, review blocks, invalid-state refusal custody, ingest mechanics, balance, honest
nulls, and claim-ledger chronology. Domain measurement values, detailed item
descriptions, input-family structure, artifact construction, and per-item
inventories remain in private custody. Direction-level findings may be
published only when their limits and private authority are explicit.

## Licensing

No license is granted merely because this repository is publicly readable.
Licensing will be selected deliberately before public release. Prose, schemas,
and any future sample code may receive different licenses.
