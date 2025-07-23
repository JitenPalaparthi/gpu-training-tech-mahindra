
# 🐳 Docker / Container Architecture – Complete Overview

## 🚀 What is Docker?
Docker is a **containerization platform** that lets you package an application and its dependencies into a **single unit (container)** that can run anywhere.

---

## 🧱 Core Components of Docker

| Component      | Description |
|----------------|-------------|
| **Docker Engine** | Core client-server tech. Runs and manages containers. |
| **Docker Daemon (`dockerd`)** | Runs as background service. Handles images, containers, volumes, and networks. |
| **Docker CLI** | Command-line tool to interact with Docker daemon. |
| **Docker Image** | Read-only template (base OS + app + dependencies). |
| **Docker Container** | A running instance of an image — isolated process on the host. |
| **Dockerfile** | Script with instructions to build Docker images. |
| **Docker Hub** | Cloud-based registry for storing and sharing Docker images. |

---

## 🏗️ How Docker Works Internally

Docker leverages Linux kernel features:

### 🔒 1. Namespaces (Isolation)

Namespaces provide **isolated views** of system resources:

| Namespace Type | Isolates |
|----------------|----------|
| `pid`          | Process IDs |
| `net`          | Network interfaces |
| `mnt`          | Mount points / filesystem |
| `uts`          | Hostname and domain name |
| `ipc`          | Interprocess communication |
| `user`         | User IDs and group IDs |

✅ This ensures each container has its **own private environment**.

### ⚖️ 2. cgroups (Control Groups) – Resource Management

Control Groups **limit and monitor** the resource usage (CPU, memory, I/O) of containers.

#### Example uses:
- Max memory a container can use
- Limit CPU shares or cores
- Throttle disk I/O

> 📦 cgroups = Linux kernel feature that enforces resource boundaries on containers.

### 🔒 3. Union File Systems (Storage)

Docker uses **UnionFS** (OverlayFS, AUFS) for **layered file systems**:

- Each image layer (OS, packages, app code) is a **separate immutable layer**.
- Containers add a **read-write layer** on top.

> 🧩 This makes Docker images **lightweight and fast to build or ship**.

### 🌐 4. Networking (Bridge, Host, Overlay)

Docker containers use virtual networks:

| Network Mode | Description |
|--------------|-------------|
| **Bridge**   | Default. Each container gets its own IP. |
| **Host**     | Shares host network stack. |
| **Overlay**  | Multi-host networking using Swarm or Kubernetes. |

---

## 🛠️ Container Lifecycle (Simplified)

```
docker run ubuntu echo "Hello"
```

Breakdown:
1. **Image Lookup**
2. **Image Download**
3. **Container Creation**
4. **Filesystem Layer Setup**
5. **Execution**

---

## 📊 Visual Diagram

```
+---------------------+
|  Docker CLI         |
+---------+-----------+
          |
+---------v-----------+       +----------------------+
|   Docker Daemon     |<----->| Docker Registry      |
+---------+-----------+       +----------------------+
          |
+---------v---------------------+
|      Container Runtime (runc) |
+---------+---------------------+
          |
     [Linux Kernel]
     +-------------------------------+
     | Namespaces  | cgroups         |
     | (net, pid,  | (CPU, mem, IO)  |
     |  mnt, etc)  |                 |
     +-------------+----------------+
```

---

## 🧠 Summary Table

| Feature        | Purpose                            |
|----------------|-------------------------------------|
| **Namespaces** | Isolation of processes, networks, etc. |
| **cgroups**    | Resource control (CPU, memory)     |
| **UnionFS**    | Layered file systems for images    |
| **Docker Daemon** | Orchestrates container operations |
| **runc**       | Low-level tool to start containers |

---

## ✅ Real-world Use Cases

- **Dev/Test Environments**
- **CI/CD Pipelines**
- **Microservices**
- **GPU Workloads (with nvidia-docker)**
