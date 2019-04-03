# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:21:31 2018

@author: Simon
"""

from tkinter import *
from playing_card_GUI import *
from playing_field import *
from game import *

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
        
        #La fenêtre contient aussi le déroulement de la partie
        #Variables cruciales pour situer le programme dans le déroulement de la partie.
        self.__doing_dog = False
        self.__counter_cards_dog = 0
      
    def set_doing_dog(self,b):
        self.__doing_dog = b
        
    def get_doing_dog(self):
        return self.__doing_dog
        
    def show(self):
        self.__field.place_hands()
        
    def inc_cards_dog(self):
        self.__counter_cards_dog += 1
    
    def get_counter_cards_dog(self):
        return self.__counter_cards_dog
        
    def get_field(self):
        return self.__field
    
win = GameWindow(1200,650)

'''On met le contenu du jeu ici'''
#On détecte à chauqe instant les mouvements de la souris
basic_game = Game(win.get_field(),win)

win.show()

#Gestion des évênements souris
def mouse_moving(event):
    players = win.get_field().get_players()  
    for p in players:
        cards = p.get_hand().get_cards()
        #print(p.is_bidder())
        if p.is_bidder() and win.get_doing_dog():
            for c in cards:
                c.hitbox_listener(event)
  
def mouse_clicked(event):
    players = win.get_field().get_players()  
    for p in players:
        cards = p.get_hand().get_cards()
        if p.is_bidder() and win.get_doing_dog():
            win.inc_cards_dog()
            if win.get_counter_cards_dog() == 6:
                win.set_doing_dog(False)
                #Fonciton permettant à la partie de se lancer (on a fini de mettre en place le jeu)
                basic_game.start_turn(basic_game.get_dealer(),basic_game.get_players(),basic_game.get_bidder())
            for c in cards:
                c.click_listener(event)

win.bind('<Motion>',mouse_moving)
win.bind('<Button-1>',mouse_clicked)

basic_game.begin_game(3)

win.mainloop()