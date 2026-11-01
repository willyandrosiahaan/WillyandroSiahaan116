sandwich_orders = ['tuna', 'ham', 'veggie', 'turkey', 'chicken', 'pastrami', 'pastrami', 'pastrami']
print("The deli has run out of pastrami.")
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
