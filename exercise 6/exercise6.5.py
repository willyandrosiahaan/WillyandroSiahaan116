river = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}
for river,country in river.items():
    print(f"The {river.title()} runs through {country.title()}.")