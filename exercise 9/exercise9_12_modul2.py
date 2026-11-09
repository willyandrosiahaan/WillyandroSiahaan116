from exercise9_12_modul import User


class Privileges:
    def __init__(self):
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


class Admin(User):
    def __init__(self, first_name, last_name, age, city, email):
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()