## Background

# You'll be designing an interactive ordering system from a food truck menu, using the skills you've learned in Python so far.

## Challenge Instructions

# The starter code provided includes the code for printing the menu for the customer, which was part of one of your Day 3 activities. You will be adapting this menu to allow customers to place an order, which includes storing the customer's order and printing the receipt with the total price of all items ordered. The starter code includes comments, which you may use as a guide for the steps you need to add. 
# Create an empty list. This list will later store a customer's order in dictionary format, as follows:
'''
customer_order = [
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]
'''
# After the sub-menu is printed, prompt the customer to enter their selection from the menu, saving it as a variable menu_selection.



menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49},
}

order = []

while True:
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}: {value['Item name']} - ${value['Price']}")

    menu_selection = input("Enter the item number you'd like to order (or 'q' to quit): ")

    if menu_selection == 'q':
        break

    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    menu_selection = int(menu_selection)

    if menu_selection not in menu_items:
        print("Invalid item number. Please select from the menu.")
    else:
        item_name = menu_items[menu_selection]["Item name"]
        quantity = input(f"How many {item_name} would you like to order? (Default: 1): ")

        if not quantity.isdigit():
            quantity = 1
        else:
            quantity = int(quantity)

        order.append({
            "Item name": item_name,
            "Price": menu_items[menu_selection]["Price"],
            "Quantity": quantity
        })

if order:
    print("Order Receipt:")
    print("Item name                | Price  | Quantity")
    print("-------------------------|--------|----------")

    for item in order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        spaces_item_name = " " * (25 - len(item_name))
        spaces_price = " " * (8 - len(str(price)))
        print(f"{item_name}{spaces_item_name}| ${price}  | {quantity}")

    total_price = sum(item["Price"] * item["Quantity"] for item in order)
    print(f"Total: ${total_price:.2f}")
else:
    print("No items in the order.")