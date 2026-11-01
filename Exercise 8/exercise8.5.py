def describe_city(city, country='USA'):
    """Display a message about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")
    
describe_city('new york')
describe_city('paris', 'france')
describe_city('tokyo', 'japan')