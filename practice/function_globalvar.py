"""
# ---------------------------
# File           : function_globalvar.py
# Created        : 11-10-2021 21:45
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
def overloading_sample(num_1,num_2=10):
    global total
    total = num_1+num_2
    print("inside fn total is {}".format(total))
    return
total = 0
if __name__ =="__main__":
 overloading_sample(99,1000)
 overloading_sample(50)
 print("in main,total is : {}".format(total))