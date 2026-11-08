from pathlib import Path

path = Path('C:/Users/LOQ/pycode/exercise 10/guest.txt')
prompt = "\nEnter your name (enter 'quit' when finished): "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break
    print(f"Welcome, {name}!")
    guest_names.append(f"{name}\n")

file_contents = "".join(guest_names)
path.write_text(file_contents)