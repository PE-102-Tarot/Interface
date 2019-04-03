# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:17 2018

@author: PE_102
"""
from Trump import Trump
from Card import Card
from Excuse import Excuse
from hand import *

INSTANCE = 0

class Player():
    """Abstract parent class for both IA and Human."""
    
    def __init__(self, score, name):
        #assert self.__class__ is not Player
        self.__instance = INSTANCE+1
        #self.__name = "Player "+str(self.__instance)
        self.__hand = Hand([],(0,0),"")
        self.__score= score
        self.__name= name
        
        #Si c'est le tour du joueur
        self.__is_playing = False
        
        #Si il est le bidder
        self.__is_bidder = False
    
    def get_hand(self):
        return self.__hand
    def get_score(self):
        return self.__score
    def get_name(self):
        return self.__name
    def set_hand(self, hand):
        self.__hand= hand
    def set_score(self, score):
        """Add the score of a game to the total score."""
        self.__score+= score
    def set_name(self, name):
        self.__name= name
    
    """J'ai cette fonction ici faute de mieux"""
    #checked
    @staticmethod
    def best_card(cards):
        """Return the index of the best card in a list
        
        The first card defines the winning suit.
        This list is often a trick of two, three or four cards.
        The index (0, 1, 2, or 3) thus defines the winner of the trick
        """
        w_card=cards[0]
        w=0
        for i in range(1,len(cards)):
            if isinstance(w_card, Trump):
                if isinstance(cards[i], Trump) and cards[i]>w_card:
                    w_card, w=cards[i], i
            elif isinstance(w_card, Card):
                if isinstance(cards[i], Trump):
                    w_card, w=cards[i], i
                elif isinstance(cards[i], Card) and cards[i].get_suit()==w_card.get_suit() and cards[i].get_rank()>w_card.get_rank():
                    w_card, w=cards[i], i
            elif isinstance(w_card, Excuse):
                w_card, w=cards[i], i
        return w

    #checked
    def playing_trump(self, trick):
        '''
        Vérifie si la main contient des atouts, si ce n'est pas le cas, elle renvoie
        toute la main du joueur en tant que cartes jouables, sinon,
        elle renvoit une liste d'atouts supérieurs au précédent atout joué
        '''
        hand=self.get_hand().get_cards()[:]
        L=[el for el in hand if isinstance(el,Trump)]
        if L==[]:
            return hand
        else:
            best_trump=0
            if isinstance( trick[Player.best_card(trick)], Trump) :
                best_trump=trick[Player.best_card(trick)].get_rank()
            K=[el for el in L if el.get_rank()>best_trump]
        
        if K==[]:
            return L
        else:
            return K
        
        return K or L

    #checked
    def playable_cards(self, trick):
        hand=self.get_hand().get_cards()[:]
        ex=[]
        for el in hand:
            if isinstance(el,Excuse):
                ex=[el]
        cards_trick = trick.get_cards()
        
        if cards_trick==[]:
            return hand #Si dans le tas de cartes jouées il n'y a rien on peut tout jouer
        elif isinstance(cards_trick[0], Trump):
            #Si la premiere carte est un atout, on doit jouer un atout,
            #si on en a pas, n'importe quelle carte
            #On ajoute l'excuse aux cartes jouables
            return self.playing_trump(cards_trick)+ex
        
        elif isinstance(cards_trick[0], Card):
            #Si on ne joue pas atout, on regarde quelle couleur est jouée
            suit=cards_trick[0].get_suit()
            #!!! N'implique pas forcément de jouer au dessus de la dernière carte
            L=[el for el in hand if (isinstance(el,Card) and el.get_suit()==suit)]
            if L==[]:
                #Si on a pas de cartes, on joue atout
                return self.playing_trump(cards_trick)+ex
            else :
                #Si on peut pas, on joue n'importe quoi
                return L+ex
            
        elif isinstance(cards_trick[0], Excuse):
            return self.playable_cards(cards_trick[1:])
 
    def is_playing(self):
        return self.__is_playing
    
    def set_playing(self,b):
        self.__is_playing = b
        
    def set_is_bidder(self,b):
        self.__is_bidder = b

    def is_bidder(self):
        return self.__is_bidder


#if __name__ == '__main__':
#    joueur=Player([],0,"Jean")#Cette classe n'est pas instanciable
