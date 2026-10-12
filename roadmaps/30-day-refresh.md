# A 30-day computer vision refresh

Suggested effort: **60–90 minutes/day**, with optional longer project sessions.

This path is for someone who previously studied machine learning or CV. It is a diagnostic and a return to practice, not a substitute for the [24-week path](beginner-to-job-ready.md). Pick one small dataset and reuse it across the month. Use CPU-friendly tasks or cached embeddings when compute is limited.

[All paths](README.md) · [Interview questions](../career/interview-preparation.md)

## Days 1–7: recover the foundations

Use [CS231n's public notes](https://cs231n.github.io/), [Szeliski's book](https://szeliski.org/Book/), and [OpenCV's camera documentation](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html) as references when you get stuck. Attempt each exercise before reading the answer.

| Day | Task | Evidence to save |
| --- | --- | --- |
| 1 | Complete the [starting-point questions](README.md#find-your-starting-point-in-45-minutes). Set up a clean environment. | A gap list and environment record. |
| 2 | Load, resize, normalize, and visualize images. Deliberately break a channel order and a dtype conversion. | A debugging notebook with symptoms and fixes. |
| 3 | Derive a matrix-product shape, softmax cross-entropy gradient, and convolution output size. | One page of worked examples. |
| 4 | Apply blur, edges, and a thresholding baseline to one task. | A failure gallery explaining illumination and scale effects. |
| 5 | Project synthetic 3D points through a pinhole camera. Alter focal length and depth separately. | A plot and a coordinate-convention note. |
| 6 | Construct group-aware splits and search for duplicates. | A split manifest and group-overlap check. |
| 7 | Calculate precision, recall, IoU, and a confusion matrix by hand on tiny examples. | Calculations checked against a library. |

**Gate:** explain why a plausible image and a plausible metric do not prove the pipeline is correct. Repair any weak item before continuing.

## Days 8–14: rebuild a dependable baseline

Use the [PyTorch transfer-learning tutorial](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) and [scikit-learn's leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html) to audit your implementation.

| Day | Task | Evidence to save |
| --- | --- | --- |
| 8 | Implement or reload a small training pipeline and overfit one tiny clean batch. | A smoke-run log. |
| 9 | Add evaluation mode, deterministic evaluation transforms, and checkpoint reload. | Predictions before and after reload. |
| 10 | Run a majority-class/classical baseline and a frozen pretrained-feature baseline. | Two results under one fixed protocol. |
| 11 | Change one training choice: learning rate, augmentation, or unfreezing. | A controlled comparison and runtime record. |
| 12 | Inspect at least 20 mistakes and classify likely causes. | An error spreadsheet with image IDs. |
| 13 | Choose an operating threshold on validation data using the task's error costs. | A decision note with expected tradeoffs. |
| 14 | Summarize the baseline and propose the smallest useful next experiment. | A one-page report with no unexplained metric. |

**Gate:** rerun evaluation without hidden notebook state. If you changed the split while experimenting, regenerate all comparable baseline results.

## Days 15–21: reconnect with modern practice

Select relevant topics from the [Research landscape](../research/landscape.md). The following exercises use inspectable reference implementations; they do not imply a ranking of current models.

| Day | Task | Evidence to save |
| --- | --- | --- |
| 15 | Use a pretrained detector or segmenter on a small labeled sample. | Predictions, coordinate checks, and a documented evaluator. |
| 16 | Compare supervised features with a frozen [DINOv2](https://github.com/facebookresearch/dinov2) representation if hardware permits. | Same-split comparison, or a clearly labeled feasibility report. |
| 17 | Run a small [CLIP](https://github.com/openai/CLIP) retrieval or zero-shot experiment. | Prompt list, retrieved examples, and failure cases. |
| 18 | Change wording and distractor labels while keeping images fixed. | A prompt-sensitivity table using validation data. |
| 19 | Inspect a generative vision-language system on a narrow answerable task. Include an absent-object question. | An answer rubric and human-checked output sample; record prompts and model version. |
| 20 | Read one relevant paper's method and evaluation, then inspect its official code. | A claim/evidence/limitation map. |
| 21 | Choose one capstone question: quality under shift, prompt sensitivity, or inference efficiency. | A fixed plan with a baseline and stopping condition. |

**Gate:** distinguish retrieval similarity, classification probability, and a generated answer. Explain how you will evaluate each without relying only on impressive examples.

## Days 22–30: ship one inspectable result

Use the [portfolio guide](../career/portfolio.md) to structure the final artifact. For an efficiency experiment, consult the runtime's official guidance, such as [ONNX Runtime quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html), and measure actual quality and latency.

| Day | Task | Evidence to save |
| --- | --- | --- |
| 22 | Implement the capstone baseline with saved predictions. | A complete baseline artifact. |
| 23 | Run the planned variant. | Configuration, result, and resource usage. |
| 24 | Compare errors and investigate an unexpected result. | A supported explanation or an explicitly unresolved hypothesis. |
| 25 | Profile the full pipeline on the target hardware. | Timings with measurement boundaries and sample count. |
| 26 | Package a local CLI or demo with input checks. | A clean run command and an example. |
| 27 | Repeat from a fresh environment or ask a peer to follow the instructions. | Installation and reproduction issues, then fixes. |
| 28 | Write the result, limitations, and failure gallery. | A project README that links to evidence. |
| 29 | Practice a five-minute explanation and five questions from the interview bank. | Recorded or written answers plus remaining gaps. |
| 30 | Compare your day-1 answers with your current answers; choose your next path. | A progress note and one bounded follow-up goal. |

Do not fill missed days by stacking more links. Reduce the experiment's scope, preserve evaluation quality, and carry unfinished prerequisites into the next month.
