
# 🧠 GPU Architecture: Components and Functionality

## What is a GPU?
A **Graphics Processing Unit (GPU)** is a specialized processor designed for parallel computation, commonly used in graphics rendering and general-purpose compute tasks like AI, simulations, and video processing.

---

## 🧱 High-Level Architecture

```
+-----------------------------------------------------------+
|                   Graphics Processing Unit                |
|                                                           |
| +----------------+   +----------------+   +------------+  |
| | Command        |-->| Graphics/Comp. |-->| Shader     |--|
| | Processor      |   | Engine         |   | Cores (ALUs)|  |
| +----------------+   +----------------+   +------------+  |
|                                                           |
| +--------+   +--------+   +--------+                      |
| | L1/L2  |-->| Texture |-->| Raster  |                     |
| | Cache  |   | Units   |   | Engines |                     |
| +--------+   +--------+   +--------+                      |
|                                                           |
| +------------------------+                                |
| | Global Memory / VRAM   |                                |
| +------------------------+                                |
+-----------------------------------------------------------+
```

---

## 🧩 Components of a GPU

### 1. Streaming Multiprocessor (SM) / Compute Units
- Includes ALUs, registers, warp scheduler, and shared memory.
- Executes instructions in parallel via warps/wavefronts.

### 2. Shader Cores / ALUs
- Handle graphics and compute tasks.
- Use SIMD architecture for massive parallelism.

### 3. Texture Units
- Perform sampling, filtering, and coordinate mapping for images.

### 4. Raster Engine
- Converts triangles (vector data) into pixels.

### 5. Render Output Units (ROPs)
- Final stage of the graphics pipeline.
- Handles blending, depth testing, and writes pixels to the framebuffer.

### 6. Memory System
- **L1 Cache:** Closest, fastest.
- **L2 Cache:** Shared across SMs.
- **VRAM (GDDR6, HBM):** Main GPU memory.

### 7. Command Processor
- Receives and schedules commands from the CPU.

### 8. Graphics & Compute Engines
- **Graphics Engine:** Handles shading stages.
- **Compute Engine:** Handles GPGPU tasks (e.g., CUDA, ML).

### 9. Warp Scheduler
- Determines which threads (warps) to execute next.

### 10. Display Engine
- Interfaces with monitor; manages frame output and resolutions.

---

## 🔁 GPU Rendering Pipeline

1. CPU sends commands.
2. GPU processes vertices.
3. Tessellation and geometry shading.
4. Rasterization.
5. Fragment shading.
6. Blending and depth testing.
7. Final frame sent to display.

---

## 🧠 GPGPU and Compute Frameworks

- **NVIDIA CUDA**
- **AMD ROCm / HIP**
- **OpenCL**
- **Vulkan Compute**
- **DirectCompute**

---

## CPU vs GPU Architecture

| Feature           | CPU                  | GPU                          |
|------------------|-----------------------|-------------------------------|
| Cores            | Few                   | Thousands                    |
| Threads          | Tens                  | Tens of thousands            |
| Task Type        | Serial                | Massively parallel           |
| Use Cases        | Logic, OS, Control    | Graphics, ML, Simulations    |




