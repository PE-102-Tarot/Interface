# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:22:48 2018

@author: Simon

Cette classe est un canvas géant (en hérite), elle représente le terrain de jeu, sur lequel
on va pouvoir installer les mains des joueurs, le tas du milieu etc...
Chacun de ces éléments devra avoir une position particulière (Nord, Sud, Est, Ouest pour les mains des joueurs,
milieu du terrain pour le tas)

"""
from tkinter import *
from playing_card_GUI import *
from player import *
from random import *
from hand import *
from trick import *
from Trump import *
from Card import *
from Excuse import *
from dog import *
from Human import *
from IA import *

class Playing_Field(Canvas):
    
    def __init__(self,parent):
        Canvas.__init__(self,parent,background="green",width = parent.get_width(), height = parent.get_height() )
        self.__parent = parent
        self.__width = parent.get_width()
        self.__height = parent.get_height()
        self.__players = []
        self.__deck = self.create_deck()
        
        #Pour le socle des plis au milieu
        self.__img_socle = PhotoImage(file="cards_img/zone.png")
        self.__label = Label(image = self.__img_socle)
        self.__label.image = self.__img_socle
        self.pos_s1 = (1200//2-115//2,600//2+20)
        self.pos_s2 = (1200//2-115//2+63,600//2+20)
        self.__def = self.create_image(self.pos_s1[0],self.pos_s1[1],anchor=NW,image=self.__img_socle)
        self.__att = self.create_image(self.pos_s2[0],self.pos_s2[1],anchor=NW,image=self.__img_socle)

        #Pour le tour de jeu
        self.__trick = Trick(self)
        
        #On véréfie si l'excuse est joué
        self.__excuse_played = False
        #On note le numéro du joueur ayant joué l'excuse si c'est le cas
        self.__player_excused = None
        
        #Pour l'affichage des cartes jouées au fur et à mesure
        #self.__t1,self.__t2,self.__t3,self.__t4 = Trick(self),Trick(self),Trick(self),Trick(self)
        
        self.__bidder = 0
        self.__dealer = 0
        self.__players_left = 0
        
        self.__first_player = 0
        
        self.__trick_bidder = Trick(self)
        self.__trick_def = Trick(self)
        
        self.__excuse_trick = Trick(self)
        self.__dog = Dog(self)
     
    def excuse_played(self):
        return self.__excuse_played
    def set_excuse_played(self,b,p):
        self.__excuse_played = b
        self.__player_excused = p
    def get_player_excused(self):
        return self.__player_excused
    def get_excuse_trick(self):
        return self.__excuse_trick
    def get_deck(self):
        return self.__deck
    
    def get_players(self):
        return self.__players
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_trick(self):
        return self.__trick
    def get_trick_bidder(self):
        return self.__trick_bidder
    def get_trick_def(self):
        return self.__trick_def
    
    def get_dog(self):
        return self.__dog
    def get_players_left(self):
        return self.__players_left
    def get_dealer(self):
        return self.__dealer
    def get_bidder(self):
        return self.__bidder
    def get_first(self):
        return self.__first_player
    def set_first(self,p):
        self.__first_player = p
    def set_players_left(self,nb):
        self.__players_left = nb
    def set_dealer(self,dealer):
        self.__dealer = dealer
    def set_bidder(self,bidder):
        self.__bidder = bidder
    def set_trick(self,trick):
        self.__trick = trick
        
    def disable_all_cards(self):
        """Désctive la possibilité de cliquer sur les cartes"""
        players = self.get_players()  
        for p in players:
            cards = p.get_hand().get_cards()
            for c in cards:
                c.disable()
    def enable_all_cards(self):
        players = self.get_players()  
        for p in players:
            cards = p.get_hand().get_cards()
            for c in cards:
                c.enable()
    def disable_cards(self,players):
        for p in players:
            cards = p.get_hand().get_cards()
            for c in cards:
                c.disable()
    def enable_cards(self,players):
        for p in players:
            cards = p.get_hand().get_cards()
            for c in cards:
                c.enable()
    
    def enable_playing_player_cards_only(self,player,players):
        for p in players:
            cards = p.get_hand().get_cards()
            for c in cards:
                if p.is_playing():
                    c.enable()
                else:
                    c.disable()
        
    def create_deck(self):
        """Creates a tarot deck of 78 cards"""
        L=[]
        for i in range(1, 22):
            L.append(Trump(i,"cards_img/"+str(i)+" atout.png",self))
        for s in ('pique', 'coeur', 'carreau', 'trèfle'):
            suit = ""
            if s == "pique":
                suit = "S"
            elif s == "coeur":
                suit = "H"
            elif s == "carreau":
                suit = "D"
            else:
                suit == "C"
                
            for i in range(1, 11):                 
                if i == 1 :
                    L.append(Card(1,suit,"cards_img/As "+s+".png",self))
                else:
                    L.append(Card(i,suit,"cards_img/"+str(i)+" "+s+".png",self))
            k = 1
            for j in ('valet','cavalier','dame','roi'):
                L.append(Card(10+k,suit,"cards_img/"+j+" "+s+".png",self))
                k+=1
        L.append(Excuse("cards_img/Excuse.png",self))
        
        return L  
    
    #Il faut maintenant gérer les évênements, à savoir : lorsqu'une carte est cliqué,
    #Elle est posée devant le joueur (modifier playing_card_GUI, playing_field)
    #Obsolète
    def place_hands(self):
        '''Cette méthode prend en argument le jeu donc la classe qui gère les cartes etc...,
        donc qui possède en attribut les mains des joueurs à la fois sous forme de tableau de classes
        héritant de Playing_Card_GUI'''

        #On initialise la position des points stratégiques EST,SUD,NORD et OUEST
        
        nord = (self.__width//2-3*50,50)
        sud = (self.__width//2-18*50*0.35//2,self.__height-100)
        est = (20,self.__height//2)
        ouest = (self.__width - 50*7,self.__height//2)
                
        side = [sud,est,nord,ouest]
        pos = ["SOUTH","EAST","NORTH","WEST"]
        
        #On initialise les joueurs
        for i in range(4):
            if i == 0:
                p = Human(0,"Joueur {}".format(i))
            else:
                p = IA(0,"Joueur {}".format(i))
            p.set_instance(i)
            cards = []
            for j in range(18):
                r = randint(0,len(self.__deck)-1)
                self.__deck[r].set_in_hand(True)
                cards.append(self.__deck[r])
                self.__deck.pop(r)
            #On donne une main au joueur aléatoirement
            #print(Hand(cards,side[i]))
            h = Hand(cards,side[i],pos[i])
            for c in cards:
                c.set_hand(h)
            p.set_hand(h)
            
            self.__players.append(p)
        
        for i in range(len(self.__deck)):
            self.__dog.add_card(self.__deck[i])
        
        h1 = self.__players[0].get_hand()
        h2 = self.__players[1].get_hand()
        h3 = self.__players[2].get_hand()
        h4 = self.__players[3].get_hand()
        
#        h1.set_position(sud)
#        h2.set_position(ouest)
#        h3.set_position(nord)
#        h4.set_position(est)
        h1.show()
        h2.show()
        h3.show()
        h4.show()
        self.__dog.show_dog(self)