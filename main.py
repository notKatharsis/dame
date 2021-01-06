import board
from GameHandler import *
from tkinter import *

gameHandler = GameHandler()



import os

#++++++++++Commands++++++++++#
def shutdown(): #Beenden des Spiels
    root.destroy()
    
def reset(): #Spiel soll neugetartet werden
    pass #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ERGÄNZEN]

def surrender():
    label4.config(text = "Player {} has surrendered".format(player), bg ='#cccccc')
    
##########################
canvashohe = 700 #Breite = 1.5Höhe[1.0 für Feld| 0.5 für Seitenmenü]
root = Tk()
root.geometry('{}x{}'.format(str(canvashohe*3/2)[:-2],canvashohe))
#root.resizable(0, 0)
root.title("Draughts")

#++++++++++Menu++++++++++#
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="exit", command=shutdown)
menubar.add_cascade(label="Datei", menu=filemenu)
root.config(menu=menubar, background='#4a536b')

#++++++++++Widgets++++++++++#
randabstand = 10
buttonhohe = 4*randabstand
schachbrett = relheight =(1-randabstand/canvashohe*2) #relative Seitenlänge des Schachbretts

#Platzhalter für das Board
board = board.Board(8, 80, root, randabstand, schachbrett, canvashohe*schachbrett) 
#t = Text(root, wrap = WORD)
#t.insert(END, 'This is an example text.')
#t.place(x = randabstand, y = randabstand, relheight =schachbrett, width = canvashohe*schachbrett)


counter = 15   #Anzahl der gesamten Spielzüge; muss nach jedem Zug aktualisiert werden <<<<<<<<<<<<<<<<[ERGÄNZEN]
bluepoints = 5 #muss nach jedem Zug aktualisiert werden <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ERGÄNZEN]
redpoints = 20 #muss nach jedem Zug aktualisiert werden <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[ERGÄNZEN]

if counter%2 == 0:
    player = "BLUE"
    farbe='#b1f8fe'
elif counter%2 == 1:
    player = "RED"
    farbe='#ff785b'

#SpielerZug Anzeige    
label1= Label(text="Player {} is playing".format(player), bg='{}'.format(farbe))
label1.place(x = canvashohe*schachbrett+2*randabstand, y= randabstand, width = canvashohe/2-randabstand, relheight = 0.08)

#BLAU Punkteanzeige
label2= Label(text="Player Blue::    {} points".format(bluepoints), bg='#aed6dc')
label2.place(x = canvashohe*schachbrett+2*randabstand, y= randabstand+(buttonhohe+randabstand), width = canvashohe/2-randabstand, relheight = 0.08)

#ROT Punkteanzeige
label3= Label(text="Player Red:    {}points".format(redpoints), bg='#ff9a8d')
label3.place(x = canvashohe*schachbrett+2*randabstand, y= randabstand+2*(buttonhohe+randabstand), width = canvashohe/2-randabstand, relheight = 0.08)

#Gegner hat aufgegeben - Nachricht
label4= Label(bg='#4a536b')
label4.place(x = canvashohe*schachbrett+2*randabstand, y= randabstand+3*(buttonhohe+randabstand), width = canvashohe/2-randabstand, relheight = 0.08)



#Aufgeben Button
button1 = Button(text="surrender", bg="#BBBBBB",fg="black", command=surrender)
button1.place(x = canvashohe*schachbrett+2*randabstand, y= canvashohe-3*(buttonhohe+randabstand) - 20, width = canvashohe/2-randabstand, relheight = 0.08) #row = 0, column = 0, sticky = W, pady = 2

#Neustart Button
button4 = Button(text="reset", bg="#BBBBBB",fg="black", command=reset) #command reset fehlt noch (siehe oben unter COMMANDS)
button4.place(x = canvashohe*schachbrett+2*randabstand, y= canvashohe-2*(buttonhohe+randabstand) - 20, width = canvashohe/2-randabstand, relheight = 0.08)

#Spiel Beenden Button
button5 = Button(text="Exit Game", bg="#BBBBBB",fg="black", command=shutdown)
button5.place(x = canvashohe*schachbrett+2*randabstand, y= canvashohe-(buttonhohe+randabstand) - 20, width = canvashohe/2-randabstand, relheight = 0.08)

#----------Widgets----------#


def onClick(event):
    gameHandler.select(event, board)

board.canvas.bind("<Button-1>", lambda event: onClick(event))

x = board.get_board()

root.mainloop()
