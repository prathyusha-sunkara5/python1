# 31.Create a list of 5 numbers and print sum
numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total = total + num

print("Sum =", total)

# 32.Find maximum value in list
numbers = [5, 20, 10, 30, 25]

max_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num

print("Maximum =", max_val)

# 33.Find minimum value in list
numbers = [10, 25, 5, 40, 15]

min_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num

print("Minimum =", min_val)

# 34.Count total elements in list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

count = 0

for num in numbers:
    count = count + 1

print("Total elements =", count)

# 35.Check if element exists in list
numbers = [10, 20, 30, 40, 50 ,70 ,90]

x = int(input("Enter number to check: "))

if x in numbers:
    print("Element found")
else:
    print("Element not found")