
# Setting GPU Limits in Kubernetes

## ✅ Prerequisites

1. NVIDIA drivers must be installed on the host nodes.
2. Deploy the NVIDIA device plugin for Kubernetes:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.14.0/nvidia-device-plugin.yml
   ```

---

## 📄 Example: Pod with GPU Limits

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-pod
spec:
  containers:
  - name: cuda-container
    image: nvidia/cuda:12.2.0-base-ubuntu22.04
    resources:
      limits:
        nvidia.com/gpu: 1 # Request 1 GPU
    command: ["nvidia-smi"]
```

---

## 🔍 Notes

- `nvidia.com/gpu` is a **resource name** provided by the NVIDIA device plugin.
- Only `limits` can be used for GPU resources (not `requests`).
- **Fractional GPUs** (e.g., `0.5`) are not supported. Use whole numbers.
- Example: `limits: nvidia.com/gpu: 2` means the container gets 2 full GPUs.

---

## 🧪 Check GPU Availability

```bash
kubectl describe node <node-name> | grep -A5 "Allocatable"
```

Expected output:

```
nvidia.com/gpu: 4
```

---

## 🔗 Useful Links

- [NVIDIA Kubernetes Device Plugin GitHub](https://github.com/NVIDIA/k8s-device-plugin)
