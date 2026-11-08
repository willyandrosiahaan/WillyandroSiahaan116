from pathlib import Path

name = input("What's your name? ")
path = Path('C:/Users/LOQ/pycode/exercise 10/guest.txt')
path.write_text(name)