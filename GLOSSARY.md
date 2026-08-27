# Glossary

> **Era note (2026-08-26):** this page predates the program's pivot from
> staged ablations to the attachable observe-and-deliver instrument. Its
> content remains accurate for the era it describes; the current surface is
> [README.md](README.md) → [STATUS_AND_CLAIMS.md](STATUS_AND_CLAIMS.md),
> and ablation-era records now live under [archive/](archive/README.md).


> **Authority note:** The private record is authoritative; this repository is the legible surface.

> **Status:** public explanation
>
> **As of:** 2026-08-04
>
> **Authority:** terminology aid only; it does not define private
> implementation or study authority.
>
> **Source basis:** approved public-curation plan, current public
> architecture, the methods demonstrated in four bounded observation runs and
> the first replay sets, the two 2026-08-02 program-direction pages, and the
> announced support-bridge evidence taxonomy.
>
> **Supersedes:** none. Dated additions and updates are marked as such.

## Actor

A model process or deterministic component performing a bounded role. “Actor”
does not imply authority to accept an outcome, publish knowledge, or continue a
chain.

## Admitted knowledge

Knowledge explicitly allowed into a bounded task context. Existence in a
private store is not admission, and admission is not evidence of use.

## Affordance visibility

*Added 2026-07-31.* Whether the working contract gives an actor a name for a
step. The associated hypothesis is that an actor does not volunteer what its
interface does not name, so making a step nameable shifts the probability it
is initiated. A hypothesis, not a demonstrated effect.

## Announcement contrast

*Added 2026-08-01.* A replay comparison in which the only difference between
arms is a sentence in the shown contract announcing that a declared step will
be *served* — the step's name being present in both arms. It measures the
effect of a service promise, and is fenced from the affordance-visibility
question, which is about whether the step is nameable at all.

## Barrier

A fresh-recovery gate that must complete before a successor may orient to
updated knowledge and enter its work graph.

## Bounded observation runner

*Added 2026-07-31.* A deliberately small instrument that runs frozen work
episodes in order, retains everything including failures, treats most
mid-run conditions as observations to record and continue past rather than as
reasons to stop, and evaluates the trajectory only after it finishes. It runs
under reduced custody, and each reduction is recorded as a limit on the
resulting claim. It is not a replacement harness or an approval layer.

## Carrier grammar

*Added 2026-08-02.* The carrier-specific layer that turns a bounded-run record
or interactive-session transcript into typed rows under one detection stack.

## Claim-authority tier

*Added 2026-07-31.* The section of a run's readout that states what the record
cannot support. It is computed from the retained conditions plus a fixed set
of structural limits, never authored, so a caveat cannot be dropped from the
next readout. Every entry is a typed unavailability with a reason, never a
value.

## Cold

Started in a distinct process or evaluation context without inheriting the
predecessor's conversation transcript. Cold does not mean uninformed: admitted
artifacts and knowledge may still be delivered deliberately.

## Commissioning

Live work used to establish and validate the research instrument and its
interfaces. Commissioning evidence can demonstrate mechanisms and failures; it
is not automatically an efficacy population.

## Continuation decision

A typed process decision that either offers the next bounded work episode or
terminates the chain for a named reason. It is executable authority, not a
descriptive label.

## Counterfactual redirect

*Added 2026-07-31.* What an evaluator judges should have been said to an actor
at a specific moment in a retained trajectory, written into the dataset after
the run. It is never shown to any model, so it changes nothing about the run
it describes. It is the entry the public code corpus never contains.

## Evidence projection

A public, redacted, aggregated, or synthetic representation of private
evidence. It is not the complete evidence authority.

## Evidence class

*Added 2026-08-04.* A tag that governs how a delivered item may affect a
typed question. `OWNER_RULING` is true by construction for its registered
scope and is the only class that closes. `RESEARCH_FINDING` and
`EXPERT_OPINION` are advisory and preserve conflicts, caveats, and dissent.
`SIGNAL-MEASUREMENT` is instrument output, not decision authority; retained
records also render that class `SIGNAL/MEASUREMENT`. Confidence without a
class tag has no extra power.

