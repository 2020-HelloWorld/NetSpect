# client.py
import time

SERVER_IP = '10.0.2.243'

import socket
import struct
from scapy.all import IP, ICMP, send

def file_to_bits(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        bits = ''.join(format(byte, '08b') for byte in content)
    return bits

def send_packet(bit, ttl, dest_ip=SERVER_IP):
    ip_packet = IP(dst=dest_ip, ttl=ttl)
    icmp_packet = ICMP(type=8)  # ICMP Echo Request
    #icmp_packet.load = len(bits)

    packet = ip_packet / icmp_packet
    send(packet, verbose=False)

def main():
    dest_ip=SERVER_IP
    filename = 'msg.txt'  # Change this to the name of your file
    bits = file_to_bits(filename)
    print(bits)
    
    
    ip_packet = IP(dst=dest_ip)
    icmp_packet = ICMP(type=8)  # ICMP Echo Request
    payload = "Start:" + str(len(bits))
    packet = ip_packet / icmp_packet/payload
    send(packet, verbose=False)
    
    

    for i,bit in enumerate(bits):
        print(i,bit)
    
        ttl = 50 if bit == '1' else 100
        time.sleep(0.1)
        send_packet(bit, ttl)

if __name__ == "__main__":
    main()

