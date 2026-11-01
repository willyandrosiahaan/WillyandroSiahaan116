sandwich_orders = ['tuna', 'ham', 'veggie', 'turkey', 'chicken']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(f"Finished sandwich: {sandwich}.")