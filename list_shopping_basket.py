user_basket = []
prices = []

user_choice = input("Enter an item (or 'done' to finish): ").lower()

while user_choice != "done":

    if user_choice == "":
        print("Invalid input!")

    elif user_choice.startswith("remove "):
        item_to_remove = user_choice.replace("remove ", "")

        if item_to_remove in user_basket:
            index = user_basket.index(item_to_remove)
            user_basket.pop(index)
            prices.pop(index)
            print(f"{item_to_remove} removed!")
        else:
            print("Item not in basket")

    elif user_choice in user_basket:
        print("Item already in basket")

    else:
        user_basket.append(user_choice)
        price = float(input("Enter price: "))
        prices.append(price)

    user_choice = input("Enter an item (or 'done' to finish): ").lower()

# --- Final receipt ---
total = 0
print("\nYour shopping list:")
for i in range(len(user_basket)):
    print(f"{user_basket[i]} - ${prices[i]:.2f}")
    total += prices[i]

print(f"Total: ${total:.2f}")