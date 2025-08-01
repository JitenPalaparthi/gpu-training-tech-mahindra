
# NVIDIA RDMA-Based NICs vs InfiniBand

## 1. What Are NVIDIA RDMA-Based NICs?

NVIDIA (formerly Mellanox) provides RDMA-capable NICs designed for high-performance computing and GPU networking.

### Major RDMA-Capable NICs

| Product Line        | Protocols Supported        | RDMA Support Type |
|---------------------|----------------------------|-------------------|
| **ConnectX-4**      | Ethernet + InfiniBand      | RoCEv1/v2, IB     |
| **ConnectX-5**      | Ethernet + InfiniBand      | RoCEv1/v2, IB     |
| **ConnectX-6**      | Ethernet + InfiniBand      | RoCEv2, IB        |
| **ConnectX-7**      | Ethernet + InfiniBand      | RoCEv2, IB        |
| **BlueField DPUs**  | SmartNIC (with ARM cores)  | RoCEv2, IB        |

---

## 2. How NVIDIA RDMA NICs Work

- Offload RDMA logic to NIC hardware (RDMA + DMA engines).
- Direct GPU memory access via **GPU Direct RDMA**.
- Supported over **Ethernet (RoCEv2)** and **InfiniBand**.

### GPU Cluster Flow:

1. GPU sends RDMA command via PCIe to NIC.
2. NIC transmits over RoCE or InfiniBand.
3. Remote RNIC performs memory access (GPU or Host).

---

## 3. RDMA over RoCE vs InfiniBand

| Feature                    | **RoCE (RDMA over Converged Ethernet)** | **InfiniBand (IB)**                   |
|----------------------------|-----------------------------------------|----------------------------------------|
| Transport                  | Ethernet (Layer 2 or Layer 3)           | Native InfiniBand                      |
| IP-based                   | Yes (RoCEv2 is routable)                | No (uses its own network stack)        |
| Hardware Requirements      | Standard Ethernet + RDMA NICs           | Requires InfiniBand switches + NICs    |
| Latency                    | Low                                     | Very Low (10–50% lower than RoCE)      |
| Congestion Control         | Optional (needs ECN/DCQCN tuning)       | Built-in flow control and credit system|
| Network Stack              | Needs configuration (DCB, PFC)          | Specialized with lossless fabric       |
| Market Use Case            | Data centers, mixed environments        | HPC, AI supercomputers, research labs  |

> **Note:** ConnectX cards support both RoCE and IB depending on config.

---

## 4. Key Takeaways

- ConnectX NICs support **both RoCE and InfiniBand**.
- **RoCE** integrates with Ethernet; **InfiniBand** requires dedicated fabric.
- Both support **GPU Direct RDMA**.
- **InfiniBand** gives superior performance but at higher infra cost.
