# Advanced projects

[Project index](README.md) · [Previous: intermediate](intermediate.md)

These projects turn paper reading into testable research questions. Begin with pretrained inference or cached features, reproduce one result, then investigate a narrow extension. A strong negative result with a sound protocol is a useful outcome.

## 25. Open-vocabulary detection and prompt sensitivity

- **Task:** measure whether text prompts identify unfamiliar categories consistently.
- **Level / compute:** advanced / one GPU for pretrained inference.
- **Data:** [LVIS](https://www.lvisdataset.org/) with the [official API](https://github.com/lvis-dataset/lvis-api). Fix the category list, synonyms, and evaluated subset in advance.
- **Baseline code:** [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO).
- **Measure:** applicable LVIS AP, rare/common/frequent-category results, prompt variance, and latency. Respect partially annotated categories when counting false positives.
- **Failure to investigate:** synonyms changing predictions, phrase-to-box mismatches, and categories declared unseen despite unknown pretraining exposure.
- **Extension / deliverable:** compare canonical names, short definitions, and a fixed prompt ensemble; report pretraining-overlap uncertainty and publish the prompt-to-label mapping.

## 26. Video segmentation with a fixed prompt budget

- **Task:** propagate an object mask through a video and quantify the value of additional interaction.
- **Level / compute:** advanced / one GPU for short videos; long sequences increase memory demands.
- **Data:** [DAVIS](https://davischallenge.org/), selecting a specific year and task protocol.
- **Baseline code:** [SAM 2](https://github.com/facebookresearch/sam2), with an explicit checkpoint and prompt policy.
- **Measure:** region similarity J, contour accuracy F, interaction count, runtime, and memory as sequence length grows.
- **Failure to investigate:** drift after occlusion, object disappearance/re-entry, and near-identical neighboring objects.
- **Extension / deliverable:** compare first-frame-only prompting with a fixed correction schedule. If ground truth generates clicks, label this as simulated interaction and keep it identical across methods.

## 27. Novel-view synthesis with Gaussian splatting

- **Task:** reconstruct one scene and evaluate unseen camera views.
- **Level / compute:** advanced / one compatible GPU for a bounded scene; high compute for large scenes or sweeps.
- **Data:** a scene from [Mip-NeRF 360](https://jonbarron.info/mipnerf360/), following the chosen method's documented camera and holdout protocol.
- **Baseline code:** [3D Gaussian Splatting reference implementation](https://github.com/graphdeco-inria/gaussian-splatting). Check code, renderer, and dataset terms separately.
- **Measure:** held-out PSNR, SSIM, LPIPS where available, rendering latency, training time, and model size.
- **Failure to investigate:** floating artifacts, unseen surfaces, exposure variation, and an impressive camera path that stays near training views.
- **Extension / deliverable:** vary training-view density while fixing evaluation cameras; export comparable renderings and a table of quality versus storage and compute.

## 28. Two-view reconstruction and pose reliability

- **Task:** reconstruct geometry from image pairs and identify when confidence is unreliable.
- **Level / compute:** advanced / one GPU for inference on resized pairs.
- **Data:** [MegaDepth](https://www.cs.cornell.edu/projects/megadepth/), with explicit scene-disjoint development/evaluation subsets and a documented pair sampler.
- **Baseline code:** [DUSt3R](https://github.com/naver/dust3r).
- **Measure:** relative rotation/translation-direction errors, pose-error AUC at declared thresholds, and geometric error under a stated alignment.
- **Failure to investigate:** little overlap, repeated structures, reflective surfaces, and nearly pure rotation with poorly constrained translation.
- **Extension / deliverable:** stratify pairs by overlap and viewpoint difference; test confidence-based abstention and publish both accepted-pair accuracy and coverage.

## 29. Multi-view geometry under a view budget

- **Task:** study whether additional images help a feed-forward geometry model or introduce inconsistent predictions.
- **Level / compute:** advanced / one GPU for few-view inference; high compute for larger view counts.
- **Data:** [ETH3D](https://eth3d.ethz.ch/), selecting a supported subset and using provided calibration/ground truth consistently.
- **Baseline code:** [VGGT](https://github.com/facebookresearch/vggt); optionally compare geometric post-processing with [Open3D](https://github.com/isl-org/Open3D).
- **Measure:** camera error, reconstruction accuracy/completeness under the official protocol where applicable, peak memory, and runtime per view count.
- **Failure to investigate:** weak image overlap, a bad view degrading the reconstruction, and incompatible scale or camera conventions.
- **Extension / deliverable:** compare evenly spaced, random, and overlap-aware view selection; save camera estimates and explain which subset improves coverage.

## 30. Label efficiency of self-supervised features

- **Task:** compare fixed representations using identical labels and classifier capacity.
- **Level / compute:** advanced / CPU after feature caching; one GPU for extraction or limited adaptation.
- **Data:** [Oxford Flowers 102](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/), with repeated label subsets drawn only from the training split.
- **Baseline code:** [DINOv2](https://github.com/facebookresearch/dinov2) versus a supervised encoder from [Torchvision](https://docs.pytorch.org/vision/stable/models.html).
- **Measure:** mean per-class accuracy versus labels per class, spread across subset seeds, and feature extraction cost.
- **Failure to investigate:** tuning the linear head more heavily for one encoder or comparing encoders with different image crops without disclosure.
- **Extension / deliverable:** compare linear probing, nearest neighbors, and one adaptation method; report model size, preprocessing, possible pretraining overlap, and where extra labels matter most.

## 31. Multilingual image-text retrieval

- **Task:** measure how retrieval quality varies across languages using the same image gallery.
- **Level / compute:** advanced / one GPU for small checkpoint inference; CPU for cached-embedding evaluation.
- **Data:** [Crossmodal-3600](https://google.github.io/crossmodal-3600/). Treat it as evaluation data; develop prompts and tuning decisions elsewhere.
- **Baseline code:** choose an explicitly multilingual SigLIP-family checkpoint supported by [big_vision](https://github.com/google-research/big_vision); verify language coverage in the specific model card.
- **Measure:** text-to-image and image-to-text Recall@K per language, macro-average, and embedding/index cost.
- **Failure to investigate:** aggregate scores hiding weak languages, translation artifacts, and confusing semantic similarity with correct image identity.
- **Extension / deliverable:** compare original captions with a separately labeled translation baseline; publish language-wise results and errors reviewed by speakers where available.

## 32. Vision-language object hallucination audit

- **Task:** test whether a model asserts that absent objects are visible and whether prompting changes that behavior.
- **Level / compute:** advanced / one GPU for a suitably small checkpoint; larger checkpoints require high compute.
- **Data:** the [POPE benchmark](https://github.com/RUCAIBox/POPE) with its required source images and separate random/popular/adversarial settings.
- **Baseline code:** a pinned [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) checkpoint and the official POPE evaluator.
- **Measure:** precision, recall, F1, accuracy, and yes-answer rate; retain invalid outputs and report their frequency.
- **Failure to investigate:** an always-no strategy can reduce false claims while becoming useless; incomplete image annotations can also invalidate a negative question.
- **Extension / deliverable:** compare two frozen prompts and a constrained output schema; manually audit a blinded sample and keep object presence separate from counting, relations, and general reasoning claims.

## 33. Document question answering with evidence

- **Task:** answer questions about a document and attach the source region supporting each answer.
- **Level / compute:** advanced / one GPU for compact inference; high compute for high-resolution or larger-model runs.
- **Data:** [DocVQA](https://www.docvqa.org/), respecting task-specific access and evaluation rules.
- **Baseline code:** [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL), compared with [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) plus a simple field lookup on a defined subset.
- **Measure:** official answer score such as ANLS for the relevant task, unsupported-answer rate on a manually audited subset, latency, and image-token or resolution budget.
- **Failure to investigate:** plausible answers from document templates, tiny text lost during resizing, and correct answers with incorrect cited regions.
- **Extension / deliverable:** compare page resizing and tiling; publish answers, evidence boxes, and a separate human rubric for grounding quality.

## 34. Video understanding under a frame budget

- **Task:** determine when video question answering requires temporal evidence instead of one revealing frame.
- **Level / compute:** advanced / one GPU for bounded short clips; high compute for longer videos or large checkpoints.
- **Data:** [Video-MME](https://github.com/MME-Benchmarks/Video-MME), with a fixed benchmark release and accessible video manifest.
- **Baseline code:** use the benchmark's evaluation workflow with [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL).
- **Measure:** official question accuracy by duration/task, sampled-frame budget, decoding time, and inference time. Separate subtitles/audio-enabled and visual-only settings.
- **Failure to investigate:** answer leakage through subtitles, missing decisive events, and comparing unequal frame budgets.
- **Extension / deliverable:** compare uniform sampling, one-frame input, and a declared temporal sampling strategy; retain the sampled frame timestamps for every example.

## 35. Tracking any point through occlusion

- **Task:** track user-selected points through a video and decide when a point is no longer visible.
- **Level / compute:** advanced / one GPU for short clips; cached predictions allow CPU-only analysis.
- **Data:** the [TAP-Vid resources](https://github.com/google-deepmind/tapnet), keeping query sampling and source-video subsets fixed.
- **Baseline code:** [TAPIR in the authors' tapnet repository](https://github.com/google-deepmind/tapnet).
- **Measure:** the benchmark's Average Jaccard, position accuracy thresholds, occlusion accuracy, and latency.
- **Failure to investigate:** reappearance at the wrong location, point drift on deforming surfaces, and camera cuts.
- **Extension / deliverable:** stratify by occlusion duration and motion; create track visualizations with visibility states and compare results at two input resolutions.

## 36. Vision-language-action evaluation in simulation

- **Task:** evaluate how a pretrained policy handles different task instructions and visual conditions.
- **Level / compute:** advanced / high compute for adaptation and rollout sweeps; a small inference check may fit one compatible GPU.
- **Data / environment:** [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO), with the exact task suite, demonstration release, and simulator version recorded.
- **Baseline code:** the documented [OpenVLA](https://github.com/openvla/openvla) evaluation workflow. Follow its checkpoint-specific action normalization and controller conventions.
- **Measure:** rollout success rate with uncertainty across fixed seeds, per-task failures, and inference latency. Offline action error is a separate diagnostic, not task success.
- **Failure to investigate:** coordinate-system errors, action scaling mistakes, sensitivity to camera appearance, and instruction shortcuts.
- **Extension / deliverable:** test one controlled visual shift in simulation; publish rollout videos, seed-level results, and a bounded failure taxonomy.

## 37. Continual learning and forgetting

- **Task:** train on sequential tasks and quantify what is lost when new classes arrive.
- **Level / compute:** advanced / CPU for a small model; one GPU for wider sweeps.
- **Data:** [CIFAR-100](https://cave.cs.toronto.edu/kriz/cifar.html), with a published class order and task partitions.
- **Baseline code:** naive fine-tuning and replay using [Avalanche](https://github.com/ContinualAI/avalanche).
- **Measure:** final average accuracy, forgetting over the task matrix, replay memory, and training cost. Distinguish class-incremental evaluation from task-aware evaluation.
- **Failure to investigate:** silently providing task identity at test time or excluding replay storage from the resource budget.
- **Extension / deliverable:** compare several memory budgets over multiple class orders; save the full task-by-time accuracy matrix and identify which categories are forgotten first.

## 38. Active learning with a real annotation budget

- **Task:** decide which unlabeled images should be annotated next under a fixed budget.
- **Level / compute:** advanced / CPU for cached features; one GPU for repeated fine-tuning rounds.
- **Data:** [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/). Use training labels only to simulate annotation; keep validation and test outside the candidate pool.
- **Baseline code:** build random sampling first with [Torchvision](https://docs.pytorch.org/vision/stable/models.html), then compare uncertainty or feature-diversity selection.
- **Measure:** accuracy against cumulative labels, area under the learning curve, selection cost, and variability across initial pools.
- **Failure to investigate:** a sampler choosing redundant images, using hidden labels during selection, or benefiting from more training per round.
- **Extension / deliverable:** compare image-count and annotation-time budgets using a declared timing model; release selected IDs per round and a protocol diagram.

## 39. Quantization without hiding accuracy losses

- **Task:** export and quantize a detector or classifier, then measure the full system trade-off.
- **Level / compute:** advanced / CPU for deployment evaluation; one GPU optional for source-model inference.
- **Data:** [COCO](https://cocodataset.org/) for a detector or [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/) for a classifier, with separate representative calibration and test data.
- **Baseline code:** [ONNX Runtime quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html), starting from a supported model/export path.
- **Measure:** task accuracy before/after export and quantization, p50/p95 latency, model size, peak memory, and operator coverage on the target execution provider.
- **Failure to investigate:** unsupported operators, preprocessing mismatch, calibration leakage, and an alleged speedup measured without preprocessing or warmup.
- **Extension / deliverable:** compare floating-point and quantized runs on the same device; publish parity checks, worst class regressions, and a reproducible benchmark command.

## 40. Synthetic-to-real detection study

- **Task:** test which synthetic rendering choices help detection on real images of the same objects.
- **Level / compute:** advanced / high compute for rendering and training sweeps; begin with a few objects and one bounded batch.
- **Data:** select permitted object assets and real images from a specific [BOP dataset](https://bop.felk.cvut.cz/datasets/); keep real evaluation scenes untouched.
- **Baseline code:** render with [BlenderProc](https://github.com/DLR-RM/BlenderProc) and train a supported detector in [Detectron2](https://github.com/facebookresearch/detectron2).
- **Measure:** real-image detection AP under a stated protocol, synthetic-only versus mixed-data results, rendering cost, and sensitivity to occlusion. Detection AP is not the official BOP 6D-pose score.
- **Failure to investigate:** unrealistic backgrounds, pose distributions that reveal labels, and tuning render parameters directly on real test data.
- **Extension / deliverable:** ablate lighting, background, and pose diversity separately; publish rendering configs, data manifests, real-image failures, and the best-supported explanation for the domain gap.
