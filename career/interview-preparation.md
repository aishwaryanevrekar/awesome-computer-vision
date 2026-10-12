# Computer vision interview preparation

Suggested plan: **four weeks, 7–10 hours/week**.

Use these questions to rehearse reasoning, calculations, debugging, and design tradeoffs. Role expectations vary: a geometry role, research role, and deployment role need different depth.

[Learning paths](../roadmaps/README.md) · [Portfolio guide](portfolio.md) · [Project catalog](../projects/README.md)

## Four-week schedule

| Week | Focus | Practice and deliverable |
| --- | --- | --- |
| 1 | Fundamentals and data | Answer questions 1–15 aloud. Implement convolution output-shape checks, a confusion matrix, IoU, and a group-overlap audit. Keep a mistake log. |
| 2 | Geometry, models, and multimodal vision | Answer questions 16–27. Draw camera coordinates, detection pipelines, attention shapes, and retrieval versus generation. Inspect one primary implementation. |
| 3 | Systems and debugging | Answer questions 28–35. Run a 45-minute system-design session and diagnose a deliberately broken pipeline. Profile one of your own projects. |
| 4 | Mock interviews and project defense | Conduct two 45-minute mocks: one coding/fundamentals and one design/project session. Revisit weak topics, and prepare a five-minute project walkthrough. |

For each answer: state assumptions, explain the mechanism, give a concrete example, then name a failure case. Score yourself from 0 to 3: **0** cannot answer; **1** recalls terms; **2** explains and calculates; **3** handles a changed assumption. The cues below are minimum checkpoints, not complete scripts.

## Fundamentals and training: questions 1–7

