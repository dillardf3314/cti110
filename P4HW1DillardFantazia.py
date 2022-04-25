# CTI-110
# P4HW1 - Score Avg
# Fantazia Dillard 
# Date 25/April/2022
# get user input 
# create loop
# if invalid in put have user enter correct input
# Print lowest score, modified list, average, and grade
#












num_score = int(input('How many scores would you like to enter?'))
#score = float(input('Enter score :'))
count = 0
my_scores = []

while count != num_score:
    score = float(input('Enter score:'))

    if score < 0 or score > 100:
        print('INVALID Score Entere!!!!')
        print('Score should be between 0 and 100')
        score = float(input('Re-enter Score:'))
    else:
        my_scores.append(score)
        count += 1



lowest_score = min(my_scores)
my_scores.remove(lowest_score)
average = sum(my_scores)/len(my_scores)


A_average = 90
B_average = 80
C_average = 70
D_average = 60




if average >= A_average:
    grade = 'A'
elif average >= B_average:
    grade = 'B'

elif average >= C_average:
    grade = 'C'

elif average >= D_average:
    grade = 'D'

else:
    grade = 'F'


print('-----------Results-------------')
print('Lowest Score :', lowest_score)
print('Modified List :', my_scores)
print('Scores Average :', average)
print('Grade          :', grade)

    

