
# PCIe vs NVLink – GPU Interconnects Explained

This document explains the difference between PCIe and NVLink, focusing on their hardware structure, protocols, and how they operate in GPU systems.

---

## 🔍 Are PCIe and NVLink Hardware or Software?

| Feature      | PCIe                          | NVLink                          |
|--------------|-------------------------------|----------------------------------|
| Type         | **Hardware + protocol stack** | **Hardware + protocol stack**    |
| Exists on    | CPU, GPU, motherboard         | NVIDIA GPUs (e.g., A100, H100)   |
| Interface    | **Physical lanes**            | **Custom physical bridges**      |
| Protocol     | Standardized packet protocol  | NVIDIA proprietary protocol      |
| Driver/Stack | OS and NVIDIA drivers         | NVIDIA driver + CUDA stack       |

---

## 🔌 What Do They Look Like?

### PCIe
- Edge connector on GPU (gold fingers)
- Plugs into PCIe slot on motherboard
- Uses lanes (x1, x4, x8, x16)

### NVLink
- Bridge-style connector between GPUs (SXM module or bridge connector)
- Appears as a physical bridge enabling high-speed GPU-to-GPU communication

---

## 📡 Protocols Used

| Feature           | PCIe                              | NVLink                                  |
|------------------|-----------------------------------|------------------------------------------|
| Physical Layer    | Differential signaling over copper | Proprietary NVIDIA signaling              |
| Data Link Layer   | CRC, Flow control, ACK/NACK       | Similar mechanisms with improved encoding |
| Protocol Layer    | PCIe TLP (Transaction Layer Packet) | NVIDIA's NVLink protocol stack           |
| Bandwidth         | PCIe Gen4 x16 ≈ 32 GB/s (bi-dir)  | NVLink v3 ≈ 100–150 GB/s (bi-dir per link) |
| Latency           | Higher                            | Lower                                     |
| Scalability       | Single root / hierarchical        | Peer-to-peer GPU fabric                   |

---

## 🎯 Use Cases

| Use Case                            | PCIe                        | NVLink                             |
|-------------------------------------|-----------------------------|-------------------------------------|
| GPU ↔ CPU Communication             | ✅ Yes                       | ✅ Yes (in SXM-based GPUs)          |
| GPU ↔ GPU (peer-to-peer)            | ⚠️ Possible, but slower      | ✅ Ultra-fast direct GPU-GPU comm   |
| Data Center Server Interconnect     | ✅ Widely supported           | ✅ High-end multi-GPU systems only  |
| Protocol Standardization            | ✅ Industry-wide standard     | ❌ NVIDIA proprietary               |

---

## 🧠 Real-World Analogy

- **PCIe**: Like a **highway** connecting various devices — general-purpose, with traffic rules and sharing.
- **NVLink**: Like a **dedicated high-speed rail** — fewer stops, optimized for GPU-to-GPU travel.

---

## 📚 Additional Notes

- PCIe slots are visible on any motherboard; GPUs with gold-finger connectors plug directly into these.
- NVLink bridges are seen on high-end GPUs like A100 or H100, and require special motherboards (e.g., SXM modules).
- NVLink is critical for massive parallel GPU workloads such as AI model training, where GPU-to-GPU communication is a bottleneck.
