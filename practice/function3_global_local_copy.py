"""
# ---------------------------
# File           : function3_global_local_copy.py
# Created        : 11-10-2021 21:44
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
num = 3
inc_by = 2
def increase_value(original_value,increment_by):
    print("Inside Method")
    print("original value {0} id {1}".format(original_value,id(original_value)))
    print("Incremented by {0} id {1}".format(increment_by,id(increment_by)))
    original_value+=increment_by
    print("Updated version:original_value {0} (new)id {1}\n".format(original_value,id(original_value)))
if __name__ == "__main__":
    print("called in main")
    print("num {0} numid {1}".format(num,id(num)))
    print("incremented by {0} icremented by id {1}\n".format(inc_by,id(inc_by)))
    increase_value(num,inc_by)
    print("called in main after function")
    print("num {0} num id {1}".format(num,id(num)))
    print("incremented by {0} incremented by id {1}\n".format(inc_by,id(inc_by)))