import scapy.all as scapy
import sys

file_path = sys.argv[1]
packets = scapy.rdpcap(file_path)