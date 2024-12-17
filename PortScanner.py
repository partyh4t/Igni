# Igni's Port Scanning Class

import subprocess

class PortScanner:
    def __init__(self, target):
        self.target = target   # target ip address

    def scan_ports(self):
        subprocess.run(f"nmap {self.target} -oA /tmp/nmap_scan", shell=True, text=True)
    



