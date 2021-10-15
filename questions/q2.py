"""
# ---------------------------
# File           : q2.py
# Created        : 14-10-2021 21:37
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
import base64
import timeit
def encrypt(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    print("Encoded: {}".format(base64_bytes))

if __name__ == "__main__":
    print(timeit.timeit("encrypt(message)", setup="from __main__ import encrypt; message='aishu'", number=1))
