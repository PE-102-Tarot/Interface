# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:29:48 2018

@author: PE_102
"""
from PlayingCard import PlayingCard

class Excuse(PlayingCard):
    """The Fool or Excuse
    
    Rank: 0
    Point: 4.5
    """
    def __init__(self):
        PlayingCard.__init__(self, 0, 4.5, 1)
    
    def __str__(self):
        return "Excuse"
    
    def __repr__(self):
        return "Excuse()"

if __name__ == '__main__':
    fool=Excuse()
    print(fool)
    print([fool])
    print(fool.get_rank())
    print(fool.get_point())
    