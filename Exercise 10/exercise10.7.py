print("Enter 'q' to quit at any time.")
while True:
    try:
        x_input = input("\nGive me a number: ")
        if x_input == 'q':
            break
        x = int(x_input)
        
        y_input = input("Give me another number: ")
        if y_input == 'q':
            break
        y = int(y_input)
    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        print(f"The sum of {x} and {y} is {x + y}.")