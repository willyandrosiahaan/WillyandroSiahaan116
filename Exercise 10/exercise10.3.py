from pathlib import Path

path = Path('C:/Users/LOQ/pycode/exercise 10/learning_python.txt')
for line in path.read_text().splitlines():
    print(line)