from datetime import datetime

def create_account():
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    email = input('Enter your email: ')
    address = input('Enter your address: ')
    mobile = input('Enter your mobile number: ')
    with open('users.txt', 'a') as f:
        f.write(f'{username}:{password}:{email}:{address}:{mobile}\n')
    print('Account created successfully!')

order_history = []

def place_order(selections=None):
    print('Menu:')
    items = ['Tandoori chicken (4 pieces)', 'Butter chicken', 'Palak paneer', 'Mutton biryani', 'Veg thali']
    prices = [240, 320, 280, 360, 200]
    for i, (item, price) in enumerate(zip(items, prices), start=1):
        print(f'{i}. {item} [INR {price}]')
    if selections is None:
        selections = []
        while True:
            choice = input('Enter item number(s), separated by commas, or q to finish: ')
            if choice == 'q':
                break
            try:
                item_numbers = [int(num.strip()) for num in choice.split(',')]
                invalid_numbers = [num for num in item_numbers if num < 1 or num > len(items)]
                if invalid_numbers:
                    print(f'Invalid item number(s) {invalid_numbers}, try again.')
                    continue
                selections.extend([num - 1 for num in item_numbers])
            except ValueError:
                print('Invalid input, try again.')
    if len(selections) == 0:
        print('No items ordered.')
    else:
        print('Selected items:')
        total_price = 0
        selected_items = []
        for item_index in selections:
            item_name = items[item_index]
            price = prices[item_index]
            total_price += price
            selected_items.append(f'{item_name} x1 [INR {price}]')
            print(selected_items[-1])
        print(f'Total: INR {total_price}')
        confirm = input('Place order? (y/n) ')
        if confirm == 'y':
            print('Order placed.')
            order_history.append({
                'items': selected_items,
                'total_price': total_price,
                'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            print('Order cancelled.')


def display_order_history():
    if len(order_history) == 0:
        print('No orders yet.')
    else:
        print('Order history:')
        for i, order in enumerate(order_history, start=1):
            print(f'Order {i} - {order["date_time"]}')
            for item in order['items']:
                print(item)
            print(f'Total: INR {order["total_price"]}\n')

def update_profile(users, current_username):
    print('Update Profile:')
    with open('users.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        username, password, email, address, mobile = line.strip().split(':')
        users[username] = {
            'password': password,
            'email': email,
            'address': address,
            'mobile': mobile
        }
    new_username = input(f'New username ({current_username}): ') or current_username
    new_password = input('New password: ')
    new_email = input(f'New email ({users[current_username]["email"]}): ') or users[current_username]['email']
    new_address = input(f'New address ({users[current_username]["address"]}): ') or users[current_username]['address']
    new_mobile = input(f'New mobile number ({users[current_username]["mobile"]}): ') or users[current_username]['mobile']

    users[current_username]['username'] = new_username
    if new_password:
        users[current_username]['password'] = new_password
    users[current_username]['email'] = new_email
    users[current_username]['address'] = new_address
    users[current_username]['mobile'] = new_mobile

    with open('users.txt', 'w') as f:
        for username, info in users.items():
            password = info['password']
            email = info['email']
            address = info['address']
            mobile = info['mobile']
            f.write(f'{username}:{password}:{email}:{address}:{mobile}\n')
    print('Profile updated successfully!')

def login():
    with open('users.txt', 'r') as f:
        lines = f.readlines()

    users = {}
    for line in lines:
        fields = line.strip().split(':')
        if len(fields) == 5:
            username, password, email, address, mobile = fields
            users[username] = {
                'password': password,
                'email': email,
                'address': address,
                'mobile': mobile
            }
        else:
            print(f"Invalid line in users.txt: {line}")

    print("Login:")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Welcome, {username}!")
        while True:
            print("Select an option:")
            print("1. Place Order")
            print("2. Order History")
            print("3. Update Profile")
            print("4. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                place_order()
            elif choice == "2":
                display_order_history()
            elif choice == "3":
                update_profile(users,username)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")
    else:
        print("Invalid username or password.")

while True:
    print("Select an option:")
    print("1. Create an account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
