# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:51:56 2018

@author: Simon

Cette classe sera liée à toutes les PlayingCards et constitue leur aspect physique

"""

'''
!!! LES HITBOX NE SONT PAS CHANGEES LORSQU'ON CHANGE LA POSITION DES CARTES !!!
'''

from tkinter import *

#Contient TOUS les fichiers images des cartes
CARDS_FACE= []

#Taille des cartes : 48x89 à peu près
WIDTH = 48
HEIGHT = 89

class Playing_Card_GUI():
    
    def __init__(self,str_image_on,parent):
        self.__name = str_image_on
        self.__image_on = PhotoImage(file=str_image_on)
        self.__image = self.__image_on
        self.__image_down = ...#Charger l'image d'une carte face verso
        
        self.__hand = None
        
        #Essentiel de rattache l'image à un label pour l'afficher effectivement
        self.__label = Label(image = self.__image_on)
        self.__label.image = self.__image_on
        
        #Permet de savoir si la carte est au bout de la main (sa hitbox sera la carte entière)
        self.__is_first = False
        
        #Vérifie si la carte est cliquable
        self.can_click = True
        
        #Deux lignes suivantes à modifier selon la taille réelle
        #La position correspond au bord haut gauche de la carte
        self.__position = [0,0]
        self.__size = [self.__image.width(),self.__image.height()] #(largeur, hauteur)
        
        if self.__is_first:
            self.__hitbox = [self.__position[0], self.__position[1], self.__size[0], self.__size[1]]
        else:
            self.__hitbox = [self.__position[0], self.__position[1], self.__size[0]*0.35, self.__size[1]]
        
        self.__parent_canvas = parent
        
        #Permet de voir quelles cartes sont dans une main
        self.__in_hand = False
        
        #☺On évite de surélever en continu quand on garde le focus
        self.__IS_UP = False
        
        #ID de l'image sur le canvas
        self.__id = None
        
        #Si le joueur est en train de faire son chien (comportement différent)
        self.__is_doing_dog = False
    
    def set_doing_dog(self,b):
        self.__is_doing_dog = b
    
    def in_hand(self):
        return self.__in_hand
    
    def disable(self):
        self.can_click = False
    def enable(self):
        self.can_click = True
    
    def hitbox_listener(self,event):
        #Si la souris a le focus sur la carte, on la surélève (et on la fait briller ?)
        if self.__in_hand and self.can_click:
            flag_x = (event.x > self.__hitbox[0] and event.x < self.__hitbox[0]+self.__hitbox[2])
            flag_y = (event.y > self.__hitbox[1] and event.y < self.__hitbox[1]+self.__hitbox[3])
            if not self.__IS_UP:
                if flag_x and flag_y:
                    self.get_up()
                    self.__IS_UP = True
            elif not flag_x or not flag_y:            
                self.get_down()
                self.__IS_UP = False

    def click_listener(self,event):
        flag_x = (event.x > self.__hitbox[0] and event.x < self.__hitbox[0]+self.__hitbox[2])
        flag_y = (event.y > self.__hitbox[1] and event.y < self.__hitbox[1]+self.__hitbox[3])
        
        if flag_x and flag_y:
            print(self.__name, " : Clicked")
            self.set_in_hand(False)
            if self.get_hand().get_player().get_doing_dog():
                #self.get_hand().remove(self)
                self.__parent_canvas.get_dog().add_card(self)
                self.add_dog(self.__parent_canvas.get_dog())
                '''
            else:
                self.__parent_canvas.get_trick().add_card(self)'''
    
    def play(self,pos):
        '''reste à afficher la carte à la position souhaitée et donnée en argument 
        (en fonction de a position de la main, faire plusieurs cas autour de l'appel
        de la fonction play)'''
        
        self.set_in_hand(False)
        #print(pos)
        self.set_position(pos[0],pos[1])
        self.draw(self.__parent_canvas)
        #self.__parent_canvas.get_trick().add_card(self)
        
    def add_trick(self,pos):
        #print(pos)
        self.set_position(pos[0],pos[1])
        if self.get_hand() != None:
            self.get_hand().remove(self)
        self.__hand = None
        self.set_in_hand(False)
        self.draw(self.__parent_canvas.get_trick().get_parent())
    
    def add_dog(self,dog):
        self.set_position(self.__parent_canvas.get_dog().get_position()[0],self.__parent_canvas.get_dog().get_position()[1])
        
        #Bug sans cette condition à cause de l'initialisation à None du constructeur
        if self.get_hand() != None:
            self.get_hand().remove(self)
        
        self.draw(self.__parent_canvas)
        self.set_in_hand(False)
        self.__hand = None
        
    def get_up(self):#Fonction de surélèvelent
        self.set_position(self.__position[0],self.__position[1]-20) #On surélève de 20px par exemple
        #self.set_hitbox([self.__position[0], self.__position[1], self.__size[0], self.__size[1]])
        self.draw(self.__parent_canvas)
    
    def get_down(self):
        self.set_position(self.__position[0],self.__position[1]+20) #On surélève de 20px par exemple
        self.draw(self.__parent_canvas)
        #self.set_hitbox([self.__position[0], self.__position[1], self.__size[0]*0.35, self.__size[1]])
        #self.__hand.reposition_hand()
    
    def set_in_hand(self,b):
        self.__in_hand = b
    
    def set_position(self,x,y):
        self.__position[0] = x
        self.__position[1] = y
        
        #penser à changer aussi la hitbox
        if self.__is_first:
            self.set_hitbox([self.__position[0], self.__position[1], self.__size[0], self.__size[1]])
        else:
            self.set_hitbox([self.__position[0], self.__position[1], self.__size[0]*0.35, self.__size[1]])
                
    def get_hitbox(self):
        return self.__hitbox
    
    def set_hitbox(self,hitbox):
        self.__hitbox = hitbox
        
    def set_first(self,b):
        self.__is_first = b
    
    def get_position(self):
        return self.__position
    
    def draw(self,canvas):
        if self.__id != None:
            canvas.delete(self.__id)
        self.__id = canvas.create_image(self.__position[0],self.__position[1],anchor=NW,image=self.__image_on)
        #canvas.config(height=self.__size[0],width=self.__size[1])       
     
#    def jouer_carte(self):
#        #placer la carte sur le tas
#        continue
     
    def set_hand(self,hand):
        self.__hand = hand
        
    def set_face_up(self,b):
        if b:
            self.__image = self.__image_on
        else:
            self.__image = self.__image_down
    #def onClick(self,game): #On définit ce qu'on doit faire avec la carte une fois cliquée (l'ajouter au tas)
    def get_name(self):
        return self.__name
    
    def get_hand(self):
        return self.__hand
    def get_parent(self):
        return self.__parent_canvas
    
    def __str__(self):
        return self.get_name()
    
def load_images():
    
    colors = ["coeur","carreau","pique","trèfle"]
    heads = ["Valet","Cavalier","Dame","Roi"]
    
    for i in range(1,10):
        for c in colors:
            if i == 1:
                CARDS_FACE.append(PhotoImage(file="cards_img/As "+c+".png")) #convertir les JPG en PNG sinon erreur ! 
            else:
                CARDS_FACE.append(PhotoImage(file="cards_img/"+str(i)+" "+c+".png"))
    
    for i in heads:
        for c in colors:
            CARDS_FACE.append(PhotoImage(file="cards_img/"+str(i)+" "+c+".png"))
            
    for i in range(1,21):
        CARDS_FACE.append(PhotoImage(file="cards_img/"+str(i)+" atout.png"))
        
    CARDS_FACE.append(PhotoImage(file="cards_img/Excuse.png"))

    
''' Ne pas oublier de créer une classe/fonction qui attribue à chaque carte la bonne image en 
fonction de ses attribus'''
            