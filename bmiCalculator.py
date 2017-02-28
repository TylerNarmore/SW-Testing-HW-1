#Author: Brandon Stone

#Calculates the BMI and decides their BMI category
def bodyMassIndex():
    while True:
        try:
            print("Enter your Height in Ft and In and your Weight in Pounds.")
            feet = int(input("Feet: "))
        except ValueError:
            print("Please enter valid integers.")
            continue
        else:
            if feet < 2 or feet > 9:
                print("Please enter feet within 2 and 8.")
                continue
            else:
                feet*=12
                break

    while True:
        try:
            inches = int(input("Inches: "))
        except ValueError:
            print("Please enter valid integers.")
            continue
        else:
            if inches < 0 or inches > 11:
                print("Please enter inches within 0 and 11.")
                continue
            else:
                height = (feet + inches) * .025
                break

    while True:
        try:
            weight = int(input("Weight: "))
        except ValueError:
            print("Please enter valid integers.")
            continue
        else:
            if weight < 30 or weight > 600:
                print("Please enter weight within 30 and 600.")
                continue
            else:
                weight*=.45
                break

    bmi = round(float((weight)/(height**2)),2)
    
    if bmi < 18.5:
        cate = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        cate = "Normal Weight"
    elif 25 <= bmi <= 29.9:
        cate = "Overweight"
    elif bmi >= 30:
        cate = "Obese"

    return bmi, cate   
