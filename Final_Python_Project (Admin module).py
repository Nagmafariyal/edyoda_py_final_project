class Admin:
    food_items= []
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid_credentials(self, username, password):
        return self.username == username and self.password == password

    def add_food_item(self):
      

        # Read the existing food items from the file and add them to the list
        with open('food_items.txt', 'r') as f:
            for line in f:
                item_id, name, quantity, price, discount, stock = line.strip().split('|')
                self.food_items.append({
                    'food_id': item_id,
                    'name': name,
                    'quantity': quantity,
                    'price': float(price),
                    'discount': float(discount),
                    'stock': stock
                })

        # Get the details of the new food item from the user
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity of the food item: ")
        price = float(input("Enter the price of the food item: "))
        discount = float(input("Enter the discount of the food item (in decimal): "))
        stock = input("Enter the stock of the food item: ")

        # Generate a unique ID for the new food item
        if len(self.food_items) == 0:
            food_id = 1
        else:
            max_id = max(int(item['food_id']) for item in self.food_items)
            food_id = max_id + 1

        # Create a dictionary representing the new food item
        new_item = {
            'food_id': str(food_id),
            'name': name,
            'quantity': quantity,
            'price': price,
            'discount': discount,
            'stock': stock
        }

        # Append the new item to the list of food items
        self.food_items.append(new_item)

        # Write the updated list of food items to the file
        with open('food_items.txt', 'a') as f:
            f.write(f"\n{new_item['food_id']}|{new_item['name']}|{new_item['quantity']}|"
                    f"{new_item['price']}|{new_item['discount']}|{new_item['stock']}")

        # Print a message to confirm that the new food item was added
        print(f"Food item with ID {food_id} added successfully.")
    def read_food_items(self):
        try:
            with open('food_items.txt', 'r') as f:
                lines = f.readlines()
                self.food_items = []
                for line in lines:
                    fields = line.strip().split('|')
                    if len(fields) >= 6:
                        food_item = {'food_id': int(fields[0]), 'name': fields[1], 'quantity': fields[2], 'price': float(fields[3]), 'discount': float(fields[4]), 'stock': fields[5]}
                        self.food_items.append(food_item)
                return self.food_items  # return the food_items list after reading the file
        except FileNotFoundError:
            return []

    def edit_food_item(self):
    # Read the list of food items from the file
        self.food_items = self.read_food_items()

        # Get the ID of the food item to be edited from the user
        food_id = int(input("Enter the ID of the food item to be edited: "))

        # Find the index of the food item with the specified ID
        index = None
        for i, item in enumerate(self.food_items):
            if item['food_id'] == food_id:
                index = i
                break

        # If the specified ID is not found, print an error message and return
        if index is None:
            print(f"Error: Food item with ID {food_id} not found.")
            return

        # Get the details of the updated food item from the user
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity of the food item: ")
        price = float(input("Enter the price of the food item: "))
        discount = float(input("Enter the discount of the food item (in decimal): "))
        stock = input("Enter the stock of the food item: ")

        # Update the food item with the specified ID
        self.food_items[index]['name'] = name
        self.food_items[index]['quantity'] = quantity
        self.food_items[index]['price'] = price
        self.food_items[index]['discount'] = discount
        self.food_items[index]['stock'] = stock

        # Write the updated list of food items to the file
        with open('food_items.txt', 'w') as f:
            for item in self.food_items:
                f.write(f"{item['food_id']}|{item['name']}|{item['quantity']}|{item['price']}|{item['discount']}|{item['stock']}\n")

        # Print a message to confirm that the food item was updated
        print(f"Food item with ID {food_id} updated successfully.")
    def remove_food_item(self):
        # Read the list of food items from the file
        self.food_items = self.read_food_items()

        # Get the ID of the food item to be removed from the user
        food_id = int(input("Enter the ID of the food item to be removed: "))

        # Find the index of the food item with the specified ID
        index = None
        for i, item in enumerate(self.food_items):
            if item['food_id'] == food_id:
                index = i
                break

        # If the specified ID is not found, print an error message and return
        if index is None:
            print(f"Error: Food item with ID {food_id} not found.")
            return

        # Remove the food item with the specified ID
        del self.food_items[index]

        # Write the updated list of food items to the file
        with open('food_items.txt', 'w') as f:
            for item in self.food_items:
                f.write(f"{item['food_id']}|{item['name']}|{item['quantity']}|{item['price']}|{item['discount']}|{item['stock']}\n")

        # Print a message to confirm that the food item was removed
        print(f"Food item with ID {food_id} removed successfully.")
    def view_food_items(self):
    # Read the list of food items from the file
        self.food_items = self.read_food_items()

        # Print the list of food items
        print("ID  | Name          | Quantity | Price   | Discount | Stock")
        print("----|---------------|----------|---------|----------|-------")
        for item in self.food_items:
            print(f"{item['food_id']:3} | {item['name']:13} | {item['quantity']:8} | {item['price']:7.2f} | {item['discount']:8.2f} | {item['stock']:5}")

admin = Admin("Nagma", "123")
def display_menu():
    print("Welcome to the Food Ordering System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if admin.is_valid_credentials(username, password):
        print("1. Add food items")
        print("2. Edit food items")
        print("3. Remove food items")
        print("4. View food items")
        option = int(input("Enter your option: "))
        if option == 1:
            admin.add_food_item()
        elif option == 2:
            admin.edit_food_item()
        elif option == 3:
            admin.remove_food_item()
        elif option == 4:
            admin.view_food_items()
        else:
            print("Invalid option. Please try again.")
    else:
        print("Invalid username or password. Please try again.")
display_menu()
