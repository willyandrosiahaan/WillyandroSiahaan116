from pathlib import Path

filenames = ['C:/Users/LOQ/pycode/exercise 10/dogs.txt', 'C:/Users/LOQ/pycode/exercise 10/cats.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading {filename}:")
        print(contents)