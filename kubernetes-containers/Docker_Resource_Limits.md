
# Docker Containers: Limiting CPU, Memory, and I/O Resources

This guide shows how to limit **CPU**, **Memory**, and **I/O** for Docker containers using command-line options backed by Linux cgroups.

---

## 🧠 1. Limit CPU

### a. Use Specific CPU Cores
```bash
docker run --cpuset-cpus="0,1" ubuntu sleep 1000
```

### b. Set CPU Shares (Relative Weight)
```bash
docker run --cpu-shares=512 ubuntu sleep 1000
```

### c. Limit CPU Quota (Precise Throttling)
```bash
# Use 50% of one CPU
docker run --cpu-quota=50000 --cpu-period=100000 ubuntu sleep 1000
```

---

## 💾 2. Limit Memory

### a. Max Memory Limit
```bash
docker run --memory=512m ubuntu sleep 1000
```

### b. Memory + Swap
```bash
docker run --memory=512m --memory-swap=1g ubuntu sleep 1000
```

---

## 💽 3. Limit Disk I/O

### a. Block IO Weight (Relative)
```bash
docker run --blkio-weight=300 ubuntu sleep 1000
```

### b. Limit Read/Write Throughput (bps)
```bash
docker run   --device-read-bps /dev/sda:1mb   --device-write-bps /dev/sda:1mb   ubuntu sleep 1000
```

### c. Limit Read/Write IOPS
```bash
docker run   --device-read-iops /dev/sda:100   --device-write-iops /dev/sda:100   ubuntu sleep 1000
```

---

## 🧪 Full Example: CPU + Memory + IO
```bash
docker run   --cpuset-cpus="0"   --cpu-quota=50000 --cpu-period=100000   --memory=512m --memory-swap=1g   --blkio-weight=500   --device-read-bps /dev/sda:1mb   --device-write-bps /dev/sda:1mb   ubuntu sleep 1000
```

---

## ✅ Summary Table

| Resource | Flag | Description |
|----------|------|-------------|
| CPU Core Binding | `--cpuset-cpus` | Bind container to specific cores |
| CPU Priority | `--cpu-shares` | Relative CPU weight |
| CPU Throttle | `--cpu-quota`/`--cpu-period` | Limit CPU execution time |
| Memory Limit | `--memory` | Max RAM container can use |
| Swap | `--memory-swap` | RAM + Swap usage |
| I/O Weight | `--blkio-weight` | Disk I/O scheduling weight |
| Read/Write BPS | `--device-read-bps`, `--device-write-bps` | Limit disk read/write rate |
| Read/Write IOPS | `--device-read-iops`, `--device-write-iops` | Limit disk IOPS |
