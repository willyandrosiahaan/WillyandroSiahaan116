friends_pizzas = ['pepperoni', 'mushrooms', 'cheese']
my_pizzas = friends_pizzas[:]

my_pizzas.append('pineapple')
friends_pizzas.append('sausage')

print("\nMy favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friend's favorite pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza)
