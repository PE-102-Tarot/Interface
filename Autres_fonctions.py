# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:14:04 2018
@author: TeamIATECH
"""
from PlayingCard import PlayingCard
from Trump import Trump
from Card import Card
from Excuse import Excuse
from Player import Player
from Human import Human
from IA import IA
import random
import operator#Pour trier les cartes

     
def bidding(dealer,players,dog):
    first_chooser = (dealer+1)%4
    
    
    for i in range(4):
        index = (first_chooser+i)%4
        if isinstance(players[index],Human):
            choice = players[index].bid(dog)
            if choice != "Passe":
                return index,choice
    print("\nPersonne n'as choisi")
    return dealer,"Passe"
    #Reshuffle Game


def result(oulders,bid,points):
    """Return the scoring points that each player gives to the bidder
    
    The bonuses are not counted here."""
    multiplier= {'Petite':1,'Garde':2,'Garde Sans':4,'Garde Contre':6}[bid]
    if oulders==0:
        g=points-36
    elif oulders==1:
        g=points-41
    elif oulders==2:
        g=points-51
    else:
        g=points-56
    if g<0:
        s=(g-25)*multiplier
    else:
        s=(g+25)*multiplier
    return s

          
def create_deck():
    """Creates a tarot deck of 78 cards"""
    L=[]
    for i in range(1, 22):
        L.append(Trump(i))
    for s in ('S', 'H', 'D', 'C'):
        for i in range(1, 15):
            L.append(Card(i, s))
    L.append(Excuse())
    return L
 
    
def deal(players):
    deck=create_deck()
    random.shuffle(deck)
    dog=deck[-6:]
    for i in range(4):
        (players[i]).set_hand(deck[(i*18):((i+1)*18)])
    return dog

def sorting(deck):
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
    output += L
    return output
        
            
    
                
                
                

def create_players(n):
    players=[]
    for i in range(n):
        players.append(IA([],0,"Joueur_Anonyme"))
    for i in range(4-n):
        players.append(Human([],0,"Joueur_Anonyme"))
    return players


def game(players,dealer):
    """Dealer(int) : Numero du dealer, Players(liste(IA,Human)): Liste qui contient les instances des humains et des IA"""
    dog=deal(players)
    bidder, bid = bidding(dealer,players,dog)#Identifier bidder & defender  # Bidder(int) Numero du bidder, Bid(str) type de Passe
    if bid =="Passe":
       return bid
    print("Le joueur "+str(bidder)+" a pris un contrat: "+bid)
    for i in range(4):
        players[i].set_hand(sorting(players[i].get_hand()))
    first_player=(dealer+1)%4
    points_bidder, points_defenders, oulders= 0, 0, 0
    previous_trick=[]
    for i in range(18):
        trick=[]
        for i in range(4):
            index=(first_player+i)%4
            card=players[index].play(trick)
            print("Joueur "+str(index)+" a joué "+str(card))
            trick.append(card)
        first_player=(first_player+Player.best_card(trick))%4
        print ("Le joueur "+str(first_player)+" a remporté ce pli\n")
        print ("-"*60)
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
    if bid=="Garde Contre":
        points_defenders+=sum(card.get_point() for card in dog)
    else:
        points_bidder+=sum(card.get_point() for card in dog)
    print("Points bidder: "+str(points_bidder))
    print("Points défenseurs: "+str(points_defenders))
    print("(Points chien: "+str(sum(card.get_point() for card in dog))+")")
    print("Oulders défenseurs: "+str(oulders))
    score=result(oulders,bid,points_bidder)
    players[bidder].set_score(score*3)
    for i in range(4):
        if i!=bidder:
            players[i].set_score(-score)
    print("Evolution score bidder: "+str(score*3))
    print("Evolution score défenseurs: "+str(-score))


def begin_game(n):
    
    dealer=random.randint(0,3)
    players=create_players(n)
    start_game(dealer,players)

def start_game(dealer,players): #Pour un reshuffle
    game_on = True
    while game_on:
        bid = game(players,dealer)
        if bid != "Passe":    
            game_on=bool('True'==input("Pour continuer, écrire True"))
            dealer+=1


if __name__ == '__main__':
    #print(Player.best_card([Card(10,'H'),Card(11,'S'),Card(8,'H'),Card(13,'H')]))
    begin_game(3)#L'humain sera le joueurs 
