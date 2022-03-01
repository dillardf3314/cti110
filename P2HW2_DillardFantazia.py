# CTI-110
# P2HW2 - Score Avg
# Fantazia Dillard 
# Date 28/Feb/2022
#Write program creating list of scores
#Find and drop lowest score
#Print low score, modified list, and average score
#


score_1 = float(input(' Enter score #1 ' ))
score_2 = float(input(' Enter score #2 ' ))
score_3 = float(input(' Enter score #3 ' ))
score_4 = float(input(' Enter score #4 ' ))
score_5 = float(input(' Enter score #5 ' ))
score_6 = float(input(' Enter score #6 ' ))
score_7 = float(input(' Enter score #7 ' ))
my_scores = [ score_1, score_2, score_3, score_4,score_5, score_6,  score_7 ]



lowest_score = min(my_scores)
my_scores.remove(lowest_score)
average_score = sum(my_scores)/len(my_scores)



print('Lowest Score :', lowest_score)
print('Modified List :', my_scores)
print('Scores Average :', average_score)
