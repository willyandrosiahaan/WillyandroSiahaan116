from random import sample

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                'A', 'B', 'C', 'D', 'E']

winning_ticket = sample(lottery_pool, 4)

print("Lottery Results")
print("----------------")
print("Winning ticket:")

for item in winning_ticket:
    print(item)

print("\nAny ticket matching these 4 numbers or letters wins a prize!")