try:
    x = int(input("Give me a number: "))
    y = int(input("Give me another number: "))
except ValueError:
    print("Sorry, I really needed a number.")
else:
    print(f"The sum of {x} and {y} is {x + y}.")