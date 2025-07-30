# 📈 GPU Monitoring with Prometheus + NVIDIA DCGM Exporter (Docker, Script-Based)

---

## 🔍 What is Prometheus?

[Prometheus](https://prometheus.io) is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. It:

- Pulls metrics via HTTP (pull model)
- Stores time-series data
- Provides a powerful query language (PromQL)
- Is ideal for monitoring infrastructure, applications, and hardware (like GPUs)

---

## 🎯 Why Use Prometheus with DCGM?

[NVIDIA DCGM (Data Center GPU Manager)](https://developer.nvidia.com/dcgm) provides telemetry and health data for NVIDIA GPUs.

The **DCGM Exporter** converts DCGM metrics into **Prometheus-compatible format**, allowing you to:

- Monitor GPU temperature, utilization, memory usage, errors
- Visualize data with Grafana
- Set alerts (optional)

---

## 🧱 Architecture

```
+-------------------+      HTTP /metrics       +-------------------+
| DCGM Exporter     |  <--------------------   | Prometheus        |
| (runs on GPU host)|                          | (scrapes metrics) |
+-------------------+                          +-------------------+
```

---

## 🧰 Requirements

- NVIDIA GPU + Driver installed
- Docker
- NVIDIA Container Toolkit (`nvidia-smi` and `docker run --runtime=nvidia` must work)

---

## 🏗️ Setup: Prometheus + DCGM Exporter (No Docker Compose)

### 📁 Directory Structure

```
gpu-monitoring/
├── prometheus.yml
├── start-dcgm-exporter.sh
└── start-prometheus.sh
```

---

## 1️⃣ Create Custom Docker Network

```bash
docker network create gpu-net
```

---

## 2️⃣ `prometheus.yml`

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'dcgm-exporter'
    static_configs:
      - targets: ['dcgm-exporter:9400']
```

---

## 3️⃣ `start-dcgm-exporter.sh`

```bash
#!/bin/bash

docker run -d \
  --rm \
  --runtime=nvidia \
  --network=gpu-net \
  --name=dcgm-exporter \
  -e NVIDIA_VISIBLE_DEVICES=all \
  -p 9400:9400 \
  nvcr.io/nvidia/k8s/dcgm-exporter:3.1.8-3.1.5-ubuntu20.04
```

> ✅ Make executable:  
```bash
chmod +x start-dcgm-exporter.sh
```

---

## 4️⃣ `start-prometheus.sh`

```bash
#!/bin/bash

docker run -d \
  --rm \
  --network=gpu-net \
  --name=prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:latest \
  --config.file=/etc/prometheus/prometheus.yml
```

> ✅ Make executable:  
```bash
chmod +x start-prometheus.sh
```

---

## ▶️ 5️⃣ Start Containers

```bash
./start-dcgm-exporter.sh
./start-prometheus.sh
```

---

## ✅ 6️⃣ Verify

- Prometheus UI: [http://localhost:9090](http://localhost:9090)
- Query example:
  ```
  DCGM_FI_DEV_GPU_TEMP
  ```
- Exporter metrics: [http://localhost:9400/metrics](http://localhost:9400/metrics)

---

## 🛑 Stop Containers

```bash
docker stop prometheus dcgm-exporter
```

---

## 🧠 Common DCGM Metrics (Examples)

| Metric | Meaning |
|--------|---------|
| `DCGM_FI_DEV_GPU_TEMP` | GPU temperature (°C) |
| `DCGM_FI_DEV_GPU_UTIL` | GPU utilization (%) |
| `DCGM_FI_DEV_FB_USED`  | GPU memory used (bytes) |
| `DCGM_FI_DEV_POWER_USAGE` | Power usage (Watts) |

---

## 📌 Notes

- No alerts or Grafana in this setup — just raw metrics.
- You can easily extend this by adding Grafana and Alertmanager later.
- For GPU node clusters, run one exporter per node and scale Prometheus targets.

---

## 📬 Resources

- DCGM Exporter GitHub: [https://github.com/NVIDIA/dcgm-exporter](https://github.com/NVIDIA/dcgm-exporter)
- Prometheus Docs: [https://prometheus.io/docs/](https://prometheus.io/docs/)
- NVIDIA DCGM: [https://developer.nvidia.com/dcgm](https://developer.nvidia.com/dcgm)

---