## Exposure partition

*Added 2026-08-02.* An append-only separation that prevents episodes which
motivated a detector from also serving as its holdout confirmation.

## Fork replay

*Added 2026-07-31.* Reconstructing the retained state at a naturally occurring
decision point in a real trajectory, varying exactly one condition, and running
a single bounded segment forward. Evidence from a replay arm is a distinct
class: it is never pooled with naturally occurring trajectories and never
presented as though the actor reached that state on its own. It is not
synthetic fork construction — the fork must have actually occurred.

## Fresh recovery

Reopening newly written knowledge through a new recovery process and its
catalog or index, rather than trusting the writer's in-memory state.

## Goal/fidelity review

Independent judgment about whether an artifact remains faithful to its
declared goal and consequential constraints. In private records this function
may be called a founder role.

## Graded reconstruction

*Added 2026-08-02.* A historical cutoff's repository state typed as exactly
pinned, partially reconstructed, or unpinned; missing state is never invented.

## Historical and operational lead

*Added 2026-08-02.* Historical opportunity lead is replay-measurable from a
cutoff; operational intervention lead is live-only. The two are never pooled.

## Host or domain knowledge

Evidence-backed knowledge about the repository or problem domain in which work
occurs.

## Inconsistent fabrication

*Added 2026-07-31.* An invented artifact that contradicts a contract its own
producer shipped — for example, a claimed result that the producer's own
generator could not have produced and that its own validator's rules make
impossible. It is detectable deterministically, without any model, precisely
because the contradiction is internal. The term is narrow on purpose:
detecting inconsistent fabrication says nothing about fabrication that is
internally consistent, and a clean result is evidence of consistency, never of
honesty.

## Interaction ladder

*Added 2026-08-01.* The graded scale of how much a supervisory instrument may
touch a working agent: observe, detect, shadow-adjudicate, advise, challenge,
gate. Each level must be earned by evidence produced at the level below —
precision before authority, counterfactual before intervention. *Updated
2026-08-02:* L1 is built and live-demonstrated but has not met its exit
checklist; L2 is a frozen two-stage design with zero rows; L3 and above are
unearned, with nothing speech-eligible.

## Judge equipoise

*Added 2026-08-01.* A replay class in which identical verdict-blind evidence
packets are presented to several differently bound judges, none of which is an
arbiter over the others. The judges' agreement is the measurement; a held-out
original record is the reference under calibration, not the answer key. Judge
strength is asserted only where an objective ground-truth anchor measures it,
and only for that anchor.

## Knowledge effect

An observed change associated with delivered knowledge. BrainCtx separates
handling, decision effect, artifact effect, and evaluated outcome effect rather
than treating acknowledgment as benefit.

## Knowledge store

An evidence-backed, catalogued body of retained knowledge. BrainCtx currently
separates host/domain knowledge from orchestration/process knowledge.

## License effect

*Added 2026-08-02.* A proposed behavior change caused by a credible downstream
reviewer and a legitimate destination for nonblocking edges; not an observed
capability.

## Orchestration or process knowledge

Knowledge about tooling, execution, custody, coordination, and run behavior,
kept separate from host/domain knowledge.

## Outcome owner

The actor authorized to decide and implement within a bounded work item. Other
roles may propose, challenge, or evaluate without taking that authority.

## Pre-registration

*Added 2026-08-01.* As used here: committing an experiment's fork, binding,
arms, observables, reporting order, and citation fences before any crossing
executes, with sample-size raises before unblinding as the only admissible
amendment. A registered observable the instrument cannot collect is recorded
as a shortfall and treated as unmeasured, never as zero; a registered arm the
instrument cannot honestly run is blocked with the blocking measurement on
record.

