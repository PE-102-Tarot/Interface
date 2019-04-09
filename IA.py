# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:49 2018

@author: PE_102
"""
from player import *


class IA(Player):
    def __init__(self, score, name):
        Player.__init__(self, score, name)
        #checked
        
    def play(self,trick):
        playable_cards=Player.playable_cards(self, trick)
        card = playable_cards[0]
        self.get_hand().remove(playable_cards[0])
        
        loc = self.get_hand().get_placement()
        x,y = self.get_hand().get_position()
        pos = (0,0)
        #On décale globalement de 20 pixels par rapport à l a position de la main
        if loc == "NORTH":
            pos = ((2*x+7*48)/2-48/2,y+89+25)
        elif loc == "EAST":
            pos = (x+7*48+25,y)
        elif loc == "WEST":
            pos = (x-25-48,y)
        card.play(pos)
        '''card.disable()
        x,y = self.get_hand().get_position()
        card.set_position(x,y-40)'''
        #on retire la carte physiquement et réellement de la main et on la met (désactivée) au dessus de la main en attente
        #print("carte ajoutee au trick")
        trick.add_card(playable_cards[0],pos)

if __name__ == '__main__':
    pass
    