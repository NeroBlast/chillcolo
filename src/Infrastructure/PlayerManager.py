
import random

class PlayerManager:

    players = []
    playerOccurence = {}

    def __init__(self,allPlayers):
        
        self.players = allPlayers
        for player in self.players:
            self.playerOccurence[player]=0
        
    def addPlayer(self,player):
        self.players.add(player)

    def pickPlayers(self,amount):
        choosen = []
        players = self.players[:]
        # print(str(amount))
        # print(players)
        n = amount
        while n > 0:
            player = random.choice(players)
            players.remove(player)
            self.playerOccurence[player] += 1
            choosen.append(player)
            n = n-1
        return choosen

    #TODO
    def pickPlayersFairly(self):
        return 0

    def getPlayerOccurence(self):
        return self.playerOccurence
    
    def getPlayers(self):
        return self.players


