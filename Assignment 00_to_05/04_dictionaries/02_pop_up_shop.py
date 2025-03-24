# Define the menu and their respective prices
menu = {
    'B': ('Burger', 200),
    'F': ('French Fries', 50),
    'P': ('Pizza', 500),
    'S': ('Sandwiches', 150)
}

# Initialize the total charge
total_charge = 0

# Display the menu
print("Menu:")
for item_code, (item_name, price) in menu.items():
    print(f"{item_code} - {item_name} (Rs. {price})")

# Take orders from the customer
while True:
    food_type = input("Enter the food type (B/F/P/S) or 'Q' to quit: ").upper()
    
    # Check if the customer wants to quit
    if food_type == 'Q':
        break
    
    if food_type in menu:
        quantity = int(input(f"How many {menu[food_type][0]} do you want to order? "))
        total_charge += menu[food_type][1] * quantity
    else:
        print("Invalid choice. Please select a valid food type.")

# Display the total charges
print(f"Total charges for the order: Rs. {total_charge}")