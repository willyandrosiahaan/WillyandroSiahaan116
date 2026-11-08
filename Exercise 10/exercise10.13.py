import json
from pathlib import Path

def get_stored_user_info(path):
    """Get stored user info if it exists."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for new user info and store it."""
    user_info = {}
    user_info['username'] = input("What is your name? ")
    user_info['age'] = input("How old are you? ")
    user_info['city'] = input("What city do you live in? ")
    
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    path = Path('C:/Users/LOQ/pycode/exercise 10/user_info.json')
    user_info = get_stored_user_info(path)
    
    if user_info:
        print(f"Welcome back, {user_info['username']}!")
        print(f"Age: {user_info['age']}")
        print(f"City: {user_info['city']}")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")

greet_user()