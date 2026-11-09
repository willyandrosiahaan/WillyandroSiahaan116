class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mango", "Matcha"]

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand("Sweet Ice Cream", "Dessert")

ice_cream.describe_restaurant()
ice_cream.display_flavors()