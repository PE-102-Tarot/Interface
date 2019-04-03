# -*- coding: utf-8 -*-PeitPet
"""
Created on Mon Oct 29 14:14:04 2018
@author: TeamIATECH

Redéfinir les print des classes pour les remplacer par des effets visuels
Vérfier la concordance des méthodes utilisées avec celles des classes 
de l'interface

Renommer cette classe "game.py" et la lancer dans window.py

"""
from PlayingCard import *
from Trump import *
from Card import *
from Excuse import *
from player import *
from Human import *
from IA import *
from playing_field import *
import random
import operator#Pour trier les cartes
from tkinter import *
import time

class Game:
    
    def __init__(self,interface,window):
        self.__interface = interface
        self.__window = window
        self.__players = None
        self.__dealer = None
        self.__bidder = None
        self.__bid = None
        #self.data = Database(players) 
        #eventuellement mettre setter/getter
    
    def get_dealer(self):
        return self.__dealer
    def get_bidder(self):
        return self.__bidder
    def get_players(self):
        return self.__players
    def get_bid(self):
        return self.__bid
    def set_dealer(self,dealer):
        self.__dealer = dealer
    def set_bidder(self,bidder):
        self.__bidder = bidder
    def set_players(self,players):
        self.__players = players
    
    def bidding(self,dealer,players,dog):
        first_chooser = (dealer+1)%4
        for i in range(4):
            index = (first_chooser+i)%4
            if isinstance(players[index],Human):
                #On ouvre une fenetre et on affiche les choix de biddings
                
                win_bid = Toplevel(self.__window)
                
                global var
                var = StringVar()
                
                def set_bid():
                    self.__interface.enable_all_cards()
                    bid = var.get()
                    print(bid)
                    win_bid.destroy()
                    self.start_game(dealer,players,index,bid)
                
                passe = Radiobutton(win_bid,text="Passe",value="Passe",variable=var,command=set_bid)
                passe.deselect()
                passe.pack(anchor=W)
                petite = Radiobutton(win_bid,text="Petite",value="Petite",variable=var,command=set_bid)
                petite.deselect()
                petite.pack(anchor=W)
                garde = Radiobutton(win_bid,text="Garde",value="Garde",variable=var,command=set_bid)
                garde.deselect()
                garde.pack(anchor=W)
                garde_s = Radiobutton(win_bid,text="Garde sans",value="Garde sans",variable=var,command=set_bid)
                garde_s.deselect()
                garde_s.pack(anchor=W)
                garde_c = Radiobutton(win_bid,text="Garde contre",value="Garde contre",variable=var,command=set_bid)
                garde_c.deselect()
                garde_c.pack(anchor=W)
                
                text = Label(win_bid,textvariable=var).pack()
                
                self.__interface.disable_all_cards()
                
                win_bid.mainloop()                
                
                #choice = players[index].bid(dog)
        #Reshuffle Game
    
    
    def result(self,oulders,bid,points,bonus_bidder,bonus_defenders):
        """Return the scoring points that each player gives to the bidder
        
        The bonuses are not counted here."""
        multiplier= {'Petite':1,'Garde':2,'Garde sans':4,'Garde contre':6}[bid]
        if oulders==0:
            g=points-36
        elif oulders==1:
            g=points-41
        elif oulders==2:
            g=points-51
        else:
            g=points-56
        if g<0:
            s=(g-25+bonus_bidder-bonus_defenders)*multiplier
        else:
            s=(g+25+bonus_bidder-bonus_defenders)*multiplier
        return s
    
              
    def create_deck(self):
        """Creates a tarot deck of 78 cards"""
