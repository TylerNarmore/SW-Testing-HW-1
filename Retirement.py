def retirement(age, salary, savings, goal):

    #calculates the years needed until the goal is met
    yearsNeeded = goal/(salary*savings)

    #If the years needed puts the user's age past 100, it returns 0
    if yearsNeeded > (100-age):
        return 0
    #if the user can achieve their goal, it rounds down and returns the age they
    #will be
    else:
        return int(age+yearsNeeded)
    
def retirementInput():

    #Makes sure the user inputs a number and an age above 12
    while True:
        try:
            age = int(input("Enter your current age:\n"))
        except ValueError or age<13:
            print("Please enter a valid age 13 or older.")
            continue
        else:
            if age<13 or age>100:
                print("Please enter an age 13-100.")
                continue
            else:
                break

    #Makes sure the user's salary is a positive number
    while True:
        try:
            salary = float(input("Enter your current yearly salary:  \n$"))
        except ValueError:
            print("Please enter a valid positive number.")
            continue
        else:
            if salary<=0:
                print("Please enter a positive number")
                continue
            else:
                break

    #Makes sure the user's savings percentage is between 0 and 100. (0,100]
    #and then divides it by 100 to get the percentage
    while True:
        try:
            savings = float(input("Enter the percent of your salary you want to save (10,15,20):  \n"))
        except ValueError:
            print("Please enter a valid saving percentage. ex 5,10,20")
            continue
        else:
            if savings<=0:
                print("Savings must be more than 0.")
                continue
            elif savings>100:
                print("Savings can't be over 100%.")
                continue
            else:
                savings/=100
                break

    #Checks if the users goal is a positive number
    #then divides by 2 to account for employeer matching
    while True:
        try:
            goal = float(input("Enter your desired retirement goal:  \n$"))
        except ValueError:
            print("Please enter a positive number. Ex 1000000")
        else:
            if goal<=0:
                print("Your goal must be more than 0.")
                continue
            else:
                goal/=2
                break
            
    #Returns the formatted inputs for the retirement function
    return age, salary, savings, goal
