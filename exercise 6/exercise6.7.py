people = [
    {'first_name': 'jose', 'last_name': 'benedict', 'age': '19', 'city': 'pontianak'},
    {'first_name': 'gilbert', 'last_name': 'boen', 'age': '19', 'city': 'pontianak'},
    {'first_name': 'kieron', 'last_name': 'leon', 'age': '19', 'city': 'pontianak'}
]
for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}, Age: {person['age']}, City: {person['city'].title()}")

 