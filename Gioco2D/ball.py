#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 


@author: spyder
"""
import random
import pygame
import sys
import time
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,255,255), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

    

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.rect.right <= 0:
                self.rect.left = 850
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.rect.left >= 850:
                self.rect.right = 0
        if keys[pygame.K_UP]:
            self.rect.y -= 5
            if self.rect.bottom <= 0:
                self.rect.top = 650
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            if self.rect.top >= 650:
                self.rect.bottom = 0


                
                
# Definisci una classe per la sprite di cerchio nero
class BlackCircle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, speed):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= height or self.rect.y <= 0:
            self.speed *= -1
        
            
class BlackCircle2(pygame.sprite.Sprite):    #orizzontali
    def __init__(self, x, y, radius, speed):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= width or self.rect.x <= 0:
            self.speed *= -1 
            
class ColoredCircle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.image = pygame.Surface((radius*2 , radius*2 ), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))     
        
        
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # Il parametro -1 imposta la riproduzione in loop

def play_effect(effect_path):
    effect = pygame.mixer.Sound(effect_path)
    effect.play()

def stop_music():
    pygame.mixer.music.stop()


# Simulazione di una collisione vincente
def handle_win_collision(effect):
    stop_music()  # Interrompi la riproduzione della canzone principale
    play_effect(effect)  # Riproduci l'effetto audio della vittoria
    play_music("space.mp3")  # Riprendi la riproduzione della canzone principale


def gameball():
    play_music("space.mp3")
    win = 0
    perso = 0
    pygame.init()
    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ball_Space")

    # Load background image
    background = pygame.image.load("sfera.png")  # Inserisci il percorso del tuo file immagine
    ball_radius = 20
    bounce_y = height // 2
    bounce_x=width//2
    bounce_speed = 10
    bounce_count = 0
    verdey = 20
    cianox = 750
    redy = 550
    blux = 20
    startred = False
    startciano = False
    startblu = False
    flag1=flag2=flag3=flag4=True
    player = Player(width // 2, height // 2, 20)
    player_sprite = pygame.sprite.GroupSingle(player)
    punteggi={"default":0}

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

        verdey += 10
        if verdey >= height or verdey <= 0:
            verdey = 0

        if verdey in (750, 550):
            startciano = True

        if startciano:
            cianox -= 10

        if cianox <= 0:
            cianox = 800

        if cianox in (20, 550):
            startred = True

        if startred:
            redy -= 10

        if redy <= 0:
            redy = 550

        if redy in (20, 20):
            startblu = True

        if startblu:
            blux += 10
        if blux >= 750:
            blux = 20

        screen.fill("purple")
      
        screen.blit(background, (0, 0))
        
    
        if flag1:
          c1=ColoredCircle( 20, redy,(255, 0, 0), ball_radius)
        if flag2:
          c2=ColoredCircle(750, verdey,(0, 255, 0), ball_radius)
        if flag3:
          c3=ColoredCircle( cianox, 550,(0, 255, 255), ball_radius)
        if flag4:
          c4=ColoredCircle( blux, 20, (0, 0, 255), ball_radius)

        
        black_circle1 = BlackCircle(width // 2 +150, bounce_y, ball_radius, 10)
        black_circle1_1 = BlackCircle(width // 2-150, bounce_y, ball_radius, 10)
        black_circle1_2 = BlackCircle(width // 2-350, bounce_y, ball_radius, 10)
        black_circle1_3 = BlackCircle(width // 2+350, bounce_y, ball_radius, 10)
        black_circle2= BlackCircle2( bounce_x, height // 2 +150 , ball_radius, 10)
        black_circle2_1= BlackCircle2( bounce_x, height // 2 -150 , ball_radius, 10)
        black_circle2_2= BlackCircle2( bounce_x, height // 2 +50 , ball_radius, 10)
        black_circle2_3= BlackCircle2( bounce_x, height // 2 - 50, ball_radius, 10)
        black_circles_group = pygame.sprite.Group(black_circle1, black_circle1_1,black_circle1_2,black_circle1_3,black_circle2,black_circle2_1,black_circle2_2,black_circle2_3)
        bounce_y += bounce_speed
        bounce_x+=bounce_speed
        if bounce_y <= ball_radius or bounce_y >= height - ball_radius:
            bounce_speed *= -1
            bounce_count += 1

            
        color1 = pygame.sprite.GroupSingle(c1)
        color2 = pygame.sprite.GroupSingle(c2)
        color3 = pygame.sprite.GroupSingle(c3)         
        color4 = pygame.sprite.GroupSingle(c4)   
        color1.update()     
        color1.draw(screen)
        color2.update()     
        color2.draw(screen)
        color3.update()     
        color3.draw(screen)
        color4.update()     
        color4.draw(screen)        
        # Aggiorna e disegna le sprite    
        player_sprite.update()
        player_sprite.draw(screen)    

        black_circles_group.update()
        black_circles_group.draw(screen)

        collisions = set(pygame.sprite.spritecollide(player_sprite.sprite, black_circles_group, False))
        if set(pygame.sprite.spritecollide(player_sprite.sprite, color1, False)):
              punteggi["color1"]=1
              flag1=False
              c1=ColoredCircle( 0, 0,(255, 0, 0), 0)
              handle_win_collision("win.mp3")
              
        if set(pygame.sprite.spritecollide(player_sprite.sprite, color2, False)):
                    punteggi["color2"]=1
                    flag2=False
                    c2=ColoredCircle( 0, 0,(255, 0, 0), 0)
                    handle_win_collision("win.mp3")

        if set(pygame.sprite.spritecollide(player_sprite.sprite, color3, False)):
              punteggi["color3"]=1
              flag3=False
              c3=ColoredCircle( 0, 0,(255, 0, 0), 0)
              handle_win_collision("win.mp3")
                
        if set(pygame.sprite.spritecollide(player_sprite.sprite, color4, False)):
                    punteggi["color4"]=1
                    flag4=False
                    c4=ColoredCircle( 0, 0,(255, 0, 0), 0)
                    handle_win_collision("win.mp3")

        if  collisions  or  bounce_count == 60 or sum(punteggi.values())==4:
            if collisions : perso+=1
            win=sum(punteggi.values())
            risultati(str(win), str(perso))
        
        # Update the display
        pygame.display.flip()

        # Control the speed of the game
        pygame.time.Clock().tick(60)
  
def risultati(win,perso):
 
 pygame.init()
 

 width, height = 800, 600
 screen = pygame.display.set_mode((width, height))
 pygame.display.set_caption('Stampa Risultati')
 font = pygame.font.Font(None, 36)
 testo_da_stampare = "HAI VINTO :) hai preso "+win+" palline CLICK PER RESTART" 
 if win==4 : 
      testo_da_stampare2="CONGRATULAZIONI"
      handle_win_collision("win.mp3")
 
 else:  testo_da_stampare2 = ""

 if int(win) < 4 or int(perso) >=1:
     stop_music()
     play_music("lose.mp3")
     testo_da_stampare = "" 
     testo_da_stampare2 = "HAI PERSO  :(  CLICK PER RESTART"
 while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button >= 1:  # Verifica se è stato cliccato il pulsante sinistro del mouse
                gameball()
            sys.exit()


    # Crea una superficie di testo
    testo_renderizzato = font.render(testo_da_stampare, True, (0, 255, 0))
    testo_renderizzato2 = font.render(testo_da_stampare2, True, (255, 0, 0))
    # Posiziona il testo al centro della finestra
    text_rect = testo_renderizzato.get_rect(center=(width // 2, height // 2))
    text_rect2 = testo_renderizzato2.get_rect(center=(width // 2, (height // 2)+50))
    # Disegna il testo sulla schermata
    background = pygame.image.load("sfera.png")
    # Mostra il testo sulla finestra
    screen.blit(background, (0,0))
    screen.blit(testo_renderizzato, text_rect)
    screen.blit(testo_renderizzato2, text_rect2)
    # Aggiorna la finestra
    pygame.display.flip()



    
pygame.init()
play_music("merry.mp3")
with open("file.txt", 'r') as file:
   testo = file.read()
    
width, height = 850, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('AUGURI!')
font = pygame.font.Font(None, 30)
text_surface = font.render(testo, True, (0, 0, 0))
text_rect = text_surface.get_rect(center=(width // 2, 100))
background = pygame.image.load("natale.jpg")
# Mostra il testo sulla finestra
screen.blit(background, (0,0))
screen.blit(text_surface, text_rect)
pygame.display.flip()
time.sleep(5)
pygame.quit()

gameball()
