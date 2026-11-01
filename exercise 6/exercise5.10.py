current_users = ['john', 'jane', 'admin', 'alice', 'bob']
new_users = ['john', 'jane', 'charlie', 'dave', 'eve']
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry, the username {new_user} is already taken. Please choose a different username.")
    else:
        print(f"The username {new_user} is available.")