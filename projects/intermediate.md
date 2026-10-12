# Intermediate projects

[Project index](README.md) · [Previous: beginner](beginner.md) · [Next: advanced](advanced.md)

For every project, pin the upstream commit and checkpoint, keep validation separate from test, and report results on the actual subset you used. A subset experiment is not a full benchmark result.

## 09. Industrial defect inspection

- **Task:** flag unusual products and localize suspicious regions using mostly normal training images.
- **Level / compute:** intermediate / one GPU for feature extraction; CPU for a small cached-feature experiment.
- **Data:** one category from [MVTec AD](https://www.mvtec.com/research-teaching/datasets/mvtec-ad); check its usage terms before building a commercial demo.
- **Baseline code:** [PatchCore reference implementation](https://github.com/amazon-science/patchcore-inspection).
- **Measure:** image AUROC and AUPRC, pixel localization metrics, and false positives at a validation-selected operating point. State whether anomaly labels were used for threshold selection.
- **Failure to investigate:** benign texture changes, unseen normal variants, and defects occupying only a few pixels.
- **Extension / deliverable:** compare feature-memory budgets; publish score distributions, defect overlays, and an explicit threshold-selection protocol.

## 10. Road-scene semantic segmentation

- **Task:** segment a street scene and identify which classes are lost when resolution is reduced.
- **Level / compute:** intermediate / one GPU for a cropped subset; larger training sweeps need more compute.
- **Data:** [Cityscapes](https://www.cityscapes-dataset.com/); preserve scene/city splits and void labels.
- **Baseline code:** select a supported pretrained segmentation configuration from [MMSegmentation](https://github.com/open-mmlab/mmsegmentation).
- **Measure:** mean IoU, per-class IoU, latency, and peak memory at each input resolution.
- **Failure to investigate:** thin poles, small pedestrians, boundary errors, and unfamiliar weather.
- **Extension / deliverable:** compare two resolutions at equal training effort, report small-object degradation, and build an overlay viewer. Treat the result as an offline benchmark, not a driving system.

## 11. Object detection with an honest speed comparison

- **Task:** detect several object categories and evaluate the accuracy/latency trade-off.
- **Level / compute:** intermediate / one GPU; CPU inference is a useful deployment comparison.
- **Data:** [COCO](https://cocodataset.org/), using a documented subset for early experiments.
- **Baseline code:** start with a supported detector in [Torchvision](https://docs.pytorch.org/vision/stable/models.html) or [Detectron2](https://github.com/facebookresearch/detectron2).
- **Measure:** COCO AP across IoU thresholds, AP50, small/medium/large-object AP, and end-to-end p50/p95 latency.
- **Failure to investigate:** crowded objects, duplicate detections, truncation, and resizing that destroys small objects.
- **Extension / deliverable:** sweep input resolution or score threshold on validation data; provide the exact preprocessing, batch size, hardware, and timed stages in a benchmark report.

## 12. Tracking through occlusion

- **Task:** maintain object identities across a video and diagnose identity switches.
- **Level / compute:** intermediate / CPU for association with cached detections; one GPU for detection.
- **Data:** [MOT17](https://motchallenge.net/data/MOT17/); keep whole sequences together and distinguish public from private detections.
- **Baseline code:** [ByteTrack](https://github.com/FoundationVision/ByteTrack), evaluated with [TrackEval](https://github.com/JonathonLuiten/TrackEval).
- **Measure:** HOTA, IDF1, ID switches, and throughput including the detector when it is part of your system.
- **Failure to investigate:** long occlusion, camera motion, similar-looking targets, and low-confidence true detections.
- **Extension / deliverable:** compare association thresholds with the same cached detections; produce a timeline showing where each track is lost, merged, or reassigned.

## 13. Document-text recognition under image degradation

- **Task:** recognize words and separate recognition errors from text-detection errors.
- **Level / compute:** intermediate / CPU inference on cropped words; one GPU for adaptation.
- **Data:** derive word crops from the boxes and text in [FUNSD](https://guillaumejaume.github.io/FUNSD/). Split whole documents before making crops and retain the document ID with every word.
- **Baseline code:** a compatible recognition pipeline from [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR).
- **Measure:** character error rate, exact word accuracy, and performance by blur, text size, and orientation. Specify case, punctuation, and lexicon rules.
- **Failure to investigate:** confident substitutions on tiny text and apparent improvement caused only by normalization.
- **Extension / deliverable:** compare raw, deskewed, and enhanced crops; publish paired examples and preserve the original image beside every transformed version.

## 14. Human pose estimation under occlusion

- **Task:** estimate 2D keypoints and quantify how detection quality affects pose quality.
- **Level / compute:** intermediate / one GPU; small offline inference sets can be run on CPU.
- **Data:** [COCO keypoints](https://cocodataset.org/); use the visibility flags consistently.
- **Baseline code:** a documented configuration from [MMPose](https://github.com/open-mmlab/mmpose).
- **Measure:** keypoint AP using the official OKS protocol, per-joint errors in a diagnostic subset, and pipeline latency.
- **Failure to investigate:** left/right swaps, missing wrists/ankles, overlapping people, and bounding-box truncation.
- **Extension / deliverable:** compare supplied boxes with detector-generated boxes; deliver an error viewer and a breakdown by occlusion and person size rather than only one average score.

## 15. Long-tailed species classification

- **Task:** compare ordinary sampling with a class-balanced training strategy.
- **Level / compute:** intermediate / one GPU on a documented subset.
- **Data:** a specified release from the [iNaturalist competition collection](https://github.com/visipedia/inat_comp). Check image licenses individually and avoid publishing sensitive observation locations.
- **Baseline code:** adapt [Torchvision classification references](https://github.com/pytorch/vision/tree/main/references/classification).
- **Measure:** macro-F1, per-class recall, and separate head/middle/tail results with fixed frequency boundaries.
- **Failure to investigate:** improved rare-class recall can coexist with worse calibration or common-class performance.
- **Extension / deliverable:** compare sampler, loss weighting, and baseline under equal optimizer steps; report training examples per class and inspect visually similar species.

## 16. Monocular depth: relative versus metric

- **Task:** evaluate whether a depth model recovers scene ordering, metric distances, or both.
- **Level / compute:** intermediate / one GPU for a small pretrained checkpoint.
- **Data:** [NYU Depth V2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html); preserve scene-level splits and the chosen invalid-depth mask.
- **Baseline code:** [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2). Select relative or metric weights explicitly; their outputs and applicable terms can differ.
- **Measure:** AbsRel, RMSE, and threshold accuracy under a stated crop, depth range, and scale-alignment rule.
- **Failure to investigate:** reflective surfaces, transparent objects, distant regions, and scaling relative depth as though it were meters.
- **Extension / deliverable:** contrast unaligned metric evaluation with clearly labeled scale-aligned analysis; include scatterplots and per-scene failures.

## 17. Stereo depth from image pairs

- **Task:** compare classical stereo matching and a learned method on rectified pairs.
- **Level / compute:** intermediate / CPU for classical matching; one GPU for learned inference.
- **Data:** [KITTI stereo benchmark](https://www.cvlibs.net/datasets/kitti/eval_stereo.php); use calibration and official valid-pixel conventions.
- **Baseline code:** OpenCV stereo matching from the [official tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html), then [RAFT-Stereo](https://github.com/princeton-vl/RAFT-Stereo).
- **Measure:** disparity endpoint error, the benchmark's bad-pixel metric, runtime, and non-occluded versus all-pixel results.
- **Failure to investigate:** textureless roads, repeated patterns, occlusion boundaries, and wrong scaling after resizing.
- **Extension / deliverable:** sweep resolution and iteration count; export depth only after validating focal length, baseline, coordinate conventions, and units.

## 18. Corruption robustness audit

- **Task:** test how a clean-image classifier behaves under common corruptions without retraining on test corruptions.
- **Level / compute:** intermediate / CPU for small inference batches; one GPU optional.
- **Data:** CIFAR-10 plus the [authors' corruption benchmarks](https://github.com/hendrycks/robustness), using the exact release and severity definitions.
- **Baseline code:** adapt the authors' evaluation utilities and a model from [Torchvision](https://docs.pytorch.org/vision/stable/models.html) or your Project 02 implementation.
- **Measure:** clean accuracy, error by corruption/severity, and calibration. Call a score mCE only when its required reference normalization is implemented.
- **Failure to investigate:** a clean-accuracy gain may hide worse blur or noise sensitivity.
- **Extension / deliverable:** produce a corruption dashboard; compare a single training intervention using a separate development protocol and a locked test suite.

## 19. Skin-lesion boundary segmentation study

- **Task:** study segmentation and annotation uncertainty in a research setting.
- **Level / compute:** intermediate / one GPU for a small 2D model.
- **Data:** a mask-annotated collection from the [ISIC Archive](https://www.isic-archive.com/); record the exact collection and permitted use. Group by patient or lesion whenever identifiers permit.
- **Baseline code:** adapt the 2D data workflow in [nnU-Net](https://github.com/MIC-DKFZ/nnUNet), beginning with a small training configuration.
- **Measure:** Dice and IoU per image, boundary error, and results by documented acquisition conditions; quantify split limitations if patient metadata is absent.
- **Failure to investigate:** hair, rulers, lighting, and repeated views of the same lesion.
- **Extension / deliverable:** compare preprocessing choices and display disagreements with annotations. Present it as a segmentation study, with no diagnostic or clinical-use claims.

## 20. Instance masks in crowded scenes

- **Task:** separate overlapping objects of the same category.
- **Level / compute:** intermediate / one GPU for fine-tuning or batched inference.
- **Data:** [COCO instance segmentation](https://cocodataset.org/), preserving crowd and ignored-region conventions.
- **Baseline code:** use Mask R-CNN in [Detectron2](https://github.com/facebookresearch/detectron2).
- **Measure:** mask AP and box AP separately, per-size results, and latency at a stated resolution.
- **Failure to investigate:** merged masks, thin structures, tiny instances, and boxes that look correct while masks are poor.
- **Extension / deliverable:** compare box and mask failures on the same images; test one crop or resolution policy and publish qualitative examples selected by a reproducible rule.

## 21. Landmark retrieval with a searchable index

- **Task:** retrieve matching landmarks and measure what an approximate index loses relative to exact search.
- **Level / compute:** intermediate / CPU for a small index; one GPU for bulk feature extraction.
- **Data:** a documented subset of [Google Landmarks Dataset v2](https://github.com/cvdfoundation/google-landmark), retaining image provenance and retrieval split definitions.
- **Baseline code:** frozen [DINOv2 features](https://github.com/facebookresearch/dinov2) with [FAISS](https://github.com/facebookresearch/faiss).
- **Measure:** retrieval mAP/Recall@K, index recall against exact nearest neighbors, index size, and latency.
- **Failure to investigate:** duplicate images, shared architectural details, and missing true positives in incomplete labels.
- **Extension / deliverable:** compare embedding normalization and index settings; ship a small searchable demo and a reproducible evaluation manifest.

## 22. Super-resolution with a distortion/perception trade-off

- **Task:** reconstruct higher-resolution images and test whether better-looking output preserves detail faithfully.
- **Level / compute:** intermediate / one GPU for patch-based training or pretrained inference.
- **Data:** [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/); choose an official degradation track and keep image-level splits before extracting patches.
- **Baseline code:** bicubic interpolation plus one supported restoration model from [BasicSR](https://github.com/XPixelGroup/BasicSR).
- **Measure:** PSNR and SSIM under stated color/crop conventions, perceptual distance if available, and runtime.
- **Failure to investigate:** invented texture, ringing, and inflated metrics from a different border crop or degradation kernel.
- **Extension / deliverable:** compare synthetic degradation with a small, clearly separate real-image set; show enlarged crops and label generated detail as an estimate.

## 23. Form understanding beyond OCR

- **Task:** extract structured fields from scanned forms, then distinguish reading errors from layout errors.
- **Level / compute:** intermediate / one GPU for a small fine-tuning run.
- **Data:** [FUNSD](https://guillaumejaume.github.io/FUNSD/); keep document-level splits and preserve entity/relation annotations.
- **Baseline code:** [LayoutLMv3](https://github.com/microsoft/unilm/tree/master/layoutlmv3), compared with an OCR-text-only baseline.
- **Measure:** entity-level precision/recall/F1; evaluate relations separately if implemented. State whether supplied OCR or predicted OCR was used.
- **Failure to investigate:** spatially adjacent labels attached to the wrong value, unreadable text, and layout templates shared across splits.
- **Extension / deliverable:** export structured JSON with source boxes; provide a table showing the effect of OCR quality and layout features independently.

## 24. Video action classification without clip leakage

- **Task:** compare a single-frame model with a temporal model under matched video sampling.
- **Level / compute:** intermediate / one GPU for short clips; a cached-feature baseline can run on CPU.
- **Data:** [UCF101](https://www.crcv.ucf.edu/research/data-sets/ucf101/), using its official split files and grouping related clips appropriately.
- **Baseline code:** select a supported configuration from [MMAction2](https://github.com/open-mmlab/mmaction2).
- **Measure:** video-level top-1 accuracy, per-class accuracy, decoded frames per video, and total inference time.
- **Failure to investigate:** predicting the scene rather than the action, overlapping clips crossing splits, and scores driven by extra test-time views.
- **Extension / deliverable:** test shuffled frame order and different frame budgets; publish video-level predictions, sampling rules, and classes that truly benefit from temporal evidence.
