import scapy.all as scapy
import sys


class Message:
    def __init__(self, message):
        self._src_ip = message['IP'].src
        self._message = message

    def ttl_check(self):
        if self._message['IP'].ttl == 64:
            return 0
        elif self._message['IP'].ttl == 128:
            return 1

    def window_size_check(self):
        if self._message['TCP'].window == 256:
            return 1

    def tcp_options_check(self):
        if len(self._message['TCP'].options) > 0:
            return 0

    def http_agent_check(self):
        print self._message['Raw']

    def to_string(self):
        if self.ttl_check() == 0 and self.tcp_options_check() == 0:
            return 'IP (TTL), ' + self._src_ip + ', Linux\n\n' + 'TCP (OPTIONS), ' + self._src_ip + ', Linux\n\n'
        elif self.ttl_check() == 1 and self.window_size_check() == 1:
            return 'IP (TTL), ' + self._src_ip + ', Windows\n\n' + 'TCP (OPTIONS), ' + self._src_ip + ', Windows\n\n'


def filter_message(message):
    if message['Ethernet'].type == 2048:
        if message['IP'].proto == 6:
            if message['TCP'].dport == 80:
                return True


input_type = sys.argv[1]
packets = []
filtered_list = []
result = set()
if input_type == '-f':
    path = sys.argv[2]
    packets = scapy.rdpcap(path)
elif input_type == '-s':
    packets = scapy.sniff

for packet in packets:
    if filter_message(packet):
        filtered_list.append(packet)
for packet in filtered_list:
    p = Message(packet)
    if p.to_string():
        result.add(p.to_string())
for res in result:
    print res