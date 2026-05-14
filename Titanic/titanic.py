import csv

RECORDS = []
HEADINGS = []

def load_data(file_path): 
    global HEADINGS
    print("loading data....", end="")

    with open(file_path) as file:
        csv_reader = csv.reader(file)
        HEADINGS = next(csv_reader)
       
        
        for value in csv_reader:
            RECORDS.append(value)
        print("Done!")
        


def display_menu():
  
    user_choice = int(input("""
  Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
  [5] Display the number of survivors per age group
 

  """))
    return user_choice


def display_passanger_names():
    print("The name of the passangers are :")

    for record in RECORDS:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0

    for record in RECORDS:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived+=1
    print(f"{num_survived} passenger survived")


def display_num_passengers_per_gender():
    females = 0
    males = 0
    for record in RECORDS:
        gender = record[4]
        if gender == "male":
            males+=1
        else:
            females+=1
    print(f"females: {females}, males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in RECORDS:
     if record[5] != "":
      age = float(record[5])
      if age < 18:
        children += 1
      elif age < 65:
        adults += 1
      else:
        elderly += 1
  
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")



def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    children_survivors = 0
    adult_survivors = 0
    elderly_survivors = 0
    


    for record in RECORDS:
     survived = int(record[1])
     if record[5] != "":
      age = float(record[5])
      if age < 18:
        children += 1
        if survived == 1:
           children_survivors+=1
      elif age < 65:
        adults += 1
        if survived == 1:
           adult_survivors+=1
           
      else:
        elderly += 1
        if survived == 1:
           elderly_survivors+1
  
    print(f"children: {children_survivors}/{children}, adults: {adult_survivors}/{adults}, elderly: {elderly_survivors}/{elderly}")


   



def run():
    load_data("D:/VS directory/Python/Projects/Titanic/titanic.csv")
    num_records = len(RECORDS)
    print(f"Successfully loaded {num_records} records.")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 1:
        display_passanger_names()
    if selected_option == 2:
        display_num_survivors()
    if selected_option == 3:
        display_num_passengers_per_gender()
    if selected_option == 4:
        display_passengers_per_age_group()
    if selected_option == 5:
       display_survivors_per_age_group()



if __name__ == "__main__":
    run()

    