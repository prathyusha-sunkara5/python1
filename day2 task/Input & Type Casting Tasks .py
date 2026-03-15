#15.
#Take a name from user input and print its data type.
name = input("enter your name :")
print("Data type of name :" , type(name))

#16.
#Take age from user input and convert it into integer
age = int(input("enter your age:"))
print("age =" , age)
print("Data type of age :" ,type(age))

#17.
#Take two numbers from user input and print their sum.
a = int(input("please enter the first number:"))
b = int(input("please enter the second number"))
sum = a + b
print ("sum of two numbers:" , sum)

#18.
#Take two marks from user input and print their average.
mark1 = int(input("enter the maths marks :"))
mark2 = int(input("enter the science marks :"))
Average = (mark1 + mark2) / 2
print ("average of both marks :" , Average)

#19.
#Take two numbers from user input and print
3*a*2 + b - 2.
a = int(input("Enter the  first number: "))
b = int(input("Enter the second number: "))
Total = 3 * a * 2 + b - 2
print("Total =", Total)

#20.
#Take a number from user input and print its data type before and after type casting.
number = input("Enter a number: ")
print("Before type casting:", type(number))
number = int(number)
print("After type casting:", type(number))