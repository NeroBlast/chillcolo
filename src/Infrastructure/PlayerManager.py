
class PlayerManager:

    players = []
    playerOccurence = {}

    def __init__(self,allPlayers):
        self.players = allPlayers
        for player in self.players:
            self.playerOccurence[player]=0
        
    def addPlayer(self,player):
        self.players.add(player)

    def getPlayerOccurence(self):
        return self.playerOccurence
    
    def getPlayers(self):
        return self.players


