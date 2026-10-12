# Beginner to job-ready: a 24-week computer vision path

Suggested effort: **8–10 hours/week** · Approximately **192–240 focused hours**.

This path assumes basic Python: functions, loops, imports, and reading a traceback. If those are new, add two to four preparatory weeks for small Python and NumPy programs. The outcome is a small collection of projects you understand, can evaluate, and can run for another person. The schedule is a suggested curriculum, not a guarantee of employment.

[All paths](README.md) · [Project choices](../projects/README.md) · [Interview preparation](../career/interview-preparation.md)

## Prepare your workspace and budget

Start with Python, a virtual environment, Git, NumPy, an image library, and a notebook or editor. Add PyTorch using the installation guidance for your own operating system and hardware when you reach week 7. Record the versions that worked. Do not install a large collection of frameworks before choosing a task.

The [included CPU examples](../examples/README.md) provide a first environment check: use image processing in week 1, histogram retrieval in week 3, and the digits baseline when studying splits and evaluation. Track your work in the [study log](../templates/study-tracker.md).

| Compute situation | Practical scope | Scope to postpone |
| --- | --- | --- |
| CPU laptop | Image processing, geometry, data audits, linear models, tiny training runs, cached feature experiments | Training large backbones or repeatedly embedding a huge collection |
| One available GPU | Small image classification, lightweight transfer learning, modest detection experiments | Foundation-model pretraining or unrestricted hyperparameter searches |
| Intermittent borrowed/cloud GPU | Prepare and debug on CPU; use a checkpointed, time-limited GPU job for the final experiment | Workflows that cannot resume after interruption |

Memory needs depend on architecture, resolution, precision, and batch size. Try one forward/backward batch and record peak memory before committing to a run. Reduce input size or batch size first. Gradient accumulation can help with effective batch size, but it does not reproduce all large-batch behavior, particularly batch-normalization statistics.

Set a personal spending limit before enabling a paid runtime; no paid service is required by this path. Save checkpoints and shut down unused resources. Keep datasets out of Git unless their size and license make redistribution appropriate.

Use this weekly rhythm: two hours learning, four to five hours building, one to two hours evaluating, and one hour writing. Read only the sections needed for that week's task.

## Weeks 1–4: images, arrays, and geometry

