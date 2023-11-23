import logging
from scapy.all import *

# Disable Scapy logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
conf.verb = 0


def tcpScan(ip, ports):
    results = []
    sourcePort = RandShort()

    p = IP(dst=ip) / TCP(sport=sourcePort, dport=ports, flags='S')

    answers, noResponse = sr(p, timeout=2, retry=1)

    for sent, received in answers:
        if received[TCP].flags == "SA":
            results.append(received[TCP].sport)

    sr(IP(dst=ip) / TCP(sport=sourcePort, dport=results, flags='AR'), timeout=1)

    return results


def portList():
    with open('ports.txt', 'r') as file:
        ports = file.readlines()[0].split(',')

    return list(map(int, ports))


def isHostUp(ip):
    icmp = IP(dst=ip) / ICMP()
    resp = sr1(icmp, timeout=0.5)
    if resp == None:
        return False
    else:
        return True
