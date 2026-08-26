# Seven gaps the program targets

> **Status:** current gap-targeting map
> **As of:** 2026-08-08
> **Authority note:** The private record is authoritative; this repository is the legible surface.

The seven rows below are scoped literature findings, not claims that no such
work exists anywhere. They come from a structured review of 29 primary
sources, with a stated search boundary, a closest located witness, and an event
that would reopen each finding. A program status describes BrainCtx's current
fill vehicle; it does not declare the field gap closed. (Anchors: `GAPS-01`,
`POSITION-01`)

## Gap map

| Scoped absence | Closest public reference and remaining difference | BrainCtx status | Evidence class |
|---|---|---|---|
| Gradual return of a model's prior across a multi-stage research trajectory | [AdaCAD](https://aclanthology.org/2025.naacl-long.581/) measures token-level context conflict; [DYNAMICQA](https://aclanthology.org/2024.findings-emnlp.838/) and [Task Matters](https://arxiv.org/abs/2506.06485) study task-level context conflict. None of the located studies follows gradual source dominance across planning, research, implementation, review, and stopping. | **In design:** a checkpointed long-form context-conflict study with an incorrect-context control. | Literature synthesis + unmeasured design record (`GAP-LONG-01`) |
| Query-free recognition of a relevant organizational knowledge store | [MemGPT](https://arxiv.org/abs/2310.08560), [Self-RAG](https://arxiv.org/abs/2310.11511), [MemoryAgentBench](https://arxiv.org/abs/2507.05257), and [LongMemEval-V2](https://arxiv.org/abs/2605.12493) begin with a memory-bearing interaction, retrieval affordance, or final query. The located work does not test whether an agent notices an unnamed store during ordinary work. | **Retained data ready / in design:** same-prefix availability study; ablation03 already showed that reading and citing do not guarantee activation. | Literature synthesis + retained observation + unmeasured design (`GAP-ACTIVATE-01`) |
| A real serviced expert channel measured from need detection through outcome | [HiL-Bench](https://arxiv.org/abs/2604.09408), [CLAMBER](https://aclanthology.org/2024.acl-long.578/), and [ClarQ-LLM](https://arxiv.org/abs/2409.06097) measure asking or clarification with authored blockers or simulated helpers. The located studies do not join detection, latency, reply quality, use, and downstream outcome for a live service. | **Retrospective fill complete; prospective fill planned:** a 31-exchange five-stage inventory now exists, while a controlled comparison remains unrun. | Retained retrospective observation; causal effect unknown (`GAP-SERVICE-01`) |
| Preference training as the cause of suppressed asking, clarification, or abstention in long-form agent work | [R-Tuning](https://arxiv.org/abs/2311.09677) and [CLAMBER](https://aclanthology.org/2024.acl-long.578/) motivate the question but do not provide matched base, instruction-tuned, and preference-trained checkpoints under fixed capability and prompts. | **External dependency:** BrainCtx can publish fixed-model behavior, but a training-stage causal study requires a partner with matched checkpoints and provenance. | Literature synthesis + dependency record (`GAP-PREFERENCE-01`) |
| Fabrication reduction caused by team availability rather than mandatory collaboration | Active-team evidence points in both directions. [Multiagent Debate](https://arxiv.org/abs/2305.14325) and [controlled debate](https://arxiv.org/abs/2511.07784) require interaction; [LOCA-bench](https://arxiv.org/abs/2602.07962) exposes subagents but scores task success rather than condition-level fabrication. | **Filling:** ablation04's powered 2×3 design isolates no channel, registered-only channel, and live serviced team. It is built but unrun; the four-run live-team demo produced zero voluntary asks. | Pinned design + demonstration measurement (`GAP-TEAM-01`) |
| Prevalence of preregistration in agent research | [Preregistration for Experiments with AI Agents](https://arxiv.org/abs/2606.11217) is a normative proposal. A six-paper convenience check found no declaration but cannot estimate field prevalence. | **Low-cost audit candidate:** seal a venue/year sample, registry search, and missingness policy before counting. | Bounded pilot observation + unmeasured audit design (`GAP-PREREG-01`) |
| Spontaneous cross-field initiation before a human supplies the cue | [Google's AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) and [The AI Scientist](https://arxiv.org/abs/2408.06292) elaborate human-provided goals or templates. The located evaluations do not test whether an agent independently seeks a structural analogy from another field. | **In design:** a blinded no-cue trial that scores initiation before novelty, then mapping quality, disanalogies, falsification, and outcome. | Literature synthesis + unmeasured design (`GAP-CROSSFIELD-01`) |

## First-of-kind positioning

The careful claim is prospective and instrument-specific. Within the declared
29-source search, the program found no qualifying instrument for
availability-only fabrication, query-free organizational-store activation, or
the full five-stage live-service chain. If the powered study runs as pinned,
it is positioned to produce first-of-kind data within that search scope. A new
qualifying primary study would reopen the claim immediately. (Anchor:
`POSITION-01`)

## What has actually been filled

One existence gap is now filled in the narrow sense: BrainCtx has a retained
five-stage serviced-ask retrospective. It contains 29 retained exchanges and
two declared supplements; 17 of 31 downstream outcomes remain unknown. It
shows that the instrument can be assembled, not that service improves work.
(Anchor: `SERVICE-RETRO-01`)

The other six gaps remain filling, in design, audit candidates, or externally
dependent. Honest status is part of the result.
