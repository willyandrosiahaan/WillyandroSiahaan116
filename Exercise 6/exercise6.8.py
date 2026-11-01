pet = [
    {'animal': 'cat', 'owner': 'alice'},
    {'animal': 'dog', 'owner': 'bob'},
    {'animal': 'bird', 'owner': 'charlie'}
]
for pet in pet:
    print(f"{pet['owner'].title()} owns a {pet['animal']}.")