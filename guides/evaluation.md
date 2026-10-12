# Evaluate computer vision systems well

A useful result states **what was measured, on which data, under which conditions, and with how much uncertainty**. Start with the evaluation protocol before changing the model.

## Split the real unit of independence

Randomly separating image files is often insufficient. Keep all views of the same patient, product, physical object, document, video, recording session, or scene in one split when the intended claim is generalization to new instances. For geographic generalization, split by location; for future performance, use a time-based holdout. When the task is instance retrieval, shared object identity across query and gallery can be intentional—describe that protocol explicitly.

Deduplicate exact files and inspect near duplicates before finalizing splits. Split original images before making crops, augmented copies, synthetic variants, or video clips. Fit normalization, feature selection, calibration, and learned preprocessing on the permitted development data. A pipeline helps keep transformations inside the proper training folds. See [scikit-learn's leakage examples](https://scikit-learn.org/stable/common_pitfalls.html).

Use training data for fitting, validation for decisions, and test data for the final locked comparison. A public benchmark can become development data through repeated tuning; acknowledge that. Foundation-model training data may be undisclosed, so use “no task-specific fine-tuning” when “unseen during pretraining” cannot be established.

## Pick metrics that match the task

| Task | Primary measures | Report alongside them |
|---|---|---|
| Classification | Accuracy; macro-F1 or balanced accuracy for imbalanced classes | Class counts, confusion matrix, per-class recall, calibration |
| Detection | AP over the benchmark's IoU thresholds | AP50, object-size slices, recall, confidence/NMS settings |
| Semantic segmentation | Per-class IoU and mean IoU | Ignore-label policy, absent-class convention, boundary failures |
| Instance segmentation | Mask AP | Box AP separately, crowd handling, small-object performance |
| Tracking | HOTA, IDF1; other benchmark measures as appropriate | Detection source, ID switches, complete sequences |
| OCR | Character error rate; exact word/field accuracy | Text normalization, lexicon use, predicted versus supplied crops |
| Retrieval | Recall@K and mAP under defined relevance | Gallery size, duplicate handling, index recall and latency |
| Depth / stereo | AbsRel, RMSE, disparity error or benchmark outlier rate | Units, alignment, crop, valid pixels, depth range |
| Pose | Official OKS AP or a declared PCK protocol | Visibility policy, box source, normalization and thresholds |
| Restoration | PSNR/SSIM with explicit conventions | Perceptual measures, degradation process, hallucinated details |
| Novel-view synthesis | Held-out PSNR/SSIM/LPIPS where applicable | Camera split, render speed, memory and model size |
| Anomaly detection | AUROC and AUPRC at image and/or pixel level | Prevalence, threshold selection, false positives, localization |
| Vision-language tasks | Task-specific exact match, ANLS, or official evaluator | Invalid outputs, prompt, image/frame budget, grounding failures |

Use the benchmark evaluator when one exists. [COCO API](https://github.com/cocodataset/cocoapi), [TrackEval](https://github.com/JonathonLuiten/TrackEval), and [TAP-Vid evaluation code](https://github.com/google-deepmind/tapnet) capture protocol details that a homegrown approximation can miss. Do not compare numbers from incompatible evaluator versions or call a proxy score an official benchmark score.

For binary overlap, IoU = TP / (TP + FP + FN) and Dice = 2TP / (2TP + FP + FN). Averaging per image versus pooling all pixels gives different answers. Define the empty-mask case instead of allowing an accidental divide-by-zero policy. For OCR, CER = (substitutions + deletions + insertions) / reference characters; insertions can make CER exceed one.

## Make comparisons fair

- Fix data versions, splits, image sizes, augmentations, prompts, and evaluation code where the hypothesis does not require changing them.
- Match the resource relevant to the claim: labeled examples, training steps, wall time, parameter count, or inference cost. These are different comparison questions.
- Record pretraining sources when disclosed, checkpoint identifiers, optimizer/schedule, precision, seeds, and every major search decision.
- Reproduce a baseline under your environment. Report a published number separately from a locally reproduced number.
- Change one major factor for an ablation. If several things change, describe a system comparison without attributing the gain to one component.
- Count failed runs and explain excluded examples. Use a fixed missing-data policy when videos or images are no longer downloadable.

For latency, state hardware, software, batch size, resolution, concurrency, and whether transfer, decoding, preprocessing, postprocessing, and rendering are included. Warm up the model and synchronize asynchronous accelerators around timed regions. Report a distribution such as p50/p95, throughput, and peak memory; throughput is not single-request latency. Consult the [PyTorch benchmark utilities](https://docs.pytorch.org/docs/stable/benchmark_utils) for controlled timing.

## Quantify uncertainty and inspect failures

Repeat inexpensive experiments across several predetermined seeds. Report the individual values or mean and spread, with the number of runs. Seed variation measures training instability; it does not by itself measure uncertainty from the test population.

For test uncertainty, resample the independent unit—whole patients, scenes, or videos where appropriate. A paired bootstrap of the score difference can compare two systems evaluated on the same units; retain the pairing. Report the confidence level, number of resamples, and sampling unit. Tiny subgroups can have wide intervals: show their sample counts and avoid ranking models on negligible differences.

Choose thresholds on validation data. Report precision/recall at the chosen operating point and performance when the model abstains, including coverage. Probability confidence is meaningful only if it corresponds to observed correctness; reliability plots and proper scoring rules help reveal overconfidence. [Scikit-learn's calibration guide](https://scikit-learn.org/stable/modules/calibration.html) explains the difference between calibration and discrimination.

Inspect failures by class, size, visibility, acquisition condition, and other documented attributes relevant to the task. Do not infer sensitive attributes from images to invent subgroup labels. Keep a reproducible error gallery: randomly sampled errors, highest-confidence errors, and representative successes all reveal different things.

## Evaluate VLM hallucination explicitly

Separate **object presence**, **counting**, **spatial relations**, **OCR**, **temporal order**, and **evidence grounding**. A good aggregate VQA score does not establish reliability in all of them.

[POPE](https://github.com/RUCAIBox/POPE) provides object-presence probes with several negative-sampling settings. Report precision, recall, F1, yes-answer rate, and invalid outputs separately for each setting. An always-no model has a different failure profile from an informative model, even when it makes few affirmative false claims. Missing annotations are not reliable proof that an object is absent.

Freeze the full prompt, system instructions, decoding parameters, image resolution, frame sampling, and output parser. Count unparseable responses according to a predeclared rule; do not silently discard them. Keep the answer extraction code and raw outputs.

For free-form answers, define a rubric before evaluation and audit a blinded sample manually. If a model judges answers, record its version, prompt, sampling settings, and disagreement with human ratings; model judgments are measurements with their own failure modes. [MM-Vet](https://github.com/yuweihao/MM-Vet) is an example of an evaluation design involving multiple visual-language capabilities and model-based scoring. Do not let a favorable judge score replace checking whether the cited image evidence supports the answer.

## Minimal results record

```text
Question and primary metric:
Dataset version / split manifest / exclusions:
Independent sampling unit:
Baseline commit / checkpoint / preprocessing:
Changed factor and matched budget:
Hardware / software / precision / seeds:
Validation-selected settings:
Test result / uncertainty / subgroup sample counts:
Latency scope / peak memory:
Failures / negative results / known leakage risks:
Reproduction command and saved prediction location:
```

[Project briefs](../projects/README.md) · [Compute and setup](compute-and-setup.md) · [Datasets and licenses](datasets-and-licenses.md)
