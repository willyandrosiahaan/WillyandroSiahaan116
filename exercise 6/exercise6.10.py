fav_num = {
    'Alice': [7, 12],
    'Bob': [42, 15],
    'Charlie': [13, 22],
    'Diana': [5, 81],
    'Eve': [23, 1]
}
for name, numbers in fav_num.items():
    print(f"{name}.")
    for number in numbers:
        print(f"  - {number}.")
