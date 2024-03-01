import socket
import time
from scapy.all import *

def bit_to_str(bits):
    byte = int(''.join([str(bit) for bit in bits]), 2)  # convert bits to integer
    char = chr(byte)
    return char

# create a UDP socket and bind it to the specified address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 8080))
print("Server started. Listening on port", 8080)

prev = time.time()
l = []
p = 0

msg = ""
while True:
    # wait for incoming packets
    data,addr = sock.recvfrom(1024)  # receive up to 1024 bytes of data
    now = time.time()
    diff = now-prev
    #print(data)
    print("Received Normal data from:",addr)
    print("Covert bit received:",diff)
    if p==0:
        p = 1
    else:
        if diff<0.15:
            l.append(0)
        else:
            l.append(1)
    if len(l)==8:
        msg +=  bit_to_str(l)
        print("Covert Info:",msg)
        l = []
    prev = now