# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:21:31 2018

@author: Simon
"""

from tkinter import *
from playing_card_GUI import *
from playing_field import *

class Window(Tk):
    
    def __init__(self,width,height):
        
        assert self.__class__ is not Window #Classe absraite
        Tk.__init__(self)
        self.__width = width
        self.__height = height    
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
        
#La fenêtre de jeu principale
class GameWindow(Window):
    
    def __init__(self,w,h):
        Window.__init__(self,w,h)
        self.__field = Playing_Field(self)
        self.__field.pack()
        
    def show(self):
        self.__field.place_hands()
        #Juste un test sur une carte, vérifier ce que veut dire l'erreur : "pyimage... doesn't exist"
    def get_field(self):
        return self.__field
    
win = GameWindow(1200,650)

'''On met le contenu du jeu ici'''
#On détecte à chauqe instant les mouvements de la souris

win.show()

#Gestion des évênements souris
def mouse_moving(event):
    players = win.get_field().get_players()  
    for p in players:
        cards = p.get_hand().get_cards()
        for c in cards:
            c.hitbox_listener(event)
  
def mouse_clicked(event):
    players = win.get_field().get_players()  
    for p in players:
        cards = p.get_hand().get_cards()
        for c in cards:
            c.click_listener(event)
      
win.bind('<Motion>',mouse_moving)
win.bind('<Button-1>',mouse_clicked)
win.mainloop()