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
#calling sounds
start_sound=pygame.mixer.Sound("music/start.mp3")
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
animation_cooldown=200

def scorecount(s1,s2,s3,s4, highest_card,shufflecards1,shufflecards2,shufflecards3,shufflecards4):
    if highest_card in shufflecards1:
        s1+=1
    elif highest_card in shufflecards2:
        s2+=1
    elif highest_card in shufflecards3:
        s3+=1
    elif highest_card in shufflecards4:
        s4+=1
    return s1,s2,s3,s4
    


def cardsShuffle():
    shufflecards1=[]
    shufflecards2=[]
    shufflecards3=[]
    shufflecards4=[]
    cards=['00C.png', '01C.png','02C.png', '03C.png', '04C.png', '05C.png', '06C.png', '07C.png', '08C.png', '09C.png', '10C.png','11C.png', '12C.png',
           '00D.png', '01D.png','02D.png', '03D.png', '04D.png', '05D.png', '06D.png', '07D.png', '08D.png', '09D.png', '10D.png','11D.png', '12D.png',
           '00S.png', '01S.png','02S.png', '03S.png', '04S.png', '05S.png', '06S.png', '07S.png', '08S.png', '09S.png', '10S.png','11S.png', '12S.png',
           '00H.png', '01H.png','02H.png', '03H.png', '04H.png', '05H.png', '06H.png', '07H.png', '08H.png', '09H.png', '10H.png','11H.png', '12H.png']
    random.shuffle(cards)
    random.shuffle(cards)
    random.shuffle(cards)    
    
    shufflecards1=cards[:13]
    shufflecards1.sort()
    
    print(shufflecards1)
    shufflecards2=cards[13:26]
    
    shufflecards3=cards[26:39]
    shufflecards4=cards[39:]
    
    
    return shufflecards1,shufflecards2,shufflecards3,shufflecards4  

		
		


def computer_player(Card_played1,Suit, Value, Cards,x,y, rotate,n):
    print(Cards)
    print(Value)
    print(Suit,'gvgh')
    dis='99t'
    
    a=True
    b=True
    c=True
    d=True
    if n==0:
        for card in Cards:
            print(card[2],'ffghvhgvh')
            if card[2]==Suit:
                a=False
                c=False
                if int(card[0:2])>Value and dis[2]==Suit:
                    if int(card[0:2])>int(dis[0:2]):
                        dis=card
                        b=False
                        d=False
                        highest_card=card
                elif int(card[0:2])<int(dis[0:2]) and b and dis[2]==Suit:
                    highest_card=Card_played1
                    dis=card
                    d=False
                elif d:
                    d=False
                    dis=card
                    if int(card[0:2])>Value:
                        highest_card=card
                        b=False
                    else:
                        highest_card=Card_played1
            elif card[2]=='S' and a:
                if card[0:2]<int(dis[0:2]) and dis[2]=='S':
                    dis=card
                    highest_card=card
                elif dis[2]!='S':
                    dis=card
                    highest_card=card
                c=False
            elif c:
                if card[0:2]<int(dis[0:2]) and dis[2]!='t':
                    dis=card
                    highest_card=Card_played1
                elif dis[2]=='t':
                    dis=card
                    highest_card=Card_played1
                
    elif n==1:
        for card in Cards:
            print(card[2],'ffghvhgvh')
            if card[2]==Suit:
                a=False
                c=False
                if highest_card[2]!=Suit and highest_card[2]=='S' and (int(dis[0:2])<14):
                    if int(card[0:2])<int(dis[0:2]):
                        dis=card
                        highest_card=Card_played1
                    
                elif int(card[0:2])>Value and dis[2]==Suit:
                    if int(card[0:2])>int(dis[0:2]):
                        dis=card
                        b=False
                        highest_card=card
                   
                    
                elif int(card[0:2])<int(dis[0:2]) and b and dis[2]==Suit:
                    highest_card=Card_played1
                    dis=card
                else:
                    dis=card
                    if int(card[0:2])>Value:
                        highest_card=card
                    else:
                        highest_card=Card_played1
                    
            elif card[2]=='S' and a:
                if highest_card[2]=="S":
                    if int(card[0:2])>int(dis[0:2]):
                        dis=card
                    dis=card
                highest_card=card
                print('123')
                c=False
            elif c:
                dis=card
                highest_card=Card_played1

            
            
    print(dis,'h')
    disp=pygame.image.load('PNG/'+dis)
    disp=pygame.transform.scale(disp,((disp.get_width())*0.09,(disp.get_height())*0.09)).convert_alpha()
    
    screen.blit(pygame.transform.rotate(disp,rotate),disp.get_rect(midbottom=(x,y)))
    return dis, highest_card



