# Igni's Port Scanning and Parsing

import subprocess
from pathlib import Path
from lxml import etree

class PortScanner:
    def __init__(self, target):
        self.target = target   # target ip address


    def scan_ports(self):
        output_path = Path.home() / "igni_output" / self.target / "nmap_scan"
        subprocess.run(["nmap", self.target, "-p-", "-sV", "-oX", (str(output_path) + ".xml"), "-oN", (str(output_path) + ".txt")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.parse_nmap_output(output_path)

    def parse_nmap_output(self, output_path):
        tree = etree.parse((str(output_path) + ".xml"))
        open_ports = tree.xpath("//port[state/@state='open']/@portid") # extracting open ports with xml.
        print(open_ports)

        




