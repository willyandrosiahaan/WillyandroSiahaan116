cities = [
    {'name': 'paris', 'country': 'france', 'population': 2148327, 'fact': 'The Eiffel Tower is one of the most famous landmarks in the world.'},
    {'name': 'new york', 'country': 'usa', 'population': 8419600, 'fact': 'The Statue of Liberty is a symbol of freedom and democracy.'},
    {'name': 'sydney', 'country': 'australia', 'population': 5312163, 'fact': 'Sydney Opera House is one of the most distinctive buildings in the world.'}
]
for city in cities:
    if city['name'] == 'new york':
        print(f"{city['name'].title()} is a city in {city['country'].upper()} with a population of {city['population']}. {city['fact']}")
    else:
        print(f"{city['name'].title()} is a city in {city['country'].title()} with a population of {city['population']}. {city['fact']}")
    