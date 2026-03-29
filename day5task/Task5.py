# 🔹 Task 5: Memory Optimization (Generator)
# Create:
# def square_generator(n):
# Yield squares instead of storing in list
# 👉 Compare:
# Normal list vs generator (print type)
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

normal_list = [i ** 2 for i in range(1, 6)]

gen = square_generator(5)

print(f"\nNormal list: {normal_list} → {type(normal_list)}")
print(f"Generator object: {gen} → {type(gen)}")
print(f"Generator values: {list(square_generator(5))}")

