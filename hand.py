# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:34:25 2018

@author: Simon
"""
from playing_card_GUI import *

WIDTH = 48
HEIGHT = 89

class Hand():
    
    def __init__(self, cards, position,placement):
        self.__cards = cards #On indique a la main quelles cartes elle possède
        self.__position = position
        self.__position_ini = position
        
        #Une main possède un joueur
        self.__player = None
        
        #Le placement permet de repérer la situation géographique de la main
        self.__placement = placement
        
        for i in range(len(self.__cards)):
            if i == len(self.__cards)-1:
                self.__cards[i].set_first(True)
                
            self.__cards[i].set_position(self.__position[0]+i*WIDTH*0.35,self.__position[1])
            #On affiche les cartes l'une à côté de l'autre ici
            #Peut etre prévoir un affichage différent pour les mains de côité ?
        
    '''Les deux fonctions suivantes permettront d'afficher ou de cacher la main en fonction
    de si le joueur concerné joue ou non'''
    
    def get_placement(self):
        return self.__placement
    
    def get_cards(self):
        return self.__cards
    def get_player(self):
        return self.__player
    def set_player(self,player):
        self.__player = player
    def add_cards(self,cards):
        for i in range(len(cards)):
            cards[i].set_position(self.__position[0]+(len(self.__cards)+i)*WIDTH*0.35,self.__position[1])
        self.__cards = self.__cards + cards
    def set_cards(self,cards):
        self.__cards = cards
    
    #inutilisée
    def replace(self):
        '''permet de repositionner toute la main, notamment lorsque le chien va être fait
        ou a été fait'''
        for i in range(len(self.__cards)):
            if i == len(self.__cards)-1:
                self.__cards[i].set_first(True)
                
            self.__cards[i].set_position(self.__position[0]+i*WIDTH*0.35,self.__position[1])
            self.show()
    def show(self):    
        for c in self.__cards:
            #c.set_face_up(True) #A créé dans la classe Playing_Card_GUI
            c.draw(c.get_parent())
    def hide(self):
        for c in self.__cards:
            c.set_face_up(False)
            
    def remove(self,card):
        '''fonctionne, on retire bien la carte, 
        mais l'afficher sur le tas et non plus dans la main)'''
        
        c = []
        for i in range(len(self.get_cards())):
            if not (card.get_name() == self.get_cards()[i].get_name()): #On compare les cartes avec leur nom d'image : (pb de comparaison avec get_suit)
                c.append(self.get_cards()[i])
        self.set_cards(c)
            
    def set_position(self, pos):
        '''reçoit en argument un tuple (x,y)'''
        self.__position = pos
        
    def get_position(self):
        return self.__position
        
#    def reposition_hand(self):
#        for i in range(len(self.__cards)):
#            if i == len(self.__cards)-1:
#                self.__cards[i].set_first(True)
#                
#            self.__cards[i].set_position(self.__position_ini[0]+i*WIDTH*0.35,self.__position_ini[1])

    def __str__(self):
        s = ""
        for c in self.__cards:
            s+=c.get_name()+", "+str(c.get_position())
        return s            
        
        