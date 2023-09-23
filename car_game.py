import pygame as pg
import random as r
import math
from tkinter import *

root = Tk()

window=pg.display.set_mode((500,700))
pg.display.set_caption('pygame')
backimage=pg.image.load('F:\\VIGNESH\\Project images\\road.png')
playerimage=pg.image.load('F:\\VIGNESH\\Project images\\car2.png')
playerimage1=pg.image.load('F:\\VIGNESH\\Project images\\car3.png')
playerimage2=pg.image.load('F:\\VIGNESH\\Project images\\car4.png')
playerimage3=pg.image.load('F:\\VIGNESH\\Project images\\car.png')
playerimage4=pg.image.load('F:\\VIGNESH\\Project images\\car5.png')
playerimage5=pg.image.load('F:\\VIGNESH\\Project images\\car6.png')

playerX=400
playerY=600

player_movementX=0
player_movementY=0

playerx2 = r.randrange(0, 450)
playery2 = r.randrange(0, 650)

playe2_movex = 0
player2_movey = 0

#collision mechanism
def collision(playerX,playerY,playerx2,playery2):
    distance=math .sqrt((playerX-playerx2)**2 + (playerY-playery2)**2)
    if distance<30:
        return True
    else:
        return False
def collision1(playerX,playerY,playerx3,playery3):
    distance=math .sqrt((playerX-playerx3)**2 + (playerY-playery3)**2)
    if distance<30:
        return True
    else:
        return False
def collision2(playerX,playerY,playerx4,playery4):
    distance=math .sqrt((playerX-playerx4)**2 + (playerY-playery4)**2)
    if distance<30:
        return True
    else:
        return False
def collision3(playerX,playerY,playerx5,playery5):
    distance=math .sqrt((playerX-playerx5)**2 + (playerY-playery5)**2)
    if distance<30:
        return True
    else:
        return False




playe3_movex = 0
player3_movey = 0

playerx3 = r.randrange(0, 300)
playery3 = r.randrange(0, 650)

playe4_movex = 0
player4_movey = 0

playerx4 = r.randrange(0, 400)
playery4 = r.randrange(0, 300)

playe5_movex = 0
player5_movey = 0

playerx5 = r.randrange(0, 450)
playery5 = r.randrange(0, 200)

#score board
'''
score_value=0
font=pg.font.Font('freesansbold.ttf',32)
textX=10
textY=10
def show_score(x,y):
    score=font.render("Score : "+str(score_value),True,(255,255,255))
    window.blit(score,(x,y))
'''
def Player():
    window.blit(playerimage1,(playerX,playerY))# self car

def Player2():#enemy
    window.blit(playerimage2,(playerx2,playery2))

def Player3():#enemy
    window.blit(playerimage3,(playerx3,playery3))
def Player4():#enemy
    window.blit(playerimage4,(playerx4,playery4))
def Player5():#enemy
    window.blit(playerimage5,(playerx5,playery5))

def back():
    window.blit(backimage,(-80,0))


running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                player_movementX=4
            if event.key==pg.K_LEFT:          #MAIN CONCEPT
                player_movementX=-4
        if event.type==pg.KEYUP:
            if event.key==pg.K_LEFT or pg.K_RIGHT:
                player_movementX=0
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                player2_movey=7
                player3_movey=7
                player4_movey=7
                player5_movey=7
    playerX+=player_movementX
    #playerY+=player_movementY

    playery2+=player2_movey

    playery3+=player3_movey
    playery4 += player4_movey
    playery5 += player5_movey

    back()
    Player()
    Player2()


    Player3()
    Player4()
    Player5()

    if playery2 >=600:
        playery2=0
        playerx2=r.randrange(0,700)
    #collision mechanism
    Colli=collision(playerX,playerY,playerx2,playery2)
    if Colli:
        break
    if playery3 >= 600:
        playery3=0
        playerx3=r.randrange(0,700)

    colli1=collision1(playerX,playerY,playerx3,playery3)
    if colli1:
        break
    if playery4 >= 600:
        playery4=0
        playerx4=r.randrange(0,700)
    colli2=collision2(playerX,playerY,playerx2,playery2)
    if colli2:
        break
    if playery5 >= 600:
        playery5=0
        playerx5=r.randrange(0,700)
    colli3=collision3(playerX,playerY,playerx5,playery5)
    if colli3:
        break

    if playery5==(400,500):
        running=False
    #show_score(textX,textY)
    pg.display.update()
root.title('game over')
root.geometry('800x600')
root.config(bg='black')
l=Label(root,text='GAME OVER',font=('classic',30,'bold'),fg='red',bg='black').place(x=300,y=300)
root.mainloop()