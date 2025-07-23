
# GPU Resource Management and cgroups

## ❓ Do cgroups manage GPUs directly?
No, Linux `cgroups` (v1 and v2) **do not natively support GPU resource management**. Unlike CPU or memory, the kernel lacks a built-in cgroup controller for GPU usage.

---

## ✅ How are GPU resources managed?

### 1. NVIDIA Container Toolkit (Docker)
- Uses `nvidia-container-runtime` to bind GPU devices to containers.
- Enables:
  - GPU assignment using `--gpus`
  - Environment-based visibility with `CUDA_VISIBLE_DEVICES`
  - Monitoring with `nvidia-smi`

**Example:**
```bash
docker run --gpus '"device=0,1"' nvidia/cuda:12.3-base nvidia-smi
```

---

### 2. Kubernetes (via Device Plugins)
- Uses the **NVIDIA Device Plugin** to expose GPUs to Pods.
- cgroups are used to group processes but **not** to limit GPU compute or memory.
- Allocation is done at device level (entire GPU or MIG instance).

---

### 3. NVIDIA cgroups Integration
- NVIDIA provides support for `nvidia-cgrouprc` for integrating device access with cgroups.
- This **restricts GPU access** to processes inside a specific cgroup but does not time-slice or limit compute.

---

## 🚫 What cgroups Cannot Do with GPUs

| Feature                      | Supported via cgroups? | Notes                          |
|-----------------------------|-------------------------|--------------------------------|
| GPU access isolation        | ✅                      | Uses device cgroups + runtime |
| GPU compute time control    | ❌                      | Not supported                  |
| GPU memory limitation       | ❌                      | App-level only                 |
| GPU scheduling              | ❌                      | Not cgroup-based               |
| GPU visibility restriction  | ✅                      | Via `CUDA_VISIBLE_DEVICES`    |

---

## 🔧 Tools & Technologies

- `nvidia-container-runtime`
- `nvidia-docker2`
- NVIDIA Kubernetes Device Plugin
- MIG (Multi-Instance GPU for A100/H100)

---

## ✅ Summary

| Use Case                    | Supported | Mechanism                            |
|----------------------------|-----------|--------------------------------------|
| Assign specific GPU        | ✅        | Docker/K8s with NVIDIA runtime       |
| Limit GPU memory or time   | ❌        | Not supported via cgroups            |
| Group GPU processes        | ✅        | Device cgroups with runtime          |
| Schedule GPU access        | ❌        | Not available                        |
