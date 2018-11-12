# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:31:52 2018

@author: TeamIATECH
"""
from Player import Player
from Trump import Trump
from Card import Card
from Excuse import Excuse


class Human(Player):
    def __init__(self, hand, score, name):
        Player.__init__(self, hand, score, name)
        self.__hand= hand
    
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
    
    def bid(self,dog):
        listeBid = ["Passe","Petite","Garde","Garde sans","Garde contre"] 
        while True:
            print(listeBid)
            print("\nVoici vous cartes : ")
            print(self.get_hand())
            choice = input("\nVotre choix de Prise? (Ecrire en lettre)")
            for i in range(len(listeBid)):
                if choice == listeBid[i]:
                    if choice == "Garde": #Le joueuur à choisi Garde
                        still_choosing =True#Il lui est donc proposé d'échanger ses cartes avec le chien(dog)
                        print("\nVous avez choisi Garde")
                        print("\nVous Pouvez échanger vos cartes avec celles qui sont dans le chien")
                        print("\Tapez 69 lorsque vous avez terminé")
                        while still_choosing:  
                             player_cards=Player.get_hand(self)
                             print("\nVos cartes : \n")
                             for i, el in enumerate(player_cards):
                                 print(str(i)+"-->"+str(el))
                             print("\nLes cartes du chien")
                             for i,el in enumerate(dog):
                                 print(str(i)+"-->"+str(el))
                             n1 = int(input("Le numero de la carte à mettre dans le chien"))
                             n2 = int(input("Le numero de la carte à mettre dans votre jeu"))
                             
                             print("\n-----------------------------------------------------------\n")
                             if n1 == 69 or n2 == 69:
                                 still_choosing = False
                                 break
                             elif n1 < 19 and n2<6 : 
                                 hand = self.get_hand()
                                 
                                 card1 = hand.pop(n1)
                                 card2 = dog.pop(n2)
                                 dog.append(card1)
                                 hand.append(card2)
                                 self.set_hand(hand)
                             else:
                                 print("Veuillez renseigner un numero valide")
                    if choice == "Petite": #Le joueuur à choisi Garde
                        still_choosing =True#Il lui est donc proposé d'échanger ses cartes avec le chien(dog)
                        print("\nVous avez choisi Petite")#bite
                        print("\nVous Pouvez échanger vos cartes avec celles qui sont dans le chien")
                        print("\Tapez 69 lorsque vous avez terminé")
                        while still_choosing:  
                             player_cards=Player.get_hand(self)
                             print("\nVos cartes : \n")
                             for i, el in enumerate(player_cards):
                                 print(str(i)+"-->"+str(el))
                             print("\nLes cartes du chien")
                             for i,el in enumerate(dog):
                                 print(str(i)+"-->"+str(el))
                             n1 = int(input("Le numero de la carte à mettre dans le chien"))
                             n2 = int(input("Le numero de la carte à mettre dans votre jeu"))
                             
                             print("\n-----------------------------------------------------------\n")
                             if n1 == 69 or n2 == 69:
                                 still_choosing = False
                                 break
                             elif n1 < 19 and n2<6 : 
                                 hand = self.get_hand()
                                 
                                 card1 = hand.pop(n1)
                                 card2 = dog.pop(n2)
                                 dog.append(card1)
                                 hand.append(card2)
                                 self.set_hand(hand)
                             else:
                                 print("Veuillez renseigner un numero valide")
                                 
                            
                            
                        
                        
                
                    return choice
            print("\nArgument non valide")


if __name__ == '__main__':
    L=[Card(10, 'H'), Card(11, 'H'), Card(14, 'H'), Card(3, 'C'), Card(3, 'D'), Card(13,'S')]
    joueur1=Human(L,0,"Jean")
