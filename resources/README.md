# Resource catalog

**94 hand-picked resources** across 9 categories. Updated 2026-10-12.

[Home](../README.md) · [Roadmaps](../roadmaps/README.md) · [Projects](../projects/README.md) · [Paper guide](../research/paper-reading.md)

> You do not need all of this. Pick what fits your current milestone and ignore the rest.

## If you read nothing else

Nine entries that cover most of what a newcomer needs:

- **[Stanford CS231n](https://cs231n.stanford.edu/)** · Study visual recognition through structured lectures and substantial implementation assignments.
- **[Dive into Deep Learning](https://d2l.ai/)** · Work through executable explanations of optimization, convolution, attention, and training systems.
- **[PyTorch Tutorials](https://pytorch.org/tutorials/)** · Follow maintained examples for tensor operations, transfer learning, profiling, and model export.
- **[OpenCV documentation](https://docs.opencv.org/4.x/)** · Implement filtering, features, calibration, geometric transforms, and camera pipelines.
- **[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)** · Understand residual connections and why deeper networks need careful optimization comparisons.
- **[An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)** · Connect image patches, positional embeddings, and transformer scaling to visual recognition.
- **[PyTorch Image Models](https://github.com/huggingface/pytorch-image-models)** · Compare pretrained backbones with consistent model creation and training utilities.
- **[COCO API](https://github.com/cocodataset/cocoapi)** · Use the reference evaluator to understand detection and segmentation precision-recall conventions.
- **[ONNX Runtime](https://onnxruntime.ai/docs/)** · Export and benchmark model inference across supported execution providers.

## Search from your terminal

```bash
python3 scripts/catalog.py search segmentation
python3 scripts/catalog.py search --level beginner
python3 scripts/catalog.py search --category datasets --json
```

Levels are beginner, intermediate, advanced, or all. Access is free, registration, or mixed. Free to read does not mean free to reuse or free to run, so check the license and the caveat.

Missing something? Edit [catalog.json](catalog.json), run `make render`, and see [CONTRIBUTING](../CONTRIBUTING.md).

## Browse

- [Foundations](#foundations) (5): Math, NumPy, and the books that make everything else easier.
- [Courses](#courses) (7): Structured lectures and hands-on courses. Pick one, finish it.
- [Papers](#papers) (18): The papers worth reading in full, from ResNet to 2026.
- [Models](#models) (22): Checkpoints and reference code you can actually run.
- [Tools](#tools) (13): Libraries and platforms for data, labeling, tracking, and 3D.
- [Datasets](#datasets) (14): Where the data lives, and what you are allowed to do with it.
- [Evaluation](#evaluation) (7): Evaluators and benchmarks, so your numbers mean something.
- [Deployment](#deployment) (5): Getting a model off your laptop and onto a device or server.
- [Communities](#communities) (3): Where the field publishes and where to ask for help.

## Foundations

_Math, NumPy, and the books that make everything else easier._

- **[NumPy beginner's guide](https://numpy.org/doc/stable/user/absolute_beginners.html)** `beginner · documentation`
  Practice arrays, indexing, broadcasting, and numerical operations before implementing image pipelines.
- **[Mathematics for Machine Learning](https://mml-book.github.io/)** `beginner · book`
  Connect linear algebra, probability, and optimization to the mathematics used in vision models.
- **[Computer Vision: Algorithms and Applications](https://szeliski.org/Book/)** `all · book · registration access`
  Build the geometry and image-formation intuition that remains useful alongside learned models.
  _Heads up: Second-edition PDF requires an information form and is for personal use; link to the book page rather than reposting it._
- **[Dive into Deep Learning](https://d2l.ai/)** `beginner · book`
  Work through executable explanations of optimization, convolution, attention, and training systems.
- **[Understanding Deep Learning](https://udlbook.github.io/udlbook/)** `intermediate · book`
  Use diagrams and exercises to connect neural-network mathematics with practical modeling decisions.

## Courses

_Structured lectures and hands-on courses. Pick one, finish it._

- **[Stanford CS231n](https://cs231n.stanford.edu/)** `beginner · course`
  Study visual recognition through structured lectures and substantial implementation assignments.
  _Heads up: Public materials are available; enrollment and assignment infrastructure are separate._
- **[Stanford CS231A](https://web.stanford.edu/class/cs231a/)** `intermediate · course`
  Learn camera models, epipolar geometry, reconstruction, and visual recognition prerequisites.
  _Heads up: Check the course offering for which lectures and assignments are publicly accessible._
- **[Practical Deep Learning for Coders](https://course.fast.ai/)** `beginner · course`
  Train useful models early, then study the mechanisms behind the training loop.
  _Heads up: Hosted notebooks or GPU services may impose quotas or charges._
- **[PyTorch Tutorials](https://pytorch.org/tutorials/)** `all · course`
  Follow maintained examples for tensor operations, transfer learning, profiling, and model export.
  _Heads up: Choose examples matching your installed PyTorch release._
- **[Hugging Face Community Computer Vision Course](https://huggingface.co/learn/computer-vision-course/en/unit0/welcome/welcome)** `beginner · course`
  Explore modern vision tasks with model libraries and guided exercises.
  _Heads up: Some exercises need a model download, account, or GPU._
- **[MIT Introduction to Deep Learning](https://introtodeeplearning.com/)** `beginner · course`
  Use a compact lecture-and-lab sequence to establish neural-network fundamentals.
  _Heads up: Inspect the year of each lab and its runtime dependencies._
- **[Full Stack Deep Learning](https://fullstackdeeplearning.com/course/2022/)** `intermediate · course`
  Learn experiment design, data management, deployment, and the engineering around a trained model.
  _Heads up: The 2022 course is selected for durable systems principles, not current package versions._

## Papers

_The papers worth reading in full, from ResNet to 2026._

- **[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)** `beginner · paper`
  Understand residual connections and why deeper networks need careful optimization comparisons.
- **[U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)** `beginner · paper`
  Trace encoder-decoder shapes and skip connections in a practical dense-prediction architecture.
- **[Faster R-CNN](https://arxiv.org/abs/1506.01497)** `intermediate · paper`
  Separate proposal generation, classification, and box regression in two-stage detection.
- **[You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640)** `intermediate · paper`
  Study the original single-stage formulation and its localization tradeoffs.
  _Heads up: The original paper does not describe modern packages that share the YOLO name._
- **[End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872)** `intermediate · paper`
  Understand object queries, bipartite matching, and detection as set prediction.
- **[An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)** `intermediate · paper`
  Connect image patches, positional embeddings, and transformer scaling to visual recognition.
- **[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)** `intermediate · paper`
  Learn image-text contrastive training and examine sensitivity to prompts and distribution shift.
  _Heads up: Original training data is not fully released for exact reproduction._
- **[A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)** `intermediate · paper`
  Study how augmentation, projection heads, and negatives shape contrastive representations.
- **[Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377)** `intermediate · paper`
  Investigate masking ratios and asymmetric encoders as a self-supervised learning design.
- **[NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934)** `advanced · paper`
  Derive ray sampling and volume rendering before trying faster reconstruction systems.
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)** `advanced · paper`
  Compare explicit Gaussian scene representations with neural radiance fields.
  _Heads up: Paper availability does not imply unrestricted rights to associated code or datasets._
- **[Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)** `advanced · paper`
  Work through the forward noise process, reverse denoising objective, and sampling cost.
- **[High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)** `advanced · paper`
  Understand the compute tradeoff of diffusion in a learned latent representation.
  _Heads up: Read each associated checkpoint's separate usage terms._
- **[DINOv3](https://arxiv.org/abs/2508.10104)** `advanced · paper`
  Study dense feature quality and transfer beyond image-level classification.
  _Heads up: Full pretraining data and compute are not accessible reproduction defaults._
- **[SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719)** `advanced · paper`
  Examine concept prompts and the interaction between image detection and video tracking.
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482)** `advanced · paper`
  Study dense predictive objectives and intermediate-layer supervision for temporally consistent representations.
  _Heads up: Reported benchmark outcomes are task-specific and require the matching evaluation protocol._
- **[VGGT-Omega](https://arxiv.org/abs/2605.15195)** `advanced · paper`
  Examine register attention and scalable geometric representation learning.
  _Heads up: Use the authors' September 2026 reproduction checkpoint for benchmark comparisons._
- **[Qwen3-VL-Embedding and Qwen3-VL-Reranker](https://arxiv.org/abs/2601.04720)** `advanced · paper`
  Separate multimodal candidate retrieval from cross-encoder reranking and measure both stages.
  _Heads up: Check benchmark versions and checkpoint sizes before comparing reported scores._

## Models

_Checkpoints and reference code you can actually run._

- **[Torchvision](https://pytorch.org/vision/stable/index.html)** `beginner · documentation`
  Start with reference datasets, transformations, and pretrained vision models in one ecosystem.
  _Heads up: Check individual pretrained weight metadata and dataset terms._
- **[PyTorch Image Models](https://github.com/huggingface/pytorch-image-models)** `intermediate · repository`
  Compare pretrained backbones with consistent model creation and training utilities.
  _Heads up: Pretrained weights can have terms different from the library license._
- **[Ultralytics](https://github.com/ultralytics/ultralytics)** `beginner · repository · mixed access`
  Build a complete detection baseline with training, validation, prediction, and export workflows.
  _Heads up: Review AGPL-3.0 and commercial licensing before using it in a product._
- **[RT-DETR](https://github.com/lyuwenyu/RT-DETR)** `intermediate · repository`
  Explore transformer detection with an explicit accuracy-versus-latency evaluation target.
  _Heads up: Benchmark on your target hardware with identical preprocessing and batch size._
- **[Grounding DINO](https://github.com/IDEA-Research/GroundingDINO)** `intermediate · repository`
  Use text-conditioned boxes to prototype open-vocabulary detection and annotation assistance.
  _Heads up: Prompted detections require validation; generated labels are not ground truth._
- **[Segment Anything 2](https://github.com/facebookresearch/sam2)** `intermediate · repository`
  Learn promptable image and video segmentation with released checkpoints and examples.
  _Heads up: Choose checkpoints and code versions together; video memory use grows with workload._
- **[Segment Anything 3 and 3.1](https://github.com/facebookresearch/sam3)** `advanced · repository · registration access`
  Explore concept segmentation and the 2026 shared-memory multi-object tracking update.
  _Heads up: Check the SAM license, gated checkpoint access, and documented CUDA requirements._
- **[DINOv3 reference implementation](https://github.com/facebookresearch/dinov3)** `advanced · repository · registration access`
  Extract dense features and compare frozen probes with downstream adaptation.
  _Heads up: Weights require access; the custom DINOv3 license and large training budgets need review._
- **[CoTracker](https://github.com/facebookresearch/co-tracker)** `intermediate · repository`
  Track points jointly to study motion, occlusion, and temporal correspondence.
  _Heads up: Code and pretrained checkpoints may have different license terms._
- **[ByteTrack](https://github.com/ifzhang/ByteTrack)** `intermediate · repository`
  Build a tracking baseline that associates high- and low-confidence detections.
  _Heads up: Tracking quality depends strongly on detector, thresholds, and dataset protocol._
- **[MMPose](https://github.com/open-mmlab/mmpose)** `intermediate · repository`
  Explore pose estimation models, datasets, and evaluation across multiple keypoint settings.
  _Heads up: Check dependency compatibility and each model's data and weight licenses._
- **[Qwen3-VL](https://github.com/QwenLM/Qwen3-VL)** `advanced · repository`
  Compare multimodal inference and fine-tuning across model sizes and input budgets.
  _Heads up: Memory and latency depend on image resolution, video frames, tokens, and checkpoint size._
- **[Qwen3-VL-Embedding and Reranker code](https://github.com/QwenLM/Qwen3-VL-Embedding)** `advanced · repository`
  Build visual-document or video search with separate embedding and reranking stages.
  _Heads up: Measure candidate recall before attributing gains to reranking._
- **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** `intermediate · repository`
  Compare scene text recognition, layout parsing, and document VLM workflows.
  _Heads up: Pin pipeline and model versions; language coverage and output schemas vary by model._
- **[VGGT](https://github.com/facebookresearch/vggt)** `advanced · repository · mixed access`
  Infer cameras, depth, point maps, and tracks from one or more views.
  _Heads up: Original weights are non-commercial; a separately gated commercial-use checkpoint has different terms._
- **[Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3)** `advanced · repository`
  Explore monocular and multiview geometry through a shared depth-ray representation.
  _Heads up: Check the license of the chosen checkpoint and memory requirements for long sequences._
- **[SAM 3D Objects](https://github.com/facebookresearch/sam-3d-objects)** `advanced · repository · registration access`
  Investigate single-image object reconstruction and inspect ambiguity in unseen geometry.
  _Heads up: SAM license applies; inspect checkpoint access and GPU requirements before downloading._
- **[V-JEPA 2 and 2.1](https://github.com/facebookresearch/vjepa2)** `advanced · repository`
  Explore video representations, dense-feature learning, and action-conditioned latent prediction.
  _Heads up: Representation evaluation and robot planning require different checkpoints and protocols._
- **[OpenVLA](https://github.com/openvla/openvla)** `advanced · repository`
  Study how a vision-language backbone is adapted to robot action prediction.
  _Heads up: Simulation results do not establish reliable control on a different robot._
- **[Physical Intelligence openpi](https://github.com/Physical-Intelligence/openpi)** `advanced · repository`
  Explore pi0, pi0-FAST, and pi0.5 inference and adaptation on robot demonstrations.
  _Heads up: Review inherited backbone terms and match action conventions to the chosen embodiment._
- **[NVIDIA Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T)** `advanced · repository · registration access`
  Study the N1.7 multimodal policy, data interface, fine-tuning, and simulation evaluation workflow.
  _Heads up: The documented backbone is gated; fine-tuning and inference have substantial GPU requirements._
- **[Wan2.2](https://github.com/Wan-Video/Wan2.2)** `advanced · repository`
  Explore text-to-video and image-to-video generation with released inference code.
  _Heads up: Generation is GPU-intensive; obtain appropriate rights for inputs and downstream media use._

## Tools

_Libraries and platforms for data, labeling, tracking, and 3D._

- **[OpenCV documentation](https://docs.opencv.org/4.x/)** `beginner · documentation`
  Implement filtering, features, calibration, geometric transforms, and camera pipelines.
- **[scikit-image](https://scikit-image.org/docs/stable/)** `beginner · documentation`
  Build interpretable image-processing baselines and inspect region-level measurements.
- **[Kornia](https://kornia.readthedocs.io/en/latest/)** `intermediate · documentation`
  Use differentiable image operations and geometry inside PyTorch pipelines.
  _Heads up: Match optional acceleration components to your runtime environment._
- **[AlbumentationsX](https://github.com/albumentations-team/AlbumentationsX)** `intermediate · repository · mixed access`
  Build synchronized image, box, mask, and keypoint augmentation pipelines.
  _Heads up: Review the current AGPL/commercial licensing terms before adoption._
- **[CVAT](https://github.com/cvat-ai/cvat)** `beginner · repository · mixed access`
  Create and review image or video annotations with task-specific labeling workflows.
  _Heads up: Self-hosting and hosted plans differ; inspect storage and collaboration requirements._
- **[Label Studio](https://github.com/HumanSignal/label-studio)** `beginner · repository · mixed access`
  Prototype labeling interfaces and organize human review of model predictions.
  _Heads up: Community and hosted or enterprise features differ._
- **[FiftyOne](https://github.com/voxel51/fiftyone)** `intermediate · repository · mixed access`
  Inspect datasets visually, compare predictions, and curate difficult evaluation slices.
  _Heads up: Distinguish open-source functionality from commercial services._
- **[DVC](https://dvc.org/doc)** `intermediate · documentation · mixed access`
  Version dataset references and connect experiments to reproducible data pipelines.
  _Heads up: Remote storage incurs its own access controls and storage costs._
- **[MLflow](https://mlflow.org/docs/latest/index.html)** `intermediate · documentation`
  Record parameters, artifacts, and model versions for comparable experiments.
  _Heads up: Configure storage and access controls when hosting a shared tracking server._
- **[Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)** `intermediate · documentation`
  Experiment with diffusion pipelines, schedulers, adaptation, and memory controls.
  _Heads up: Library licensing does not replace individual model-card terms._
- **[LeRobot](https://github.com/huggingface/lerobot)** `intermediate · repository`
  Explore robot datasets, policy training, evaluation, and supported hardware interfaces.
  _Heads up: Robot hardware, embodiment compatibility, and dataset terms require separate checks._
- **[COLMAP](https://colmap.github.io/)** `intermediate · documentation`
  Establish a structure-from-motion and multiview-stereo baseline for reconstruction experiments.
  _Heads up: Difficult texture, repeated patterns, and camera motion affect reconstruction reliability._
- **[Open3D](https://www.open3d.org/docs/release/)** `intermediate · documentation`
  Inspect, register, and process point clouds and meshes with reusable geometry tools.

## Datasets

_Where the data lives, and what you are allowed to do with it._

- **[CIFAR-10 and CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html)** `beginner · dataset`
  Use small images to practice splitting, optimization, and controlled baseline comparisons.
  _Heads up: Low resolution limits conclusions about real-world visual recognition._
- **[Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)** `beginner · dataset`
  Practice transfer learning and segmentation on a manageable labeled dataset.
  _Heads up: Check the dataset's research-use and image-rights notes before redistribution._
- **[COCO](https://cocodataset.org/)** `intermediate · dataset`
  Learn standard annotation formats and compare object-level vision pipelines.
  _Heads up: Annotations and source images have different licenses; check individual image rights._
- **[PASCAL VOC](https://www.robots.ox.ac.uk/~vgg/projects/pascal/VOC/)** `beginner · dataset`
  Use a historically important benchmark to learn detection and segmentation evaluation.
  _Heads up: Specify the challenge year, split, and metric variant._
- **[Open Images](https://storage.googleapis.com/openimages/web/index.html)** `intermediate · dataset`
  Explore large-scale, multilabel image annotation and object localization.
  _Heads up: Check image-level licenses, attribution, and available image URLs._
- **[ImageNet](https://www.image-net.org/)** `intermediate · dataset · registration access`
  Understand the benchmark behind many pretrained classification backbones.
  _Heads up: Image access requires registration and compliance with the dataset's terms._
- **[KITTI Vision Benchmark Suite](https://www.cvlibs.net/datasets/kitti/)** `intermediate · dataset · registration access`
  Study stereo, optical flow, detection, and odometry with structured driving benchmarks.
  _Heads up: Observe non-commercial terms and task-specific download or submission requirements._
- **[nuScenes](https://www.nuscenes.org/)** `advanced · dataset · registration access`
  Explore camera, lidar, and radar perception with a documented autonomous-driving dataset.
  _Heads up: Check the applicable non-commercial dataset license and access agreement._
- **[Ego4D](https://ego4d-data.org/)** `advanced · dataset · registration access`
  Study first-person temporal understanding and action-oriented benchmarks.
  _Heads up: A signed data agreement and substantial storage may be required._
- **[MVTec Anomaly Detection](https://www.mvtec.com/company/research/datasets/mvtec-ad)** `intermediate · dataset`
  Evaluate defect localization with normal training examples and annotated anomalies.
  _Heads up: Review the dataset's non-commercial license before industrial product use._
- **[DocVQA](https://www.docvqa.org/)** `intermediate · dataset · registration access`
  Test question answering over document images and inspect text-extraction dependencies.
  _Heads up: Individual tasks and challenge downloads have their own access terms._
- **[DROID](https://droid-dataset.github.io/)** `advanced · dataset`
  Inspect diverse robot manipulation demonstrations and cross-environment data variation.
  _Heads up: Full downloads are large; check dataset terms and calibration/action conventions._
- **[MedMNIST](https://medmnist.com/)** `beginner · dataset`
  Practice small-scale medical image classification with standardized tasks and baselines.
  _Heads up: Educational benchmarking does not validate a model for clinical decisions._
- **[DOTA](https://captain-whu.github.io/DOTA/)** `intermediate · dataset`
  Learn oriented object detection and the challenges of large aerial images.
  _Heads up: Specify dataset version, tiling protocol, and dataset usage terms._

## Evaluation

_Evaluators and benchmarks, so your numbers mean something._

- **[COCO API](https://github.com/cocodataset/cocoapi)** `intermediate · repository`
  Use the reference evaluator to understand detection and segmentation precision-recall conventions.
  _Heads up: Record category mapping, area ranges, and maximum detections alongside results._
- **[TorchMetrics](https://lightning.ai/docs/torchmetrics/stable/)** `intermediate · documentation`
  Use tested metric implementations while checking task definitions and aggregation behavior.
  _Heads up: Metric defaults and distributed aggregation can change the meaning of a reported score._
- **[LMMs-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)** `advanced · repository`
  Run multimodal evaluation with explicit model, task, and prompt configurations.
  _Heads up: Some tasks require licensed datasets, credentials, external judges, or paid APIs._
- **[MMMU](https://mmmu-benchmark.github.io/)** `advanced · benchmark`
  Examine multidisciplinary visual reasoning and per-domain failure modes.
  _Heads up: Use the correct split and avoid tuning on held-out benchmark answers._
- **[MathVista](https://mathvista.github.io/)** `advanced · benchmark`
  Audit visual mathematical reasoning and distinguish perception errors from reasoning errors.
  _Heads up: Record answer extraction, prompt, and evaluator configuration._
- **[WILDS](https://wilds.stanford.edu/)** `intermediate · benchmark`
  Evaluate generalization across domains with explicitly defined distribution shifts.
  _Heads up: Individual datasets have separate download and use requirements._
- **[OmniDocBench](https://github.com/opendatalab/OmniDocBench)** `advanced · benchmark`
  Measure document parsing components and reading order using a versioned benchmark.
  _Heads up: Scores from different benchmark versions or matching rules are not directly comparable._

## Deployment

_Getting a model off your laptop and onto a device or server._

- **[ONNX Runtime](https://onnxruntime.ai/docs/)** `intermediate · documentation`
  Export and benchmark model inference across supported execution providers.
  _Heads up: Confirm operator support and numerical parity for your exported graph._
- **[OpenVINO](https://docs.openvino.ai/)** `intermediate · documentation`
  Explore conversion, quantization, and inference on supported Intel hardware.
  _Heads up: Hardware support and quantization behavior depend on the selected runtime version._
- **[NVIDIA TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/latest/)** `advanced · documentation`
  Optimize compatible GPU inference while profiling latency, precision, and memory.
  _Heads up: NVIDIA hardware and version compatibility constrain engine portability._
- **[ExecuTorch](https://docs.pytorch.org/executorch/stable/)** `advanced · documentation`
  Investigate exporting and running PyTorch models on mobile and embedded targets.
  _Heads up: Operator and backend support vary by target device._
- **[Triton Inference Server](https://github.com/triton-inference-server/server)** `advanced · repository`
  Study model serving, batching, concurrency, and end-to-end inference observability.
  _Heads up: Server throughput is not equivalent to single-request end-to-end latency._

## Communities

_Where the field publishes and where to ask for help._

- **[CVF Open Access](https://openaccess.thecvf.com/)** `all · portal`
  Find official conference papers and supplemental material from major computer vision venues.
  _Heads up: Conference inclusion is evidence of publication, not proof that every reported claim generalizes._
- **[arXiv Computer Vision and Pattern Recognition](https://arxiv.org/list/cs.CV/recent)** `all · portal`
  Track new preprints, then verify methods, artifacts, revisions, and evaluation details.
  _Heads up: Preprints may not be peer reviewed; check submission and revision dates._
- **[PyTorch Forums](https://discuss.pytorch.org/)** `all · portal`
  Search implementation questions and learn to produce minimal reproducible bug reports.
  _Heads up: Community replies require validation against current documentation and your environment._
