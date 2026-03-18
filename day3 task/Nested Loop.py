# 16.Print pattern:
# *
# **
# ***
# ****

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()


# 17. Print pattern:
# 1
# 12
# 123
# 1234
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 18. Print multiplication table (1 to 5) using nested loop

for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

# 19. Print:
# A B C
# A B C
# A B C    
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

#20.Print:
# 1 2 3
# 4 5 6
# 7 8 9    
num = 1

for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num = num + 1
    print()