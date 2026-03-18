# 36.Add 3 elements using append()
numbers = [1, 2, 3]

numbers.append(4)
numbers.append(5)
numbers.append(6)

print(numbers)

# 37.Insert element at specific index
numbers = [20, 40, 60, 90]

numbers.insert(2, 25)

print(numbers)

# 38.Remove element using remove()
numbers = [1, 2, 3, 4, 5]

numbers.remove(3)

print(numbers)

# 39.Reverse list without using .reverse()
numbers = [1, 2, 3, 4]

reversed_list = []

for num in numbers:
    reversed_list = [num] + reversed_list

print(reversed_list)

# 40.Sort list without using .sort()
numbers = [4, 1, 3, 2]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)