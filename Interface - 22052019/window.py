# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:21:31 2018

@author: Simon
"""

from tkinter import *
from playing_card_GUI import *
from playing_field import *
from game import *
import time

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
        self.__count = 0
        #La fenêtre contient aussi le déroulement de la partie
        #Variables cruciales pour situer le programme dans le déroulement de la partie.
        self.__doing_dog = False
        self.__end_turn = False
        self.__counter_cards_dog = 0
        self.time1 = 0
        self.time2 = time.time()
      
    def set_doing_dog(self,b):
        self.__doing_dog = b
        
    def get_doing_dog(self):
        return self.__doing_dog
    def set_count(self,n):
        self.__count = n
        if self.__count < 0:
            self.__count = 0
    def get_count(self):
        return self.__count
    def set_end_turn(self,b):
        self.__end_turn = b
        
    def get_end_turn(self):
        return self.__end_turn
    
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
        elif p.is_playing():
            playable = p.playable_cards(win.get_field().get_trick())
            for c in cards:
                if c in playable:
                    c.hitbox_listener(event)
  
def mouse_clicked(event):
    flag = True
    players = win.get_field().get_players() 
    win.set_count(win.get_count()+1)
    double = False
    #Gestion du double clic (il faut que l'écart de temps soit supérieur à 1s)
    if win.get_count()%2 == 0:
        win.time1 = time.time()
    else: 
        win.time2 = time.time()
    if abs(win.time1 - win.time2)<1:
        print("DOUBLE CLIC")
        double = True
    if double:
        win.set_count(win.get_count()-1)
        double = False
    else:
        for p in players:
            cards = p.get_hand().get_cards()
            #Il faut vérifier qu'on clique bien dans la hitbox
            if p.is_bidder() and win.get_doing_dog():          
                for c in cards:
                    c.click_listener(event)
                    if c.is_clicked():
                        win.inc_cards_dog()
                        c.set_clicked(False)
                        if win.get_counter_cards_dog() == 6: 
                            #On double la détection ici pour que la 6e carte cliquée aille bien dans le chien
                            print("fin chien")  
                            event.x,event.y = 0,0
                            time.sleep(0.5)
                            win.set_doing_dog(False)
                            #Fonciton permettant à la partie de se lancer (on a fini de mettre en place le jeu)
                            basic_game.start_turn_seg_1(basic_game.get_dealer(),basic_game.get_players(),basic_game.get_bidder(),None)
                    
            elif p.is_playing() and isinstance(p,Human):
                playable = p.playable_cards(win.get_field().get_trick())
                #if win.get_field().excuse_played():
                    #if win.get_field().get_player_excused() == win.get_field().get_first(): #Si celui qui a joué l'excuse est le premier à jouer
                '''new_trick = Trick(win.get_field())
                    for c in win.get_field().get_trick(): #On fait ignorer à "playable_cards" que l'excuse a été jouée
                        if type(c) != Excuse:
                            new_trick.add_card(c,(-100,-100))
                    playable = p.playable_cards(new_trick)
                else:'''
                for c in cards:
                    if c in playable:
                        c.enable()
                        c.click_listener(event)
                        if c.is_clicked():
                            #print("carte ",c," jouee")
                            p.play(c,win.get_field().get_trick())
                            #p.get_hand().show()
                            p.set_playing(False)
                            flag = False
                            basic_game.start_turn_seg_2()
                            win.set_count(0)
                            break
    if win.get_count()%2 == 0:
        win.time1 = time.time()
    else: 
        win.time2 = time.time()
    if abs(win.time1 - win.time2)<1:
        print("DOUBLE CLIC")
        double = True
    if double:
        win.set_count(win.get_count()-1)
        double = False
    else:
        if win.get_end_turn() and win.get_count() == 1:
            basic_game.start_turn_seg_3()
            win.set_count(0)
        #flag =True #permet de ne pas jouer plusieurs fois de suite
    print(win.get_count())
win.bind('<Motion>',mouse_moving)
win.bind('<Button-1>',mouse_clicked)

basic_game.begin_game(3)

win.mainloop()