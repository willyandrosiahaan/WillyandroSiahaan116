def city_country(city, country):
    """Display a message about a city and its country."""
    format = f"{city}, {country}"
    return format.title()

city= city_country('paris', 'france')
city2= city_country('new york', 'usa')
city3= city_country('tokyo', 'japan')
print(city)
print(city2)
print(city3)