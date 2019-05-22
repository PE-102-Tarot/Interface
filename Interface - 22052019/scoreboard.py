# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:39:36 2019

@author: gouwa
"""
from tkinter import *

class Scoreboard(Toplevel):
    
    def __init__(self,parent,nb_players,score,winner):
        Toplevel.__init__(self,parent)
        self.geometry("200x200")
        self.title = "Tableau des scores"
        self.parent = parent
        self.main_text = Label(self,text="RESULTATS DE LA PARTIE",padx=5,pady=5,justify='center')
        self.main_text.pack()
        
        self.winner = winner
        txt = ""
        if winner == 'D':
            txt = "La défense remporte la partie"
        else:
            txt = "Le joueur ",bidder," remport la partie"
        
        infos = []
        
        for i in range(nb_players):
            lab = Label(self,text="Joueur "+str(i)+" : "+str(score[i]),padx=2,pady=2,justify='left')
            lab.pack()
            infos.append(lab)
        
        self.win_text = Label(self,text=txt)
        self.win_text.pack()
        
        self.restart = Button(self,text="Recommencer")
        self.restart.pack()
        self.quit = Button(self,text="Quitter",command=self.finish)
        self.quit.pack()
        
    def show(self):
        self.mainloop()

    def finish(self):
        self.parent.destroy()
        self.destroy()
    
    