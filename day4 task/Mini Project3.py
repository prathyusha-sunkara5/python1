# 3 shop cart system
# Shopping Cart System
# Concepts: List, Dictionary, Loop
# Simulate an online cart.
# Requirements:
# Add products (name, price, quantity)
# Calculate total bill
# Remove item from cart
# Display all items in formatted way?

cart = []
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    cart.append(product)
    print(" Product added to cart!")

def remove_product():
    name = input("Enter product name to remove: ")
    
    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print(" Product removed!")
            return
    
    print(" Product not found")


def display_cart():
    if not cart:
        print("🛒 Cart is empty")
        return
    
    print(" Your Cart:")
    print("-" * 40)
    print(f"{'Name':<10}{'Price':<10}{'Qty':<5}{'Total':<10}")
    print("-" * 40)
    
    for item in cart:
        total = item["price"] * item["quantity"]
        print(f"{item['name']:<10}{item['price']:<10}{item['quantity']:<5}{total:<10}")
    
    print("-" * 40)


def total_bill():
    total = sum(item["price"] * item["quantity"] for item in cart)
    print(f" Total Bill: ₹{total}")

while True:
    print("\n===== Shopping Cart Menu =====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Total Bill")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        total_bill()
    elif choice == "5":
        print(" Exiting cart system")
        break
    else:
        print(" Invalid choice")

