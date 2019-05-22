# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:29:20 2018

@author: PE_102
"""
from PlayingCard import PlayingCard


class Card(PlayingCard):
    """Spades, Hearts, Diamonds and Clovers
    
    Rank: from 1 to 14
    Point: 0.5 or 1.5 or 2.5 or 3.5 or 4.5
    Suit: 'S','H','D','C'
    """
    def __init__(self, n, s,str_image_on, parent):
        PlayingCard.__init__(self, n,str_image_on, parent)
        self.__suit=s
        self.rank = n
        if n>10:
            self.set_point(n-9.5)
    
    def get_suit(self):
        return self.__suit
    
    def get_rank(self):
        return self.rank
    
    def __str__(self):
        """Clever use of dictionnaries"""
        return "{} de {}".format({11:'Valet',12:'Cavalier',13:'Reine',14:'Roi'}
                                 .get(self.get_rank(),self.get_rank()),
                                 {'S':"Pique",'H':"Coeur",'D':"Carreau",'C':"Trèfle"}[self.__suit])
    
    def __repr__(self):
        return "Card({},'{}')".format(self.get_rank(), self.__suit)
    
#if __name__ == '__main__':
#    L=[Card(10, 'H'), Card(11, 'H'), Card(14, 'H'), Card(3, 'C'), Card(3, 'D'), Card(13,'S')]
#    print(L)
#    for el in L:
#        print(el)
#        print(el.get_rank())
#        print(el.get_point())
#        print(el.get_suit())
#
#    
