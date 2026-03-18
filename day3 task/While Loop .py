# 11.Print numbers from 1 to 20 using while
i =1
while i <= 20:
    print(i)
    i = i + 1


# 12.Find factorial of a number using while
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)


#13.Reverse a number using while
num = int(input("Enter a number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", rev)

# 14.Count digits in a number
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Number of digits =", count)

# 15.Keep asking input until user enters "stop"

text = ""

while text != "stop":
    text = input("Enter something: ")





