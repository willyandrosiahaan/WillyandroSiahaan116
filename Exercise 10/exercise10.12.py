import json
from pathlib import Path

path = Path('C:/Users/LOQ/pycode/exercise 10/number.json')

if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}.")
else:
    number = input("What is your favorite number? ")
    path.write_text(json.dumps(number))
    print("Thanks, I'll remember that next time!")