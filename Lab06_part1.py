"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""
import time
from datetime import date
## create the player_stats data structure

player_stats = {
                'rooney' :[(date(2012,6,23),2),
                           (date(2012,6,25),2)],
                'ronaldo':[(date(2012,6,19),0),
                           (date(2012,6,20),3)],
                'torres' :[(date(2012,6,21),0),
                           (date(2012,6,21),1)]
                }


## implement highest_score
def highest_score(player_stats):
    highest_score = 0
    highest_scorer = []
    for i in player_stats:
        for j in player_stats[i]:
            if (j[1] > highest_score):
                highest_score = j[1]
                highest_scorer = (i,j[0],j[1])
    return highest_scorer

## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    highest_score_for_player = 0

    for i in player_stats[player]:
        if (i[1] > highest_score_for_player):
            highest_score_for_player = i[1]
    return highest_score_for_player

## implement highest_scorer
def highest_scorer(player_stats):
    highest_scorer = ""
    score = 0
    list1={}
    for i in player_stats:
        sum1 = 0
        for j in range(len(player_stats[i])):
            sum1 = sum1 + player_stats[i][j][1]
            list1[i]=sum1
    for i in list1:
        if (list1[i] >= score):
            highest_scorer = i
    return highest_scorer

"""
Dictionary with Tuples:
The name of the player serves as a Key which has
a list of tuples of when the players played and
the goals scored

this way we can refrence the date the goals were
scored by the players
"""
