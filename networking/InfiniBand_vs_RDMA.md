
# InfiniBand vs RDMA

## ❓ Misconception Clarified
**InfiniBand is not faster than RDMA — it enables RDMA.**

RDMA (Remote Direct Memory Access) is a **technology**, while InfiniBand is a **transport protocol and hardware platform** that implements RDMA very efficiently.

---

## 📌 Definitions

| Term         | What it is             | Relationship              |
|--------------|------------------------|---------------------------|
| **RDMA**     | Technology/mechanism   | Used by InfiniBand (and also RoCE, iWARP) |
| **InfiniBand** | Transport protocol + hardware | Implements RDMA most efficiently |

---

## ✅ Why InfiniBand is Often “Faster” in Practice

| Reason | Explanation |
|--------|-------------|
| 🚀 **Lower latency** | InfiniBand is optimized for <2μs latency vs 10–20μs with RoCEv2 |
| 🛣️ **Lossless fabric** | Built-in congestion control, flow control, and lossless delivery |
| 🔌 **Hardware offloads** | Handles RDMA operations in the NIC without CPU |
| 🧠 **Direct GPU access** | Supports GPUDirect RDMA between GPUs across nodes |
| ⚙️ **Optimized protocol stack** | InfiniBand avoids TCP/IP overhead present in RoCE or iWARP |

---

## 🧪 Benchmark Comparison

| Metric | **InfiniBand (IB)** | **RoCEv2 (RDMA over Ethernet)** |
|--------|---------------------|----------------------------------|
| Latency | 1–2 microseconds | 5–20 microseconds |
| Bandwidth | 200–400 Gbps (HDR/NDR) | 100–200 Gbps |
| CPU usage | Very low | Higher (due to Ethernet stack) |
| Reliability | Very high | Can vary (depends on network tuning) |

---

## 🎯 TL;DR

- **RDMA** is the method.
- **InfiniBand** is a transport and hardware technology that **implements RDMA extremely efficiently**.
- InfiniBand is **often the fastest RDMA transport**, better than Ethernet-based options.

