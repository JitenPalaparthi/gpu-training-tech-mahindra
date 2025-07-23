
# 🧠 GPU Execution Hierarchy: From Die to Thread

This document explains how a GPU is structured from the **GPU Die** level down to the **individual thread**, using a layered architectural model.

---

## 1️⃣ GPU Die (Top-Level)

The **GPU die** is the physical silicon chip containing all GPU components.

**Includes:**
- Multiple **Streaming Multiprocessors (SMs)**
- **Memory controllers**
- **Caches (L1, L2)**
- Specialized cores (Tensor, RT)
- I/O Interfaces (PCIe, NVLink)

---

## 2️⃣ Streaming Multiprocessors (SMs)

Each SM is a self-contained compute unit capable of running many threads in parallel.

**Each SM contains:**
- CUDA Cores
- Tensor Cores
- Warp Schedulers
- Load/Store Units
- Shared Memory
- Register File

📌 **Example**: NVIDIA A100 has **108 SMs**

---

## 3️⃣ Thread Blocks

- SMs execute **thread blocks**, which are user-defined groups of threads.
- Each block is assigned to **one SM**.
- Threads in a block share memory and can synchronize.

---

## 4️⃣ Warps (Scheduling Unit)

- A **warp** = **32 threads**
- All threads in a warp execute **the same instruction** (SIMT model).
- Warp scheduling is done per SM.

📌 **Example**: Each SM can hold up to **64 warps** (2048 threads).

---

## 5️⃣ Threads

- The **smallest unit** of execution.
- Each thread has:
  - Private registers
  - Access to shared memory (with block) and global memory

---

## 📊 Hierarchy Table

| Level        | Description                               | Example Count        |
|--------------|-------------------------------------------|----------------------|
| **GPU Die**  | Entire chip                               | 1                    |
| **SM**       | Streaming multiprocessor                  | 108 (in A100)        |
| **Block**    | Group of threads assigned to an SM        | ~1–16 per SM         |
| **Warp**     | 32 threads per warp                       | 64 per SM            |
| **Thread**   | Smallest compute unit                     | 2048 per SM          |

---

## 📉 Visual Layout

```plaintext
GPU Die
└── SM 0
    ├── Block 0
    │   ├── Warp 0 (32 threads)
    │   ├── Warp 1 (32 threads)
    │   └── ...
    └── Block 1
        ├── Warp 0 (32 threads)
        └── ...
└── SM 1
    └── ...
```

---

## ✅ Summary

Each GPU Die is a powerful compute device made of many SMs. Each SM manages warps and blocks of threads. The GPU executes thousands of threads in parallel by coordinating across this deep hierarchy.
