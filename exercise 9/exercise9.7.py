class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print("\nUser Information:")
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"Age  : {self.age}")
        print(f"City : {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can edit post"
        ]

    def show_privileges(self):
        print("\nAdministrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


print("===== CREATE ADMIN =====")
first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")
city = input("City: ")
email = input("Email: ")

admin = Admin(first_name, last_name, age, city, email)


while True:
    print("\n===== ADMIN MENU =====")
    print("1. Show User Information")
    print("2. Greet User")
    print("3. Show Privileges")
    print("4. Exit")

    choice = input("Choose menu (1-4): ")

    if choice == "1":
        admin.describe_user()

    elif choice == "2":
        admin.greet_user()

    elif choice == "3":
        admin.show_privileges()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice! Try again.")