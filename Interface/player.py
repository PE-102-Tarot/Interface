# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:13:51 2018

@author: Simon
"""
INSTANCE = 0

from hand import *

class Player:

    def __init__(self):
        self.__instance = INSTANCE+1
        self.__name = "Player "+str(self.__instance)
        self.__hand = Hand([],(0,0))
        
    def get_hand(self):
        #print(self.__hand)
        return self.__hand
    
    def set_hand(self,hand):
        self.__hand = hand