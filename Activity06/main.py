class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"

class ItemManager:
    def __init__(self, filename="Activity06/items.txt"):
        self.items = {}
        self.filename = filename
        self.load_items()

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Error: Item ID already exists.")
            return
        if price < 0:
            print("Error: Price cannot be negative.")
            return
        self.items[item_id] = Item(item_id, name, description, price)
        self.save_items()
        print("Item created successfully.")

    def read_item(self, item_id):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        print(self.items[item_id])

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        if price is not None and price < 0:
            print("Error: Price cannot be negative.")
            return
        if name:
            self.items[item_id].name = name
        if description:
            self.items[item_id].description = description
        if price is not None:
            self.items[item_id].price = price
        self.save_items()
        print("Item updated successfully.")

    def delete_item(self, item_id):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        del self.items[item_id]
        self.save_items()
        print("Item deleted successfully.")

    def display_items(self):
        if not self.items:
            print("No items to display.")
            return
        for item in self.items.values():
            print(item)

    def save_items(self):
        with open(self.filename, "w") as file:
            for item in self.items.values():
                file.write(f"{item.item_id},{item.name},{item.description},{item.price}\n")

    def load_items(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    item_id, name, description, price = line.strip().split(",")
                    self.items[item_id] = Item(item_id, name, description, float(price))
        except FileNotFoundError:
            pass

def main():
    manager = ItemManager()
    while True:
        print("\nItem Management Menu:")
        print("[C] - Create Item")
        print("[R] - Read Item")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[L] - List All Items")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            break
        
        try:
            if choice == 'C':
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
            elif choice == 'R':
                item_id = input("Enter item ID: ")
                manager.read_item(item_id)
            elif choice == 'U':
                item_id = input("Enter item ID: ")
                name = input("Enter new name (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            elif choice == 'D':
                item_id = input("Enter item ID: ")
                manager.delete_item(item_id)
            elif choice == 'L':
                manager.display_items()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter numeric values for price.")

if __name__ == "__main__":
    main()