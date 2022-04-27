#
# Create python code that adds or subtract two random numbers
#Create menu with options of add, subtract ,and exit
# 27/April/2022
# CTI-110 P5HW2 - Math Quiz
# Fantazia Dillard
#


import random


print("MAIN MENU")
print("---------------------")
print("1. Adding Random Numbes")
print("2. Subtracting Random Numbers")
print("3. Exit")
print()
user_input = int(input("Please choose one of the menu options:"))


while user_input == 1:
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        print(" ",num1)
        print("+",num2)
        user_answer = int(input(""))
        answer = num1 + num2

        while answer == num1 + num2:
            if user_answer < answer:
                 print("Sorry, guess is too low")
                 user_answer = int(input("Try again:"))
            elif user_answer > answer :
                 print ("Sorry, guess is too high")
                 user_answer = int(input("Try again:"))
            else:
                 print("Congratulations!!!! your answer is correct...")
                 break
                 continue

while user_input == 2:
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        print(" ",num1)
        print("-",num2)
        user_answer = int(input(""))
        answer = num1 - num2

        while answer == num1 - num2:
                if user_answer < answer:
                        print("Sorry, guess is too low")
                        user_answer = int(input("Try again:"))
                elif user_answer > answer :
                         print ("Sorry, guess is too high")
                         user_answer = int(input("Try again:"))
                else:
                         print("Congratulations!!!! your answer is correct...")
                         break
                         continue

while user_input == 3:
        print("Thank you for playing...")
        print("Bye!!")
        break

while user_input > 3:
         print("INVALID CHOICE!!!! Please enter option 1,2,or 3")
         user_input = int(input("Please choose one of the menu options:"))
         continue
    
 
    
