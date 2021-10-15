"""
# ---------------------------
# File           : calculator.py
# Created        : 14-10-2021 10:43
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""


class Calculator:
    def addition(num1, num2):
        return num1 + num2

    def subtraction(num1, num2):
        return num1 - num2

    def multiplication(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2

    if __name__ == "__main__":
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

    while 1:
        option = input("Enter the operation you want to start 1/2/3/4:")
        if option in ("1", "2", "3", "4"):
            a = int(input("Enter the value for a"))
            b = int(input("Enter the value for b"))

            if option == "1":
                total = addition(a, b)
                print("Addition value: {}".format(total))
            elif option == "2":
                total = subtraction(a, b)
                print("Subtraction value: {}".format(total))
            elif option == "3":
                total = multiplication(a, b)
                print("Multiplication value: {}".format(total))
            elif option == "4":
                total = division(a, b)
                print("Division value: {}".format(total))
            again = input("if you want to start the next operation type  for yes or no:")
            if again == "no":
                print("Thank you")
                break
        else:
            print("!!!Enter the right option!!!")
