friend = ['Jose', 'Grace', 'Boen']
message = f"Come to my place for dinner, {friend[0]}!"
message += f"\nCome to my place for dinner, {friend[1]}!"
message += f"\nCome to my place for dinner, {friend[2]}!"
print(message)

print(f"{friend[2]} can't come to my place.")
remove = friend.pop(2)
add = friend.append("Kieron")
message = f"Come to my place for dinner, {friend[0]}!"
message += f"\nCome to my place for dinner, {friend[1]}!"
message += f"\nCome to my place for dinner, {friend[2]}!"
print(message)

print("I found a bigger table!")
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

print(f"\nLength of list : {len(friend)}")