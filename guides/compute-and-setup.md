# Compute and setup

Choose the smallest experiment that answers the question. Model weights are only part of memory use: activations, gradients, optimizer states, image resolution, video length, batching, and the runtime all matter. A “one GPU” label is a starting scope, not a universal memory guarantee.

## Choose a practical route

| Available hardware | Useful starting work | Check before expanding |
|---|---|---|
| CPU laptop | Classical vision, small classifiers, dataset audits, cached embeddings, evaluation | RAM, decoding time, disk usage, supported inference operators |
| Apple Silicon | The CPU route plus supported PyTorch MPS inference/training | MPS availability, unsupported operators/dtypes, unified-memory pressure |
| One NVIDIA GPU | Transfer learning, compact detection/segmentation, small pretrained VLMs, bounded 3D scenes | Device memory, driver/runtime compatibility, custom CUDA extensions |
| Larger accelerator or multiple GPUs | Longer video, larger checkpoints, foundation-model adaptation, broader sweeps | Measured need, distributed setup, communication overhead, checkpointing |

Useful work does not require training a foundation model. Extract features once, cache predictions, train a linear head, reproduce an evaluator, inspect failures, or compare data-selection strategies. Most of the [project briefs](../projects/README.md) have a bounded starting point.

## Isolate each upstream environment

Use a separate environment per project. Follow the upstream repository's supported Python and package versions; do not combine several research repositories into a single environment and upgrade every dependency at once.

For a plain Python project, the [standard-library virtual environment documentation](https://docs.python.org/3/library/venv.html) is a portable starting point. For example, on macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Then follow the selected project's installation instructions. Use its lockfile when provided. Otherwise record the working dependency set, Python version, operating system, and upstream commit. The [local examples](../examples/README.md) have their own requirements and commands.

For PyTorch, use the official [installation selector](https://pytorch.org/get-started/locally/) for the chosen operating system and compute backend. Use the matching Torchvision build. A copied command with a CUDA suffix from an old tutorial is not a substitute for checking compatibility.

## CPU, Apple Silicon, and CUDA

**CPU:** start with small batches and a small data subset. Check whether the baseline itself supports CPU execution; some research code assumes CUDA or compiles accelerator-only operators. Cache features and use a lightweight model before considering a port.

**Apple Silicon:** use a build supporting [PyTorch MPS](https://docs.pytorch.org/docs/stable/mps.html). Check availability at runtime. CUDA-specific code cannot be made MPS-compatible solely by changing a device string; check operator support, dtypes, custom kernels, and numerical agreement on a small sample.

**NVIDIA CUDA:** follow the upstream project's build requirements and the [NVIDIA CUDA installation documentation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/) when a toolkit or custom extension is required. A system driver, a framework's packaged runtime, and a compiler toolkit are separate components. Verify the actual environment before changing any of them.

After installing PyTorch, this diagnostic reports available devices without downloading weights:

```python
import platform
import torch

print("Python:", platform.python_version())
print("PyTorch:", torch.__version__)
print("CUDA runtime:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())
print("MPS available:", torch.backends.mps.is_available())

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

x = torch.ones((2, 2), device=device)
print("Tensor smoke check:", (x @ x).cpu())
```

This checks only a basic tensor operation. Next run the project's smallest inference example and a forward/backward step if training is intended. Compare a tiny reference batch before assuming that a backend, export, mixed-precision mode, or quantized model is equivalent.

## Estimate before scaling

1. Inspect dataset and checkpoint download sizes, decompression needs, temporary files, and cache locations.
2. Load the smallest suitable checkpoint and run one sample at the intended resolution.
3. Record peak memory and wall time for a short, representative batch. Include decoding and preprocessing if those matter to the task.
4. Increase one of batch size, resolution, sequence length, or model size at a time.
5. Extrapolate only as a rough planning estimate. Confirm with a larger pilot; compilation, data loading, and distributed overhead can change scaling.

When memory is tight, first reduce batch size or input size if that still preserves the research question. Then consider frozen features, gradient accumulation, mixed precision, or activation checkpointing where supported. Gradient accumulation changes the number of examples per optimizer update, but does not reproduce every effect of a larger physical batch, especially batch-dependent layers.

Quantization can change operator support and task quality; validate both before calling it a deployment improvement. Follow the [ONNX Runtime quantization guide](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) for compatible workflows and calibration requirements.

## Use remote compute deliberately

Before launching a paid job, check current provider pricing, storage and transfer charges, availability, and account limits. Set a budget alert or job limit, save checkpoints to persistent storage, and confirm shutdown behavior. This guide makes no promise of free GPU access, fixed hourly costs, or a particular model fitting a named device.

Record actual accelerator hours, failed runs, and total storage used in your report. Smaller, repeatable experiments usually teach more than an oversized run whose failure cannot be diagnosed.

[Evaluation](evaluation.md) · [Datasets and licenses](datasets-and-licenses.md)
