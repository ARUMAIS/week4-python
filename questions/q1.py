"""
# ---------------------------
# File           : q1.py
# Created        : 14-10-2021 20:00
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
import platform
import os

def print_config_details():
    print("Platform processor:", platform.processor())
    print("Machine type:", platform.machine())
    print("Network name:", platform.node())
    print("Operating system:", platform.system())
    print("Platform architecture:", platform.architecture())
    print("PATH value:", os.environ['PATH'])
if __name__ == "__main__":
    print_config_details()
