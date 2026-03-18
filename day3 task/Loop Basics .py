# 1.Print numbers from 1 to 50 using for loop
for i in range(1,51):
    print(i)

# 2.Print even numbers from 1 to 100
for i in range(2, 101, 2):
    print(i)


# 3.Print odd numbers from 1 to 100
for i in range(1,101,2):
    print(i)

# 4. Print multiplication table of 7
for i in range(1,11):
    print("7*",i,"=",7*i)

# 5.Find sum of numbers from 1 to 100
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)


# 6.Print numbers in reverse from 50 to 1
for i in range(50,0,-1):
    print(i)



# 7.Count how many numbers are divisible by 3 (1–100)
count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += 1

print(count)


# 8. Print squares of numbers from 1 to 10
for i in range(1,11):
    print(i*i)

# 9. Print cube of first 10 numbers
for i in range(1,11):
    print(i*i*i)

# 10. Take input n, print numbers from 1 to n
n = int(input("enter the number :"))
for i in range(1,n + 1):
    print(i)


    