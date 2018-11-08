# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:15:50 2018

@author: PE_102
"""
class PlayingCard():
    """Abstract parent class for Trump, Card and Excuse.
    
    Rank: le numéro de la carte
    Point: la valeur en points de la carte
    La fonction init des trois classes filles attribue automatiquement la valeur en points de la carte.
    """
    
    def __init__(self, n, p=0.5, o=0):
        assert self.__class__ is not PlayingCard
        self.__rank=n
        self.__point=p
        self.__oulder=o
    
    def get_rank(self):
        return self.__rank
    def get_point(self):
        return self.__point
    
    def set_point(self, p):
        """Only used when creating "counters" (face cards and oudlers)"""
        self.__point=p
     
    def get_oulder(self):
        return self.__oulder
    def set_oulder(self, o):
        self.__oulder=o
    

if __name__ == '__main__':
    carte=PlayingCard(10,2.5)#Cette classe n'est pas instanciable
