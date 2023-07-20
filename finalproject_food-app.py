class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    food_items = []

    @classmethod
    def add_food_item(cls, name, quantity, price, discount, stock):
        food_id = len(cls.food_items) + 1
        new_food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        cls.food_items.append(new_food_item)
        print(f"Food Item '{name}' added with FoodID: {food_id}")

    @classmethod
    def edit_food_item(cls, food_id, name, quantity, price, discount, stock):
        for food_item in cls.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print(f"Food Item '{name}' (FoodID: {food_id}) updated successfully.")
                return
        print(f"Food Item with FoodID: {food_id} not found.")

    @classmethod
    def view_food_items(cls):
        for food_item in cls.food_items:
            print(f"FoodID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, "
                  f"Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")

    @classmethod
    def remove_food_item(cls, food_id):
        for food_item in cls.food_items:
            if food_item.food_id == food_id:
                cls.food_items.remove(food_item)
                print(f"Food Item with FoodID: {food_id} removed successfully.")
                return
        print(f"Food Item with FoodID: {food_id} not found.")


class User:
    users = []

    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    @classmethod
    def register_user(cls, full_name, phone_number, email, address, password):
        new_user = User(full_name, phone_number, email, address, password)
        cls.users.append(new_user)
        print(f"User '{full_name}' registered successfully.")

    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and user.password == password:
                return user
        print("Invalid email or password. Please try again.")
        return None

    def place_new_order(self):
        print("Menu:")
        for food_item in Admin.food_items:
            print(f"{food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

        order_items = input("Enter the array of numbers of food items to order (e.g., [2, 3]): ")
        order_items = [int(item) for item in order_items.strip('[]').split(',')]
        selected_items = [Admin.food_items[item - 1] for item in order_items]

        print("Selected items:")
        for item in selected_items:
            print(f"{item.name} ({item.quantity}) [INR {item.price}]")

        place_order = input("Do you want to place the order? (yes/no): ")
        if place_order.lower() == 'yes':
            self.order_history.append(selected_items)
            print("Order placed successfully!")
        else:
            print("Order not placed.")

    def view_order_history(self):
        if not self.order_history:
            print("No order history.")
        else:
            for idx, order_items in enumerate(self.order_history, start=1):
                print(f"Order {idx}:")
                for item in order_items:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully.")


# Sample Usage:
# Admin functionality
Admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 10, 50)
Admin.add_food_item("Vegan Burger", "1 piece", 320, 20, 30)
Admin.add_food_item("Truffle Cake", "500gm", 900, 15, 25)

Admin.view_food_items()

Admin.edit_food_item(2, "Veggie Burger", "1 piece", 350, 20, 35)
Admin.remove_food_item(3)

Admin.view_food_items()

# User functionality
User.register_user("John Doe", "9876543210", "john@example.com", "123 Main St, City", "password123")
User.register_user("Jane Smith", "9876543211", "jane@example.com", "456 Park Ave, Town", "password456")

user1 = User.login("john@example.com", "password123")
if user1:
    user1.place_new_order()
    user1.place_new_order()

user2 = User.login("jane@example.com", "password456")
if user2:
    user2.place_new_order()
    user2.place_new_order()
    user2.view_order_history()

# Update User Profile
user1.update_profile("John Smith", "9876543219", "john.smith@example.com", "789 Side St, Village", "newpassword789")
