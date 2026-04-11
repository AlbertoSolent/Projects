numbers = [4, 1, 9, 2, 7]
max_num = numbers[0]
second_max = numbers[1]
for num in numbers:
    if num> max_num:
        second_max = max_num
        max_num = num
        
    elif num < max_num and num >second_max:
        second_max = num
print(second_max)