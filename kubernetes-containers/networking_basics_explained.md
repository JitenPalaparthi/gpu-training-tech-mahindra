
# 🧠 Networking Concepts: Explained in Order

---

## 1. **IPAM (IP Address Management)**
- IPAM is a system used to **plan, track, and manage IP addresses** in a network.
- Central to managing:
  - IP addresses
  - Subnets
  - DHCP and DNS integration
- Helps avoid conflicts and ensures efficient IP allocation.

---

## 2. **DHCP (Dynamic Host Configuration Protocol)**

### DHCP Server:
- Assigns network configuration to clients dynamically.
- Parameters provided:
  - IP address
  - Subnet mask
  - Gateway (default route)
  - DNS server
  - Lease time

### DHCP Client:
- Sends a **DHCP Discover** broadcast to find a server.
- Receives configuration from DHCP Server via:
  - Offer
  - Request
  - Acknowledge

---

## 3. **IP Address**
- A unique address used to identify a device on the network.
- Types:
  - IPv4: e.g., 192.168.1.10
  - IPv6: e.g., fe80::1a2b:3c4d

---

## 4. **Subnet Mask**
- Used to divide an IP address into **network** and **host** portions.
- Example: 255.255.255.0

---

## 5. **Default Gateway**
- A router IP where packets are sent if the destination is **outside the local subnet**.
- Example:
  - IP: `192.168.1.1` is usually the default gateway in home networks.

---

## 6. **MAC Address (Media Access Control)**
- A unique identifier for a **network interface card (NIC)**.
- Format: `00:1A:2B:3C:4D:5E`
- Assigned at the hardware level; used at the **data link layer**.

---

## 7. **Default Route**
- The route that packets take when there is **no specific route** to a destination.
- Usually points to the **default gateway**.

---

## 8. **DNS Names (Domain Name System)**
- Translates human-readable domain names to IP addresses.
- Example:
  - `www.google.com` → `142.250.195.36`

---

## 9. **Routing Table**
- A set of rules used to determine where data is sent.
- Can be seen using:
```bash
netstat -rn
```

---

## 10. **Lease Time**
- Duration for which an IP address is assigned to a client by DHCP.
- After expiry, the IP is re-requested or reassigned.

---

## 11. **NAT (Network Address Translation)**
- Allows multiple devices to share a single public IP.
- Translates private IP addresses (e.g., `192.168.x.x`) to a public IP.

---

## 12. **ARP (Address Resolution Protocol)**
- Resolves IP address to MAC address within a local network.

---

## 🧾 Summary Table

| Concept         | Description                                           |
|------------------|-------------------------------------------------------|
| IPAM            | IP management system                                   |
| DHCP Server     | Assigns IP & config to clients                         |
| DHCP Client     | Requests IP & config from DHCP server                  |
| IP Address      | Device ID on the network                               |
| Subnet Mask     | Divides network & host part of IP                      |
| Gateway         | Routes traffic outside the local network               |
| MAC Address     | Hardware address of NIC                                |
| Default Route   | Fallback route for packets                             |
| DNS Names       | Domain name to IP address translation                  |
| Routing Table   | Maintains all routes in the system                     |
| Lease Time      | Duration of IP lease from DHCP                         |
| NAT             | Private to public IP translation                       |
| ARP             | Resolves IP to MAC in local LAN                        |

---
