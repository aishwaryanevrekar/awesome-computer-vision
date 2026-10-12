# Datasets, licenses, and responsible use

A download link is a starting point for a dataset review. Record where the data came from, what the labels mean, which uses are permitted, and which population or conditions the data actually represents.

## Keep four kinds of terms separate

| Asset | Where to check | What to record |
|---|---|---|
| Source code | Repository license and notices | License version, attribution, redistribution conditions |
| Model weights | Exact checkpoint/model card and accompanying terms | Checkpoint ID, permitted use, additional restrictions |
| Dataset and annotations | Dataset release page, license, access agreement | Dataset version, image versus annotation terms, citation |
| Individual media or derived assets | Original media records and asset-specific terms | Creator, source, license, provenance and modifications |

These terms can differ even within one project. For example, inspect both the code and dataset sections in [MM-Vet](https://github.com/yuweihao/MM-Vet), the checkpoint descriptions in [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2), and the dataset-specific conditions on [BOP](https://bop.felk.cvut.cz/datasets/). Recheck the exact release you use; a table in a resource list cannot replace its primary terms.

## Before downloading

- Define the intended use: private learning, a public research report, redistribution, a hosted demo, or commercial use.
- Locate the original release, its documentation, and any access agreement. If terms are unclear, resolve that before redistribution or deployment.
- Check whether source images and annotations have different permissions. A dataset loader's software license does not grant rights to the images it downloads.
- Estimate disk and memory needs. Prefer a documented subset when the full release is unnecessary.
- Inspect sensitive content and available consent/provenance information. Choose another dataset when it cannot support the intended use responsibly.

Use official entry points such as [COCO](https://cocodataset.org/), [MVTec AD](https://www.mvtec.com/research-teaching/datasets/mvtec-ad), [Cityscapes](https://www.cityscapes-dataset.com/), and [ISIC](https://www.isic-archive.com/) to find the applicable release information. Access requirements and allowed uses differ across collections.

## Make a dataset card

```text
Name / release / source URL / retrieval date:
Original creators and required citation:
Image terms / annotation terms / access agreement:
Intended use and distribution plan:
Number of examples / classes / annotation types:
Collection context and known coverage gaps:
Personal or sensitive information and handling:
Split policy / grouping keys / duplicate checks:
Preprocessing / exclusions / label changes:
Local checksums or immutable manifest:
Known limitations / contact or correction mechanism:
```

Document absent metadata as absent. Do not claim patient independence, geographic coverage, demographic balance, or consent when the release does not establish it. A convenient category count is not evidence of representative coverage.

## Protect the validity of the experiment

Audit label definitions, coordinate systems, class IDs, ignored regions, and annotation versions before training. A box format mismatch can make a working model appear broken; duplicated subjects can make a broken experiment appear strong.

Keep original data read-only where practical and save preprocessing as a reproducible transform. Retain a manifest connecting each derived crop, frame, mask, or synthetic example to its source. Split before augmentation, and do not let synthetic variants of test examples enter training. See the [evaluation guide](evaluation.md).

Treat missing files and changed URLs as part of the result: record excluded IDs and counts rather than silently evaluating an easier subset. For web-scale or foundation-model comparisons, describe known training overlap and what cannot be checked.

## Match the demo to the evidence

For self-collected footage, obtain permission from the people involved and avoid unnecessary faces, screens, documents, number plates, or location metadata. Use staged or synthetic non-sensitive documents for OCR demos when possible. Keep a practical deletion process for identifiable material you collect.

For medical images, benchmark segmentation or classification as a research task; a held-out score does not establish clinical usefulness. For robotics and driving data, an offline benchmark does not establish that a system can safely control hardware. For wildlife data, avoid exposing sensitive species locations in a public demo. These limitations belong beside the result, where a reader can interpret it.

Prefer aggregate metrics and permitted visual examples in a public portfolio. Do not redistribute raw datasets, private captures, checkpoints, or scraped media merely because a training script can access them. Link to the official download and include a small permitted fixture or a data-preparation script instead.

## Before publishing a project

- Include the dataset/model citations and retained notices required by the original sources.
- State the exact data release, split, exclusions, and any derived labels.
- Check every sample image and video you plan to publish for permission and unintended personal information.
- Separate the license for your implementation from upstream data, weights, and media.
- Describe known blind spots, unsupported uses, and how someone can reproduce or correct the result.

[Project briefs](../projects/README.md) · [Compute and setup](compute-and-setup.md)
