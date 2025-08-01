# NetQ: Overview, Use Cases, and NVIDIA Integration

## 📌 What is NetQ?

**NetQ** is NVIDIA’s real-time network operations tool designed for monitoring, troubleshooting, and visibility into **Ethernet-based** and **Infiniband-based** networks — especially when using **NVIDIA Cumulus Linux** or **SONiC**-based switches.

It integrates with **NVIDIA switches** and telemetry sources to provide deep insights into:

- Switch and host configurations
- Network protocols (BGP, MLAG, EVPN, VXLAN)
- Events, alerts, and operational states
- Performance metrics and network health

---

## 🧠 Key Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 📶 Telemetry Collection     | Real-time streaming of switch state and events                             |
| 🧩 Protocol Monitoring       | BGP, MLAG, OSPF, VLANs, VXLAN, EVPN                                        |
| 🛠 Troubleshooting Tools     | Live trace, config diff, path tracing, failure alerts                      |
| ⏱ Time-Series Metrics       | Latency, packet drops, congestion stats over time                          |
| 📉 Health Score              | Node and network-level health based on thresholds                          |
| 🔧 Integration               | Works with Prometheus, Grafana, or NetQ GUI                                |

---

## 🖥 NetQ in NVIDIA AI/Networking Labs

- **NetQ runs on NVIDIA AIR** (AI Infrastructure Resource simulator) for testing and education
- Integrated with **Cumulus Linux** or **SONiC** running on switches
- Can also be run inside containers or VM-based labs

---

## 📦 NetQ Components

- `NetQ Agent` – Runs on the switch or host, collects data
- `NetQ Telemetry Server` – Receives, stores, and processes telemetry data
- `NetQ UI` – Dashboard for visualization
- `NetQ CLI` – Command-line tool for ops teams
- Optional: `Prometheus Exporter` for external observability tools

---

## 🔧 Example NetQ CLI Commands

```bash
# Check network-wide BGP status
netq show bgp

# Interface status across nodes
netq show interface all

# See changes in config
netq show config diff

# View historical state
netq trace <hostname>

# Check MLAG status
netq show mlag