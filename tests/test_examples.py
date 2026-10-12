"""Check meaningful invariants in the runnable examples."""

import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
from PIL import Image

from examples.digits_baseline import train
from examples.image_processing import process, sobel_magnitude, synthetic_scene
from examples.image_retrieval import create_demo, descriptor, rank_images


class ExampleTests(unittest.TestCase):
    def test_sobel_constant_and_step(self):
        self.assertTrue(np.all(sobel_magnitude(np.ones((8, 8))) == 0))
        step = np.zeros((8, 8))
        step[:, 4:] = 255
        edges = sobel_magnitude(step)
        self.assertGreater(float(edges[:, 3:5].min()), 0)
        self.assertTrue(np.all(edges[:, :3] == 0))

    def test_image_outputs_and_uniform_image(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            process(synthetic_scene(), output)
            with Image.open(output / "comparison.png") as comparison:
                self.assertEqual(comparison.size, (1024, 284))
            process(Image.new("RGB", (32, 32), "white"), output)
            with Image.open(output / "sobel.png") as edges:
                self.assertEqual(int(np.asarray(edges).sum()), 0)

    def test_retrieval_excludes_query_and_records_corrupt_image(self):
        with tempfile.TemporaryDirectory() as temporary:
            query, gallery = create_demo(Path(temporary))
            query_in_gallery = gallery / "query.png"
            query_in_gallery.write_bytes(query.read_bytes())
            (gallery / "corrupt.png").write_text("not an image", encoding="utf-8")
            (gallery / "._metadata.png").write_text("macOS sidecar", encoding="utf-8")
            ranked, skipped = rank_images(query_in_gallery, gallery, 6)
            self.assertEqual(len(ranked), 6)
            self.assertEqual(Path(ranked[0]["path"]).name, "orange-circle.png")
            self.assertTrue(all(Path(row["path"]) != query_in_gallery for row in ranked))
            self.assertAlmostEqual(float(np.linalg.norm(descriptor(query))), 1.0)
            self.assertEqual(len(skipped), 1)
            with self.assertRaises(ValueError):
                rank_images(query, gallery, 0)

    def test_classifier_split_integrity_and_baseline(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            report = train(output)
            splits = [set(report["split_indices"][key]) for key in ("train", "validation", "test")]
            self.assertFalse(splits[0] & splits[1] or splits[0] & splits[2] or splits[1] & splits[2])
            self.assertEqual(len(set.union(*splits)), 1797)
            self.assertEqual(sum(map(sum, report["confusion_matrix"])), report["split_sizes"]["test"])
            self.assertEqual({row["image_index"] for row in report["test_predictions"]}, splits[2])
            self.assertTrue(all(abs(sum(row["probabilities"]) - 1.0) < 1e-8 for row in report["test_predictions"]))
            self.assertGreater(report["test_accuracy"], report["dummy_test_accuracy"] + 0.5)
            self.assertTrue((output / "errors.png").is_file())
            self.assertEqual(json.loads((output / "metrics.json").read_text())["seed"], 42)


if __name__ == "__main__":
    unittest.main()
