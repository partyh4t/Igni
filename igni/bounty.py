# Igni's Bounty Module

import subprocess

'''
What to add to this:
    - check my bug bounty section in notion.
    - need to research and figure out an actual workflow first and foremost.
        - to do that, i should try out various tools, figure out which works best, and slowly implement them into the script one by one.
        - can utilize multiple tools for a specific task if need be, simply by supplying cli arg for example.

    - Structural ideas:
        - can structure each major part of the process into a specific class. So subdomain enum, directory bruteforcing, exploitation automation, etc.
        
'''

class BountyEnum:
    def __init__(self, domain):
        self.domain = domain

    # this'll take a target domain preferably.
    def get_subdomains(self):
        subprocess.run(f"subfinder -d {self.domain} -all | anew all_domains.txt", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #subprocess.run(f"")
