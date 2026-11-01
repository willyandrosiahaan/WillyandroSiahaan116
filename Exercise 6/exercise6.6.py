favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
name = {'jen', 'sarah', 'edward', 'phil', 'james'}
for person in name:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}.")
    else:
        print(f"{person.title()}, please take our poll!")