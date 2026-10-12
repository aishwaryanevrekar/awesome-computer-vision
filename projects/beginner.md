# Beginner projects

[Project index](README.md) · [Next: intermediate](intermediate.md) · [Included runnable examples](../examples/README.md)

Start with small, inspectable experiments. The data and code links below are upstream resources; the work described in each brief is yours to implement.

## 01. Handwritten digit classifier and error explorer

- **Task:** classify digits, then build a gallery of confident mistakes and ambiguous inputs.
- **Level / compute:** beginner / CPU. Use the small 8×8 digits dataset; it is not MNIST.
- **Data:** [scikit-learn digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html). Keep a fixed held-out test set and stratify the development split.
- **Baseline code:** adapt the official [SVM digit classification example](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html); compare with logistic regression, with preprocessing fitted only on training data.
- **Measure:** accuracy, macro-F1, confusion matrix, and performance after controlled blur or translation.
- **Failure to investigate:** a high test score on clean digits does not establish robustness to phone photographs or unusual handwriting.
- **Extension / deliverable:** ship a command-line evaluator and an HTML or notebook error gallery; explain three recurring confusions and test one proposed fix.

## 02. A small image classifier you can debug

- **Task:** train a compact convolutional model and compare augmentation choices.
- **Level / compute:** beginner / CPU on a labeled subset; one GPU for fuller experiments.
- **Data:** [CIFAR-10](https://cave.cs.toronto.edu/kriz/cifar.html). Derive validation data from training data and preserve the official test split.
- **Baseline code:** adapt the [PyTorch CIFAR-10 tutorial](https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html).
- **Measure:** accuracy, per-class recall, training/validation loss, runtime, and the gap between training and validation scores.
- **Failure to investigate:** overfitting to a small split or accidentally augmenting validation images differently on every evaluation.
- **Extension / deliverable:** compare no augmentation, flips/crops, and one stronger augmentation under the same training budget; publish learning curves and saved predictions.

## 03. Pet breed transfer learning

- **Task:** compare a frozen image encoder with fine-tuning on a fine-grained classification problem.
- **Level / compute:** beginner / CPU for cached embeddings; one GPU for fine-tuning.
- **Data:** [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/). Use the official split, derive development data from training, and inspect near duplicates.
- **Baseline code:** adapt the [PyTorch transfer-learning tutorial](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) with a matching dataset loader and class count.
- **Measure:** macro-F1, top-1 accuracy, and confusion among visually similar breeds.
- **Failure to investigate:** background, crop style, or image source can become a shortcut.
- **Extension / deliverable:** compare full images and subject crops; publish a concise model card with the worst-performing classes and out-of-domain examples.

## 04. Flower recognition with a label budget

- **Task:** determine how classification quality changes when only a few training examples are available per category.
- **Level / compute:** beginner / CPU using fixed features; one GPU optional.
- **Data:** [Oxford Flowers 102](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/). Keep the published test split fixed while subsampling only training data.
- **Baseline code:** use an encoder from [Torchvision models](https://docs.pytorch.org/vision/stable/models.html) and a linear classifier.
- **Measure:** mean per-class accuracy and variation across several fixed label-subset seeds.
- **Failure to investigate:** sampling only the easiest images makes a small-data result misleading.
- **Extension / deliverable:** plot accuracy against labels per class; compare a color-histogram baseline, frozen features, and one fine-tuned model at a matched label budget.

## 05. Document scanner with measurable geometry

- **Task:** detect page corners, rectify perspective, and compare thresholding choices.
- **Level / compute:** beginner / CPU.
- **Data:** capture your own blank or non-sensitive printed pages at several angles; use [OpenCV sample assets](https://github.com/opencv/opencv/tree/4.x/samples) for initial geometry exercises. Record page identity so the same page does not cross splits.
- **Baseline code:** combine contours, perspective transforms, and thresholding from the [OpenCV Python tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html).
- **Measure:** corner error normalized by image diagonal, successful-page rate, and runtime on a fixed resolution.
- **Failure to investigate:** shadows, curved pages, and a background with a stronger contour than the page.
- **Extension / deliverable:** export rectified pages plus confidence flags; annotate a small test set and compare automatic corners with manual correction.

## 06. Find the same object from another angle

- **Task:** retrieve gallery images of the query object without returning the query itself.
- **Level / compute:** beginner / CPU.
- **Data:** [COIL-100](https://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php). Separate query and gallery viewpoints; state whether the object identities are shared, as intended for instance retrieval.
- **Baseline code:** compute color or local-feature descriptors with [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html), then use cosine or Euclidean nearest neighbors.
- **Measure:** Recall@1, Recall@5, mean average precision, and query latency; define all relevant gallery images explicitly.
- **Failure to investigate:** matching background or color rather than object identity; near-adjacent viewpoints can make evaluation too easy.
- **Extension / deliverable:** compare handcrafted descriptors and a frozen learned embedding; show retrieved results at increasing viewpoint gaps and list false matches.

## 07. Foreground extraction with an interaction budget

- **Task:** extract a pet foreground from a supplied rectangle and measure where classical segmentation fails.
- **Level / compute:** beginner / CPU.
- **Data:** [Oxford-IIIT Pet trimaps](https://www.robots.ox.ac.uk/~vgg/data/pets/). Keep boundary/unknown pixels separate from foreground and background in the evaluator.
- **Baseline code:** use [OpenCV GrabCut](https://docs.opencv.org/4.x/d8/d83/tutorial_py_grabcut.html). Define a repeatable rectangle-generation rule using a separately supplied prompt; ground truth may simulate an interaction only if clearly labeled.
- **Measure:** foreground IoU, boundary quality, and corrections required per image.
- **Failure to investigate:** fur, low contrast, and disconnected foreground regions.
- **Extension / deliverable:** compare rectangle-only and rectangle-plus-scribble prompts at fixed interaction budgets; publish overlays and the exact prompt protocol.

## 08. Hand landmark interaction demo

- **Task:** turn hand landmarks into a simple gesture-controlled interface, such as moving a pointer or advancing slides.
- **Level / compute:** beginner / CPU for the lightweight baseline; check actual device support.
- **Data:** record consenting participants or only your own hands, following the input format in the [MediaPipe hand landmark guide](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker). Split by recording session and participant when possible.
- **Baseline code:** use the guide's official example and a geometric gesture rule before training a gesture classifier.
- **Measure:** gesture precision/recall, false activations per minute, end-to-end latency, and tracking dropout rate.
- **Failure to investigate:** occluded fingers, motion blur, lighting changes, and left/right mirroring.
- **Extension / deliverable:** add a dwell-time or explicit activation gesture; demonstrate performance on held-out recordings and document where the interface becomes unreliable.
