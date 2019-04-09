# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:45:50 2019

@author: simon
"""
from playing_card_GUI import * 


class Dog:
    
    def __init__(self, parent):
        self.__parent_canvas = parent
        self.__position = (self.__parent_canvas.get_width()-250,self.__parent_canvas.get_height()-150)
        self.__cards = []
        
    def add_card(self,card):
        card.add_dog(self)
        self.__cards.append(card)
        #Il faut raise une erreur ici si le nombre de cartes dans le chien est trop grand
     
    def get_cards(self):
        return self.__cards
    
    def get_length(self):
        return len(self.__cards)
        
    def get_parent(self):
        return self.__parent_canvas
    
    def get_position(self):
        return self.__position
    
    def give_cards(self,player):
        player.add_dog(self)
        
        self.__cards = []
    
    def show_dog(self,canvas):
        i=0
        for c in self.__cards:
            c.set_position(self.__position[0] +i*WIDTH*0.35,self.__position[1])
            i+=1
            #c.set_face_up(True) #A créé dans la classe Playing_Card_GUI
            c.draw(canvas)