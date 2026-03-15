# 38.
# Take a number (1-7) and print day name using match.
day = int(input("Enter a number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# 39.
# Take a number (1-3) and print:
# 1 → Red
# 2 → Blue
# 3 → Green

num = int(input("Enter a number (1-3): "))
match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

# 40.
# Take a number (1-4) and print:
# 1 → Apple
# 2 → Mango
# 3 → Orange
# 4 → Banana

num = int(input("Enter a number (1-4): "))
match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")



