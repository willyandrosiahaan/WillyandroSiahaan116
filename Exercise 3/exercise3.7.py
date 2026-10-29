friend = ['Jose', 'Grace', 'Boen']
message = f"Come to my place for dinner, {friend[0]}!"
message += f"\nCome to my place for dinner, {friend[1]}!"
message += f"\nCome to my place for dinner, {friend[2]}!"
print(message)

print(f"\n{friend[2]} can't come to my place.")
remove = friend.pop(2)
add = friend.append("Kieron")
message = f"Come to my place for dinner, {friend[0]}!"
message += f"\nCome to my place for dinner, {friend[1]}!"
message += f"\nCome to my place for dinner, {friend[2]}!"
print(message)

print(f"\nI found a bigger table!")
guest1 = friend.insert(0, "Lionel")
guest2 = friend.insert(2, "Elson")
guest3 = friend.append("Reon")
message = f"Come to my place for dinner, {friend[0]}!"
message += f"\nCome to my place for dinner, {friend[1]}!"
message += f"\nCome to my place for dinner, {friend[2]}!"
message += f"\nCome to my place for dinner, {friend[3]}!"
message += f"\nCome to my place for dinner, {friend[4]}!"
message += f"\nCome to my place for dinner, {friend[5]}!"
print(message)
print(friend)

print("\nI can only invite two people for dinner.")
remove1 = friend.pop()
print(f"Sorry, {remove1}, I can't invite you to dinner.")
remove2 = friend.pop() 
print(f"Sorry, {remove2}, I can't invite you to dinner.")
remove3 = friend.pop()
print(f"Sorry, {remove3}, I can't invite you to dinner.")
remove4 = friend.pop()
print(f"Sorry, {remove4}, I can't invite you to dinner.")
print(f"{friend[0]} and {friend[1]}, you are still invited to dinner.")
del friend[0]
del friend[0]
print(friend)