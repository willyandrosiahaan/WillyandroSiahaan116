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