from scapy.all import *
import time
SERVER_IP = '192.168.250.204' #<Server IP>
SERVER_PORT = 1234
SOURCE_PORT=12346


def comm():
    syn = IP(dst=SERVER_IP)/TCP(dport=SERVER_PORT,sport=SOURCE_PORT, flags="S",chksum=0)

    syn_ack = sr1(syn)

    # Send ACK packet to complete the 3-way handshake
    ack = IP(dst=SERVER_IP)/TCP(dport=SERVER_PORT,sport=SOURCE_PORT, flags="A", ack=syn_ack.seq + 1,chksum=0,seq=1)
    send(ack)
    time.sleep(1)

    with open('tosend.txt', 'rb') as f:
        file_bytes = bytearray(f.read())
        bits = ''.join(format(byte, '08b') for byte in file_bytes)
        print(bits)
    n = len(bits)
    print(n)
    i = 1
    ip_packet = IP(dst=SERVER_IP)

# Create an ICMP packet with payload "10"
    icmp_packet = ICMP() / str(n)

    # Combine the IP and ICMP packets
    packet = ip_packet / icmp_packet

    # Send the packet
    k=[sr1(packet)]
    
    while i-1 < n:
        #print("Trying bit number:", i)
        # print(bits[i])
        t = int(time.time())
        
        if t % 2 == int(bits[i-1]):
            # print("hi")
            pkt = IP(dst=SERVER_IP) / \
                TCP(sport=SOURCE_PORT, dport=SERVER_PORT, seq=i,chksum=0,flags="PA",ack=1,
                    options=[('Timestamp', (t, 0))])/"0"
            i += 1
            k[0]=sr1(pkt)
    
    fin_pack=IP(dst=SERVER_IP) / \
                TCP(sport=SOURCE_PORT, dport=SERVER_PORT, seq=k[0].ack,chksum=0,flags="FA",ack=1)
    fin_ack=sr1(fin_pack)
    #ack=IP(dst=SERVER_IP) /TCP(sport=12345, dport=SERVER_PORT, seq=fin_ack[TCP].ack,chksum=0,flags="A",ack=fin_ack[TCP].seq+1)
    #send(ack)

    # Send the packet with timestamp option
comm()
