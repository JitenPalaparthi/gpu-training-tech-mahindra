
# 🚀 GPU-to-GPU Communication over Network Using RDMA

This process is also referred to as:

> **GPUDirect RDMA** — direct memory access between GPUs across nodes **without CPU involvement**.

---

## 🧠 1. What Is GPUDirect RDMA?

It’s a NVIDIA feature that enables RDMA NICs (like Mellanox ConnectX) to **directly read/write GPU memory** via PCIe, bypassing:
- The CPU
- System RAM
- Kernel driver stack

➡️ This enables **GPU-to-GPU data transfers across the network** with **very low latency** and **high throughput**.

---

## 🏗️ 2. Basic Components in the Path

| Component             | Role |
|----------------------|------|
| GPU A                | Source of data |
| RNIC A               | RDMA NIC attached to Node A |
| Network              | RoCE/Infiniband transport |
| RNIC B               | RDMA NIC on Node B |
| GPU B                | Destination GPU |
| PCIe + DMA Engines   | Used by NICs to talk to GPUs directly |

---

## 🔄 3. Step-by-Step: GPU-to-GPU via RDMA

### 💡 Assume: Node A (GPU A), Node B (GPU B)

| Step | What Happens |
|------|--------------|
| 1️⃣ | Application on Node A registers GPU memory (using `cudaHostRegister`) |
| 2️⃣ | RNIC A maps that memory using **Memory Translation Table (MTT)** |
| 3️⃣ | Application on Node A initiates RDMA **write** or **send** |
| 4️⃣ | RNIC A uses DMA over PCIe to fetch data directly from GPU A memory |
| 5️⃣ | RNIC A transmits data over **RDMA fabric** (e.g., Infiniband, RoCEv2) |
| 6️⃣ | RNIC B receives data and performs DMA to write directly into GPU B memory |
| 7️⃣ | Completion Queues updated → signaling done to both applications |

✅ At no point is CPU RAM or kernel buffer involved.

---

## ⚙️ 4. Key Requirements for This to Work

| Requirement | Details |
|-------------|---------|
| **GPUDirect RDMA Support** | Must be enabled in both GPUs and drivers |
| **CUDA-aware MPI / NCCL** | Libraries must support GPU buffers |
| **Proper IOMMU + PCIe topology** | NIC and GPU should be on the same PCIe root complex (ideal) |
| **Pinned Memory** | GPU memory must be pinned (registered) to prevent page faults |
| **Compatible NIC (RNIC)** | Mellanox ConnectX-4 or later |

---

## ⚡ 5. Performance Benefits

| Metric | Traditional (CPU copy) | GPUDirect RDMA |
|--------|------------------------|----------------|
| Latency | 30–50 µs              | 3–5 µs         |
| CPU Usage | High                 | Near 0%        |
| Throughput | Lower (due to copies) | 40–100+ Gbps  |

---

## 📊 Example Use Case

### Deep Learning Distributed Training (e.g., using PyTorch or TensorFlow + NCCL):
- Node A computes gradients on GPU
- Using NCCL over RDMA, these are sent directly to GPU B on Node B
- GPU B aggregates and backpropagates, no CPU needed
