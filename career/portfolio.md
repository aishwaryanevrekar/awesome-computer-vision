# Build a computer vision portfolio people can evaluate

A useful project answers a concrete question and provides evidence that its answer holds under stated conditions. A polished demo helps people understand it; saved predictions, a defensible split, and reproduction instructions let them assess it.

[Project catalog](../projects/README.md) · [24-week path](../roadmaps/beginner-to-job-ready.md) · [Research path](../roadmaps/research.md) · [Interview preparation](interview-preparation.md)

## Choose a small set with different kinds of evidence

Three strong projects are a reasonable target, not a hiring requirement. Start with one complete project before creating the next repository.

| Project | What it can demonstrate | Example scope |
| --- | --- | --- |
| Applied model | Data handling, metrics, error analysis, and a useful baseline | Detect a bounded set of objects or classify a small licensed image collection, with a held-out source or session. |
| Deployed pipeline | Reproducible preprocessing, input handling, profiling, and operating constraints | A local document or image-search tool with measured quality, latency, and failure behavior. |
| Research or specialist investigation | Controlled experimentation and depth in one area | A scoped paper replication, geometry experiment, or representation comparison with explicit limitations. |

Align the third project with the work you want to do. Geometry, robotics, medical imaging research, remote sensing, industrial inspection, document understanding, and multimodal retrieval have different evaluation needs. Do not claim deployment readiness in a sensitive application from a classroom experiment.

## Minimum evidence for every project

- **Task and user:** one paragraph explaining the decision the system supports, what the input is, and what a correct output means.
- **Data provenance:** source, version, collection method if applicable, annotation process, redistribution terms, and the independent split unit. Link restricted datasets instead of uploading copies.
- **Baseline:** a simple reference solution evaluated under the same protocol. “No model,” a classical method, or frozen features may be appropriate.
- **Measured result:** metric definitions, split, sample counts, saved predictions, and a command to regenerate the report. Record all material model-selection decisions.
- **Failure analysis:** examples of misses and false alarms, plausible causes, and what you actually checked. Include failures from the intended use case.
- **Runtime evidence:** hardware, software, input size, precision, batch size, and what the timer includes. Label unmeasured performance as unmeasured.
- **Reproduction:** environment, data preparation, run commands, configuration, weights or download instructions, and expected output files.
- **Limits and attribution:** known scope, unsupported uses, upstream code and model credit, and relevant licenses.

For research artifacts, compare your reporting with the [Machine Learning Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf). For learned preprocessing and evaluation, audit the workflow against [scikit-learn's common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).

## Suggested project layout

A layout to adapt for your own project:

```text
project/
  README.md
  LICENSE
  requirements.txt          # or another pinned environment definition
  configs/                 # baseline and selected experiment settings
  src/                     # data, training, evaluation, inference
  tests/                   # critical metric and transformation checks
  data/README.md           # source, acquisition, license, and split rules
  artifacts/README.md      # where large weights/predictions live
  reports/                 # metrics, plots, failure examples, experiment log
  demo/                    # small permitted sample inputs and outputs
```

Keep data and large artifacts separate from the source repository when necessary. A private artifact is acceptable when access is explained; an inaccessible artifact cannot support a public reproducibility claim. Never upload private user images, credentials, or a dataset you lack permission to distribute.

## A README a reviewer can inspect in five minutes

Start with the task and the measured result, then show a small demonstration. State “results pending” if evaluation is unfinished. Avoid a headline metric without the conditions needed to interpret it.

Use the following outline, replacing every instruction with project-specific evidence:

```text
1. Problem: intended input, output, user, and constraints.
2. Demonstration: one ordinary success and one informative failure.
3. Results: baseline and selected approach on the same named split.
4. Data: source, license, labels, grouping, and leakage checks.
5. Method: enough detail to explain your decisions and reproduce them.
6. Run: setup, data preparation, evaluation, and inference commands.
7. Analysis: ablation, failure categories, and operational measurements.
8. Limitations: what the evidence does not establish.
9. Credits: upstream implementations, papers, datasets, and models.
```

Record result rows using a structure such as the following. The table contains placeholders, not benchmark results.

| Approach | Split and sample/group count | Metric and value | Runtime setting | Evidence |
| --- | --- | --- | --- | --- |
| Baseline | Fill with your fixed evaluation set | Fill with a measured value | Fill with hardware and timing scope | Link report and configuration |
| Selected method | Use the same evaluation set | Fill with a measured value | Use comparable settings or label differences | Link predictions and report |

Use the [official evaluator](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py) when claiming a COCO-style detection result, and name its settings. A new dataset scored by that evaluator is not the COCO benchmark. Similarly, running an author's released checkpoint is different from reproducing the author's training.

## Add one useful ablation

Choose a decision your reader might question: an augmentation, a resolution, a prompt, a loss term, or a fine-tuning strategy. Hold the rest of the protocol fixed, compare against the baseline, and explain the observed quality and cost. If results are noisy, show per-run values or state that only one run was affordable.

For an efficiency project, use a profiler such as the [PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) to locate the bottleneck before changing it. Report both a performance gain and any quality loss under the same evaluation protocol. Do not infer end-to-end speed from parameter count alone.

## Prepare to defend your decisions

In a five-minute walkthrough, spend roughly one minute on the problem and data, one minute on the baseline, two minutes on experiments and failures, and one minute on limitations and next steps. These are suggested timings; adapt them to the audience.

Be ready to answer: Why this split? Why this metric? What did the simplest baseline achieve? Which improvement failed? What changes on another camera or source? What would you do with fewer labels? What is your own contribution versus upstream code? Explain the exact parts you implemented and the parts you reused.

Write résumé bullets from real artifacts. A useful structure is “Built [system] for [task]; evaluated on [protocol]; changed [decision], producing [measured result and tradeoff].” Omit numbers you did not measure and claims about business impact you did not observe.

## Final self-review

Ask someone to run the documented command in a clean environment and to identify your central result without asking you. Fix missing dependencies, hidden notebook state, unavailable sample files, and unclear instructions. Then ensure every public performance claim points to an artifact that supports it.

Completion is a project that can be inspected, questioned, and rerun within its stated scope. Keep improving it when new evidence reveals a weakness.
