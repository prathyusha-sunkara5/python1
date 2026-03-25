# 5Concepts: Set
# Track unique visitors.
# Requirements:
# Store visitor names in a set
# Avoid duplicates
# Print total unique visitors?

visitors = set()

# Take number of entries
n = int(input("Enter number of visitors: "))

# Input visitor names
for i in range(n):
    name = input(f"Enter visitor {i+1} name: ")
    visitors.add(name)   # Set automatically ignores duplicates

# Display results
print("Unique Visitors:")
for visitor in visitors:
    print(visitor)

print("Total Unique Visitors:", len(visitors))
