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
        
    def insert_card(self,card,index):
        #Cette méthode permet d'ajouter une carte à la liste sans la mettre nécessairement
        #Physiquement dans le trick (seulement pour l'excuse !!!!)
        self.__cards = self.__cards[:index]+[card]+self.__cards[index:]
    def remove_card(self,index):
        #Utilisation restreinte à l'excuse seulement ! sinon bug !!
        self.__cards = self.__cards[:index]+self.__cards[index+1:]
    def get_cards(self):
        return self.__cards
    
    def get_parent(self):
        return self.__parent_canvas
    
    def get_position(self):
        return self.__position
    def set_position(self,pos):
        self.__position = pos