import pygame
from sys import exit
from PIL import Image
import random

pygame.init()
#set Game resolution
screen = pygame.display.set_mode((1000,600))
#Title of the game
pygame.display.set_caption('CallBreak')
#Framerate of the Game
clock=pygame.time.Clock()
# Font inside the Game
font = pygame.font.Font('fontsss/Pixeltype.ttf', 50)
#calling picture in the Game
Table_top=pygame.image.load('PNG/table.jpg').convert()#convert_alpha for cards
Table_rect=Table_top.get_rect(topleft=(0,0))
Writing= Writing= font.render('CallBreak',False,'Black')
start= font.render('Click anywhere or Press any key on the screen to start the game',False,'Black')

bot1=pygame.image.load("PNG/back.png")
bot1=pygame.transform.rotate(bot1,-90) 
w=bot1.get_width()
b=bot1.get_height()
bot=pygame.transform.scale(bot1,(w*0.04,b*0.04)).convert_alpha()
screen.blit(Table_top,(0,0))
def maingame():
    a='j'

    while True:
        if a=='k':
            break
        
        
        screen.blit(Writing,(500,20))
        screen.blit(start,(20,300))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #mouse_pos=pygame.mouse.get_pos()
        #Table_rect.collidepoint(mouse_pos):
        
        for item in pygame.mouse.get_pressed():
            
            if item==True:
                a='k'
        if  True in pygame.key.get_pressed():
            a='k'
                
                   
                
                
        
        
        
        


    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    #now inserting the picture in the game 
        screen.blit(Table_top,(0,0))
        
        screen.blit(bot,bot.get_rect(midleft=(5,300)))
        screen.blit(pygame.transform.rotate(bot,-90),bot.get_rect(midtop=(500,5)))
        screen.blit(pygame.transform.rotate(bot,-180),bot.get_rect(midright=(995,300)))
        pygame.display.update()
        clock.tick(60)
maingame()

def cards():
    shufflecards1=[]
    shufflecards2=[]
    shufflecards3=[]
    shufflecards4=[]
    
    cards=['2C.png', '3C.png', '4C.png', '5C.png', '6C.png', '7C.png', '8C.png', '9C.png', '10C.png','2D.png', '3D.png', '4D.png', '5D.png', '6D.png', '7D.png', '8D.png', '9D.png', '10D.png',
           '2S.png', '3S.png', '4S.png', '5S.png', '6S.png', '7S.png', '8S.png', '9S.png', '10S.png','2H.png', '3H.png', '4H.png', '5H.png', '6H.png', '7H.png', '8H.png', '9H.png', '10H.png',
           'AH.png', 'AD.png', 'AS.png', 'AC.png', 'KH.png', 'KD.png', 'KS.png', 'KC.png', 'QH.png', 'QD.png', 'QS.png', 'QC.png', 'JH.png', 'JD.png', 'JS.png', 'JC.png']
    random.shuffle(cards)
    
           
           
