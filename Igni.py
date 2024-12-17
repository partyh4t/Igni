# Igni

'''
This is my attempt at creating an automated pen-testing solution to assist penetration testers in automating the same old tasks
you'd typically run on most targets.
'''

# TODO:
    # Add logging functionality
    # Create a folder somewhere (likely in /tmp), to store all the files, logs, cmd output, etc

import PortScanner

target = input("Enter your target here: ")

targ1 = PortScanner(target)
targ1.scan_ports()