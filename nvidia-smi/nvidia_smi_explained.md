
# NVIDIA-SMI Output Explained

## 🧾 Header
```
NVIDIA-SMI 550.54.15    Driver Version: 550.54.15    CUDA Version: 12.4
```

| Field              | Description                                                             |
|--------------------|-------------------------------------------------------------------------|
| `NVIDIA-SMI`       | Version of the `nvidia-smi` CLI tool.                                   |
| `Driver Version`   | Version of the installed NVIDIA driver.                                 |
| `CUDA Version`     | Highest version of CUDA supported by the driver.                        |

---

## 🧠 GPU Details Block

### Device Identification
| Field                | Explanation |
|----------------------|-------------|
| `GPU`                | GPU index (starts from 0). |
| `Name`               | Name of the GPU (e.g., Tesla T4). |
| `Persistence-M`      | `On/Off`. If **On**, the GPU stays initialized between runs (useful for performance). |
> ✅ **Enable with:** `nvidia-smi -pm 1`

### Hardware and Display
| Field          | Explanation |
|----------------|-------------|
| `Bus-Id`       | PCIe Bus ID. Format: `domain:bus:device.function`. |
| `Disp.A`       | Display Active. If `Off`, this GPU isn't handling a monitor. Mostly `Off` on servers. |
| `Volatile Uncorr. ECC` | Unrecoverable memory errors detected during run time. (0 = good). |

> ECC is **Error Correction Code** for memory. Useful in data centers for preventing crashes due to memory errors.

### Environment & Utilization
| Field                  | Description |
|------------------------|-------------|
| `Fan`                  | Fan speed in %. `N/A` for GPUs without fans (like Tesla T4). |
| `Temp`                 | GPU temperature in °C. **Typical range: 30°C - 85°C**. |
| `Perf`                 | Performance state (`P0` = max, `P8` = idle). |
| `Pwr:Usage/Cap`        | Power draw vs. rated capacity. Example: `10W / 70W`. |

> ⚠️ **GPU Temp Thresholds:**
> - **< 30°C**: Idle
> - **30–70°C**: Normal operating range
> - **> 85°C**: High; may throttle
> - **> 95°C**: Dangerous

### Memory & GPU Load
| Field             | Description |
|-------------------|-------------|
| `Memory-Usage`    | Used vs Total GPU memory. E.g., `0MiB / 15360MiB`. |
| `GPU-Util`        | Percent of active SM cores. |
| `Compute M.`      | Compute mode (Default / Exclusive etc.) |

> `GPU-Util = 0%` means the GPU is idle. High values indicate active workload.

### MIG Mode
| Field    | Explanation |
|----------|-------------|
| `MIG M.` | MIG Mode status. Only supported on A100, A30, etc. Not Tesla T4. `N/A` = Not supported. |
> **MIG = Multi-Instance GPU** – partitions a single GPU into smaller logical GPUs for workload isolation.

---

## 📦 Processes Block
| Field           | Description |
|------------------|-------------|
| `GPU`            | GPU ID |
| `PID`            | Process ID |
| `Type`           | C (Compute) / G (Graphics) |
| `Process name`   | Name of the process (Python, TensorFlow, etc.) |
| `GPU Memory`     | Memory used by that process |

---

## 🚦 Performance States (`Perf`)
| Perf State | Meaning             |
|------------|---------------------|
| `P0`       | Maximum performance |
| `P1`–`P7`  | Reduced performance |
| `P8`       | Lowest (idle)       |

> GPU automatically shifts between these based on load.

---

## 💥 ECC Errors
| Type        | Explanation |
|-------------|-------------|
| **Single-Bit** | Minor errors; corrected in hardware. |
| **Double-Bit** | Serious; may crash application. |

> ECC is mostly enabled in data center GPUs like T4, A100, etc.

---

## 🔢 Bus ID Format: `00000000:00:04.0`
| Component        | Meaning                    |
|------------------|----------------------------|
| `00000000`       | Domain (usually 0)         |
| `00:04`          | Bus:Device number          |
| `.0`             | Function number (if device supports multiple functions) |

---

## 📘 Summary Table

| Metric             | Normal Range / Value     |
|--------------------|--------------------------|
| Temp               | 30–85°C                  |
| Power Usage        | 10–70W for Tesla T4      |
| Memory Usage       | 0–15360 MiB              |
| GPU-Util           | 0–100%                   |
| Perf State         | P0 (max) to P8 (idle)    |
| ECC                | 0 errors preferred       |
