#Philip Afful Nunoo
#Part II lab 06
####################Player Class######################
import datetime
import time
from datetime import date

class Player:
    def __init__(self,firstname,lastname,team = None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,score):
        self.scores.append(score)

        return

    def total_score(self):
        sum1 = 0.00
        for i in self.scores:
            sum1 = sum1 + i            

        return sum1

    def average_score(self):
        average = self.total_score()/len(self.scores)
        return average

newPlayer = Player('David','Beckham')
playerScore = [0, 0, 1, 0,1]
for score in playerScore:
    newPlayer.add_score(score)

print "The average is : "
print newPlayer.average_score()


#Philip Afful Nunoo
#Part III lab 06
######################Team Class###########################
class Team:
    def __init__(self,name,league,manager_name,points, players = None):
        self.team_name = name
        self.team_league = league
        self.team_manager_name = manager_name
        self.team_points = points
        self.team_players = []

    def add_player(self,player):
        self.team_players.append(player)

    def __str__(self):
        string = "\nTeam: "+self.team_name
        string = string + "\nLeague: " + self.team_league
        string = string + "\nPoints: "+ str(self.team_points)
        return string#"Team:",self.team_name,"in league",self.team_league

portugal = Team('portugal','pgLeague','Kofi',21)
spain = Team('spain','spLeague','Kwadwo',16)

print portugal
print spain

torres = Player('Fernando','torres','spain')
ronaldo = Player('Christiano','ronaldo','portugal')

spain.add_player(torres)
portugal.add_player(ronaldo)

##############Match Class######################

class Match:
    def __init__(self,homeTeam,awayTeam,datePlayed):
        self.home_team = homeTeam
        self.away_team = awayTeam
        self.date = datePlayed
        self.home_scores = {}
        self.away_scores = {}

    def home_score(self):
        sum1 = self.home_scores.values()
        return sum1

    def away_score(self):
        sum1 = self.away_scores.values()
        print sum1
        return sum1 

    def winner(self):
        
        if self.home_score()>self.away_score():
            return self.home_team
        elif self.away_score()>self.home_score():
            return self.away_team
        else:
            return "Draw"

    def add_score(self,player,score):
        result = {}
        result = {"team":player.team}
        
        if (player.team == self.home_team):
            result = {"type": "home"}
            self.home_scores = {player.last_name:score}
            print self.home_scores
        else:
            #result = {"type": "away"}
            #self.away_scores = {player.last_name:score}
            #print self.away_scores
            if (self.away_scores[player.last_name]):
                self.away_scores[player.last_name] += score
            else:
                self.away_scores = {player.last_name:score}

        player.add_score(score)
        
        return result

euro_semi_final = Match('spain','portugal',date(2012,6,23))
euro_semi_final.add_score(ronaldo, 5)
euro_semi_final.add_score(torres, 1)

print "The winner is: ", euro_semi_final.winner()
