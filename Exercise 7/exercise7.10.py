poll = {}
active = True
name = input("What is your name? ")
response = input("Which place would you like to visit someday? ")
poll[name] = response
repeat = input("Would you like to let another person respond? (yes/no) ")
while repeat.lower() == 'yes':
    name = input("What is your name? ")
    response = input("Which place would you like to visit someday? ")
    poll[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    
    if repeat.lower() == 'no':
        break
    

print("\n--- Poll Results ---")
for name, response in poll.items():
    print(f"{name} would like to visit {response}.")