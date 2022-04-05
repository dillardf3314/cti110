# CTI-110
# P4HW1 - Score Avg
# Fantazia Dillard 
# Date 4/Mar/2022
# get user input 
# create loop
# if invalid in put have user enter correct input
#

num_score = int(input('How many scores would you like to enter?'))
score = float(input(' Enter score: ' ))
count = 0
my_scores = [0]

while count == num_score:
    num_score = int(input())
    my_scores.append(num_score)



    if count >= 100:
        print('INVALID Score Entered!!!!')
        print('Score should be between 0 and 100')
    score = float(input())
    if count <= 0:
        print('INVALID Score Entered!!!!')
        print('Score should be between 0 and 100')
    score = float(input())


        
else:
 my_scores.append(score)










lowest_score = min(my_scores)
my_scores.remove(lowest_score)
average_score = sum(my_scores)/len(my_scores)


print('-----------Results-------------')
print('Lowest Score :', lowest_score)
print('Modified List :', my_scores)
print('Scores Average :', average_score)

