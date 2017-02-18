import sys
from emailVerifier import emailVerifier

def printOptions():
    print("1) BMI Calculator")
    print("2) Retirement Calculator")
    print("3) Distance Formula")
    print("4) Email Verifier")
    print("5) Exit")


def select(choice):
    if choice == 1:
        bmiCalculator()
        
    elif choice == 2:
        retirement()
        
    elif choice == 3:
        distanceFormula()
        
    elif choice == 4:
        print(emailVerifier(input("Enter email to be checked: ")))
        
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
                    print("Error, select option 1-5 \n")
                else:
                    cond = False
            except:
                print("Error, select option 1-5 \n")

        
        print()
        select(choice)
        print()
    
main()
