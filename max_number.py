numbers = []

for i in range(5):
    user_number = int(input("enter number: "))
    numbers.append(user_number)


max_num = numbers[0]

for i in numbers:
    if i> max_num:
        max_num = i
print(max_num)
