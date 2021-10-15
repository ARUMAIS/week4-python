"""
# ---------------------------
# File           : q3.py
# Created        : 14-10-2021 22:08
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""

def add_course_details:
    while 1:
        Enter course name (press q to exit):
            course_name
        Enter course code (press q to exit):
            couse_code
    course_dict = {"Msc in DevOps": ('IT902'), "Msc in Cloud Computing": ('IT903')}

def update_course_details:
    Enter course name to update (press q to exit):
        check and update the course_dict

def print_course_details:
    print course_dict

def print_common_names:
    For each key in course_dict
        keysplit = key.split(" ");
        for i in range(dict.lengh):
            internal_split = dict[i].split("")
            if keysplit intersection internal_split
                print (key and dict[i])

if __name__ == "__main__":
    while 1:
        Select 1 of options below
            1. Enter course detail and course code
                add_course_details()
            2. Edit course name
                update_course_details()
            3. Pretty print data
                print_course_details()
            4. Print common names
                print_common_names()
