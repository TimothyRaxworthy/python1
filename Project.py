'''
Project
You are tasked with creating a simple inventory management system for a market. The system should allow users to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.
Functionality:
Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.
Project Structure:
Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.
Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the inventory.
Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding, updating, viewing, removing items, or searching by category.
'''

#Inventory list
inventory = []

#First create function that searches for specific items
def find_item_by_name(name):
    name_lower = name.strip().lower()
    for idx, item in enumerate(inventory):
        if item['name'] == name_lower:
            return item, idx
    return None, None

#Add Item function
def add_item():
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ").strip()

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"Item '{name}' added successfully.\n")
    return

#update Item
def update_item():
    name = input("Enter the name of the item to update:\n").strip()
    item, idx = find_item_by_name(name)
    if item is None:
        print(f"Item '{name}' not found.")
        return
    #Update price
    price_input = input(f"Current Price is {item['price']}. New Price:\n").strip()
    if price_input:
        try:
            item["price"] = float(price_input)
        except ValueError:
            print("Invalid price")
            return

    #Update quantity
    qty_input = input(f"Quantity is {item['quantity']}. New Quantity:\n").strip()
    if qty_input:
        try:
            item["quantity"] = int(qty_input)
        except ValueError:
            print("Invalid quantity")
            return

    #Update category

    cat_input = input(f"Category is {item['category']}. New Category:\n").strip()
    if cat_input:
        item["category"] = cat_input

    inventory[idx] = item
    print(f"Updated: {item['name']}")

def view_inventory():
    if not inventory:
        print("Inventory is empty")
        return

    print("\nInventory:")
    print("-" * 50)
    for item in inventory:
        print(f"name: {item['name']}")
        print(f"price: {item['price']}")
        print(f"quantity: {item['quantity']}")
        print(f"category: {item['category']}")
        print("-" * 50)

def remove_item():
    name = input("Enter the name of item to remove:\n").strip()
    _, idx = find_item_by_name(name)
    if idx is None:
        print("Item not found.")
        return
    removed = inventory.pop(idx)
    print(f"Removed: {removed['name']}")

def search_by_category():
    category = input("Enter category to search:\n").strip().lower()
    results = [item for item in inventory if item["category"].lower() == category]
    if not results:
        print("No items foud in that category.")
        return
    print(f"\nItems in category '{category}':")
    print("-" * 50)
    for item in results:
        print(f"{item['name']} - Price: {item['price']} - Quantity: {item['quantity']}")
    print("-" * 50)

def print_menu():
    print("""
Choose an option:
1) Add item
2) Update item
3) View inventory
4) Remove item
5) Search by category
6) Exit
""")



def main():
    while True:
        print_menu()
        choice = input("> ").strip()
        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

