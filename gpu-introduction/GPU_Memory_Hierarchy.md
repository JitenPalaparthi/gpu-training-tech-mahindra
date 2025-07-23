
# GPU Memory Hierarchy Explained

This document covers the memory architecture inside an NVIDIA GPU, from fastest to slowest, with detailed descriptions and use cases.

---

## 🧠 GPU Memory Hierarchy (from fastest to slowest)

```
         [ Registers (Per Thread) ]
                  ↓
         [ L1 Cache / Shared Memory (Per SM) ]
                  ↓
         [ L2 Cache (Shared across all SMs) ]
                  ↓
         [ Global Memory (VRAM - GDDR6/HBM) ]
                  ↓
         [ Host Memory (CPU DRAM via PCIe/NVLink) ]
```

---

## 📘 Detailed Explanation of Each Memory Type

| Memory Type       | Scope          | Access Speed      | Size (Approx)        | Accessed By         | Use Case                                                                 |
|-------------------|----------------|-------------------|-----------------------|----------------------|--------------------------------------------------------------------------|
| **Registers**      | Per thread     | 🚀 Fastest         | 32–64 KB/thread block | Thread               | Store local thread variables (e.g., loop counters, temp values)          |
| **L1 Cache**       | Per SM         | ⚡ Very Fast       | 32–128 KB             | Thread block (via SM)| Implicit cache for global memory; reduces latency                        |
| **Shared Memory**  | Per SM         | ⚡ Very Fast       | 64–128 KB             | Thread block (via SM)| Explicit programmer-controlled cache for sharing data between threads    |
| **L2 Cache**       | Entire GPU     | ⚡ Fast            | 2–96 MB               | All SMs              | GPU-wide cache for global memory; reduces VRAM access                    |
| **Global Memory**  | Entire GPU     | 🐢 Slower          | 8–80+ GB              | All threads          | Main GPU DRAM (GDDR6/HBM); large data storage                            |
| **Constant Memory**| Entire GPU     | ⚡ Fast (cached)   | 64 KB (cached)        | All threads          | Read-only values used across threads (e.g., weights, configs)            |
| **Texture/Surface Memory** | Entire GPU | Specialized | Based on config | All threads | Optimized for 2D/3D spatial locality — image/video processing |
| **Local Memory**   | Per thread     | 🐌 Slower (L2-backed) | Virtual            | Individual threads   | Used when registers spill; not "local" in the normal sense               |
| **Host Memory**    | CPU RAM        | 🐢 Slowest         | 16–1024 GB+           | Needs explicit copy  | Accessed from host or via `cudaMemcpy`; very slow for real-time tasks   |

---

## 🔁 Memory Access Latency (Approximate)

| Memory Type      | Latency (cycles) |
|------------------|------------------|
| Registers         | 1 cycle          |
| Shared Memory     | ~2–3 cycles      |
| L1 Cache          | ~10–30 cycles    |
| L2 Cache          | ~200–300 cycles  |
| Global Memory     | ~400–800 cycles  |
| Host Memory       | 1000+ cycles     |

---

## 🧪 Use Case Mapping

| Scenario                       | Memory Used          |
|--------------------------------|----------------------|
| Per-thread computation         | Registers            |
| Fast intra-warp/thread sync    | Shared Memory        |
| Caching reused global data     | L1 Cache             |
| Across-kernel data sharing     | Global Memory        |
| Large dataset storage          | Global / Host Memory |
| Image/Video processing         | Texture Memory       |
| Read-only broadcast values     | Constant Memory      |

---

## 📂 GPU Memory Layout Visualization

```
+---------------------+
|  Registers (Thread) |
+---------------------+
|  Shared Mem / L1    | <-- Per SM
+---------------------+
|       L2 Cache      | <-- Shared across all SMs
+---------------------+
|   Global Memory     | <-- GDDR6 / HBM
+---------------------+
|   Host Memory (CPU) | <-- Via PCIe / NVLink
+---------------------+
```
