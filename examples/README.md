# Starter programs

Three small programs. Run them in a minute, break them in an hour, learn from them for a week.

[Home](../README.md) · [Roadmaps](../roadmaps/README.md) · [Projects](../projects/README.md)

All three run on a CPU. The default demos need no network, no model weights, no account, and no dataset download.

## Setup

Python 3.11 or newer, from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r examples/requirements.txt
make demo                        # or run each program below
```

Results land in `outputs/` (ignored by Git).

## 1. See what an edge detector sees

```bash
python examples/image_processing.py
python examples/image_processing.py --image path/to/photo.jpg   # your own photo
```

Open `outputs/image-processing/comparison.png`. You get the RGB image, grayscale, Gaussian blur, and Sobel gradient magnitude side by side.

**Try this:** change the blur radius, add noise, and compare gradients before and after smoothing. Then explain why a texture edge is not an object boundary. The preview rescales each panel for display, so brightness is not a confidence score.

## 2. Train a classifier you can trust

```bash
python examples/digits_baseline.py
```

The 8x8 digits dataset, split 60/20/20 (1,077 / 360 / 360 images). The validation split selects the regularization strength, scaling is fitted inside the pipeline, and the test set is touched once.

On a laptop it reaches about **97% test accuracy and 0.97 macro-F1**, against **10%** for a most-frequent-class baseline. Open `outputs/digits/metrics.json` for the confusion matrix, split indices, per-image predictions, and package versions, and `errors.png` to see what it got wrong.

**Try this:** compare the linear model with a small MLP using validation data only, then make one final test comparison. A high score on tidy 8x8 digits says nothing about a phone photo of someone's handwriting.

## 3. Build an image search baseline

```bash
python examples/image_retrieval.py --demo
python examples/image_retrieval.py --query q.jpg --gallery photos/ --top-k 5   # your own images
```

Open `outputs/retrieval/matches.png` and `results.json`. Candidates are ranked by cosine similarity between normalized RGB histograms. The query is excluded and unreadable files are reported, not silently skipped.

**Try this:** compare a different shape in the same color against the same shape in a different color, and explain the failure. Later, swap histograms for frozen image embeddings and measure Recall@K against hand-labelled matches. A similarity score is not an accuracy metric.

## Checklist for any experiment

Save the command, environment, split definition, result, three failure examples, and your next hypothesis. The [experiment template](../templates/experiment-report.md) and the [evaluation guide](../guides/evaluation.md) are built for this.

## References

- [scikit-learn digits example](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)
- [Pillow Image API](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- [NumPy histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)

External libraries and datasets keep their own licenses.
