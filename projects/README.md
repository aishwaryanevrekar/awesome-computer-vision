# Projects

**40 project briefs. Zero toy tutorials.**

Every brief tells you the dataset, the baseline to start from, the metric to report, and the specific way it will probably go wrong. That last part is the point: anyone can train a model, and far fewer people can explain why it failed.

[Beginner](beginner.md) · [Intermediate](intermediate.md) · [Advanced](advanced.md) · [Back to home](../README.md)

> These are specifications, not finished apps. Each links to upstream code to adapt; the work is yours. If you want code that runs right now, start with the [starter programs](../examples/README.md).

## Pick your lane

| I want a... | Do these, in order |
|---|---|
| First portfolio piece | 01 → 03 → 05 → 09 |
| Detection and deployment story | 02 → 11 → 12 → 39 |
| Segmentation project | 03 → 07 → 10 → 20 → 26 |
| OCR and documents | 05 → 13 → 23 → 33 |
| 3D and geometry | 17 → 16 → 28 → 29 → 27 |
| Vision-language research | 06 → 21 → 31 → 32 → 34 |
| Low-compute research | 01 → 18 → 30 → 37 |
| Robotics and video | 08 → 14 → 24 → 35 → 36 |

**Compute key:** 💻 CPU is fine. ⚡ GPU means one modest GPU and a bounded subset. 🔥 High means the full sweep can outgrow a workstation; scope it down first. See [compute and setup](../guides/compute-and-setup.md).

## Beginner (01 to 08)

*You can write Python, manipulate arrays, and make plots.*

