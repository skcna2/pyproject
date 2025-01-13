from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")

while True:
    first = input("\nintroduce tu nombre: ")
    if first == 'q':
        break
    last = input("introduce tu apellido: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"\tNeatly formatted name: {formatted_name}.")
    assert formatted_name == f"{first} {last}"

