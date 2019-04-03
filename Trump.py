# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:27:59 2018

@author: PE_102
"""
from PlayingCard import *


class Trump(PlayingCard):
    """Trump Cards"""
    def __init__(self, n,str_image_on, parent):
        PlayingCard.__init__(self,n,str_image_on, parent)
        if n==1 or n==21:
            self.set_point(4.5)
            self.set_oulder(1)
    
    def __str__(self):
        return "{} d'Atout".format(self.get_rank())
    
    def __repr__(self):
        return "Trump({})".format(self.get_rank())
        
    def __lt__(self, other):
        """Rich comparison method. Since two cards are always differents,
        only strict inferiority and strict superiority need to be implemented.
        This may not be very useful because at least one of the 2 cards must be
        a Trump for the comparison to work. But if L is a list of Trump cards,
        sorted(L) will return a correctly sorted list"""
        if isinstance(other,Trump):
            return self.get_rank() < other.get_rank()
        else:
            return False

    def __gt__(self, other):
        """Rich comparison method. Since two cards are always differents,
        only strict inferiority and strict superiority need to be implemented.
        This may not be very useful because at least one of the 2 cards must be
        a Trump for the comparison to work. But if L is a list of Trump cards,
        sorted(L) will return a correctly sorted list"""
        if isinstance(other,Trump):
            return self.get_rank() > other.get_rank()
        else:
            return True


#if __name__ == '__main__':
#    Atout10=Trump(10)
#    Atout1=Trump(1)
#    Atout21=Trump(21)
#    L=[Atout10,Atout1,Atout21]
#    print(L)
#    print(Atout10)
#    print(Atout1)
#    print(Atout21)
#    print(Atout10.get_rank())
#    print(Atout1.get_rank())
#    print(Atout21.get_rank())
#    print(Atout10.get_point())
#    print(Atout1.get_point())
#    print(Atout21.get_point())
#    print(sorted(L))
#    
    