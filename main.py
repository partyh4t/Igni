# Igni

'''
This is my attempt at creating an automated pen-testing solution to assist penetration testers in automating the same old tasks
you'd typically run on most targets.
'''

# TODO:
    # Add logging functionality
    # DONE - Create a folder somewhere (likely in /tmp), to store all the files, logs, cmd output, etc
    # Add argument parsing
    #

from igni.portscanner import PortScanner
from igni.smb import EnumSmb
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Set your target ablaze, with Igni.")
#group = parser.add_mutually_exclusive_group() - Useful if we want to have multiple conflicting args, eg if -v is issued, we wouldnt want -q (quiet) to be issued as well.
parser.add_argument("target", help="IP address of target machine.")
parser.add_argument("-v", '--verbose', help="Increase output verbosity.", action='store_true') #TODO: add code to increase verbosity (maybe have it print out tool output.)
parser.add_argument("-b", '--batch', help="Don't ask for user input, use default behavior.", action='store_true') #TODO: once script has alot of functionality in it, implement this to select default behavior. Optimally i'd want an interactive mode, maybe -i, and then if args are being passed from cli, then most will probably use --batch.
args = parser.parse_args()

folder_path = Path.home() / "igni_output" / args.target
folder_path.mkdir(parents=True, exist_ok=True)

def main():
    target = PortScanner(args.target)
    open_ports = target.scan_ports()

    for i in int(open_ports):
        if i == 445:
            print("SMB Open. Enumerating File Shares...")

        
main()

    
