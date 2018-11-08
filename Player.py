# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:17 2018

@author: PE_102
"""
from Trump import Trump
from Card import Card
from Excuse import Excuse


class Player():
    """Abstract parent class for both IA and Human."""
    
    def __init__(self, hand, score, name):
        assert self.__class__ is not Player
        self.__hand= hand
        self.__score= score
        self.__name= name
    
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
            if isinstance(w_card, Card):
                if isinstance(cards[i], Trump):
                    w_card, w=cards[i], i
                elif isinstance(cards[i], Card) and cards[i].get_suit()==w_card.get_suit() and cards[i].get_rank()>w_card.get_rank():
                    w_card, w=cards[i], i
            if isinstance(w_card, Excuse):
                w_card, w=cards[i], i
        return w

    def playing_trump(self, trick):
        hand=self.get_hand()[:]
        L=[el for el in hand if isinstance(el,Trump)]
        if L==[]:
            return hand
        else:
            best_trump=trick[Player.best_card(trick)].get_rank()
            K=[el for el in L if el.get_rank()>best_trump]
            """
                if K==[]:
                    return L
                else:
                    return K
            """
            return K or L

    def playable_cards(self, trick):
        hand=self.get_hand()[:]
        ex=[]
        for el in hand:
            if isinstance(el,Excuse):
                ex=[el]
        if trick==[]:
            return hand
        elif isinstance(trick[0], Trump):
            return self.playing_trump(trick)+ex
        elif isinstance(trick[0], Card):
            suit=trick[0].get_suit()
            L=[el for el in hand if (isinstance(el,Card) and el.get_suit()==suit)]
            return L+ex or self.playing_trump(trick)+ex
        elif isinstance(trick[0], Excuse):
            return self.playable_cards(trick[1:])
        
    def bid(self):
        listeBid = ["Passe","Petite","Garde","Garde sans","Garde contre"]
        while True:
            print(listeBid)
            choice= input("Votre choix de Prise? (Ecrire en lettre)")
            for i in range(len(listeBid)):
                if choice == listeBid[i]:
                    return choice
            print("\nArgument non valide")


if __name__ == '__main__':
    joueur=Player([],0,"Jean")#Cette classe n'est pas instanciable
