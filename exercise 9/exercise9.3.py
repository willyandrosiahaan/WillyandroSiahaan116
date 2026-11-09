class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print("User Information:")
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"Age  : {self.age}")
        print(f"City : {self.city}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")

user1 = User("Willy", "Siahaan", 18, "Solo", "willy@example.com")
user2 = User("Gilbert", "Boen", 19, "Taiper", "boen@example.com")
user3 = User("Jose", "Benedict", 21, "Jakarta", "jose@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()