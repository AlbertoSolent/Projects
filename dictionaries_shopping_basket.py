fruit_prices = {
        "apple": 1.20,
        "banana": 0.80,
        "orange": 1.00
    }


while True:
        print("\n--- Fruit Price Menu ---")
        print("1. Look up a fruit")
        print("2. Add a new fruit")
        print("3. Update a price")
        print("4. View all fruits")
        print("5. Exit")

        user_choice = int(input("Enter your choice 1-5: "))

        if user_choice == 1:
                for k in fruit_prices.keys():
                        print(k)

                fruit = input("\nenter a fruit name: ").lower()
                if fruit in fruit_prices:
                    print(f"{fruit} costs {fruit_prices[fruit]:.2f}")
                else:
                    print(f"sorry {fruit} doesent exist")

        elif user_choice == 2:
            fruit_to_add = input("\nAdd a new fruit: ").lower()
            new_fruit_price = float(input("Enter price: "))
            fruit_prices[fruit_to_add] = new_fruit_price
            print(f"{fruit_to_add} added succesfully ")

        elif user_choice == 3:
              for k, v in fruit_prices.items():
                        print(f"{k}: ${v}")

              fruit_to_update = input("\nEnter fruit to update: ")
              new_price = float(input("Enter new price: "))
              fruit_prices[fruit_to_update] = new_price
              print("price updated succesfully")
        elif user_choice == 4:
               print("Updated menu")
               for k, v in fruit_prices.items():
                        print(f"{k}: ${v}")

        elif user_choice == 5:
               break
print("\nGood Bye !")
               
        





