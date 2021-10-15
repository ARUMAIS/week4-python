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
        course_name = input("Enter the LYIT course:")
        Enter coursename(pressqtoexit):
        course_code = input("Enter the course code:")
        Enter course code (press q to exit):
            course_code
    course_dict = {"Msc in DevOps": ('IT902'), "Msc in Cloud Computing": ('IT903')}

def update_course_details:
    while 1:
        update_course_name = input("Enter the course name to update:")

    exit = input("press q to exit:")
       if quit == "q":
           print("Thank you")
           break
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
 print("----MENU----")
 print("1.Add LYIT course & codes")
 print("2.Edit the course name")
 print("3.Print the data in the list")
 print("4.Print the common course names")
 choice = input("Enter the option 1/2/3/4:")
while 1:
        if choice in ("1","2","3","4"):
            if choice == "1":
                add_course_details()
            elif choice == "2":
                update_course_details()
            elif choice == "3":
                print_course_details()
            elif choice == "4":
                print_common_names()
        else:
           print("Enter the valid option")