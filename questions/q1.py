"""
# ---------------------------
# File           : q1.py
# Created        : 14-10-2021 20:00
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# System information
# using platform and os module
"""
import platform  #import the platform module
import os        #for the operating system

def print_config_details():
    '''
       Going to print the system configuration details
       Parameters:
       none
       Returns:
       none
    '''
    print("-" * 68)
    print("Platform processor:", platform.processor())
    print("Machine type:", platform.machine())
    print("Network name:", platform.node())
    print("Operating system:", platform.system())
    print("Platform architecture:", platform.architecture())
    print("PATH value:", os.environ['PATH'])
    print("-" * 68)
if __name__ == "__main__":
    print_config_details()