| # | Project | What you do | Compute |
|---:|---|---|:---:|
| 01 | [Handwritten digit classifier and error explorer](beginner.md#01-handwritten-digit-classifier-and-error-explorer) | Classify digits, then build a gallery of confident mistakes and ambiguous inputs. | 💻 CPU |
| 02 | [A small image classifier you can debug](beginner.md#02-a-small-image-classifier-you-can-debug) | Train a compact convolutional model and compare augmentation choices. | 💻 CPU |
| 03 | [Pet breed transfer learning](beginner.md#03-pet-breed-transfer-learning) | Compare a frozen image encoder with fine-tuning on a fine-grained classification problem. | 💻 CPU |
| 04 | [Flower recognition with a label budget](beginner.md#04-flower-recognition-with-a-label-budget) | Determine how classification quality changes when only a few training examples are available per category. | 💻 CPU |
| 05 | [Document scanner with measurable geometry](beginner.md#05-document-scanner-with-measurable-geometry) | Detect page corners, rectify perspective, and compare thresholding choices. | 💻 CPU |
| 06 | [Find the same object from another angle](beginner.md#06-find-the-same-object-from-another-angle) | Retrieve gallery images of the query object without returning the query itself. | 💻 CPU |
| 07 | [Foreground extraction with an interaction budget](beginner.md#07-foreground-extraction-with-an-interaction-budget) | Extract a pet foreground from a supplied rectangle and measure where classical segmentation fails. | 💻 CPU |
| 08 | [Hand landmark interaction demo](beginner.md#08-hand-landmark-interaction-demo) | Turn hand landmarks into a simple gesture-controlled interface, such as moving a pointer or advancing slides. | 💻 CPU |

## Intermediate (09 to 24)

*You can train and evaluate a classifier and explain a train/validation/test split.*

| # | Project | What you do | Compute |
|---:|---|---|:---:|
| 09 | [Industrial defect inspection](intermediate.md#09-industrial-defect-inspection) | Flag unusual products and localize suspicious regions using mostly normal training images. | ⚡ GPU |
| 10 | [Road-scene semantic segmentation](intermediate.md#10-road-scene-semantic-segmentation) | Segment a street scene and identify which classes are lost when resolution is reduced. | ⚡ GPU |
| 11 | [Object detection with an honest speed comparison](intermediate.md#11-object-detection-with-an-honest-speed-comparison) | Detect several object categories and evaluate the accuracy/latency trade-off. | ⚡ GPU |
| 12 | [Tracking through occlusion](intermediate.md#12-tracking-through-occlusion) | Maintain object identities across a video and diagnose identity switches. | 💻 CPU |
| 13 | [Document-text recognition under image degradation](intermediate.md#13-document-text-recognition-under-image-degradation) | Recognize words and separate recognition errors from text-detection errors. | 💻 CPU |
| 14 | [Human pose estimation under occlusion](intermediate.md#14-human-pose-estimation-under-occlusion) | Estimate 2D keypoints and quantify how detection quality affects pose quality. | ⚡ GPU |
| 15 | [Long-tailed species classification](intermediate.md#15-long-tailed-species-classification) | Compare ordinary sampling with a class-balanced training strategy. | ⚡ GPU |
| 16 | [Monocular depth: relative versus metric](intermediate.md#16-monocular-depth-relative-versus-metric) | Evaluate whether a depth model recovers scene ordering, metric distances, or both. | ⚡ GPU |
| 17 | [Stereo depth from image pairs](intermediate.md#17-stereo-depth-from-image-pairs) | Compare classical stereo matching and a learned method on rectified pairs. | 💻 CPU |
| 18 | [Corruption robustness audit](intermediate.md#18-corruption-robustness-audit) | Test how a clean-image classifier behaves under common corruptions without retraining on test corruptions. | 💻 CPU |
| 19 | [Skin-lesion boundary segmentation study](intermediate.md#19-skin-lesion-boundary-segmentation-study) | Study segmentation and annotation uncertainty in a research setting. | ⚡ GPU |
| 20 | [Instance masks in crowded scenes](intermediate.md#20-instance-masks-in-crowded-scenes) | Separate overlapping objects of the same category. | ⚡ GPU |
| 21 | [Landmark retrieval with a searchable index](intermediate.md#21-landmark-retrieval-with-a-searchable-index) | Retrieve matching landmarks and measure what an approximate index loses relative to exact search. | 💻 CPU |
| 22 | [Super-resolution with a distortion/perception trade-off](intermediate.md#22-super-resolution-with-a-distortionperception-trade-off) | Reconstruct higher-resolution images and test whether better-looking output preserves detail faithfully. | ⚡ GPU |
| 23 | [Form understanding beyond OCR](intermediate.md#23-form-understanding-beyond-ocr) | Extract structured fields from scanned forms, then distinguish reading errors from layout errors. | ⚡ GPU |
| 24 | [Video action classification without clip leakage](intermediate.md#24-video-action-classification-without-clip-leakage) | Compare a single-frame model with a temporal model under matched video sampling. | ⚡ GPU |

## Advanced (25 to 40)

*You can reproduce a baseline, read a paper, and design a controlled comparison.*

| # | Project | What you do | Compute |
|---:|---|---|:---:|
| 25 | [Open-vocabulary detection and prompt sensitivity](advanced.md#25-open-vocabulary-detection-and-prompt-sensitivity) | Measure whether text prompts identify unfamiliar categories consistently. | ⚡ GPU |
| 26 | [Video segmentation with a fixed prompt budget](advanced.md#26-video-segmentation-with-a-fixed-prompt-budget) | Propagate an object mask through a video and quantify the value of additional interaction. | ⚡ GPU |
| 27 | [Novel-view synthesis with Gaussian splatting](advanced.md#27-novel-view-synthesis-with-gaussian-splatting) | Reconstruct one scene and evaluate unseen camera views. | ⚡ GPU |
| 28 | [Two-view reconstruction and pose reliability](advanced.md#28-two-view-reconstruction-and-pose-reliability) | Reconstruct geometry from image pairs and identify when confidence is unreliable. | ⚡ GPU |
| 29 | [Multi-view geometry under a view budget](advanced.md#29-multi-view-geometry-under-a-view-budget) | Study whether additional images help a feed-forward geometry model or introduce inconsistent predictions. | ⚡ GPU |
| 30 | [Label efficiency of self-supervised features](advanced.md#30-label-efficiency-of-self-supervised-features) | Compare fixed representations using identical labels and classifier capacity. | 💻 CPU |
| 31 | [Multilingual image-text retrieval](advanced.md#31-multilingual-image-text-retrieval) | Measure how retrieval quality varies across languages using the same image gallery. | ⚡ GPU |
| 32 | [Vision-language object hallucination audit](advanced.md#32-vision-language-object-hallucination-audit) | Test whether a model asserts that absent objects are visible and whether prompting changes that behavior. | ⚡ GPU |
| 33 | [Document question answering with evidence](advanced.md#33-document-question-answering-with-evidence) | Answer questions about a document and attach the source region supporting each answer. | ⚡ GPU |
| 34 | [Video understanding under a frame budget](advanced.md#34-video-understanding-under-a-frame-budget) | Determine when video question answering requires temporal evidence instead of one revealing frame. | ⚡ GPU |
| 35 | [Tracking any point through occlusion](advanced.md#35-tracking-any-point-through-occlusion) | Track user-selected points through a video and decide when a point is no longer visible. | ⚡ GPU |
| 36 | [Vision-language-action evaluation in simulation](advanced.md#36-vision-language-action-evaluation-in-simulation) | Evaluate how a pretrained policy handles different task instructions and visual conditions. | 🔥 High |
| 37 | [Continual learning and forgetting](advanced.md#37-continual-learning-and-forgetting) | Train on sequential tasks and quantify what is lost when new classes arrive. | 💻 CPU |
| 38 | [Active learning with a real annotation budget](advanced.md#38-active-learning-with-a-real-annotation-budget) | Decide which unlabeled images should be annotated next under a fixed budget. | 💻 CPU |
| 39 | [Quantization without hiding accuracy losses](advanced.md#39-quantization-without-hiding-accuracy-losses) | Export and quantize a detector or classifier, then measure the full system trade-off. | 💻 CPU |
| 40 | [Synthetic-to-real detection study](advanced.md#40-synthetic-to-real-detection-study) | Test which synthetic rendering choices help detection on real images of the same objects. | 🔥 High |

## What "done" means

A project is finished when someone else can disagree with it productively:

1. **Before you run anything**, write the hypothesis, split policy, compute budget, and primary metric.
2. **Run the simplest valid baseline** and save its config, checkpoint, predictions, and environment.
3. **Change one major thing** and compare on the same data and protocol.
4. **Look at ten failures** and say what conditions break it.
5. **Publish** a short report, a reproducible command, a results table, and the limitations. Include the experiments that did not work if they affect the conclusion.

Use the [experiment report template](../templates/experiment-report.md), read the [evaluation guide](../guides/evaluation.md) and [dataset checklist](../guides/datasets-and-licenses.md) first, and respect upstream licenses.

Baseline links are starting points. Upstream environments and checkpoints may need adjustment before they run.
