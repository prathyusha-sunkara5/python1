#35.
#Create a program for job eligibility:
# Conditions
# Age ≥ 18
# Height ≥ 160
# Weight ≥ 60
# Print selected or rejected.

name = input("enter your name :")
age = int (input("enter your age :"))
height = int(input("enter your height:"))
weight = int(input("enter your weight:"))
if (age >= 18):
    if (height >= 160):
        if (weight >= 60):
            print(name , "congratulations you're selected" )
        else:
            print(name , "you're weight is not eligible")
    else:
        print(name , "you're height is not eligible")
else:
    print(name , "you're age is not eligible")

# 36.
# Create a college admission program:
# Conditions
# Marks ≥ 60
# Age ≥ 17

name = input("enter your name")
marks = int (input("enter your marks"))
age = int(input("enter your age"))
if marks >= 60:
    if age >= 17:
        print(name ,"congratulations you got the admission")
    else:
        print(name , "your age is not eligible to get the admission")
else:
    print(name ,"your marks is less than equal to 60 so,you are not selected")

# 37.
# Create a sports selection program:
# Conditions
# Age ≥ 16
# Height ≥ 150
# Weight ≥ 50
 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print(name, "you are selected")
        else:
            print(name, "your weight is not eligible")
    else:
        print(name, "your height is not eligible")
else:
    print(name, "your age is not eligible")







        




    