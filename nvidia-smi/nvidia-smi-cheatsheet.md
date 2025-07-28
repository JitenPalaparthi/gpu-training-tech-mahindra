
# NVIDIA-SMI Command Cheat Sheet

## 🧩 Basic Commands

```bash
nvidia-smi
```
- Shows general GPU information (usage, processes, memory, temperature, etc.)

```bash
nvidia-smi -L
```
- Lists all available GPUs.

```bash
nvidia-smi --help
```
- Shows help and usage instructions.

---

## 🧠 Monitoring and Status

```bash
nvidia-smi dmon
```
- Live monitoring of GPU metrics (memory, power, temp, SM usage)

```bash
nvidia-smi --query-gpu=utilization.gpu,memory.total,memory.used,temperature.gpu --format=csv
```
- Custom GPU status query.

```bash
watch -n 1 nvidia-smi
```
- Continuously monitor GPU usage every 1 second.

---

## 🚦 Process and Application Management

```bash
nvidia-smi pmon -i 0
```
- Monitor processes running on GPU 0.

```bash
nvidia-smi topo -m
```
- Show topology between GPUs and CPUs (especially useful for multi-GPU setups).

```bash
nvidia-smi --gpu-reset -i 0
```
- Reset GPU 0 (requires root and no processes using it).

---

## 🔐 Persistence Mode

```bash
nvidia-smi -pm 1
```
- Enable persistence mode (keep GPU initialized).

```bash
nvidia-smi -pm 0
```
- Disable persistence mode.

---

## All queries 

```bash
nvidia-smi --help-query-gpu
```

## 🧪 ECC and Error Reporting

```bash
nvidia-smi --query-gpu=ecc.errors.uncorrected.total,ecc.mode.current --format=csv
```
- Display ECC error counts and mode.

```bash
nvidia-smi --query-gpu=temperature.gpu,fan.speed --format=csv
```
- Show temperature and fan speed.

---

## ⚙️ Power and Clock Management

```bash
nvidia-smi -pl 100
```
- Set GPU power limit to 100W.

```bash
nvidia-smi --query-gpu=power.draw,power.limit --format=csv
```
- View current power usage and limit.

```bash
nvidia-smi --query-gpu=clocks.gr,clocks.sm,clocks.mem --format=csv
```
- Show clock speeds.

---

## 🧩 MIG (Multi-Instance GPU) — Ampere Only

```bash
nvidia-smi -i 0 -mig 1
```
- Enable MIG mode on GPU 0.

```bash
nvidia-smi mig -i 0 -cgi 1g.5gb
```
- Create a MIG GPU instance of type 1g.5gb on GPU 0.

```bash
nvidia-smi mig -dci --gi 0 --ci 0
```
- Delete compute instance 0 from GPU instance 0.

---

## 📤 Logging and Output

```bash
nvidia-smi --log-file nvidia_output.txt
```
- Save output to a log file.

```bash
nvidia-smi --format=csv --query-gpu=timestamp,name,utilization.gpu,temperature.gpu
```
- Export GPU stats in CSV format.

---

## 📚 Extra Tips

- You can use `nvidia-smi -i 0` to target GPU 0 specifically.
- `nvidia-smi` is available in all CUDA-enabled environments and drivers.
- For advanced real-time tracking, consider `DCGM`, `nvtop`, or Python bindings.

---
