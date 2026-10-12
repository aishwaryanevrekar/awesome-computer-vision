# Computer vision research: what to study and test

A selective map of research directions that have public papers or implementations, last updated October 2026. It is not a leaderboard. Dates identify releases or papers.

Each section separates **evidence** from a **study direction**. A useful experiment must still demonstrate a benefit on its own data, budget, and evaluation protocol. The reading sequence is in [paper-reading.md](paper-reading.md); implementations and learning materials are in the [resource catalog](../resources/README.md).

## 1. Reusable visual features beyond classification

**Evidence.** DINOv3, published in August 2025, emphasizes transferable dense visual representations. Its repository includes frozen-feature demonstrations and downstream evaluation code, and records metadata-guided adaptation recipes released on 12 June 2026. The full large-model training setup uses private pretraining data. [Paper](https://arxiv.org/abs/2508.10104), [official implementation and updates](https://github.com/facebookresearch/dinov3).

**Study direction.** Learn frozen backbones, nearest-neighbor retrieval, linear probes, and adaptation before attempting foundation-model pretraining. Compare a small supervised baseline, a frozen representation, and a fine-tuned model on the same split. Report annotation cost and performance on a new camera or environment. Better transfer from a particular backbone is a hypothesis to test, not an assumed outcome.

## 2. Segmentation is becoming a prompt-and-track interface

**Evidence.** SAM 3, introduced in November 2025, connects concept prompts with segmentation and tracking. The official repository dates SAM 3.1 Object Multiplex to 27 March 2026 and describes shared memory for multi-object tracking. [SAM 3 paper](https://arxiv.org/abs/2511.16719), [SAM 3/3.1 implementation](https://github.com/facebookresearch/sam3).

**Study direction.** Compare point, box, and text prompts on small objects, ambiguous descriptions, occlusion, and re-entry. Measure human corrections per video minute, mask quality, identity errors, and peak memory. A convincing annotation tool should save review time while preserving label quality; attractive overlays alone do not establish that.

## 3. Vision-language models need explicit perception tests

**Evidence.** The Qwen3-VL repository records its first model release on 23 September 2025, followed by additional sizes and a November technical report. It supports images and video, with dense and mixture-of-experts variants. [Official repository](https://github.com/QwenLM/Qwen3-VL), [technical report](https://arxiv.org/abs/2511.21631).

**Study direction.** Separate recognition, localization, counting, OCR, and reasoning into different evaluation slices. Vary image resolution and frame sampling before changing the prompt. Include unanswerable questions and grade unsupported answers separately. Model size and an impressive broad benchmark score do not establish reliability on receipts, diagrams, or a specific camera feed.

## 4. Multimodal retrieval has its own modeling stack

**Evidence.** Qwen3-VL-Embedding and Qwen3-VL-Reranker, reported on 8 January 2026, distinguish a shared embedding space from pairwise relevance scoring across text, images, document images, and video. The reference repository includes evaluation workflows. [Paper](https://arxiv.org/abs/2601.04720), [implementation](https://github.com/QwenLM/Qwen3-VL-Embedding).

**Study direction.** Build a small visual search collection with independently written queries and relevance judgments. Report candidate recall before reranking, then nDCG or reciprocal rank after reranking. Keep a cheap baseline such as a conventional image-text embedding model. This isolates whether an improvement comes from finding the right item or reordering items already retrieved.

## 5. Document understanding benefits from specialized evaluation

**Evidence.** PaddleOCR-VL-1.5, published on 29 January 2026, studies document parsing under scanning, skew, warping, screen photography, and illumination changes. The PaddleOCR repository records VL-1.6 in May and PP-OCRv6 in June 2026. OmniDocBench provides component-level evaluation for layout, text, formulas, tables, and reading order. [VL-1.5 paper](https://arxiv.org/abs/2601.21957), [PaddleOCR releases](https://github.com/PaddlePaddle/PaddleOCR), [OmniDocBench](https://github.com/opendatalab/OmniDocBench).

**Study direction.** Compare an OCR pipeline with a document VLM using identical page images. Inspect table structure, reading order, and missing fields independently of character accuracy. Add multilingual and photographed pages. Record the exact benchmark version; the same headline metric on different versions is not a valid comparison.

## 6. Geometry models are broadening reconstruction workflows

**Evidence.** VGGT (March 2025) predicts multiple geometric quantities from views; Depth Anything 3 (November 2025) uses a depth-ray representation for several geometry tasks. VGGT-Omega followed in May 2026 with architectural and training changes. Its authors now direct benchmark comparisons to a September 2026 reproduction checkpoint after identifying a concern with the original checkpoint. [VGGT](https://arxiv.org/abs/2503.11651), [Depth Anything 3](https://arxiv.org/abs/2511.10647), [VGGT-Omega paper](https://arxiv.org/abs/2605.15195), [checkpoint guidance](https://github.com/facebookresearch/vggt-omega).

**Study direction.** Learn camera intrinsics, coordinate frames, projection, and scale ambiguity. Compare a conventional structure-from-motion pipeline with a feed-forward model. Test repeated textures, reflective surfaces, low overlap, and moving objects. Evaluate pose and depth against appropriate references; a plausible point cloud can still contain substantial geometric error. Pin the checkpoint, image resolution, frame selection, and alignment procedure.

## 7. Video representations are moving beyond a pooled clip label

**Evidence.** V-JEPA 2.1, submitted on 15 March 2026, studies dense predictive loss, intermediate-layer supervision, and joint image/video training. The authors report results for several dense and global tasks; these are task-specific evaluations, not a universal measure of physical understanding. [Paper](https://arxiv.org/abs/2603.14482), [reference implementation](https://github.com/facebookresearch/vjepa2).

**Study direction.** Distinguish action classification, anticipation, correspondence, and action-conditioned prediction. Test whether predictions change when frame order is reversed or informative frames are removed. Track both task accuracy and temporal consistency. An image-only baseline and a shuffled-frame control help establish whether a model uses motion information.

## 8. Vision-language-action models require embodiment-aware tests

**Evidence.** OpenVLA (2024) provides an accessible VLA research starting point. Physical Intelligence's openpi exposes pi0, pi0-FAST, and pi0.5; its pi0.5 release is recorded in September 2025. At this review, NVIDIA's Isaac GR00T repository documents N1.7, including fine-tuning, open-loop evaluation, and simulation workflows. [OpenVLA](https://arxiv.org/abs/2406.09246), [openpi](https://github.com/Physical-Intelligence/openpi), [GR00T reference repository](https://github.com/NVIDIA/Isaac-GR00T).

**Study direction.** Start with recorded demonstrations or a supported simulator. Learn action normalization, coordinate conventions, horizon length, and control frequency. Separate action-prediction error from closed-loop task success. Evaluate unseen object positions and environments, and record interventions. Success on one robot does not establish success on another embodiment.

## 9. Generative video is useful for studying controllability and failure

**Evidence.** Wan2.2 provides text-to-video and image-to-video implementations, including a diffusion mixture-of-experts design. The repository dates its initial release to July 2025. This is a concrete open implementation to study, not a claim that it is the newest or best video generator. [Official repository](https://github.com/Wan-Video/Wan2.2).

**Study direction.** Begin with diffusion fundamentals, then study identity preservation, prompt control, temporal continuity, and sampling cost. For synthetic training data, train a baseline with real data first, then add generated examples and evaluate on held-out real data. Count failures and duplication. A realistic generated video is not evidence of correct physical dynamics or a better downstream model.

## 10. Deployment is part of the experiment

**Evidence.** Current ONNX Runtime documentation describes quantization, calibration, and debugging accuracy changes. ExecuTorch and TensorRT document deployment paths with target-specific support. These are engineering resources reviewed on 12 October 2026, rather than new research releases. [ONNX Runtime quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html), [ExecuTorch](https://docs.pytorch.org/executorch/stable/), [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/latest/).

**Study direction.** Measure image decode, resize, inference, postprocessing, and transfer costs together. Report hardware, precision, warm-up, batch size, p50/p95 latency, throughput, and peak memory. Verify output parity after export and measure accuracy again after quantization. A smaller model that meets the application budget can be a better project result than an expensive model with a higher offline score.

## 11. Stronger evaluation remains a research opportunity

**Evidence.** WILDS provides benchmarks organized around distribution shift. OmniDocBench exposes structured document components rather than only an aggregate outcome. Both illustrate why task definition and data variation matter alongside architecture. [WILDS](https://wilds.stanford.edu/), [OmniDocBench](https://github.com/opendatalab/OmniDocBench).

**Study direction.** Treat the following as experiment proposals: camera-held-out evaluation, subject-disjoint medical splits, time-separated video splits, near-duplicate detection, annotation disagreement, and calibration under shift. A useful contribution may be a well-documented failure slice or a more reliable measurement method. Establish the gap before proposing a new loss or adding another model.

## Choosing a direction

For a first portfolio project, choose one input type, one user need, and one measurable failure. A document parser, defect detector, visual search engine, or video annotation assistant can all support meaningful experiments. For research, start with one paper's claim, reproduce a tractable part, and identify where its assumptions break.

Use the [paper reading guide](paper-reading.md) to turn that question into a reading sequence and a controlled improvement experiment. Revisit this landscape when an upstream release changes available checkpoints, licensing, evaluation code, or the validity of a comparison.
