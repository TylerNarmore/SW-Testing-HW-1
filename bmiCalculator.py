import math

class bodyMassIndex:
    def __init__(self):
        while True:
            try:
                feet = float(input("Feet: "))
                inches = float(input("Inches: "))
                weight = float(input("Enter your weight in pounds: "))
                self.feet = feet * 12.0
                self.inches = inches
                self.weight = weight * .45
            except ValueError:
                print("Please enter valid inputs")
                continue
            else:
                if feet <= 0 or inches <= 0 or weight <= 0:
                    print("Please enter values that are above zero.")
                    continue
                else:
                    break

    def index(self):
        meters = float((self.feet + self.inches) * 0.025)
        meters = math.pow(meters, 2)
        bmi = self.weight / meters
        
        if bmi <= 18.5:
            return "BMI: " + "%.2f" % bmi + " Category: Underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            return "BMI: " + "%.2f" % bmi + " Category: Normal Weight"
        elif bmi >= 25 and bmi <= 29.9:
            return "BMI: " + "%.2f" % bmi + " Category: Overweight"
        elif bmi >= 30:
            return "BMI: " + "%.2f" % bmi + " Category: Obese"
