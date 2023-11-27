import pygame
from sys import exit
from PIL import Image
import random

    
    
    


shufflecards1=[]
shufflecards2=[]
shufflecards3=[]
shufflecards4=[]    
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
Writing= Writing= font.render('CallBreak',False,'Black')
start= font.render('Click anywhere or Press any key on the screen to start the game',False,'Black')
bot1=pygame.image.load("PNG/back.png")
bot1=pygame.transform.rotate(bot1,-90) 
w=bot1.get_width()
b=bot1.get_height()
bot=pygame.transform.scale(bot1,(w*0.04,b*0.04)).convert_alpha()
screen.blit(Table_top,(0,0))
def cardsShuffle():
    cards=['2C.png', '3C.png', '4C.png', '5C.png', '6C.png', '7C.png', '8C.png', '9C.png', '10C.png','2D.png', '3D.png', '4D.png', '5D.png', '6D.png', '7D.png', '8D.png', '9D.png', '10D.png',
           '2S.png', '3S.png', '4S.png', '5S.png', '6S.png', '7S.png', '8S.png', '9S.png', '10S.png','2H.png', '3H.png', '4H.png', '5H.png', '6H.png', '7H.png', '8H.png', '9H.png', '10H.png',
           'AH.png', 'AD.png', 'AS.png', 'AC.png', 'KH.png', 'KD.png', 'KS.png', 'KC.png', 'QH.png', 'QD.png', 'QS.png', 'QC.png', 'JH.png', 'JD.png', 'JS.png', 'JC.png']
    random.shuffle(cards)
    
    
    shufflecards1=cards[:13]
    
    shufflecards1.sort()
    shufflecards2=cards[13:26]
    
    shufflecards3=cards[26:39]
    shufflecards4=cards[39:]
    
    
    return shufflecards1,shufflecards2,shufflecards3,shufflecards4  


class Player():#pygame.sprite.Sprite):
        shufflecards1,shufflecards2,shufflecards3,shufflecards4=cardsShuffle()
        def __init__(self, x, y, botcards,cardnum  ):
                self.dis='shufflecards{}[{}]'.format(botcards, cardnum)
                self.di=self.dis
                self.image=pygame.image.load('PNG/'+self.dis)
                self.scale=pygame.transform.scale(self.image,((self.image.get_width())*0.09,(self.image.get_height())*0.09)).convert_alpha()
        def display():
                screen.blit(self.scale,self.scale.get_rect(midbottom=((x),y)))
		
		

def Gameplay(N): 
    x=0
    suits=['C','S','D','H']
    shufflecards1,shufflecards2,shufflecards3,shufflecards4=cardsShuffle()
    for card in shufflecards2:
        if shufflecards1[N][1]==card[1]:
            cardsdis=Player(500,300,2,N)
            cardsdis.display()

