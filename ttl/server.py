# server.py
import sys
startf=[0]
import socket
from scapy.all import *
msg=""
l=[]
def interpret_packets1(packet):
	global msg
	if IP in packet :
		ttl = packet[IP].ttl
		

		# Extract the payload from the ICMP packet
	       
		
		if packet[ICMP].type==8 and packet[IP].src!='10.0.0.243':
		  print(f"Received packet with TTL: {ttl}")
			# Interpret the payload and perform actions based on the bit
			#bit = int.from_bytes(payload, byteorder='big')
		  
		  bit=1 if ttl==50 else 0
		  msg+=str(bit)
		  print(msg)
		  print(len(msg))
		  if len(msg)==l[0]:
                   num = int(msg, 2)

                   num_bytes = (len(msg) + 7) // 8
                   bytes_data = num.to_bytes(num_bytes, byteorder='big')
                   f=open("msg.txt","w")
                   f.write(bytes_data.decode('utf-8'))
                   sys.exit(0)
		  
		  

def interpret_bits(packet):
    if IP in packet :
        ttl = packet[IP].ttl
        

        # Extract the payload from the ICMP packet
       
        
        if packet[ICMP].type==8 and packet[IP].src!='10.0.0.243':
          if Raw in packet:
          		payload = str(packet[Raw].load, 'utf-8')
          		print(payload)
          		l.append(int(payload.split(":")[1]))
          		print(l)
          		startf[0]=1
          		sniff(prn=interpret_packets1, filter='icmp', count=-1)
def main():

    # Sniff ICMP packets and call interpret_bits function for each packet
    sniff(prn=interpret_bits, filter='icmp', stop_filter=lambda p: startf[0])

if __name__ == "__main__":
    main()

