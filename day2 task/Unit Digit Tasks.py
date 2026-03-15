# #21.
# #Take a number as string input and print the last digit.
num = input("Enter a number: ")
print("Last digit:", num[-1])

# #22.
# #Take a number and print the unit digit using % operator.
num = int(input("Enter a number : "))
print("Unit digit :" , num % 10) 

#23.
#Take a number and remove the last digit using // operator.
num = int(input("Enter a number: "))
print("Number without last digit:", num // 10)

# 24.
# Take a number and print the second last digit.
num = int(input("Enter a number: "))
print("Second last digit:", (num // 10) % 10)

# 25.
# Take a 5 digit number and print its last digit.
num = int(input("Enter a 5-digit number: "))
print("Last digit:", num % 10)
