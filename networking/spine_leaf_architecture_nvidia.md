
# Spine-Leaf Architecture with NVIDIA Switches

## 📚 Overview

Spine-leaf architecture is a two-layer network topology used in modern data centers to provide predictable latency, high bandwidth, and scalable infrastructure.

## 🕸️ Architecture Diagram

```
               +-------------------+      +-------------------+
               |    Spine Switch 1 |------|    Spine Switch 2 |
               +--------+----------+      +----------+--------+
                        |                          |
         +--------------+------------+ +-----------+------------+
         |                           | |                        |
+--------+--------+        +--------+--------+       +---------+--------+
|   Leaf Switch 1  |        |   Leaf Switch 2  |       |   Leaf Switch 3 |
+--------+--------+        +--------+--------+       +---------+--------+
         |                           |                         |
   +-----+-----+              +------+-----+             +-----+-----+
   |   Server 1  |            |   Server 2   |           |   Server 3 |
   +-------------+            +--------------+           +-------------+
```

- **Spine Switches**: Core layer with full-mesh connectivity to leafs
- **Leaf Switches**: Access layer connecting endpoints (servers, GPUs)
- **Non-blocking Fabric**: Every leaf is connected to every spine

---

## 🔌 NVIDIA Switches

| Switch Model       | Port Speed | Total Ports | Total Bandwidth | Latency      |
|--------------------|------------|-------------|------------------|--------------|
| NVIDIA SN4700      | 100 GbE    | 32 QSFP28   | 6.4 Tbps         | ~300 ns      |
| NVIDIA SN4600      | 200 GbE    | 32 QSFP56   | 12.8 Tbps        | ~300 ns      |
| NVIDIA SN3700      | 100 GbE    | 32 QSFP28   | 6.4 Tbps         | ~300 ns      |
| NVIDIA QM8790      | HDR 200    | 40 HDR      | 16 Tbps          | <90 ns (IB)  |

### 📶 Bandwidth Calculation Example

- 32 ports × 100 Gbps = 3.2 Tbps × 2 (full-duplex) = 6.4 Tbps

---

## 🧠 NVIDIA NetQ Monitoring (Optional)

NVIDIA NetQ helps monitor the fabric:

- Spine-leaf topology health
- Interface counters
- ECMP route monitoring
- GPU + NIC + Switch telemetry

---

## 🔄 Advantages

- Scalable and modular design
- Predictable latency
- Full bisection bandwidth

---

## 🧩 Additional Notes

- Spine-leaf often uses **ECMP** (Equal Cost MultiPath)
- Most modern topologies in NVIDIA AIR or DGX PODs are based on this
- Supports **RDMA** and **RoCEv2** over lossless Ethernet

