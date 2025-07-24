
# 🐳 Docker Resource Limiting Commands for NGINX

This markdown document shows how to apply CPU, memory, and I/O (block device) limits to an NGINX Docker container.

---

## 🧠 1. CPU Limits

### ✅ Limit by CPU cores
```bash
docker run -d --name my-nginx --cpus="1.5" nginx
```
> Limits the container to use at most **1.5 CPU cores**.

---

### ✅ Pin to specific CPU cores (CPU affinity)
```bash
docker run -d --name my-nginx --cpuset-cpus="0,2" nginx
```
> Allows container to run **only on CPU 0 and 2**.

---

## 🧠 2. Memory Limits

### ✅ Set maximum memory usage
```bash
docker run -d --name my-nginx --memory="512m" nginx
```
> Limits container to **512 MB of RAM**.

---

### ✅ Set soft memory limit (reservation)
```bash
docker run -d --name my-nginx --memory-reservation="256m" nginx
```
> This is a **soft limit** — container is guaranteed 256 MB but can use more if available.

---

### ✅ Combine memory limit and reservation
```bash
docker run -d --name my-nginx --memory="512m" --memory-reservation="256m" nginx
```

---

## 🧠 3. Block I/O Limits

### ✅ Limit read/write rate per device
```bash
docker run -d --name my-nginx \
  --device-read-bps /dev/sda:1mb \
  --device-write-bps /dev/sda:1mb \
  nginx
```

---

### ✅ Limit read/write IOPS
```bash
docker run -d --name my-nginx \
  --device-read-iops /dev/sda:1000 \
  --device-write-iops /dev/sda:1000 \
  nginx
```

---

## 🧠 4. CPU Shares (Relative Weight)

### ✅ Set CPU shares (default = 1024)
```bash
docker run -d --name my-nginx --cpu-shares=512 nginx
```
> Lower value = lower priority under CPU contention.

---

## ✅ Full Example: All Limits Combined

```bash
docker run -d --name my-nginx \
  --cpus="1.0" \
  --memory="512m" \
  --device-read-bps /dev/sda:1mb \
  --device-write-bps /dev/sda:1mb \
  nginx
```

---
