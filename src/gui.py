from tkinter import *
from Infrastructure import RuleWrapper
from Infrastructure import RuleGetter
from Infrastructure import PlayerManager

def addPlayer():
    player = playerEntry.get()
    getter.addPlayer(player)
    print(getter.getPlayers())
    players.append(Label(window,text = player))
    players[len(players)-1].grid(column=0, row=len(players)+2)
    playerEntry.delete(0,'end')

def next():
    regle = getter.getRandomRule()
    print(regle)
    rule.configure(text = regle)
    


getter = RuleGetter.RuleGetter([])
players =[]


window = Tk()
window.title("Chillcolo")
window.geometry('1500x800')

lbl = Label(window, text="Joueurs : ")
lbl.grid(column=0, row=0)



playerEntry = Entry(window,width=150)
playerEntry.grid(column=1, row=0)
playerEntry.focus()

adp = Button(window, text="Add Player", command=addPlayer)
adp.grid(column=2, row=0)

rule = Label(window, text="", font =("Courier",40), wraplength = 1000)
rule.grid(column=1, row=2)

play = Button(window, text="Next", command=next)
play.grid(column=3, row=0)


window.mainloop()


