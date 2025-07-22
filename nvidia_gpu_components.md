
# 🔍 NVIDIA GPU Architecture: Components Explained

This document details the key components inside an NVIDIA GPU, from compute units to memory systems and specialized cores.

---

## 🧠 Top-Level Components

| Component             | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **SM (Streaming Multiprocessor)** | Core compute unit, handles warp scheduling, thread execution, memory access. |
| **CUDA Cores**         | ALUs that execute threads inside a warp (INT, FP, logical ops).            |
| **Tensor Cores**       | Specialized cores for matrix ops in AI workloads (FP16, TF32, INT8, FP8). |
| **RT Cores**           | Ray tracing acceleration for real-time 3D rendering.                      |
| **L1 Cache / Shared Memory** | Fast on-chip cache and block-level shared memory.                |
| **L2 Cache**           | Shared cache between all SMs.                                              |
| **Register File**      | Private storage for thread-local variables.                               |
| **Warp Scheduler**     | Issues instructions to warps for execution.                               |
| **Instruction Dispatch Unit** | Sends instructions to functional units.                        |
| **Texture Units**      | Sample, interpolate, and process textures.                                |
| **Memory Controllers** | Interface to global memory (GDDR6, HBM).                                  |
| **NVLink / PCIe**      | Interconnect for GPUs and host communication.                             |
| **NVENC/NVDEC**        | Video encode and decode accelerators.                                     |

---

## 🧩 In-Depth Component Breakdown

### 1. 🚀 Streaming Multiprocessor (SM)
- The core execution unit.
- Includes CUDA cores, tensor cores, warp schedulers, etc.
- Example: A100 has **108 SMs**.

### 2. 🔢 CUDA Cores
- Handle arithmetic and logical ops per thread.
- SIMD (SIMT model): all 32 threads in a warp execute same instruction.

### 3. 📐 Tensor Cores
- Matrix multiplication units.
- Optimized for AI/ML training and inference.
- Used heavily in deep learning frameworks.

### 4. 🔦 RT Cores
- Accelerate BVH traversal and triangle intersection.
- Offload heavy ray tracing computations from CUDA cores.

### 5. 📥 L1 Cache / Shared Memory
- Low-latency memory close to SMs.
- Shared memory is manually managed per block.
- Often configurable as split/shared.

### 6. 🗂️ L2 Cache
- GPU-wide cache for data shared across SMs.
- Sits between SMs and global memory.

### 7. 🎯 Warp Scheduler
- Schedules instructions for **warps** (32 threads).
- Issues to execution pipelines.

### 8. 🧮 Register File
- High-speed storage per thread.
- Used for local variables and instruction operands.

### 9. 🧵 Texture Units
- Handle filtering, sampling, and interpolation.
- Mostly used in rendering pipelines.

### 10. 💾 Memory Controller
- Manages data access from DRAM (global memory).
- Optimized for coalesced memory access.

### 11. 🔗 NVLink / PCIe
- High-bandwidth links between GPUs or host.
- NVLink is much faster than traditional PCIe.

### 12. 🎬 NVENC / NVDEC
- Hardware video encoding (NVENC) and decoding (NVDEC).
- Used in streaming, video editing, broadcasting.

---

## 📊 Simplified GPU Block Diagram

```plaintext
GPU Die
├── SM 0
│   ├── CUDA Cores
│   ├── Tensor Cores
│   ├── RT Cores
│   ├── Shared Mem / L1
│   └── Warp Scheduler
├── SM 1
│   └── ...
├── L2 Cache
├── Memory Controller
└── PCIe / NVLink
```

---

## ✅ Summary

NVIDIA GPUs are built for massive parallelism. Key points:
- **SMs** are the basic compute blocks.
- **CUDA Cores** do general math, **Tensor Cores** do AI math, and **RT Cores** do ray tracing.
- Caches, registers, and schedulers enable high-throughput execution.
- NVLink and PCIe ensure GPUs work seamlessly in clusters or with CPUs.
