while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")
        