def maingame():
    
    a='j'
    shufflecards1,shufflecards2,shufflecards3,shufflecards4=cardsShuffle()
    count_played=0
    

    while True:
        if a=='k':
            break
        
        start_sound.play()
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
    start_sound.stop()
    a,b,c,d,e,f,g,h,i,j,k,l,m=90,160,230,300,370,440,510,580,650,720,790,860,930
    last_time=pygame.time.get_ticks()
    while True:
        
        #now inserting the picture in the game 
            screen.blit(Table_top,(0,0))
            screen.blit(bot,bot.get_rect(midleft=(5,300)))
            screen.blit(pygame.transform.rotate(bot,-90),bot.get_rect(midtop=(500,5)))
            screen.blit(pygame.transform.rotate(bot,-180),bot.get_rect(midright=(995,300)))
            mouse_pos=pygame.mouse.get_pos()
            # 1st card
            dis1=pygame.image.load('PNG/'+shufflecards1[0])
            disp1=pygame.transform.scale(dis1,((dis1.get_width())*0.09,(dis1.get_height())*0.09)).convert_alpha()
            recta1=disp1.get_rect(midbottom=(a,550))
            if recta1.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
                n=0
                screen.blit(disp1,disp1.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[0],shufflecards1[0][2],int(shufflecards1[0][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[0],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[0],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    s1,s2,s3,s4=scorecount(0,0,0,0, highest_card,shufflecards1,shufflecards2,shufflecards3,shufflecards4)
                    a=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
                    
            else:
            
                screen.blit(disp1,recta1)

            #2nd card
            dis2=pygame.image.load('PNG/'+shufflecards1[1])
            disp2=pygame.transform.scale(dis2,((dis2.get_width())*0.09,(dis2.get_height())*0.09)).convert_alpha()
            recta2=disp2.get_rect(midbottom=(b,550))
            if recta2.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
                
                screen.blit(disp2,disp2.get_rect(midbottom=(b,300)))
                dis, highest_card=computer_player(shufflecards1[1],shufflecards1[1][2],int(shufflecards1[1][0:2]), shufflecards2, 440,300,0)
                dis1,highest_card=computer_player(highest_card,shufflecards1[1][2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2,highest_card=computer_player(highest_card,shufflecards1[1][2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    scorecount(s1,s2,s3,s4, highest_card,shufflecards1,shufflecards2,shufflecards3,shufflecards4)
                    b=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp2,recta2)
            #3rd card
            dis3=pygame.image.load('PNG/'+shufflecards1[2])
            disp3=pygame.transform.scale(dis3,((dis3.get_width())*0.09,(dis3.get_height())*0.09)).convert_alpha()
            recta3=disp3.get_rect(midbottom=(c,550))
            if recta3.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp3,disp3.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[2],shufflecards1[2][2],int(shufflecards1[2][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[2],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[2],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    c=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp3,recta3)
            
            #4th card
            dis4=pygame.image.load('PNG/'+shufflecards1[3])
            disp4=pygame.transform.scale(dis4,((dis4.get_width())*0.09,(dis4.get_height())*0.09)).convert_alpha()
            recta4=disp4.get_rect(midbottom=(d,550))
            if recta4.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp4,disp4.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[3],shufflecards1[3][2],int(shufflecards1[3][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[3],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[3],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    d=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp4,recta4)
            #5th card
            dis5=pygame.image.load('PNG/'+shufflecards1[4])
            disp5=pygame.transform.scale(dis5,((dis5.get_width())*0.09,(dis5.get_height())*0.09)).convert_alpha()
            recta5=disp5.get_rect(midbottom=(e,550))
            if recta5.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp5,disp5.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[4],shufflecards1[4][2],int(shufflecards1[5][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[4],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[4],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    e=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp5,recta5)

            #6th card
            dis6=pygame.image.load('PNG/'+shufflecards1[5])
            disp6=pygame.transform.scale(dis6,((dis6.get_width())*0.09,(dis6.get_height())*0.09)).convert_alpha()
            recta6=disp6.get_rect(midbottom=(f,550))
            if recta6.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp6,disp6.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[5],shufflecards1[5][2],int(shufflecards1[5][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[5],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[5],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    f=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp6,recta6)
            

            #7th card
            dis7=pygame.image.load('PNG/'+shufflecards1[6])
            disp7=pygame.transform.scale(dis7,((dis7.get_width())*0.09,(dis7.get_height())*0.09)).convert_alpha()
            recta7=disp7.get_rect(midbottom=(g,550))
            if recta7.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp7,disp7.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[6],shufflecards1[6][2],int(shufflecards1[6][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[6],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[6],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    g=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp7,recta7)

            #8th card
            dis8=pygame.image.load('PNG/'+shufflecards1[7])
            disp8=pygame.transform.scale(dis8,((dis8.get_width())*0.09,(dis8.get_height())*0.09)).convert_alpha()
            recta8=disp8.get_rect(midbottom=(h,550))
            if recta8.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp8,disp8.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[7],shufflecards1[7][2],int(shufflecards1[7][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[7],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[7],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    h=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp8,recta8)

            #9th card
            dis9=pygame.image.load('PNG/'+shufflecards1[8])
            disp9=pygame.transform.scale(dis9,((dis9.get_width())*0.09,(dis9.get_height())*0.09)).convert_alpha()
            recta9=disp9.get_rect(midbottom=(i,550))
            if recta9.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp9,disp9.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[8],shufflecards1[8][2],int(shufflecards1[8][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[8],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[8],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    i=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp9,recta9)

            #10th card
            dis10=pygame.image.load('PNG/'+shufflecards1[9])
            disp10=pygame.transform.scale(dis10,((dis10.get_width())*0.09,(dis10.get_height())*0.09)).convert_alpha()
            recta10=disp10.get_rect(midbottom=(j,550))
            if recta10.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp10,disp10.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[9],shufflecards1[9][2],int(shufflecards1[9][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[9],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[9],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    j=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp10,recta10)

            #11th card
            dis11=pygame.image.load('PNG/'+shufflecards1[10])
            disp11=pygame.transform.scale(dis11,((dis11.get_width())*0.09,(dis11.get_height())*0.09)).convert_alpha()
            recta11=disp11.get_rect(midbottom=(k,550))
            if recta11.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
                screen.blit(disp11,disp11.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[10],shufflecards1[10][2],int(shufflecards1[10][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[10],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[10],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    k=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp11,recta11)

            #12th card
            dis12=pygame.image.load('PNG/'+shufflecards1[11])
            disp12=pygame.transform.scale(dis12,((dis12.get_width())*0.09,(dis12.get_height())*0.09)).convert_alpha()
            recta12=disp12.get_rect(midbottom=(l,550))
            if recta12.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp12,disp12.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[11],shufflecards1[11][2],int(shufflecards1[11][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[11],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[11],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    l=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp12,recta12)
            

            #13th card
            dis13=pygame.image.load('PNG/'+shufflecards1[12])
            disp13=pygame.transform.scale(dis13,((dis13.get_width())*0.09,(dis13.get_height())*0.09)).convert_alpha()
            recta13=disp13.get_rect(midbottom=(m,550))
            
            if recta13.collidepoint(mouse_pos)and (True in pygame.mouse.get_pressed()) :
            
                screen.blit(disp13,disp13.get_rect(midbottom=(370,300)))
                dis=computer_player(shufflecards1[12],shufflecards1[12][2],int(shufflecards1[12][0:2]), shufflecards2, 440,300,0)
                dis1=computer_player(shufflecards1[12],dis[2],int(dis[0:2]), shufflecards3, 510,300,0)
                dis2=computer_player(shufflecards1[12],dis1[2],int(dis1[0:2]), shufflecards4, 580,300,0)
                current_time=pygame.time.get_ticks()
                if current_time - last_time>= animation_cooldown:
                    m=10000
                    shufflecards2.remove(dis)
                    shufflecards3.remove(dis1)
                    shufflecards4.remove(dis2)
                    last_time=current_time
                    count_played+=1
                    
            else:
                screen.blit(disp13,recta13)
            if count_played==13:
                break
                
                
                    
            pygame.display.update()
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    while True:
            End_game= font.render('The Game is over',False,'Black')
            screen.blit(Table_top,(0,0))
            screen.blit(End_game,(400,300))
            pygame.display.update()

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                    
                    
            
            clock.tick(60)
maingame()




    
           
           
