"""Train and evaluate a linear image classifier without downloading data."""

import argparse
import json
import platform
from importlib.metadata import version
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from sklearn.datasets import load_digits
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def train(output: Path, seed: int = 42) -> dict:
    """Keep the test split sealed until C is selected on validation data."""
    digits = load_digits()
    indices = np.arange(len(digits.target))
    trainval, test = train_test_split(
        indices, test_size=0.2, stratify=digits.target, random_state=seed
    )
    fit, valid = train_test_split(
        trainval, test_size=0.25, stratify=digits.target[trainval], random_state=seed
    )
    candidates = []
    for regularization in (0.01, 0.1, 1.0):
        model = make_pipeline(
            StandardScaler(), LogisticRegression(C=regularization, max_iter=2000)
        )
        model.fit(digits.data[fit], digits.target[fit])
        score = f1_score(digits.target[valid], model.predict(digits.data[valid]), average="macro")
        candidates.append({"C": regularization, "validation_macro_f1": float(score)})
    selected = max(candidates, key=lambda row: row["validation_macro_f1"])
    model = make_pipeline(
        StandardScaler(), LogisticRegression(C=selected["C"], max_iter=2000)
    )
    model.fit(digits.data[trainval], digits.target[trainval])
    predicted = model.predict(digits.data[test])
    probabilities = model.predict_proba(digits.data[test])
    dummy = DummyClassifier(strategy="most_frequent").fit(digits.data[trainval], digits.target[trainval])
    report = {
        "dataset": "scikit-learn bundled digits (8x8 grayscale)",
        "seed": seed,
        "split_sizes": {"train": len(fit), "validation": len(valid), "test": len(test)},
        "split_indices": {"train": fit.tolist(), "validation": valid.tolist(), "test": test.tolist()},
        "selection": candidates,
        "selected_C": selected["C"],
        "refit_on_train_and_validation": True,
        "test_accuracy": float(accuracy_score(digits.target[test], predicted)),
        "test_macro_f1": float(f1_score(digits.target[test], predicted, average="macro")),
        "dummy_test_accuracy": float(accuracy_score(digits.target[test], dummy.predict(digits.data[test]))),
        "confusion_matrix": confusion_matrix(digits.target[test], predicted, labels=range(10)).tolist(),
        "labels": list(range(10)),
        "test_predictions": [
            {"image_index": int(index), "truth": int(truth), "prediction": int(prediction), "probabilities": probability.tolist()}
            for index, truth, prediction, probability in zip(test, digits.target[test], predicted, probabilities)
        ],
        "environment": {"python": platform.python_version(), **{p: version(p) for p in ("numpy", "scikit-learn", "Pillow")}},
        "limitation": "A stratified toy image split, not a writer-independent or real-world OCR evaluation.",
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "metrics.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    wrong = np.flatnonzero(predicted != digits.target[test])[:20]
    board = Image.new("RGB", (5 * 100, max(1, (len(wrong) + 4) // 5) * 116), "#111827")
    draw = ImageDraw.Draw(board)
    for n, offset in enumerate(wrong):
        pixels = (digits.images[test[offset]] / 16 * 255).astype(np.uint8)
        tile = Image.fromarray(pixels).resize((80, 80), Image.Resampling.NEAREST)
        x, y = (n % 5) * 100 + 10, (n // 5) * 116
        board.paste(tile, (x, y + 24))
        draw.text((x, y + 6), f"{digits.target[test[offset]]} -> {predicted[offset]}", fill="white")
    if not len(wrong):
        draw.text((10, 10), "No errors in this test split.", fill="white")
    board.save(output / "errors.png")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path, default=Path("outputs/digits"))
    args = parser.parse_args()
    report = train(args.output, args.seed)
    print(json.dumps({key: report[key] for key in ("selected_C", "test_accuracy", "test_macro_f1", "dummy_test_accuracy")}, indent=2))
    print(f"Metrics, split indices, environment and error examples: {args.output}")


if __name__ == "__main__":
    main()
