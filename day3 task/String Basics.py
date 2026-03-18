# 21.Count total characters in a string
text = input("Enter a string: ")

count = 0

for ch in text:
    count = count + 1

print("Total characters =", count)

# 22. Count vowels in a string
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1

print("Vowels =", count)

# 23.Count consonants in a string
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count = count + 1

print("Consonants =", count)

#24.Reverse a string using loop
text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

print("Reversed =", rev)


# 25.Check if string is palindrome
text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")