def maingame():
    a='j'
    
    shufflecards1,shufflecards2,shufflecards3,shufflecards4=cardsShuffle()
    
    
    rect=[]
    

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
    a=930
    while True:
        
        #now inserting the picture in the game 
            screen.blit(Table_top,(0,0))
            
            screen.blit(bot,bot.get_rect(midleft=(5,300)))
            screen.blit(pygame.transform.rotate(bot,-90),bot.get_rect(midtop=(500,5)))
            screen.blit(pygame.transform.rotate(bot,-180),bot.get_rect(midright=(995,300)))
            #disp.get_rect(midbottom=(a,550))
            '''
            a=90
            #yu=[]
            for car in shufflecards1:
                #yu.append('PNG/'+car)
                
                
                dis=pygame.image.load('PNG/'+car)
                 
                w=dis.get_width()
                b=dis.get_height()
                disp=pygame.transform.scale(dis,(w*0.09,b*0.09)).convert_alpha()
                recta=disp.get_rect(midbottom=(a,550))
                rect.append(recta)
                
                #screen.blit(disp,recta)
                a+=70



            class carddistribution(pygame.sprite.Sprite):
                def __init___(self, width, height, pos_x, pos_y ):
                    self.image=pygame.surface([width, height])
                    self.rect=self.image.get_rect(midbottom=(pos,550))'''
                    




            # 1st card
            dis1=pygame.image.load('PNG/'+shufflecards1[0])
            disp1=pygame.transform.scale(dis1,((dis1.get_width())*0.09,(dis1.get_height())*0.09)).convert_alpha()
            recta1=disp1.get_rect(midbottom=(90,550))
            screen.blit(disp1,recta1)
            #2nd card
            dis2=pygame.image.load('PNG/'+shufflecards1[1])
            disp2=pygame.transform.scale(dis2,((dis2.get_width())*0.09,(dis2.get_height())*0.09)).convert_alpha()
            recta2=disp2.get_rect(midbottom=(160,550))
            screen.blit(disp2,recta2)
            #3rd card
            dis3=pygame.image.load('PNG/'+shufflecards1[2])
            disp3=pygame.transform.scale(dis3,((dis3.get_width())*0.09,(dis3.get_height())*0.09)).convert_alpha()
            recta3=disp3.get_rect(midbottom=(230,550))
            screen.blit(disp3,recta3)
            #4th card
            dis4=pygame.image.load('PNG/'+shufflecards1[3])
            disp4=pygame.transform.scale(dis4,((dis4.get_width())*0.09,(dis4.get_height())*0.09)).convert_alpha()
            recta4=disp4.get_rect(midbottom=((300),550))
            screen.blit(disp4,recta4)
            #5th card
            dis5=pygame.image.load('PNG/'+shufflecards1[4])
            disp5=pygame.transform.scale(dis5,((dis5.get_width())*0.09,(dis5.get_height())*0.09)).convert_alpha()
            recta5=disp5.get_rect(midbottom=((370),550))
            screen.blit(disp5,recta5)
            #6th card
            dis6=pygame.image.load('PNG/'+shufflecards1[5])
            disp6=pygame.transform.scale(dis6,((dis6.get_width())*0.09,(dis6.get_height())*0.09)).convert_alpha()
            recta6=disp6.get_rect(midbottom=((440),550))
            screen.blit(disp6,recta6)
            #7th card
            dis7=pygame.image.load('PNG/'+shufflecards1[6])
            disp7=pygame.transform.scale(dis7,((dis7.get_width())*0.09,(dis7.get_height())*0.09)).convert_alpha()
            recta7=disp7.get_rect(midbottom=((510),550))
            screen.blit(disp7,recta7)
            #8th card
            dis8=pygame.image.load('PNG/'+shufflecards1[7])
            disp8=pygame.transform.scale(dis8,((dis8.get_width())*0.09,(dis8.get_height())*0.09)).convert_alpha()
            recta8=disp8.get_rect(midbottom=((580),550))
            screen.blit(disp8,recta8)
            #9th card
            dis9=pygame.image.load('PNG/'+shufflecards1[8])
            disp9=pygame.transform.scale(dis9,((dis9.get_width())*0.09,(dis9.get_height())*0.09)).convert_alpha()
            recta9=disp9.get_rect(midbottom=((650),550))
            screen.blit(disp9,recta9)
            #10th card
            dis10=pygame.image.load('PNG/'+shufflecards1[9])
            disp10=pygame.transform.scale(dis10,((dis10.get_width())*0.09,(dis10.get_height())*0.09)).convert_alpha()
            recta10=disp10.get_rect(midbottom=((720),550))
            screen.blit(disp10,recta10)
            #11th card
            dis11=pygame.image.load('PNG/'+shufflecards1[10])
            disp11=pygame.transform.scale(dis11,((dis11.get_width())*0.09,(dis11.get_height())*0.09)).convert_alpha()
            recta11=disp11.get_rect(midbottom=((790),550))
            screen.blit(disp11,recta11)
            #12th card
            dis12=pygame.image.load('PNG/'+shufflecards1[11])
            disp12=pygame.transform.scale(dis12,((dis12.get_width())*0.09,(dis12.get_height())*0.09)).convert_alpha()
            recta12=disp12.get_rect(midbottom=((860),550))
            screen.blit(disp12,recta12)
            #13th card
            
            
            dis13=pygame.image.load('PNG/'+shufflecards1[12])
            disp13=pygame.transform.scale(dis13,((dis13.get_width())*0.09,(dis13.get_height())*0.09)).convert_alpha()
            recta13=disp13.get_rect(midbottom=(a,550))
            mouse_pos=pygame.mouse.get_pos()
            if recta13.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
                screen.blit(disp13,disp13.get_rect(midbottom=(500,300)))
                Gameplay(12)
                a=10000
                
                
            else: screen.blit(disp13,recta13)
                    
            pygame.display.update()
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                    
            
            clock.tick(60)
maingame()




    
           
           
