"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
print("\n\n<---something to do with triangle--->\n")
n1 = int(round(float(input("Enter a number: "))))
n2 = int(round(float(input("Enter a number: "))))

question = input("\nIs one of the numbers the hypotenuse of a triangle?(y/n): ")

if question == "y":
    question2 = input("\nwhich number?(1/2): ")
    if question2 == "1":
        n3 = round(math.sqrt(math.pow(n1,2) - math.pow(n2,2)), 1)
        print(f"\nmissing side = {n3}") 
    elif question2 == "2":
        n3 = round(math.sqrt(math.pow(n2,2) - math.pow(n1,2)), 1)
        print(f"\nmissing side = {n3}")
elif question == "n":
    print("\nYour missing length cannot be calculated because you don't have a hypotenuse\n\n")
else:
    print("\nLOL you can only input y or n\n\n")