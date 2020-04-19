from Infrastructure import RuleWrapper
from Infrastructure import RuleGetter
from Infrastructure import PlayerManager


def main():
    players = []
    #Starting
    while True:
        print("Enter a player / type play when ready")
        line = input()
        if(line=="play" or line == ""):
            break
        players.append(line)
        print(players)
    
    getter = RuleGetter.RuleGetter(players)

    while True:
        print("Next?")
        line = input()
        if line == "quit":
            break
        rule = getter.getRandomRule()
        print(rule)
    
    


main()