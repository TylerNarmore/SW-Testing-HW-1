import sys
import warnings
from emailVerifier import emailVerifier
from distanceForm import distance
from Retirement import *
from bmiCalculator import *

#Prints menu options
def printOptions():
    print("1) BMI Calculator")
    print("2) Retirement Calculator")
    print("3) Distance Formula")
    print("4) Email Verifier")
    print("5) Exit")


#Calls functions based on choice
def select(choice):
    if choice == 1:
        bmi,cate = bodyMassIndex()
        print("BMI: ",bmi," Category: ",cate)
        
    elif choice == 2:
        age,salary,savings,goal = retirementInput()
        futureAge=retirement(age,salary,savings,goal)
        if futureAge==0:
            print("You can not achieve that goal in your lifetime.")
        else:
            print("You will be",futureAge,"when your goal is met.")
        
    elif choice == 3:
        try:
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))
            print("Distance between points: ", distance(x1, y1, x2, y2))
        except ValueError:
            print("Valid Numbers Only")
        
    elif choice == 4:
        if emailVerifier(input("Enter email to be checked: ")):
            print("Valid Email")
        else:
            print("Invalid Email")
        
    elif choice == 5:
        sys.exit(1)

def main():
    while 1:
        cond = True
        printOptions()
        while cond:
            try:
                choice = int(input("Select an option(1-5): "))
                if choice not in [1,2,3,4,5]:
                    print("Error, select option 1-5")
                else:
                    cond = False
            except:
                print("Error, select option 1-5")


        
        print()
        select(choice)
        print()
    return 0
    

