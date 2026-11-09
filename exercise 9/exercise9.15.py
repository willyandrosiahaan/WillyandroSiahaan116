from random import sample

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                'A', 'B', 'C', 'D', 'E']

my_ticket = (3, 7, 'A', 'D')

attempts = 0

while True:
    attempts += 1

    winning_ticket = tuple(sample(lottery_pool, 4))

    if winning_ticket == my_ticket:
        print("Winning ticket:", winning_ticket)
        print(f"My ticket won after {attempts} attempts!")
        break