import random
import time


list_of_numbers = []
list_lenght_max = 10
value = 0
while True:
    number = random.randint(1,6)
    print(number)
    
    if number < 5:
        value = 1
    elif number > 7:
        value = 2
    else: value = 0

    list_of_numbers.append(value)

    if len(list_of_numbers) > list_lenght_max:
        del list_of_numbers[0]

    if list_of_numbers[0] == 1 and list_of_numbers[len(list_of_numbers) - 1] == 1 and list_of_numbers.count(1) >= 7 :
        print("Turn left")

    if list_of_numbers[0] == 2 and list_of_numbers[len(list_of_numbers) - 1] == 2 and list_of_numbers.count(1) >= 7:
        print("Turn Right")

    time.sleep(0.5)