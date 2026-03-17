# 📡 DDoS Attack Simulation and Analysis Using Python & Wireshark
---

## 1. Title
**Simulation and Forensic Analysis of SYN Flood and UDP Flood DDoS Attacks Using Python and Wireshark**

## 2. Aim
To simulate SYN Flood and UDP Flood DDoS attacks using Python (Scapy) on localhost, capture the network traffic using Wireshark, and analyze the packet patterns to identify attack signatures and understand network vulnerabilities.

## 3. Objectives

| # | Objective | Status |
|---|-----------|--------|
| 1 | Understand the theoretical concepts of DDoS attacks | ✅ Completed |
| 2 | Write Python script for SYN Flood attack using Scapy | ✅ Completed |
| 3 | Write Python script for UDP Flood attack using Scapy | ✅ Completed |
| 4 | Capture normal baseline traffic using Wireshark | ✅ Completed |
| 5 | Capture SYN flood traffic during attack | ✅ Completed |
| 6 | Capture UDP flood traffic during attack | ✅ Completed |
| 7 | Analyze packet patterns and identify attack signatures | ✅ Completed |
| 8 | Compare normal vs attack traffic behavior | ✅ Completed |

## 4. Tools and Technologies

| Tool | Version | Purpose | Installation Command |
|------|---------|---------|----------------------|
| **Windows 11** | 23H2 | Operating System | Pre-installed |
| **Python** | 3.7+ | Script development | python.org |
| **Scapy** | Latest | Packet crafting | `pip install scapy` |
| **Wireshark** | 4.x | Packet capture & analysis | wireshark.org |
| **Npcap** | 1.86+ | Packet capture driver | npcap.com |
| **PowerShell** | Any | Command execution | Built-in |
| **GitHub** | - | Version control | github.com |


## 5. Project Structure

```text
DDoS-Assignment/
│
├── README.md            # Complete project documentation
├── attack1_syn.py       # SYN flood attack script
├── attack2_udp.py       # UDP flood attack script
├── baseline.pcapng      # Normal traffic capture (20 sec)
├── syn_flood.pcapng     # SYN flood attack capture (20 sec)
├── udp_flood.pcapng     # UDP flood attack capture (20 sec)
├── 1_normal.png         # Screenshot - Normal traffic
```



## 6. File Descriptions

### Python Scripts

#### `attack1_syn.py` - SYN Flood Attack Script
- **Purpose:** Generates TCP SYN packets with spoofed source IPs  
- **Target:** 127.0.0.1:80  
- **Duration:** 20 seconds  
- **Threads:** 2  
- **Rate Limiting:** 5ms delay between packets  

#### `attack2_udp.py` - UDP Flood Attack Script
- **Purpose:** Generates UDP packets with random payloads  
- **Target:** 127.0.0.1:53  
- **Duration:** 20 seconds  
- **Threads:** 2  
- **Payload Size:** 100–500 bytes random data  


## 7. Experiment Procedure

### Phase 1: Baseline Traffic Capture

1. Open Wireshark
2. Select "Adapter for loopback traffic capture"
3. Apply filter: ip.addr == 127.0.0.1
4. Start capture
5. Wait 20 seconds
6. Stop capture
7. Save as baseline.pcapng

### Phase 2: SYN Flood Attack
```text
cd Desktop\DDoS_Assignment
python attack1_syn.py
```

Wireshark filter:
```text
tcp.port == 80
```
Phase 3: UDP Flood Attack
```text
python attack2_udp.py
```
Wireshark filter:
```text
udp.port == 53
```

## 8. Wireshark Analysis
Normal Traffic

Filter used:
```text
ip.addr == 127.0.0.1
```
| Parameter   | Observation          |
| ----------- | -------------------- |
| Packet Rate | Low                  |
| Protocols   | TCP, TLS             |
| Pattern     | Normal communication |

SYN Flood

Filter used:
```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```
| Parameter   | Observation |
| ----------- | ----------- |
| Packet Rate | Very High   |
| Source IP   | Random      |
| TCP Flags   | SYN only    |

UDP Flood

Filter used:
```text
udp.port == 53
```
| Parameter   | Observation                  |
| ----------- | ---------------------------- |
| Packet Rate | High                         |
| Payload     | Random                       |
| Response    | ICMP Destination Unreachable |

### 9. Results

| Metric        | SYN Flood | UDP Flood |
| ------------- | --------- | --------- |
| Total Packets | 4343      | 4185      |
| Duration      | 20 sec    | 20 sec    |
| Packet Rate   | 217/sec   | 209/sec   |

### 10. Attack Comparison

| Feature       | SYN Flood         | UDP Flood            |
| ------------- | ----------------- | -------------------- |
| Protocol      | TCP               | UDP                  |
| Attack Method | Exploit handshake | Bandwidth exhaustion |
| Detection     | SYN packets       | UDP traffic spike    |

### 11. Challenges Faced
| Problem                     | Solution                          |
| --------------------------- | --------------------------------- |
| Wireshark showing 0 packets | Corrected filter                  |
| Npcap loopback issue        | Reinstalled with loopback support |
| System slowdown             | Reduced threads                   |

### 12. Disclaimer

⚠️ Educational Use Only

All experiments were performed on localhost (127.0.0.1) for academic learning purposes only.
Unauthorized DDoS attacks are illegal under:
India IT Act 2000 (Section 66)