Core references: [Stanford's Python/NumPy tutorial](https://cs231n.github.io/python-numpy-tutorial/) for array practice; [Szeliski's book](https://szeliski.org/Book/) for image formation and image processing; [OpenCV calibration documentation](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html) for camera conventions. Use the author's book download page rather than redistributing the PDF.

| Week | Learn and build | Deliverable and mastery gate |
| --- | --- | --- |
| 1 | Inspect arrays, RGB/BGR conventions, integer versus floating-point images, resizing, and file failures. Make a contact sheet of a small image folder. | An image-inspection script reports dimensions, channels, and unreadable files. Explain why a visually strange result might be a channel-order or value-range problem. |
| 2 | Implement simple convolution on a tiny array; compare smoothing, edges, and thresholding on real images. Explore aliasing when downsampling. | A notebook with original, transformed, and difference images. Explain one case where thresholding is sufficient and one where it fails. |
| 3 | Review matrix products, derivatives, mean, variance, and conditional probability. Implement nearest-neighbor classification on simple image descriptors. | A baseline with a fixed split and a confusion matrix. Derive the dimensions of every matrix operation and identify the independent sampling unit. |
| 4 | Study coordinates, intrinsics, extrinsics, perspective projection, and homography. Warp a photographed planar object into a front-facing view. | Annotated point correspondences and a warped image. Explain why a single homography fails for a general 3D scene with camera translation. |

**Checkpoint:** given an unfamiliar image dataset, you can inspect it, explain its representation, and create a reproducible non-neural baseline. If you cannot trace the inputs and outputs of your code, repeat the smallest exercise instead of adding a model.

## Weeks 5–8: machine learning and a working training loop

Read the relevant optimization and regularization sections in the [Deep Learning book](https://www.deeplearningbook.org/), use [CS231n](https://cs231n.stanford.edu/) as the course spine, and follow the [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) when implementing tensors and training. The current CS231n offering has some enrolled-student-only material; public notes and older linked recordings are usable without enrollment.

| Week | Learn and build | Deliverable and mastery gate |
| --- | --- | --- |
| 5 | Implement a linear classifier or logistic regression with NumPy. Check a small numerical gradient against your analytical gradient. | A loss curve and gradient-check report. Explain logits, loss, parameters, and the update step without pointing to a library call. |
| 6 | Inspect label counts and duplicates; choose group-aware splits; fit preprocessing on training data only. Compare a majority-class baseline with your classifier. | A data card and saved split manifest. Explain what information may flow from each split into model selection. |
| 7 | Implement a PyTorch dataset, loader, model, loss, optimizer, evaluation function, and checkpoint. Start with a very small subset. | A command that can overfit a tiny clean batch and reload its checkpoint. State what this sanity check establishes and what it does not. |
| 8 | Train a small CNN. Compare learning rates and one regularization change. Keep augmentation off the evaluation path. | A comparison table on the same validation split. Diagnose underfitting, overfitting, or a data pipeline bug from concrete evidence. |

**Checkpoint:** you can explain every step of training, show that checkpoint reload preserves predictions within an appropriate tolerance, and distinguish training loss from held-out performance. Use the [scikit-learn pitfalls guide](https://scikit-learn.org/stable/common_pitfalls.html) to audit leakage and preprocessing.

## Weeks 9–12: transfer learning and credible evaluation

Use [PyTorch's transfer-learning tutorial](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) as a starting point for frozen-feature and fine-tuning experiments. Build your own dataset and analysis around the pattern; credit code you adapt.

| Week | Learn and build | Deliverable and mastery gate |
| --- | --- | --- |
| 9 | Extract pretrained features, cache them with image IDs, and train a small classification head. Compare against week 8. | A feature-cache manifest and baseline report. Explain which parameters learned from your labels. |
| 10 | Unfreeze a limited part of the backbone. Compare it with the frozen baseline using the same preprocessing and validation protocol. | Two configurations and a compute log. Explain whether a gain justifies added time and complexity. |
| 11 | Select metrics and an operating threshold using validation data. Inspect class imbalance, calibration, and application-specific error costs. | A precision–recall view plus a threshold decision. Explain why accuracy alone may hide an unusable model. |
| 12 | Review at least 30 errors, grouped by plausible cause. Evaluate a prespecified slice such as blur or lighting. Run the untouched test set once after selection. | A short report with baseline, chosen model, test protocol, denominators, and failure examples. Separate observed errors from hypotheses about their cause. |

**Checkpoint:** another person can identify the test set, recover the selected configuration, and understand which decision the metric supports. Consult [scikit-learn's metric definitions](https://scikit-learn.org/stable/modules/model_evaluation.html) when implementing calculations. Small test sets require cautious conclusions; many decimals do not add evidence.

## Weeks 13–16: localization and a chosen specialization

Follow the [TorchVision detection tutorial](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html) for dataset conventions. For detection evaluation, inspect the [official COCO evaluator](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py), including its matching and evaluation settings. Use a modest dataset and a pretrained checkpoint.

| Week | Learn and build | Deliverable and mastery gate |
| --- | --- | --- |
| 13 | Understand boxes, masks, IoU, and annotation conventions. Visualize every annotation in a small sample before training. | A data validator and overlay gallery. Explain how a wrong coordinate convention can silently destroy evaluation. |
| 14 | Fine-tune a small detector or segmentation model. Make geometric transforms update annotations together with images. | A baseline evaluation and examples of true positives, false positives, and misses. Explain class, size, and overlap settings for your metric. |
| 15 | Choose one branch: tracking/video, OCR/documents, geometry/3D, or image retrieval. Read one primary implementation and build a small inference pipeline. | A written task definition and a working baseline. Explain what your branch requires beyond single-image classification. |
| 16 | Evaluate your branch under one realistic shift: another session, camera, document layout, or image source. | A slice report and three investigated failures. Separate “did not run” from “ran and failed.” |

**Checkpoint:** finish one branch before expanding. If GPU access is limited, weeks 14–16 may use pretrained inference and focus on annotation, evaluation, and postprocessing; clearly label that choice instead of claiming training experience.

## Weeks 17–20: representations, multimodal vision, and deployment

Use the official [CLIP repository](https://github.com/openai/CLIP) to explore image–text retrieval and prompt sensitivity. It is a useful teaching baseline, not the strongest current model. Choose more recent alternatives through the [research landscape](../research/landscape.md) only when they fit your task and hardware.

| Week | Learn and build | Deliverable and mastery gate |
| --- | --- | --- |
| 17 | Compare text–image similarity with a supervised baseline. Freeze a small prompt set before test evaluation. | A retrieval or zero-shot classification report. Explain why similarity scores are not automatically calibrated probabilities. |
| 18 | Evaluate a vision-language model or an accessible existing output set on a narrow, human-checkable task. Include absent objects, difficult text, and an abstention option. | An evaluation sheet with a clear rubric and independently checked answers. Record model/checkpoint, prompt, decoding settings, and uncertain labels. |
| 19 | Package your chosen model behind a local CLI or small demo. Check corrupt inputs, unsupported image sizes, and preprocessing parity. | A clean-install run command and example input/output. Keep user-facing results separate from tracebacks and diagnostics. |
| 20 | Profile loading, decoding, preprocessing, inference, and postprocessing. Try one justified optimization. | A quality/latency/memory comparison with hardware, batch size, warmup, and measurement boundaries. Explain the accuracy cost of any change. |

**Checkpoint:** the demo reproduces the offline preprocessing and reports failures predictably. If trying quantization, read [ONNX Runtime's quantization guidance](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html); measure it on the target runtime. Smaller weights alone do not establish lower end-to-end latency.

## Weeks 21–24: an independent capstone and interview evidence

| Week | Learn and build | Deliverable and mastery gate |
| --- | --- | --- |
| 21 | Pick one problem from the [project catalog](../projects/README.md), define the user and constraints, and lock an evaluation plan. Reuse your pipeline where appropriate. | A one-page proposal with a simple baseline, split rule, metric, compute cap, and explicit non-goals. |
| 22 | Improve one measured failure mode. Keep an experiment log and compare against the unchanged baseline. | One controlled ablation. Explain what changed, what stayed fixed, and what alternative explanation remains. |
| 23 | Rerun the final workflow from a fresh environment. Create a failure gallery, model/data notes, and a short demo recording. | A peer-readable [portfolio project](../career/portfolio.md). Every headline number links to an evaluation artifact. |
| 24 | Practice the [interview questions](../career/interview-preparation.md), conduct a mock project review, and fix the biggest comprehension gap. | A five-minute explanation plus a deeper technical walkthrough. Answer “What would you do next with twice the data but the same compute?” |

## Finish with evidence, then choose depth

Completion means you have a data/split record, a reproducible baseline, an evaluated improvement, a runnable demonstration, and an honest limitations section. A failed improvement can still be a useful result when the experiment answers a clear question.

For engineering depth, repeat the capstone with deployment constraints and a new data source. For research depth, continue with the [12-week replication path](research.md). For geometry-heavy roles, spend additional time on calibration, multiview geometry, optimization, and coordinate conventions before adding another model family.
