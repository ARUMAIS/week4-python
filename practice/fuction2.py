"""
# ---------------------------
# File           : fuction2.py
# Created        : 11-10-2021 15:01
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
"""
 Prints a welcome message.
 Demonstrates passing a variable into a function
 Parameters:
 lnum LYIT lnumber of student
 Returns:
 none
 """
def l_num(l_num):
    print (f"Hi,{l_num}")
    return
def print_name(student_name):
 """
 Prints a welcome message.
 Parameters:
 student_name
 Returns:
 none
 """
 fname, lname = str(student_name).split(" ")
 print(f'Hi {fname} {lname}, welcome to LYIT!')
 return
if __name__ == '__main__':
 print_name('Ruth Lennon') # Call the print_name function
 # print_lnum is not called so do not print details
 l_num(1234)