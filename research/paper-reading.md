# Research papers: from first reading to a useful improvement

**40 papers, each with prerequisites and an experiment to try.**

Start with the common foundations, then follow a specialty. Reading everything in order is optional. The aim is to understand a claim, reproduce a manageable part of it, and test a well-defined improvement.

Paper links go to the original manuscript, official proceedings, or an academic copy of the original paper. Years generally indicate the first public manuscript; the conference year can differ. The 2025–2026 selections are supported by public papers and official artifacts, not forecasts. See the [Research landscape](landscape.md) for release and evaluation caveats.

## Before your first paper

You should be able to load an image, inspect array shapes, implement a train/validation split, train a small classifier, and explain a confusion matrix. Learn gradients, matrix multiplication, convolution, probability, and overfitting alongside the first readings. Use [CS231n](https://cs231n.stanford.edu/), [Dive into Deep Learning](https://d2l.ai/), and [Szeliski's book](https://szeliski.org/Book/) when a concept is missing.

| Level | Read when you can… | A reasonable output |
| --- | --- | --- |
| Beginner | Follow a training loop and inspect images or features | An annotated architecture diagram and a small controlled experiment |
| Intermediate | Explain a loss, evaluate a baseline, and debug data or tensor shapes | One reproduction result with a fair baseline and failure analysis |
| Advanced | Read attention and probability notation; understand the specialty's metrics | An ablation, robustness study, or adaptation with a clear limitation |

A paper can be suitable for a beginner to **read** while its original experiment is far too expensive to reproduce. The exercises below deliberately allow smaller datasets, pretrained checkpoints, and analysis. Label these as educational experiments or partial reproductions.

## A. Beginner: representations, convolution, and dense prediction

Read 1–6 for a first pass. For a deep-learning-first route, start at 3 and return to 1–2 when studying matching or geometry.

| # | Paper | Learn this | Exercise |
| --- | --- | --- | --- |
| 1 | [SIFT — Distinctive Image Features from Scale-Invariant Keypoints](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf) · 2004 | Separate finding repeatable locations from describing and matching them. | Match a scene to rotated and resized versions; plot the fraction of geometrically consistent matches as the transformation increases. |
| 2 | [Histograms of Oriented Gradients for Human Detection](https://www.cs.princeton.edu/courses/archive/fall13/cos429/papers/Dalal05.pdf) · 2005 | Understand how local gradient statistics encode shape before learned features. | Visualize HOG cells on the same image at two resolutions, then compare a HOG classifier with a raw-pixel baseline. |
| 3 | [AlexNet — ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) · 2012 | Connect architecture, nonlinearities, regularization, and training infrastructure. | Train a small CNN with and without augmentation under the same budget; compare learning curves and inspect ten errors. |
| 4 | [VGG — Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) · 2014 | Trace how stacked small convolutions change receptive fields and parameter count. | Compute shapes and parameter counts for a small VGG-style model; compare one large kernel with stacked smaller kernels. |
| 5 | [ResNet — Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) · 2015 | Explain residual learning and distinguish optimization failure from overfitting. | Compare shallow plain and residual networks with matched training settings; inspect training loss before comparing validation accuracy. |
| 6 | [U-Net](https://arxiv.org/abs/1505.04597) · 2015 | Explain the roles of downsampling, upsampling, and skip connections in localization. | Train a small segmentation model; remove one skip connection and compare IoU plus thin-boundary errors. |

**Checkpoint:** draw a model from memory, explain every tensor dimension, and show why your baseline is fair. If these are difficult, repeat a small experiment before adding new architectures.

## B. Intermediate: objects, keypoints, and motion

Prerequisites: stage A; IoU, precision/recall, image coordinates, and basic linear algebra. For tracking, learn association and a basic Kalman filter. For optical flow, review image warping and interpolation.

| # | Paper | Learn this | Exercise |
| --- | --- | --- | --- |
| 7 | [Faster R-CNN](https://arxiv.org/abs/1506.01497) · 2015 | Separate proposal recall, classification, and box refinement. | Run a pretrained detector; measure how proposal count affects missed objects, runtime, and final detection quality. |
| 8 | [You Only Look Once](https://arxiv.org/abs/1506.02640) · 2015 | Understand the original one-stage detection formulation and its error modes. | Compare a one-stage baseline with a two-stage baseline at the same input size; categorize localization and background errors. |
| 9 | [Feature Pyramid Networks](https://arxiv.org/abs/1612.03144) · 2016 | Explain why small and large objects need useful features at different spatial scales. | Resize the same validation images and report accuracy by object-size bin; inspect which errors change with resolution. |
| 10 | [Mask R-CNN](https://arxiv.org/abs/1703.06870) · 2017 | Understand instance masks, multi-task heads, and spatial alignment. | Overlay boxes and masks separately; compare box failures with mask-boundary failures on a fixed set of examples. |
| 11 | [Simple Baselines for Human Pose Estimation and Tracking](https://arxiv.org/abs/1804.06208) · 2018 | Learn heatmap-based keypoints and why crop quality affects top-down pose estimation. | Perturb person boxes and measure keypoint error; compare visible and occluded joints under the same perturbation. |
| 12 | [ByteTrack](https://arxiv.org/abs/2110.06864) · 2021 | Explain why low-confidence detections can help preserve an existing identity. | Hold detections fixed, vary the association thresholds, and report identity switches and fragmented tracks. |
| 13 | [RAFT](https://arxiv.org/abs/2003.12039) · 2020 | Understand correlation, iterative refinement, and optical-flow warping. | Estimate flow on a short sequence; visualize warped-frame residuals and inspect occlusion or motion-boundary failures. |

**Checkpoint:** a good detector does not automatically imply a good tracker, and good box overlap does not imply a good instance mask. Name the output and metric before comparing models.

## C. Intermediate to advanced: attention, self-supervision, and language

Prerequisites: gradient-based training, softmax, dot products, embeddings, and the difference between pretraining and downstream evaluation. Read 14 before 15–16; read 17–20 before selecting a foundation-model specialty.

| # | Paper | Learn this | Exercise |
| --- | --- | --- | --- |
| 14 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · 2017 | Derive scaled dot-product attention and distinguish token, head, and embedding axes. | Implement a small attention layer; verify tensor shapes and show how memory grows as token count increases. |
| 15 | [Vision Transformer](https://arxiv.org/abs/2010.11929) · 2020 | Explain image patch tokenization, positions, and the role of pretraining data. | Compare two pretrained backbones on one small dataset; hold adaptation budget fixed and report resolution and parameter count. |
| 16 | [DETR](https://arxiv.org/abs/2005.12872) · 2020 | Explain learned queries, bipartite matching, and a set-based detection objective. | Solve a tiny box-matching example by hand, then inspect unmatched queries and duplicate predictions from a checkpoint. |
| 17 | [SimCLR](https://arxiv.org/abs/2002.05709) · 2020 | Explain positive pairs, negative pairs, augmentations, and the projection head. | Change one augmentation in a small contrastive run; evaluate frozen features with the same linear probe. |
| 18 | [DINO — Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294) · 2021 | Understand teacher-student self-distillation and the importance of representation evaluation. | Extract frozen features for a small image collection; inspect nearest neighbors and compare with supervised features. |
| 19 | [Masked Autoencoders](https://arxiv.org/abs/2111.06377) · 2021 | Separate reconstruction quality from the quality of a reusable encoder. | Vary mask ratio in a toy reconstruction task and compare a downstream probe, not only reconstruction loss. |
| 20 | [CLIP](https://arxiv.org/abs/2103.00020) · 2021 | Understand contrastive image-text alignment and zero-shot classification through prompts. | Freeze labels and test several prompt templates; report per-class changes and failure cases on unfamiliar categories. |
| 21 | [LLaVA — Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) · 2023 | Trace the connection between a vision encoder, language model, and instruction data. | Create a small visual-question set with answerable and unanswerable items; classify errors as perception, reasoning, or unsupported claims. |
| 22 | [Grounding DINO](https://arxiv.org/abs/2303.05499) · 2023 | Connect language-conditioned recognition with object localization. | Compare category nouns, descriptive phrases, and distracting attributes; measure box precision and missed instances. |
| 23 | [Segment Anything](https://arxiv.org/abs/2304.02643) · 2023 | Understand promptable masks, ambiguity, and model-assisted annotation. | Compare point and box prompts on twenty difficult images; record mask quality and correction count. |
| 24 | [SAM 2](https://arxiv.org/abs/2408.00714) · 2024 | Explain how memory carries segmentation information across video frames. | Annotate an object before occlusion; inspect drift and re-entry behavior, then measure the effect of an additional correction. |

**Checkpoint:** specify whether a comparison uses a frozen encoder, a linear probe, partial adaptation, or full fine-tuning. Different training regimes answer different questions.

## D. Advanced: generation, 3D, and action

Prerequisites vary. Diffusion needs probability and noisy conditional prediction. Geometry needs camera projection, coordinate transforms, and volume rendering. Robotics needs demonstration formats, action spaces, and open-loop versus closed-loop evaluation. Pick one branch before attempting all six papers.

| # | Paper | Learn this | Exercise |
| --- | --- | --- | --- |
| 25 | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) · 2020 | Connect a forward noise process with learned reverse denoising. | Implement a tiny diffusion model on small images; visualize noisy inputs and samples at several timesteps. |
| 26 | [Latent Diffusion Models](https://arxiv.org/abs/2112.10752) · 2021 | Understand the compression-versus-detail tradeoff of generating in latent space. | Compare reconstruction errors with generation errors and measure how resolution and sampling steps affect memory and time. |
| 27 | [NeRF](https://arxiv.org/abs/2003.08934) · 2020 | Derive ray sampling, density, transmittance, and compositing. | Render a simple synthetic scene with known cameras; hold out views and inspect geometry as well as image similarity. |
| 28 | [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079) · 2023 | Compare an explicit Gaussian scene representation with a neural radiance field. | Use the same posed images for two reconstruction baselines; report held-out view quality, training time, render time, and storage. |
| 29 | [DUSt3R](https://arxiv.org/abs/2312.14132) · 2023 | Understand pairwise point-map prediction and alignment into a common frame. | Reconstruct image pairs with decreasing overlap; inspect confidence, pose consistency, and failure on repeated textures. |
| 30 | [OpenVLA](https://arxiv.org/abs/2406.09246) · 2024 | Trace the conversion from visual and language features to robot actions. | Inspect one demonstration dataset and a supported evaluation setup; document action units, normalization, camera views, and task-success definition. |

**Checkpoint:** evaluate the actual target. Novel-view rendering, metric geometry, realistic generation, and task completion are distinct outcomes.

## E. Advanced: 2025 methods to understand before extending them

These papers connect the previous foundations to available modern systems. A pretrained inference or adaptation study is usually more feasible than reproducing their pretraining.

| # | Paper | Read after | Learn this and try it |
| --- | --- | --- | --- |
| 31 | [DINOv3](https://arxiv.org/abs/2508.10104) · August 2025 | 15, 18, 19 | Study dense representations and their transfer. Compare frozen features with a small fine-tuned baseline on one segmentation or retrieval task; keep the label budget fixed. |
| 32 | [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) · November 2025 | 16, 22–24 | Understand concept-level prompting across image and video. Evaluate ambiguous descriptions and absent objects; measure false positives as well as mask overlap. |
| 33 | [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) · November 2025 | 14, 20, 21 | Examine multimodal inputs, resolution, and video handling. Hold questions fixed while varying visual token or frame budget; compare accuracy, unsupported answers, and latency. |
| 34 | [VGGT](https://arxiv.org/abs/2503.11651) · March 2025 | 15, 29; camera geometry | Study joint prediction of geometric quantities from views. Change frame spacing and overlap, then inspect pose and depth against known references. |
| 35 | [Depth Anything 3](https://arxiv.org/abs/2511.10647) · November 2025 | 29, 34 | Understand the depth-ray representation and multiple input settings. Compare single-view and multiview results; document scale alignment and evaluate geometry consistency. |
| 36 | [pi0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) · April 2025 | 20, 30; imitation learning | Examine heterogeneous training data and generalization claims. Use a supported simulator or recorded-data evaluation to test one held-out condition; distinguish this from a real-robot reproduction. |

For implementation details, start from [DINOv3](https://github.com/facebookresearch/dinov3), [SAM 3](https://github.com/facebookresearch/sam3), [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL), [VGGT](https://github.com/facebookresearch/vggt), [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3), and [openpi](https://github.com/Physical-Intelligence/openpi). Check code and checkpoint licenses separately.

## F. Advanced: 2026 reading

Treat these as focused extensions of a specialty. Read the evaluation setup and release notes before using a reported result as your baseline.

| # | Paper | Read after | Learn this and try it |
| --- | --- | --- | --- |
| 37 | [PaddleOCR-VL-1.5](https://arxiv.org/abs/2601.21957) · January 2026 | 15, 21, 33; OCR metrics | Study document parsing under physical image distortions. Compare clean scans with matched photographed or warped pages and report text, table, and reading-order errors separately. |
| 38 | [Qwen3-VL-Embedding and Qwen3-VL-Reranker](https://arxiv.org/abs/2601.04720) · January 2026 | 20, 33; retrieval metrics | Understand candidate retrieval versus pairwise reranking. Build a labeled image/document search set; report recall before reranking and ranking quality plus added latency afterward. |
| 39 | [V-JEPA 2.1](https://arxiv.org/abs/2603.14482) · March 2026 | 18, 19; video sampling | Examine dense predictive loss and deep self-supervision. Compare frozen video features with an image-only baseline, then shuffle frames to test sensitivity to temporal information. |
| 40 | [VGGT-Omega](https://arxiv.org/abs/2605.15195) · May 2026 | 34, 35 | Study register attention and geometric training at scale. Use the designated reproduction checkpoint, vary input frames, and compare geometric error with peak memory. |

The [V-JEPA code](https://github.com/facebookresearch/vjepa2), [retrieval implementation](https://github.com/QwenLM/Qwen3-VL-Embedding), and [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) provide starting points. SAM 3.1 is a March 2026 implementation update worth testing after paper 32; pin its [release and checkpoints](https://github.com/facebookresearch/sam3). For paper 40, the authors specify a September 2026 [reproduction checkpoint](https://github.com/facebookresearch/vggt-omega) for benchmark comparisons; do not mix results from the original and reproduction checkpoints.

## Reading routes by specialty

The numbers below refer to the tables above. Complete the stated prerequisites when skipping between stages.

| Goal | Suggested sequence | A concrete improvement question |
| --- | --- | --- |
| Classification and transfer | 3 → 4 → 5 → 15 → 17 → 18 → 19 → 31 | Can a frozen backbone match fine-tuning with fewer labels under a camera shift? |
| Detection | 5 → 7 → 8 → 9 → 14 → 16 → 22 | Can resolution or data changes improve small-object recall at a fixed latency? |
| Segmentation and annotation | 6 → 10 → 23 → 24 → 32 | Which prompts reduce correction time on thin, occluded, or ambiguous objects? |
| Tracking, pose, and motion | 9 → 11 → 12 → 13 → 24 → 39 | Does temporal information improve identity continuity or only framewise quality? |
| VLMs and visual search | 14 → 15 → 20 → 21 → 33 → 38 | Is a failure caused by perception, candidate recall, reranking, or unsupported reasoning? |
| OCR and document understanding | 6 → 15 → 21 → 33 → 37 → 38 | Which page distortions or layouts break extraction, and can a targeted change fix them? |
| 3D and spatial vision | 1 → camera geometry → 27 → 28 → 29 → 34 → 35 → 40 | Does a method preserve geometry when overlap drops or the scene moves? |
| Generative vision | 6 → 14 → 25 → 26 | Does a control or efficiency change preserve quality on a fixed prompt set? |
| Robotics and VLA | 20 → 21 → 30 → 36 → 39 | Does an adaptation transfer to held-out conditions within one documented embodiment? |

## How to read one paper

1. **First pass, about 20 minutes:** read the abstract, figures, introduction, and conclusion. Write the task, central idea, strongest evidence, and one limitation in your own words.
2. **Second pass, about 60–90 minutes:** trace inputs, intermediate representations, outputs, and loss terms. Follow one example through the method. Read experimental controls, appendix details, and failure cases.
3. **Third pass, as needed:** read the implementation and reproduce the smallest meaningful result. Match preprocessing, splits, checkpoint, and metric before changing the method.
4. **Compare with a neighbor:** read one preceding method and one later method. Explain exactly what changed and whether data, compute, or evaluation changed too.

These times are planning estimates, not completion requirements. Difficult papers can take several sessions. An abstract or a demo is enough to decide whether to investigate a paper; it is insufficient evidence for claiming a reproduction.

## A practical reproduction checklist

- [ ] Name the exact claim or table row being tested; record paper version and date.
- [ ] Save code commit, checkpoint identifier, environment, configuration, and random seed.
- [ ] Check data access, licenses, preprocessing, label mapping, and train/validation/test splits.
- [ ] Split by person, scene, document, video, or time where random image splitting would leak information.
- [ ] Run a small smoke test and overfit a tiny batch to detect implementation problems.
- [ ] Match the reference metric, evaluator version, threshold selection, and aggregation.
- [ ] Distinguish full reproduction, checkpoint evaluation, partial reproduction, and a toy educational experiment.
- [ ] Compare a simple baseline with the method at an explicit data and compute budget.
- [ ] Record failures, confidence intervals or run variability where practical, and unsuccessful trials.
- [ ] Keep final test data untouched until choices are fixed; log all validation-driven decisions.
- [ ] Measure runtime and memory on named hardware when efficiency is part of the claim.
- [ ] Explain deviations and unresolved mismatches before presenting a new improvement.

For large pretrained models, repeated full training may be unaffordable. Prefer repeated low-cost probes or bootstrap uncertainty over evaluation units such as scenes or documents. State what uncertainty this measures; it does not estimate variability across unseen pretraining runs.

## Turn a failure into an improvement

A defensible improvement starts with a repeatable problem. Examples include small-object recall, mask boundaries, an OCR script, retrieval of charts, camera shift, frame sampling, or geometric inconsistency. Changing many components at once makes the result harder to explain.

| Step | Record |
| --- | --- |
| Observe | A fixed error slice with representative examples and its frequency |
| Hypothesize | A mechanism that could explain the errors and a measurable prediction |
| Control | An unchanged baseline, split, metric, resolution, and training budget |
| Change | One intervention: data, loss, architecture, adaptation, or inference |
| Ablate | Remove the intervention or compare with a cheaper alternative |
| Check transfer | Evaluate a second dataset or a held-out condition when feasible |
| Account for cost | Extra labels, parameters, memory, compute, and end-to-end latency |
| Conclude | Where it helped, where it failed, and what remains uncertain |

For example, if a detector misses tiny objects, first stratify recall by object area. Compare increased input resolution with a targeted crop policy under a stated latency limit. Keep the detector checkpoint, threshold-selection procedure, and held-out scenes fixed. If both improve recall, report the extra compute and analyze whether the gains survive a new camera. This is a useful result even when no new architecture is introduced.

## Reading and experiment note template

Copy this into an issue, notebook, or your own experiment log:

```text
Paper and version:
Primary link and code commit:
Task and output:
Prerequisites I had to review:
Central idea in three sentences:
One equation or diagram I can explain:
Claim I will test:
Data, split, and leakage checks:
Baseline and fixed budget:
Exact command/configuration and checkpoint:
Metric and evaluator version:
Result, variability, and cost:
Five representative failures:
Difference from the paper's setup:
Improvement hypothesis:
One-factor intervention and ablation:
Held-out evaluation result:
What this result supports, and what it does not:
Next experiment:
```

## Keep the reading list useful

A good addition includes a primary paper link, prerequisites, a specific learning objective, one feasible exercise, and available artifacts. Explain why it fills a gap in this sequence. A newer publication date alone is not enough. Corrections to dates, links, licensing notes, or reproduction instructions are useful contributions too.
