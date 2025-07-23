
# 🔧 Linux Control Groups (cgroups) – In-Depth Explanation

## 🧠 What are cgroups?

**Control Groups (cgroups)** are a **Linux kernel feature** that allows you to **group processes** and **control their access** to system resources.

> **Primary purpose**: Limit, prioritize, isolate, and account for resources like **CPU**, **memory**, **I/O**, and **network bandwidth**.

---

## 🏗️ cgroups Architecture

```
                        ┌────────────┐
                        │  Process A │
                        └────┬───────┘
                             │
                 ┌───────────▼────────────┐
                 │     cgroup Subsystem   │
                 │  (e.g., memory, cpu)   │
                 └──────┬───────┬─────────┘
                        │       │
         ┌──────────────▼──┐ ┌──▼─────────────┐
         │ memory subsystem│ │   cpu subsystem│
         └────────────────┘ └─────────────────┘
```

---

## 📦 Types of Resources Managed by cgroups

| Subsystem (Controller) | Purpose |
|------------------------|---------|
| `cpu`                  | Limits CPU time usage |
| `cpuacct`              | Tracks CPU usage |
| `cpuset`               | Assigns CPUs (cores) to groups |
| `memory`               | Limits memory usage and OOM control |
| `blkio`                | Throttles block I/O (disks) |
| `devices`              | Controls device access (e.g., `/dev`) |
| `freezer`              | Pauses/resumes process groups |
| `net_cls`, `net_prio`  | Manages network traffic and priorities |
| `pids`                 | Limits number of processes (fork bombs) |
| `rdma`                 | Limits use of RDMA resources |

---

## 🧩 How cgroups Work

1. **Hierarchy**  
   - Cgroups are organized in a **tree structure**.
   - Each node in the tree can have **resource limits** and **attached processes**.

2. **Processes**  
   - A process can belong to **multiple cgroups** (one per resource controller).

3. **Controllers**  
   - Each controller (e.g., memory, cpu) enforces limits on a per-cgroup basis.

---

## ⚙️ Example: Setting a Memory Limit

### 1. Create a new cgroup:
```bash
sudo mkdir /sys/fs/cgroup/memory/mygroup
```

### 2. Set memory limit:
```bash
echo $((128*1024*1024)) | sudo tee /sys/fs/cgroup/memory/mygroup/memory.limit_in_bytes
```

### 3. Add a process (e.g., PID 12345) to the group:
```bash
echo 12345 | sudo tee /sys/fs/cgroup/memory/mygroup/tasks
```

Now, process `12345` is **limited to 128MB RAM**.

---

## 🔄 Cgroup Versions

| Feature | cgroup v1 | cgroup v2 |
|--------|-----------|-----------|
| Controller isolation | Yes | Unified hierarchy |
| Simpler APIs | ❌ | ✅ |
| More predictable behavior | ❌ | ✅ |
| Used by systemd | Partial | Full support (modern distros) |

Most modern Linux systems (e.g., Ubuntu 22.04+, RHEL 8+) use **cgroup v2**.

---

## 📊 Real Use Cases

- **Docker & Podman**: Limits containers to avoid resource starvation.
- **Kubernetes**: Schedules Pods based on CPU/memory cgroup quotas.
- **CI/CD**: Isolate test runs using memory & CPU limits.
- **Multi-tenant Servers**: Fair share of resources.

---

## 🧠 Summary Table

| Term | Meaning |
|------|---------|
| **Controller** | Kernel module managing a resource type (e.g., `memory`, `cpu`) |
| **Hierarchy** | Tree of cgroups with associated resource limits |
| **Cgroup** | A group of processes with applied limits |
| **Subsystem** | Another name for controller in v1 |
| **v1/v2** | Two major versions of cgroup APIs |