## Rung

One bounded sequential work episode in a chain. A successor rung may inherit an
accepted predecessor artifact and deliberately admitted recovered knowledge.

## Seal

A content-bound record of a protocol, package, or result state. A seal makes
later change visible; it does not make the sealed material public.

## Shadow supervision

*Added 2026-07-31.* Supervision performed over a finished run rather than
during it. Every stage is labeled, including the ones where nothing fired; a
capped subset is adjudicated; and counterfactual redirects are authored into
the dataset. Because it runs after the trajectory and no actor sees its
output, its observer effect is zero by construction — and for the same reason
it cannot demonstrate that supervision changes work.

## Social fold

*Added 2026-08-02.* A final artifact that folds together drafting, review,
correction, and assurance work by different people, leaving product more visible
than process.

## Staged world-contact ladder

*Added 2026-07-31.* The six-stage rubric used to score a world-contact act:
need surfaced, contact initiated, independent evidence returned, evidence
changes the decision basis, the plan uses the delta, the task outcome changes.
An act may stop at any stage, and partial credit is real credit. Process
appropriateness is scored on this ladder; task success is recorded beside it
and never folded into it.

## Stasis-expectation verification defect

*Added 2026-07-31.* An instrument-side failure in which verification machinery
treats the legitimate evolution of an artifact as a violation — typically by
checking it against a hash frozen before an admitted change. The defect is in
the instrument, not the actor, and it is the failure mode the program's
expect-evolution principle exists to forbid.

## Successor

A distinct later work process that follows a predecessor only after the
required product, learning, and continuation boundaries permit it.

## Supervision opportunity

*Added 2026-08-02.* A time-pinned point in a reconstructable episode at which
a shadow watcher could be evaluated using only cutoff-available evidence.

## Temporal aperture

*Added 2026-08-02.* The rule that a historical watcher packet contains only
evidence available at its cutoff; later reviews and outcomes remain
evaluation-only.

## Typed incompleteness

*Added 2026-08-02.* A legitimate named disposition for an unresolved edge —
such as hand-raise, deferred, known issue, or unavailable — while admitted
work continues.

## Uncertainty-expression effect

*Added 2026-08-02.* A proposed behavior change caused by making typed
incompleteness available; the prediction is proportionate allocation, not
more hedging.

## Unsupported condition

*Added 2026-08-02.* The condition in which supervision is invisible to the
actor. All measurements relevant to the proposed three-effect line so far
have this form; it grants no speech authority.

## Watcher

A differently situated supervisory role that examines work without becoming
the outcome owner. Current checkpoint-level observation and proposed paired
pre-action supervision are different study stages.

## Watcher advice effect

*Added 2026-08-02.* A proposed behavior change caused by delivering a specific
concern. Compliance with advice is not correctness and is measured separately.

## World contact and process contact

*Added 2026-07-31.* The axis on which an unasked-for inserted step is
adjudicated. A **world-contact** step verifies current external reality: it is
cheap, it produces evidence, and it brings the work closer to contact with its
outcome. A **process-contact** step only reinforces, certifies, or gates: it is
self-referential and defers that contact. The first is not drift even though
nobody asked for it; the second is drift even though it looks like diligence.

## Epistemic contact cue

*Added 2026-08-27.* BrainCtx's unifying intervention shape: limited
evidence that the actor's context may be incomplete, plus a possibly
relevant fact or source, a citation or investigation route, a bounded
reason it may bear, and explicit permission to verify and dismiss. A cue
is a possibility, never a verdict; an incorrect cue that causes an
appropriate check and is dismissed can still be doing its job.

## Externally aware memory

*Added 2026-08-27.* Retained project knowledge made active from OUTSIDE
the actor's own recall: the surrounding system recognizes that a stored
fact, precedent, or implementation may bear on the current decision and
surfaces it with a locator — leaving currentness and applicability for
the actor to verify against the present state of the work.

