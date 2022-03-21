# CTI-110
# P3HW2 - Pizza Order
# Fantazia Dillard
# 21-Mar-2022
# Ask user to input number of students
# Ask user to input number of students sharing pizza
# Out put number of students , pizza and price
#


import math

num_students = int(input('How many students do you want to order pizza for?'))
people_per_pizza = float(input('Enter number of people per pizza (1.5, 2, 3):'))
num_pizza = num_students/people_per_pizza

    
if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
    num_pizza = math.ceil(num_pizza)



    num_pizza = num_students/people_per_pizza
    num_pizza = math.ceil(num_pizza)
    price = num_pizza * 5
    tax = (price * .06)

    print('----Pizza Order--------')
    print('Number of Students :', num_students)
    print('Pizza Needed:', num_pizza)
    print(f'Price :${price + tax:.2f}')
    print()

else:
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2, 3')
    print()
    print('Run program again')
