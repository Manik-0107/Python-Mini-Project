# Food Menu Dictionary
menu = {
    "Pizza" : 250,
    "Burger" : 120,
    "Pasta" : 180,
    "Sandwich" : 90,
    "French Fries" : 80,
    "Cold Coffee" : 70,
    "Ice Cream" : 60
}

# Greating message
print("Welcome to the Java Hotel !!!")

# Display Menu
print("\n---> Today's Menu <---")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

# Take order
order_total = 0
while True:
    item = input("\nEnter the item you want to order ( or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    elif item in menu:
        order_total += menu[item]
        print(f"{item} added to your order. Current total: ₹{order_total}")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")

# Final Bill
print("\nThank you for your order!!!")
print(f"Your total bill is: ₹{order_total}")




"""

Welcome to the Java Hotel !!!

---> Today's Menu <---
Pizza: ₹250
Burger: ₹120
Pasta: ₹180
Sandwich: ₹90
French Fries: ₹80
Cold Coffee: ₹70
Ice Cream: ₹60

Enter the item you want to order ( or type 'done' to finish): Burger
Burger added to your order. Current total: ₹120

Enter the item you want to order ( or type 'done' to finish): Pasta
Pasta added to your order. Current total: ₹300

Enter the item you want to order ( or type 'done' to finish): Ice Cream
Ice Cream added to your order. Current total: ₹360

Enter the item you want to order ( or type 'done' to finish): done

Thank you for your order!!!
Your total bill is: ₹360


"""
