car_started = False  # The car is initially stopped

while True:
    print("\n--- CAR MENU ---")
    print("Type 'start' to start the car")
    print("Type 'stop' to stop the car")
    print("Type 'quit' to exit the program")
    
    command = input("> ").lower()  # Ask the user for input

    if command == "start":
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("Car started... Ready to go!")
    
    elif command == "stop":
        if not car_started:
            print("Car is already stopped!")
        else:
            car_started = False
            print("Car stopped.")
    
    elif command == "quit":
        print("Exiting the car simulator...")
        break  # Exit the while loop
    
    else:
        print("I don't understand that. Please type start, stop, or quit.")