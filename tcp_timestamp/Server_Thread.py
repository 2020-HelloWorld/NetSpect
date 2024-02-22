from scapy.all import *

# Define server address and port
SERVER_HOST = '0.0.0.0' #<Interface IP>
SERVER_PORT = 1234

# Define a function to handle incoming packets
n = []
i=0

def handle_packet1(packet):
	if ICMP in packet and packet.payload:
		#global n
		n.append(int(packet.payload.load))
		print("Incoming data len:", n)


startf=[0]
def handle_3way(packet):
    if packet[TCP].flags=="S":
            syn_ack_pkt = IP(dst=packet[IP].src)/TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags="SA", chksum=0,seq=0, ack=packet[TCP].seq + 1)
            send(syn_ack_pkt)
    elif packet[TCP].flags=="A":
          startf[0]=1
          
sniff(filter='(tcp dst port 1234)', prn=handle_3way,stop_filter=lambda p: startf[0])
            



bits=[]


sniff(filter='icmp', prn=handle_packet1,count=1)
print("Waiting for",n[0],"packets")



    
def handle_packet(packet):

    # Check if TCP Timestamp option is present
    if TCP in packet and packet[TCP].options:
        tcp_fields = packet[TCP].fields
        for option in tcp_fields['options']:
            if option[0] == 'Timestamp':
                timestamp_value = option[1]
                print("TCP Timestamp:", timestamp_value)
                bits.append(str(timestamp_value[0]%2))
                print("Bits Received",len(bits))
                reply_pkt = IP(dst=packet[IP].src)/TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags="A", chksum=0,seq=packet[TCP].ack, ack=packet[TCP].seq + 1)
                send(reply_pkt)

# Start sniffing for incoming packets
sniff(filter='(tcp dst port 1234)', prn=handle_packet,count=n[0])



startf=[0]
def handle_3wayFin(packet):
    if packet[TCP].flags=="FA":
            syn_ack_pkt = IP(dst=packet[IP].src)/TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags="A", chksum=0,seq=packet[TCP].ack, ack=packet[TCP].seq + 1)
            send(syn_ack_pkt)
            syn_ack_pkt = IP(dst=packet[IP].src)/TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags="RA", chksum=0,seq=packet[TCP].ack, ack=packet[TCP].seq + 1)
            send(syn_ack_pkt)
            startf[0]=1
          
sniff(filter='(tcp dst port 1234)', prn=handle_3wayFin,stop_filter=lambda p: startf[0])


#Create Bitstring
bitstring="".join(bits)
num = int(bitstring, 2)

# calculate the number of bytes needed to represent the integer
num_bytes = (len(bitstring) + 7) // 8

# convert the integer to bytes
bytes_data = num.to_bytes(num_bytes, byteorder='big')


#Write to file
f=open("msg.txt","w")
f.write(bytes_data.decode('utf-8'))



