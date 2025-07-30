
# DCGM (Data Center GPU Manager) Commands – Local GPU Machine Usage

This document lists key `dcgmi` commands that can be run directly on a local NVIDIA GPU machine along with brief explanations.

---

## 1. View DCGM Version

```bash
dcgmi discovery -v
```
**Description**: Displays the version of the installed DCGM tools.

---

## 2. Discover Available GPUs

```bash
dcgmi discovery -l
```
**Description**: Lists all GPU devices available on the local system.

---

## 3. View Health of GPUs

```bash
dcgmi health -g 0
```
**Description**: Checks the health of GPU 0 (use different GPU IDs for others).

---

## 4. Enable Stats Collection

```bash
dcgmi stats -e
```
**Description**: Enables statistics collection on all local GPUs.

---

## 5. View Stats for a Specific GPU

```bash
dcgmi stats -i 0
```
**Description**: Shows GPU utilization, memory usage, etc., for GPU 0.

---

## 6. Create a GPU Group

```bash
dcgmi group -c mygroup -i 0,1
```
**Description**: Creates a group called `mygroup` including GPU IDs 0 and 1.

---

## 7. Run Diagnostics

```bash
dcgmi diag
```
**Description**: Runs built-in diagnostic tests on all GPUs.

---

## 8. List Groups

```bash
dcgmi group -l
```
**Description**: Lists all created groups on the local system.

---

## 9. Show Group Info

```bash
dcgmi group -i <group_id> -d
```
**Description**: Shows detailed information about the specified group.

---

## 10. Start Policy Manager

```bash
dcgmi policy -e
```
**Description**: Enables policy engine to start monitoring limits and thresholds.

---

## 11. View Active Policies

```bash
dcgmi policy -l
```
**Description**: Lists currently active policies.

---

## 12. Monitor Job Stats

```bash
dcgmi stats -jstart
```
**Description**: Starts job statistics collection.

---

## 13. Stop Job Monitoring

```bash
dcgmi stats -jstop
```
**Description**: Stops job statistics collection.

---

## 14. Reset Stats

```bash
dcgmi stats -r
```
**Description**: Resets all collected statistics.

---

## 15. Help

```bash
dcgmi --help
```
**Description**: Displays help for all available DCGM commands.

---

> 💡 Note: Always run these commands with appropriate permissions. Some may require `sudo`.
