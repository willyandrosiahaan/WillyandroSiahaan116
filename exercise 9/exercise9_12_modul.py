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