References: [CS231n convolution notes](https://cs231n.github.io/convolutional-networks/), the [Deep Learning book](https://www.deeplearningbook.org/), and [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html).

1. **A 64×64 RGB image enters a convolution with 16 output channels, a 3×3 kernel, stride 2, padding 1, dilation 1, and bias. What is the output shape and parameter count?**
   Cue: 16×32×32 without the batch dimension; 16×3×3×3 + 16 = 448 parameters. Explain why image width affects activation memory but not this parameter count.

2. **Derive the gradient of softmax cross-entropy with respect to logits for a one-hot target.**
   Cue: the per-example gradient is predicted probabilities minus the target vector. State any batch reduction factor. Explain stable log-sum-exp and why applying softmax twice is wrong.

3. **Why can training loss decrease while validation performance gets worse?**
   Cue: overfitting is one explanation; also inspect distribution mismatch, label noise, metric/threshold changes, and evaluation preprocessing. Propose a check that distinguishes two hypotheses.

4. **Your model cannot fit 16 clean examples. What do you check first?**
   Cue: image/label alignment, shapes, loss inputs, nonzero gradients, optimizer parameters, learning rate, mode, and augmentation. Reduce the pipeline until one update has an inspectable effect.

5. **What changes between training mode, evaluation mode, and disabled gradient tracking?**
   Cue: mode controls behaviors such as dropout and batch normalization; disabling gradient recording concerns autograd. One does not automatically substitute for the other.

6. **How would you choose between training from scratch, a frozen backbone, and fine-tuning?**
   Cue: consider labels, domain shift, compute, and a common evaluation protocol. Begin with a cheap baseline; justify unfreezing through evidence rather than model size.

7. **Why can an augmentation hurt?**
   Cue: it may change the label, erase the relevant feature, create unrealistic inputs, or desynchronize boxes/masks. Give task-specific examples such as flipped text and cropped-out objects.

## Data and evaluation: questions 8–15

References: [scikit-learn's pitfalls guide](https://scikit-learn.org/stable/common_pitfalls.html), [metric definitions](https://scikit-learn.org/stable/modules/model_evaluation.html), [calibration guide](https://scikit-learn.org/stable/modules/calibration.html), and the [official COCO evaluator](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py).

8. **How would you split a dataset containing many frames from each video?**
   Cue: group by the deployment-relevant independent unit, potentially video, camera, location, or session. Near-duplicate frames across splits inflate apparent generalization. Explain how a time-based holdout changes the question.

9. **Which preprocessing operations can leak information?**
   Cue: fitting normalization, feature selection, imputation, or dimensionality reduction using held-out data. Fit learned transformations on training data, then apply them consistently; preserve test isolation during selection.

10. **For TP = 30, FP = 10, and FN = 20, calculate precision, recall, and F1.**
    Cue: precision = 0.75; recall = 0.60; F1 = 2TP/(2TP+FP+FN) = 2/3. Discuss error costs before choosing the threshold.

11. **Why might a model with 99% accuracy be useless on a defect dataset?**
    Cue: inspect prevalence and the confusion matrix. A majority-class predictor could reach that accuracy. Examine rare-class recall and precision at a usable operating point.

12. **How do IoU, AP50, and COCO-style AP differ?**
    Cue: IoU measures spatial overlap; AP evaluates ranked detections under matching rules; AP50 uses a 0.50 IoU threshold. Standard COCO AP averages across 0.50:0.05:0.95 and categories, with additional settings that must match.

13. **Why can pixel accuracy conceal poor segmentation?**
    Cue: dominant background can overwhelm small foreground errors. Inspect per-class IoU or Dice, the aggregation rule, and the convention for empty masks.

14. **What does it mean for confidence scores to be calibrated?**
    Cue: predicted probabilities should agree with empirical frequencies under the evaluated distribution. Use held-out calibration data; reliability diagrams reveal behavior that accuracy alone does not.

15. **Model A scores 0.3 points above model B. Is A better?**
    Cue: ask about test size, paired errors, run variability, and practical relevance. Resample independent units when estimating uncertainty; avoid treating correlated frames as independent samples.

## Camera geometry: questions 16–20

References: [OpenCV camera calibration and 3D reconstruction](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html) and Hartley and Zisserman's [Multiple View Geometry](https://www.robots.ox.ac.uk/~vgg/hzbook/).

16. **What are camera intrinsics and extrinsics? Write the pinhole projection relation.**
    Cue: scaled homogeneous pixel coordinates satisfy `s·p = K[R|t]P`. Intrinsics map camera coordinates to pixels; extrinsics transform the stated world frame into the camera frame. Declare conventions.

17. **If an image is resized or cropped, what happens to the intrinsic matrix?**
    Cue: resizing scales focal lengths and principal-point coordinates along the relevant axes. Cropping shifts the principal point. Account for the actual sequence of transforms.

18. **When is a homography an appropriate image-to-image model?**
    Cue: a planar scene or pure camera rotation under a pinhole model. General translation with depth variation causes parallax and violates the single-plane mapping.

19. **What is the relationship between the fundamental matrix and essential matrix?**
    Cue: the fundamental matrix constrains corresponding pixel coordinates; the essential matrix uses calibrated coordinates. With consistent conventions, `E = K₂ᵀ F K₁`. Discuss degeneracy and unknown scale.

20. **How would you diagnose a poor camera calibration?**
    Cue: inspect reprojection residuals, spatial coverage, view diversity, target measurements, distortion assumptions, and held-out views. A single low average error can conceal structured failures.

## Models, retrieval, and vision-language systems: questions 21–27

References: the [CLIP paper](https://arxiv.org/abs/2103.00020), [DINOv2 implementation](https://github.com/facebookresearch/dinov2), and [Transformers multimodal input documentation](https://huggingface.co/docs/transformers/main/en/chat_templating_multimodal). Model-specific processors and supported inputs must match the checkpoint and library version you use.

21. **How does detection differ from classification, and why is postprocessing part of evaluation?**
    Cue: detection predicts locations and classes for a variable number of instances. Thresholding, duplicate suppression, box conversion, and matching rules affect reported errors.

22. **How does increasing image resolution affect a standard global-attention vision transformer?**
    Cue: with fixed patch size, doubling both dimensions gives four times as many tokens and sixteen times as many attention-score entries. Distinguish this from total model runtime and optimized memory use.

23. **What can you learn from a linear probe on frozen features?**
    Cue: it measures how useful a fixed representation is under the chosen probe protocol. The backbone does not learn from downstream labels; probe tuning and preprocessing still affect the conclusion.

24. **How does a CLIP-style retriever differ from an autoregressive vision-language model?**
    Cue: one compares image/text embeddings; the other generates token sequences conditioned on visual and textual inputs. Retrieval relevance and factual answer correctness require different evaluation.

25. **Why can zero-shot classification change when you alter the candidate labels or prompt wording?**
    Cue: text embeddings and the comparison set change. Validate prompt choices separately and record them. A normalized score among supplied candidates is not proof of real-world certainty.

26. **How would you evaluate a VLM that extracts fields from invoices?**
    Cue: define field schemas, normalization, missing-field behavior, and a document-separated test set. Measure field-level correctness and document-level success; inspect hallucinated fields and retain source evidence.

27. **How would you test whether a VLM is relying on language priors instead of the image?**
    Cue: use controlled image swaps, absent-object cases, counterfactual pairs, and answerable questions. Compare outputs with a rubric; fluent explanations alone do not demonstrate visual grounding.

## Deployment, debugging, and system design: questions 28–35

References: [PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html), [ONNX Runtime quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html), and [PyTorch reproducibility guidance](https://docs.pytorch.org/docs/main/notes/randomness.html).

28. **What belongs in a credible inference benchmark?**
    Cue: hardware, runtime, precision, input size, batch size, warmup, sample count, and timing boundaries. Synchronize asynchronous device work appropriately. Report latency distribution and throughput separately.

29. **Design a system to count packages passing a camera without counting each frame as a new package.**
    Cue: clarify flow direction, occlusion, throughput, and tolerated errors. Consider detection, tracking, a crossing rule, and event deduplication. Evaluate count error per sequence and investigate identity switches.

30. **A model is fast in a notebook but slow in the application. What is your investigation plan?**
    Cue: profile decode, resize, transfer, inference, postprocessing, serialization, and queueing separately. Reproduce realistic concurrency and image sizes before optimizing the neural network.

31. **Why might quantization make an application less useful even if the model file shrinks?**
    Cue: unsupported kernels, conversion overhead, and accuracy changes can dominate. Use representative calibration data where required and measure the target runtime, including difficult slices.

32. **How do you choose between edge inference and server inference?**
    Cue: connectivity, latency, data handling, hardware limits, updates, and operational cost. Define fallback behavior and measure end-to-end service quality under the expected workload.

33. **What would you monitor when production labels arrive a week late?**
    Cue: monitor input validity, pipeline failures, latency, and distribution signals immediately; later join delayed labels for task metrics. Distribution change is a trigger to investigate, not proof of accuracy loss.

34. **A deployment's predictions differ from offline evaluation. What do you compare?**
    Cue: checkpoint identity, decoder, channel order, resize/crop, normalization, model mode, precision, and postprocessing. Use identical input files and intermediate tensors to isolate the first divergence.

35. **How would you release a model update and recover from a regression?**
    Cue: version weights and preprocessing together, run acceptance evaluations, use a limited rollout or shadow comparison, define rollback triggers, and retain the previous working bundle.

## A 45-minute practice session

Spend five minutes clarifying the task and constraints, ten minutes on a derivation or short implementation, twenty minutes on design/debugging, and ten minutes defending a project result. Ask the reviewer to change one assumption: fewer labels, a different camera, no GPU, or a stricter latency requirement.

Finish by recording the exact point where your explanation became vague. Repair it with a small experiment or worked example. Memorizing the cues without being able to apply them is not completion.
