# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:28:18 2018

@author: Simon

Classe correspondant aux cartes placées au milieu.
-Le pli est gagné à la fin de chaque tour de table
-A chaque tour, on lui ajoute la carte cliquée par le joueur

"""


class Trick:
    
    def __init__(self, parent):
        self.__parent_canvas = parent
        self.__position = (self.__parent_canvas.get_width()//2-40,self.__parent_canvas.get_height()//2-40)
        self.__cards = []
        
    def add_card(self,card,pos):
        card.add_trick(pos)
        self.__cards.append(card)
        
    def get_cards(self):
        return self.__cards
    
    def get_parent(self):
        return self.__parent_canvas
    
    def get_position(self):
        return self.__position
    def set_position(self,pos):
        self.__position = pos