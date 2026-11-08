from pathlib import Path

path = Path('C:/Users/LOQ/pycode/exercise 10/learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    line = line.replace('Python', 'C')
    print(line)