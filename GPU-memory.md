+---------------------+
|  Registers (Thread) |
+---------------------+
|  Shared Mem / L1    | <-- Per SM
+---------------------+
|       L2 Cache      | <-- Shared across all SMs
+---------------------+
|   Global Memory     | <-- GDDR6 / HBM
+---------------------+
|   Host Memory (CPU) | <-- Via PCIe / NVLink
+---------------------+