#!/usr/bin/python3

# Igni - My simple bugbounty enumeration script - by @partyh4t

"""
TODO: # Add output directory option and functionality, so that we can specify where to output the files, that way we dont have to worry about the script overwriting files if we run it on a different target domain - DONE
      # Add screenshot functionality, so that we can screenshot all live domains - DONE
      # Add function that will split any api's and normal domains apart, and store in seperate files, if an argument is passed.
"""

import subprocess
import argparse
import os

# Arg Parser Formatter (Mainly so that I can have a custom width for the help text and only metavar for long args)
class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=80)

    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ', '.join(action.option_strings) + ' ' + args_string

fmt = lambda prog: CustomHelpFormatter(prog)


# Parser Args and Variables
parser = argparse.ArgumentParser(description="Set your targets ablaze, with Igni.", formatter_class=fmt)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-d", "--domain", help="target domain", metavar="<domain>")
group.add_argument("-dL", "--domain-list", help="list of target domains", metavar="<domain_list>")
parser.add_argument("-o", "--output", help="output directory", metavar="<output_dir>")
parser.add_argument("-t", "--test", help="test", action="store_true")
parser.add_argument("-ss", "--screenshot", help="screenshot all live domains", action="store_true")
args = parser.parse_args()
RESET = "\033[0m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"

# Terminal ASCII Art
def print_banner():
    banner = f"""                                                                                                                                                                                                                                                                      
                  ++                 
               .**#*.                ____            _ 
              .*###*.               /  _/___ _____  (_)
             .*###+  ..             / // __ `/ __ \/ / 
            .*###=  .*#:          _/ // /_/ / / / / /  
           :*###=   *###:        /___/\__, /_/ /_/_/   
          :*###-    :####-           /____/           
         :*###-      :*###=   
        -###*:        .*###=.
       =####.          .*###+.
      =####.            .*###*.
     +###*.             ..+###*.
   .*####==================*####:.
  .*#############################:.
  ********************************:.

    """
    print(banner)


# main functions start here.
def get_subdomains(domain, output_dir):
        print(f"[{BLUE}INF{RESET}] Enumerating subdomains with {YELLOW}subfinder{RESET}")
        subprocess.run(f"subfinder -silent -d {domain} -all 2>&1 | anew {output_dir}/subdomains.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[{BLUE}INF{RESET}] Resolving domains with {YELLOW}dnsx{RESET}")
        subprocess.run(f"dnsx -silent -l {output_dir}/subdomains.txt | anew {output_dir}/resolved_domains.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[{BLUE}INF{RESET}] Checking for live domains with {YELLOW}httpx{RESET}")
        subprocess.run(f"httpx -silent -l {output_dir}/resolved_domains.txt > {output_dir}/live.tmp", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(f"cat {output_dir}/live.tmp | anew {output_dir}/live_domains.txt && rm {output_dir}/live.tmp" , shell=True)
        if args.screenshot:
            subprocess.run(f"gowitness scan file -f {output_dir}/live_domains.txt --write-db", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[{GREEN}INF{RESET}] Done!")   

def main():
    print_banner()
    if args.output:
        output_dir = os.path.expanduser(args.output)
        output_dir = os.path.abspath(output_dir)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    else:
        output_dir = os.getcwd()
    if args.test:
         print(f"test")
         return
    if args.domain_list:
        f = open(f"{args.domain_list}", "r")
        for i in f:
            get_subdomains(i, output_dir)
    else:
         get_subdomains(args.domain, output_dir)
          

main()
