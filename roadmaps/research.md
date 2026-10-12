# A 12-week path to a credible computer vision replication

Suggested effort: **10–15 hours/week** · Intended for learners who can already train, debug, and evaluate a model.

The goal is a narrowly scoped claim supported by runnable evidence. A useful outcome can be a reproduced result, a carefully diagnosed discrepancy, or evidence that a proposed improvement does not help under your conditions. A published paper is not a required outcome.

[All paths](README.md) · [Research landscape](../research/landscape.md) · [Project catalog](../projects/README.md)

## Prerequisites and research contract

Before starting, demonstrate that you can implement a loss, inspect gradients, overfit a tiny batch, save and reload a model, construct a leakage-resistant split, and calculate the task's metric. Be comfortable reading tensor shapes and one page of mathematical notation. Use the [beginner path](beginner-to-job-ready.md) to repair missing prerequisites.

Choose a paper with an accessible manuscript, an official implementation or a sufficiently specified method, obtainable data, and a feasible evaluation. Write a contract before running experiments:

```text
Claim to investigate:
Paper section/table and exact evaluation setting:
What I will reproduce:
What I will change or omit, and why:
Dataset version and independent split unit:
Baseline, primary metric, secondary metrics:
Compute and storage cap:
Planned runs and stopping rule:
Evidence that would support or weaken the claim:
```

Use the [paper-note template](../templates/paper-note.md) for your reading record and the [experiment-report template](../templates/experiment-report.md) for each controlled comparison.

Keep the distinction between three scopes explicit:

| Scope | What you can reasonably claim |
| --- | --- |
| Evaluate an author's released checkpoint | You reproduced or investigated an evaluation result under stated conditions. |
| Train a reduced version or a new dataset variant | You performed an adaptation or scaled experiment; you did not reproduce the full training result. |
| Match the specified training and evaluation protocol | You attempted a training replication; report every known difference before comparing numbers. |

For experiment reporting, consult the [Machine Learning Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf). Record exact code, dependencies, data, and hardware. A seed is useful but is not a guarantee of identical outcomes across environments; see [PyTorch's reproducibility notes](https://docs.pytorch.org/docs/main/notes/randomness.html).

## Pick one bounded research question

These are starter questions. The outcomes are yours to find.

| Direction | Example question | A modest first experiment |
| --- | --- | --- |
| Visual representation | Does a frozen representation retain performance across capture sessions on my dataset? | Compare a small [DINOv2](https://github.com/facebookresearch/dinov2) backbone with a supervised pretrained baseline, using the same classifier protocol. |
| Image–text alignment | Does prompt choice change the ranking of a fixed set of classes? | Use [CLIP](https://github.com/openai/CLIP), freeze several prompt templates on validation data, then evaluate held-out images. |
| Data efficiency | Does labeling a targeted error slice help more than labeling the same number of random examples? | Define the acquisition rule before revealing labels and compare equal annotation budgets. |
| Efficient inference | Does a runtime optimization preserve performance on small objects or difficult text? | Start with a fixed checkpoint and compare predictions and latency under identical preprocessing. |
| Geometry | When does a learned matching pipeline fail compared with a classical baseline? | Select a small scene-separated evaluation and report pose or matching errors under a documented geometric protocol. |

The [CLIP paper](https://arxiv.org/abs/2103.00020) and [DINOv2 paper](https://arxiv.org/abs/2304.07193) are useful examples of representation-learning research. The checkpoints make downstream experiments possible without repeating pretraining. They are selected here for inspectability and teaching value; consult the landscape for newer work.

## Twelve weeks of artifacts

| Week | Work | Required artifact and exit condition |
| --- | --- | --- |
| 1 | Read the abstract, figures, method, evaluation, and limitations. Follow the central baseline citations. | A one-page paper map: question → method → evidence → assumption. You can identify which table actually supports the main claim. |
| 2 | Inspect official code and configuration. Trace an input from loader through preprocessing, model, and evaluator. | A protocol table with paper setting, code setting, your setting, and consequence of each difference. |
| 3 | Obtain a small legal data subset; audit labels and split units. Run inference or a tiny training job. | A smoke-run artifact, data manifest, and budget estimate from measured runtime and memory. Reduce scope if the full plan exceeds the cap. |
| 4 | Reproduce the simplest baseline or checkpoint evaluation first. Inspect several individual predictions. | Baseline metrics, predictions, and a command to regenerate them. No new method is added until the baseline is understood. |
| 5 | Run your intended replication/adaptation with fixed preprocessing and evaluation. | A discrepancy log. Differences are traced to data, weights, implementation, training, or metric settings where possible. |
| 6 | Verify metric behavior with tiny hand-checkable examples. Audit duplicates, grouping, annotation transforms, and denominator choices. | An evaluation audit and one independently recalculated result. Explain why a metric change is real or a measurement correction. |
| 7 | Choose one mechanism to investigate, such as an augmentation, loss term, prompt, or feature layer. Write the hypothesis before running it. | A small ablation matrix with the baseline, one changed factor, fixed variables, and planned interpretation. |
| 8 | Execute the controlled experiments. Repeat stochastic training with multiple seeds if the budget permits. | Per-run metrics and compute records, including failed runs. Report single-run findings as single-run findings. |
| 9 | Evaluate prespecified slices and one out-of-distribution condition that is separate from tuning. | A table with sample/group counts and qualitative failures. Avoid making population claims from a tiny slice. |
| 10 | Analyze uncertainty and alternative explanations. Compare paired predictions when the same examples are available. | Effect size and an appropriate uncertainty analysis; describe the resampling unit and dependence assumptions. No selective reporting of only favorable seeds. |
| 11 | Ask another person, or use a fresh environment, to follow the reproduction instructions. Write the report around the evidence. | A clean-run log, limitations section, and complete artifact index. Fix undocumented manual steps. |
| 12 | Present the strongest supported conclusion and answer objections. Package the work for review. | A concise report, runnable configurations, plotted results, and a next experiment that could falsify your current explanation. |

## A compute plan that can survive contact with reality

Start with cached features or checkpoint inference when possible. Measure the cost of one run before selecting the experiment matrix. A reasonable initial cap might be one baseline, two variants, and up to three seeds per configuration; this is an example planning limit, not a universal requirement. If you cannot afford repeated training, narrow the claim and document that uncertainty instead of inventing precision.

Separate research time from accelerator time. Debug shapes and file handling on a tiny subset. Reserve the longest runs for configurations that pass those checks. Checkpoint interruption-prone jobs. Record unsuccessful runs and their causes so they cannot quietly disappear from your account of the experiment.

For confidence intervals, consider what is independent. Thousands of frames from a handful of videos do not constitute thousands of independent video-level observations. If bootstrapping, resample the appropriate group and report the method; repeated-seed variability answers a different question from variability across sampled test cases.

## Write the report so another reader can disagree productively

Use this order: research question, scope, related evidence, protocol, baseline, controlled experiments, results, failure analysis, limitations, reproduction instructions. State whether your findings apply to one dataset, one checkpoint, one device, or a broader tested set.

Every result table should identify the data split, metric definition, model/checkpoint, resolution, and run count. Every efficiency comparison should identify hardware, runtime, precision, batch size, warmup, and whether input/output work is included. Mark differences from a paper's published conditions; numbers from incompatible conditions do not establish superiority.

End with one specific proposed next experiment. “Use a bigger model” is not enough: identify the observation that motivates it, what remains fixed, and which outcome would change your explanation.
