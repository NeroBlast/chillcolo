from Infrastructure import PlayerManager
lstplayers = ["Vincent","Charlie","PE","David","Aurelian","Connard"]
manager = PlayerManager.PlayerManager(lstplayers)

occurence = manager.getPlayerOccurence()
print(occurence)

players = manager.getPlayers()
print(players)
