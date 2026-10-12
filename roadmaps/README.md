# Roadmaps

Four plans, one rule: **every week ends with something you can run and show.** No plan here asks you to "understand" a topic without producing evidence.

[Home](../README.md) · [Projects](../projects/README.md) · [Resources](../resources/README.md) · [Study tracker](../templates/study-tracker.md)

## Pick your plan

| You are... | Plan | Length | You finish with |
|---|---|---|---|
| Comfortable with Python, new to vision | [Beginner to job-ready](beginner-to-job-ready.md) | 24 weeks | An evaluated model, a deployed demo, a defensible report |
| Training models already, want to do research | [Research path](research.md) | 12 weeks | A scoped replication, an ablation, a technical report |
| Rusty, want back in fast | [30-day refresh](30-day-refresh.md) | 30 days | Repaired fundamentals and one current, honestly evaluated project |
| Interviewing soon | [Interview prep](../career/interview-preparation.md) | 4 weeks | 35 practiced questions and clear explanations |
| Holding repos nobody can follow | [Portfolio guide](../career/portfolio.md) | A weekend | Projects another person can reproduce |

## Find your starting point in 45 minutes

Answer these closed-book, in 45 minutes. Keep your answers; they are your baseline.

1. Load an image. State its height, width, channel order, dtype, and value range. Resize it without distorting the aspect ratio.
2. Why must adjacent video frames not be scattered randomly across train and test?
3. TP = 30, FP = 10, FN = 20. Compute precision and recall. Which one do you protect for a missed-defect problem?
4. How do you tell a broken training loop from a model that is just too small?
5. What would someone need to rerun your experiment on another machine?

<details>
<summary>Answer key and what to do with your score</summary>

1. `H x W x C`, usually `uint8` in `[0, 255]`; OpenCV loads BGR and Pillow loads RGB. Scale both sides by the same factor, then pad or crop if you need a fixed size.
2. Neighboring frames are nearly identical, so the test set leaks into training and the score is inflated. Split by video, not by frame.
3. Precision = 30/40 = 0.75, recall = 30/50 = 0.60. A missed defect is a false negative, so protect recall.
4. Overfit a tiny batch. A working loop drives the loss to near zero; if it cannot, the loop (labels, loss, learning rate, data order) is broken. If it can but validation stalls, suspect capacity or data.
5. Code revision, config, data version and split, seeds, environment, and the exact command.

**Scoring:** shaky on 1 and 2, start at week 1. Fine on 1 and 2 but shaky on 3 to 5, start at week 7. Comfortable with all five, take the research path or the 30-day refresh. You can skip any week where you can already show its deliverable.

</details>

## The weekly loop

```
 read  ->  implement  ->  evaluate  ->  explain a failure
 25%        50%           25%
```

- Ship one runnable artifact every week and write down what a failure taught you.
- Keep one small dataset through the early weeks so a new concept is not also a new data-cleaning job.
- Split by the real unit of independence (subject, product, scene, recording session) before you make crops or augmentations.
- Protect the test set until the final decision.

Start by running the [three CPU examples](../examples/README.md) to check your environment, then copy the [study tracker](../templates/study-tracker.md).

## Next stop

Need a project? Browse the [project briefs](../projects/README.md). Need a different course? Search the [catalog](../resources/README.md). Picking a specialty? Read the [Research landscape](../research/landscape.md).

"Job-ready" here means you have practiced the common engineering tasks and have evidence you can do them. It is not a promise of a job, and one roadmap cannot replace deep specialization. Camera geometry, data quality, trustworthy evaluation, and profiling stay useful while model families change.
