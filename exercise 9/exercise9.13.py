from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


print("Rolling a 6-sided die 10 times:")
die6 = Die()

for _ in range(10):
    die6.roll_die()

print("\nRolling a 10-sided die 10 times:")
die10 = Die(10)

for _ in range(10):
    die10.roll_die()

print("\nRolling a 20-sided die 10 times:")
die20 = Die(20)

for _ in range(10):
    die20.roll_die()