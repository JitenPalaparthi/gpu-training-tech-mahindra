
# GPU Networking Basics

## 1. Overview

GPU networking is essential for scaling high-performance computing (HPC) and AI workloads across multiple GPUs and nodes. Technologies such as **NVLink**, **RDMA**, and **InfiniBand** play a key role in ensuring fast data transfers and reduced latency.

---

## 2. NVLink

### What is NVLink?
NVIDIA's high-bandwidth, energy-efficient interconnect that allows direct GPU-to-GPU communication.

### Features:
- Higher bandwidth than PCIe (up to 600 GB/s aggregate bidirectional bandwidth)
- Lower latency
- Allows unified memory access across GPUs

### Use Case:
- Multi-GPU training in a single node (e.g., DGX A100 systems)

### Example:
```bash
nvidia-smi topo -m
```
This shows the GPU interconnect topology including NVLink.

---

## 3. RDMA (Remote Direct Memory Access)

### What is RDMA?
RDMA allows one computer to directly place data into the memory of another without involving the CPU.

- General network communication

    App → OS → NIC → Network → NIC → OS → App

- With RDMA

    APP → NIC → Network → NIC → App

### Features:
- Low latency communication (~1-2 microseconds)
- High throughput
- Reduces CPU overhead

### Use Case:
- GPU Direct RDMA: Enables GPUs to read/write from/to remote memory directly over the network.

### Example:
Used in MPI workloads for deep learning or CFD simulations.

```bash
# RDMA diagnostics
ibv_devinfo
rdma-devices
```

---

## 4. InfiniBand

### What is InfiniBand?
A high-speed network communication standard used in HPC clusters.

### Features:
- Supports RDMA
- Extremely low latency and high throughput
- Supports Quality of Service (QoS), congestion control

### Use Case:
- Inter-node GPU communication in supercomputers (e.g., Summit, Frontier)

### Example:
```bash
ibstat
ibstatus
ibping
```

---

## 5. GPU Direct Technologies

### GPU Direct RDMA
Allows 3rd-party devices (like NICs) to communicate directly with GPU memory.

### GPU Direct Storage
Allows storage I/O to bypass CPU and go directly to GPU memory.

### Use Case:
- Large dataset training (e.g., 3D medical imaging)

---

## 6. Other Related Technologies

| Technology       | Purpose                             | Used With         |
|------------------|--------------------------------------|-------------------|
| RoCE (RDMA over Converged Ethernet) | RDMA over Ethernet | Cloud & datacenters |
| PCIe             | General GPU interconnect             | All systems       |
| NVSwitch         | Scalable NVLink switch               | DGX systems       |

---

## 7. Summary

| Tech       | Bandwidth      | Latency     | Scope           |
|------------|----------------|-------------|------------------|
| NVLink     | Up to 600 GB/s | ~10ns       | Intra-node       |
| RDMA       | ~100 Gbps+     | 1-2 µs      | Inter-node       |
| InfiniBand | ~400 Gbps      | Sub-µs      | Interconnect     |

---

## 8. Tools

- `nvidia-smi`
- `ibstat`, `ibstatus`
- `rdma-devices`
- `nv_peer_mem` (kernel module for RDMA)
