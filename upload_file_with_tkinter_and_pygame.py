# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:22:42 2020

@author: Coyot STARK
"""
import tkinter
import sys,pygame, pygame.mixer
from tkinter import filedialog
from pygame.locals import *
from Detection import detectionim 


pygame.init()

taille = width, height = 620,480



screen = pygame.display.set_mode(taille)
"""les boutons"""
btnimage = pygame.image.load('btnimage.png')
btnimage = pygame.transform.scale(btnimage, (200,53))
btnvideo = pygame.image.load('btnvideo.png')
btnvideo = pygame.transform.scale(btnvideo, (200,53))

"""les panneaux"""
stop = pygame.image.load('stop.png')
stop = pygame.transform.scale(stop, (100,100))
AB25 = pygame.image.load('AB25.png')
AB25 = pygame.transform.scale(AB25, (100,100))
interdit = pygame.image.load('interdit.png')
interdit = pygame.transform.scale(interdit, (100,100))
ceder = pygame.image.load('ceder.png')
ceder = pygame.transform.scale(ceder, (100,100))
son = pygame.mixer.Sound('occ.wav')
son.play()

screen.blit(btnimage,(200,200))
screen.blit(btnvideo,(200,300))
screen.blit(stop,(0,0))
screen.blit(AB25,(520,380))
screen.blit(interdit,(0,380))
screen.blit(ceder,(520,0))

pygame.display.flip()


while 1:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif (event.type == MOUSEBUTTONDOWN and mx>=200 and mx<=400 and my >= 200 and my <=253):
            root = tkinter.Tk()
            root.wm_withdraw()
            try:
                filename = filedialog.askopenfilename(filetypes =(("Image", "*.png .jpg"),("All Files","*.*")))
            except:
                print("choisir un bon fichier")
            if str(filename) !="":
                print("le fichier est :",filename)
            
        elif (event.type == MOUSEBUTTONDOWN and mx>=200 and mx<=400 and my >= 300 and my <=353):
            print("Charger une video")
        
