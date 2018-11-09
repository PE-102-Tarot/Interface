# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:31:52 2018

@author: PE_102
"""
from Player import Player
from Trump import Trump
from Card import Card
from Excuse import Excuse


class Human(Player):
    def __init__(self, hand, score, name):
        Player.__init__(self, hand, score, name)
    
    def play(self, trick):
        if trick==[]:
            print("C'est à vous de commencer le pli. Voici votre main:\n")
        #else:
          #  print("Rappel:les cartes jouées sont:")
           # for el in trick:
            #    print(el)
        print("\nVous pouvez jouer les cartes suivantes:")
        playable_cards=Player.playable_cards(self, trick)
        for i, el in enumerate(playable_cards):
            print(str(i)+"-->"+str(el))
        while True:
            try:
                card=int(input("Votre choix? (Indice Python)"))
            except ValueError:
                print("Entrez un numéro de la liste.")
                continue
            if card>=len(playable_cards) or card<0:
                    print("Entrez un numéro de la liste.")
            else:
                break
        self.get_hand().remove(playable_cards[card])
        return (playable_cards[card])
    
    def bid(self):
        listeBid = ["Passe","Petite","Garde","Garde sans","Garde contre"] 
        while True:
            print(listeBid)
            choice = input("Votre choix de Prise? (Ecrire en lettre)")
            for i in range(len(listeBid)):
                if choice == listeBid[i]:
                    return choice
            print("\nArgument non valide")


if __name__ == '__main__':
    L=[Card(10, 'H'), Card(11, 'H'), Card(14, 'H'), Card(3, 'C'), Card(3, 'D'), Card(13,'S')]
    joueur1=Human(L,0,"Jean")
