
# Docker Resource Limits: CPU, Memory, and GPU

## 🧠 What Are Docker Resource Limits?

Docker containers by default can use all available system resources (CPU, RAM, GPU). But in production or shared environments, we set **resource limits** to ensure fair usage and isolation.

---

## 🚀 1. CPU Limits

### 🔹 `--cpus="N"`
- Restricts the **maximum number of CPU cores** the container can use.
- Accepts fractional values. For example:
  - `--cpus="1"` → up to 1 full core
  - `--cpus="0.5"` → up to 50% of one core

### 🔹 What Does `0.5` CPU Mean?
- It doesn't split a physical core.
- It uses **Linux CFS (Completely Fair Scheduler)** to limit time slice.
- Example:
  - `--cpus="0.5"` sets `--cpu-quota=50000` and `--cpu-period=100000`
  - Means: 50ms of execution per 100ms = 50% CPU usage.

### 🔹 `--cpu-shares=N`
- Sets **relative CPU weight**, not a hard limit.
- Used when multiple containers compete for CPU.

### 🔹 `--cpuset-cpus="0,1"`
- Restricts the container to run only on CPU cores 0 and 1.

---

## 🧠 2. Memory Limits

### 🔹 `--memory="X"`
- Sets a **hard RAM limit**.
- If the container exceeds it, it is **OOMKilled**.

### 🔹 `--memory-reservation="X"`
- A **soft limit**.
- Acts as a guaranteed baseline during memory pressure.

### 📐 Memory Calculation Example
If your app uses:
- Base: 300MB
- Peak: 450MB
- Buffer: 20%

Then use: `--memory="550m"`

---

## 🧠 3. I/O Limits

### 🔹 `--device-read-bps` / `--device-write-bps`
- Example:
```bash
docker run --device-read-bps /dev/sda:1mb nginx
```

---

## 🧠 4. GPU Limits (NVIDIA Runtime Required)

> Only available if using NVIDIA GPU and Docker + NVIDIA Container Toolkit

### 🔹 Use NVIDIA runtime:
```bash
docker run --gpus all nvidia/cuda:12.0-base nvidia-smi
```

### 🔹 Limit specific GPU access:
```bash
docker run --gpus '"device=0"' nvidia/cuda:12.0-base nvidia-smi
```

### 🔹 Limit number of GPUs:
```bash
docker run --gpus 2 nvidia/cuda:12.0-base nvidia-smi
```

### 🔹 Specify GPU capabilities:
```bash
docker run --gpus all,capabilities=compute,utility nvidia/cuda:12.0-base nvidia-smi
```

---

## 🧾 Summary Table

| Option               | Type       | Purpose                            |
|----------------------|------------|------------------------------------|
| `--cpus`             | CPU        | Limit number of CPU cores          |
| `--cpu-shares`       | CPU        | Relative CPU priority              |
| `--cpuset-cpus`      | CPU        | Restrict to specific cores         |
| `--memory`           | Memory     | Hard memory limit                  |
| `--memory-reservation`| Memory    | Soft memory request                |
| `--device-read-bps`  | I/O        | Throttle read speed from devices   |
| `--gpus`             | GPU        | Allocate GPU(s) to container       |

---

## 🧠 Final Notes

- CPU quotas are enforced using Linux cgroups.
- GPU support requires NVIDIA Container Toolkit and proper drivers.
- Always test limits in staging before production.

