#Author: Brandon Stone

#Calculates the BMI
def bodyMassIndex(feet,inches,weight):
    if feet<2 or weight<30 or weight>600 or inches<0:
        return 0
    else:
        height = float(((feet*12) + inches) * .025)
        bmi = (weight * .45) / (height ** 2)
        return float(format(bmi, '.2f'))

#Gets input from the user and decides their BMI category
def index():
    while True:
        try:
            print("Enter your Height in Ft and In and your Weight in Pounds.")
            feet = float(input("Feet: "))
            inches = float(input("Inches: "))
            weight = float(input("Weight:  "))
        except ValueError:
            print("Please enter valid inputs integers.")
            continue
        else:
            if feet < 2:
                print("Please enter feet above 2.")
                continue
            elif inches < 0:
                print("Please enter inches above 0.")
            elif weight < 30 or weight > 600:
                print("Enter weight that is between 30 and 600.")
                continue
            else:
                break

    bmi = bodyMassIndex(feet,inches,weight)
    
    if bmi < 18.5:
        return "BMI: " + str(bmi) + " Category: Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "BMI: " + str(bmi) + " Category: Normal Weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "BMI: " + str(bmi) + " Category: Overweight"
    elif bmi >= 30:
        return "BMI: " + str(bmi) + " Category: Obese"