#        L=[]
#        for i in range(1, 22):
#            L.append(Trump(i))
#        for s in ('S', 'H', 'D', 'C'):
#            for i in range(1, 15):
#                L.append(Card(i, s))
#        L.append(Excuse())
        return self.__interface.get_deck()
     
    #remplace la méthode place_hands() de l'interface
    def deal(self,players):
        '''deck=self.create_deck()
        random.shuffle(deck)
        dog=deck[-6:]
        
        #On initialise la position des points stratégiques EST,SUD,NORD et OUEST
        
        nord = (self.__interface.get_width()//2-3*50,50)
        sud = (self.__interface.get_width()//2-3*50,self.__interface.get_height()-100)
        est = (20,self.__interface.get_height()//2)
        ouest = (self.__interface.get_width() - 50*7,self.__interface.get_height()//2)
                
        side = [sud,est,nord,ouest]
        
        for i in range(4):
            (players[i]).set_hand(Hand(deck[(i*18):((i+1)*18)],side[i]))
            
        h1 = players[0].get_hand()
        h2 = players[1].get_hand()
        h3 = players[2].get_hand()
        h4 = players[3].get_hand()
        
        h1.show(self.__interface)
        h2.show(self.__interface)
        h3.show(self.__interface)
        h4.show(self.__interface)'''
        
        return self.__interface.get_dog()
    
    def sorting(self,deck):
        output = []
        n = len(deck)
        color = ["S","H","D","C"]
        for i in range(4):#On s'occupe d'abord des cartes normales
            L = []
            for j in range(n):
                if isinstance(deck[j],Card) and deck[j].get_suit() == color[i]:
                    L.append(deck[j]) #On met tout les cartes d'une meme couleur dans une liste L
            L.sort(key = operator.attrgetter('rank'))   
            """WARNING : Marche mais je dois creer un attribut public des cartes self.rank..."""
            output +=L
        L = []
        for j in range(n):#Puis des atouts
            if isinstance(deck[j],Trump):
                L.append(deck[j])
        L.sort()
        for j in range(n):
            if isinstance(deck[j],Excuse):
                L.append(deck[j])
        output += L
        return output          
    
    def create_players(self,n):
        players=[]
        '''for i in range(n):
            players.append(IA(0,"Joueur_Anonyme"))
        for i in range(4-n):
            players.append(Human(0,"Joueur_{}".format(i+1)))'''
        players = self.__window.get_field().get_players()
        return players
        
    def game(self,players,dealer,bidder,bid):
        """Dealer(int) : Numero du dealer, Players(liste(IA,Human)): Liste qui contient les instances des humains et des IA"""

        #bidder, bid = self.bidding(dealer,players,dog)#Identifier bidder & defender  # Bidder(int) Numero du bidder, Bid(str) type de Passe
        if bid =="Passe":
           return bid
        print("Le joueur "+str(bidder)+" a pris un contrat: "+bid)
        
        self.set_players(players)
        self.set_bidder(bidder)
        self.set_dealer(dealer)
                
        #C'est au bidder de jouer après le bidding puisqu'il doit faire son chien
        players[bidder].set_playing(True)
        players[bidder].set_is_bidder(True)
        
        #On informe la fenêtre que le bidder doit faire son chien
        self.__window.set_doing_dog(True)
        
        self.__interface.enable_playing_player_cards_only(players[bidder],players)
        #self.do_dog()
        '''#seulement si on veut vraiment trier les cartes des joueurs
        for i in range(4):
            players[i].set_hand(self.sorting(players[i].get_hand().get_cards()))
            #On met à jour les mains
            '''
        
    def start_turn(self,dealer,players,bidder):
        
        first_player=(dealer+1)%4
        #On initialise les points des joueurs à 0
        points_bidder, points_defenders, oulders,bonus_bidder,bonus_defenders= 0, 0, 0, 0, 0
        #previous trick = le plis précédent
        previous_trick=[]
        #boucle des 18 tours de jeu -> on en met un seul pour l'instant
        #for i in range(18):
        trick=Trick(self.__interface)
        for j in range(4):
            index=(first_player+j)%4
            if isinstance(players[index], IA):
                card = players[index].play(trick) 
            else:
                card = None
                #dans ce cas là c'est l'humain qui joue, gérer les variables de la fenetre
            #print("Joueur "+str(index)+" a joué "+str(card))
            trick.add_card(card)
        '''first_player=(first_player+Player.best_card(trick))%4
        print ("Le joueur "+str(first_player)+" a remporté ce pli\n")
        
        for j,el in enumerate(trick):#Traitement de l'excuse:
            if isinstance(el, Excuse):#Si un joueur a posé l'excuse
                if i!=17:#Si ce n'est pas le dernier pli
                    if (j==bidder and i!=17):#Si ce joueur est le Preneur
                        points_bidder+=4#On donne les points de l'excuse au Preneur
                        points_defenders-=4#On retire les points de l'excuse à la défense
                        oulders-=1
                    elif (first_player==bidder and i!=17):#Sinon le gagnant n'est pas être la défense
                        points_defenders+=4#On donne les points de l'excuse à la défense
                        points_bidder-=4#On retire les points de l'excuse au Preneur
                        oulders+=1
                    #Dans le dernier cas, la défense a joué l'Excuse et l'a gagnée normalement. 
                else:#Si c'est le dernier pli
                    #Si c'est le Preneur qui a joué l'Excuse pas de chgt à faire
                    #(Chelem non traité pour l'instant)
                    #Si la défense a joué et perdu l'Excuse, rien à faire non plus.
                    #Seul cas à traiter: la défense a joué l'Excuse et l'a gagnée.
                    if first_player!=bidder and j!=bidder:
                        points_bidder+=4#On donne les points de l'excuse au Preneur
                        points_defenders-=4#On retire les points de l'excuse à la défense
                        oulders-=1
    
            
                    
            if first_player==bidder:
                points_bidder+=sum(card.get_point() for card in trick)
            else:
                points_defenders+=sum(card.get_point() for card in trick)
                oulders+=sum(card.get_oulder() for card in trick)
            previous_trick=trick
            if i == 17:
                for i in range(4):#PETIT AU BOUT
                    if isinstance(trick[i],Trump) and trick[i].get_rank()==1:#C'est le seul moyen de verifier qu'on a bien le petit au Bout
                        print("\nPetit au bout")
                        if first_player == bidder:#On ajoute la prime
                            bonus_bidder+=10
                        else:
                            bonus_defenders +=10
            
            print ("-"*60)     
                  
        
        if bid=="Garde Contre":
            points_defenders+=sum(card.get_point() for card in dog)
        else:
            points_bidder+=sum(card.get_point() for card in dog)
        print("Points bidder: "+str(points_bidder))
        print("Points défenseurs: "+str(points_defenders))
        print("(Points chien: "+str(sum(card.get_point() for card in dog))+")")
        print("Oulders défenseurs: "+str(oulders))
        score=result(oulders,bid,points_bidder,bonus_bidder,bonus_defenders)
        players[bidder].set_score(score*3)
        for i in range(4):
            if i!=bidder:
                players[i].set_score(-score)
        print("Evolution score bidder: "+str(score*3))
        print("Evolution score défenseurs: "+str(-score))'''
    
    def begin_game(self,n):
        
        dealer=random.randint(0,3)
        players=self.create_players(n)#checked
        #self.start_game(dealer,players)
        dog=self.deal(players)
        self.bidding(dealer,players,dog)
        
    def start_game(self,dealer,players,bidder,bid): #Pour un reshuffle
        game_on = True
        #while game_on:
        b = self.game(players,dealer,bidder,bid)
            #Ne pas décommenter tant que les bugs et l'implémentation totale n'est pas corrigée
        '''if b != "Passe":    
                game_on=bool('True'==input("Pour continuer, écrire True"))
                dealer+=1'''
        #self.end_game(dealer,players)
        
    def end_game(self,dealer,players):
        print("\n---------------------------------\n")
        print(" La partie est terminée")
        for i in range(4):
            print("\n Le score du joueur " + str(i) + " est de " + str(players[i].get_score()))
            
        
    def do_dog(self):
        time.sleep(1)
        print("Veuillez faire votre chien en cliquant sur 6 cartes de votre main")
        


#if __name__ == '__main__':
#    #print(Player.best_card([Card(10,'H'),Card(11,'S'),Card(8,'H'),Card(13,'H')]))
#    begin_game(3)#L'humain sera le joueurs 
