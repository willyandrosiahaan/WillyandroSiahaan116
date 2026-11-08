from pathlib import Path

filenames = ['C:/Users/LOQ/pycode/exercise 10/dogs.txt', 'C:/Users/LOQ/pycode/exercise 10/cats.txt']

for filename in filenames:
    path = Path(filename)
    print(f"\nReading {filename}:")
    try:
        contents = path.read_text(encoding='utf-8')
        print(contents)
    except FileNotFoundError:
        print(f"  -> Sorry, the file {filename} could not be found.")