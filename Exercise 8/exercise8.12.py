def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")


make_sandwich('ham', 'cheese')
make_sandwich('chicken', 'lettuce', 'tomato')
make_sandwich('beef', 'cheese', 'onion', 'sauce')