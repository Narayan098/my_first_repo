import pygame
from random import*
import time
import random

font_name=pygame.font.match_font('arial')
pygame.init()
pygame.mixer.init()

def draw_text(text,size,x,y):
    font1=pygame.font.Font(font_name,size)
    text_surface=font1.render(text,True, [102,0,102])
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    gameDisplay.blit(text_surface,text_rect)


gameDisplay = pygame.display.set_mode((1280,611))
pygame.display.set_caption('crowdy lane')

clock = pygame.time.Clock()
crashed = True
carImg = pygame.image.load(r'images\3.png')

background = pygame.image.load(r'images\background.jpg')


obcar=pygame.image.load(r'images\6.png')

obcar2=pygame.image.load(r'D:images\5.png')

obcar3=pygame.image.load(r'images\4.png')

crash_sound=pygame.mixer.Sound(r'sound\crash.wav')

move1=pygame.mixer.Sound(r'sound\carmove1.wav')
move2=pygame.mixer.Sound(r'sound\carmove2.wav')
move3=pygame.mixer.Sound(r'sound\carmove3.wav')
move4=pygame.mixer.Sound(r'sound\carmove4.wav')
move5=pygame.mixer.Sound(r'sound\carmove5.wav')
move6=pygame.mixer.Sound(r'sound\carmove6.wav')


while(1):


    
    s=random.randint(1,6)
    if s==1: 
        pygame.mixer.Sound.play(move1)
    if s==2: 
        pygame.mixer.Sound.play(move2)
    if s==3:  
        pygame.mixer.Sound.play(move3)
    if s==4:  
        pygame.mixer.Sound.play(move4)
    if s==5:  
        pygame.mixer.Sound.play(move5)
    if s==6:
        pygame.mixer.Sound.play(move6)
          


    if(crashed==True):
        gameDisplay.blit(background,(0,0))  
        draw_text("Press Enter To Play  ",80,640,50)
        draw_text("Press Escape To Quit",80,640,150)
        count=0
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT  :
                 pygame.quit()
                 quit()

            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_KP_ENTER:
                    crashed=False
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    if(crashed==False):
        count=0

     
        x = 50
        y = 510

        ox=1300
        oy=510

        ox2=1800
        oy2=460

        ox3=2200
        oy3=510


        gameDisplay.blit(background, (0,0))
        draw_text("CROWDY LANE",90,640,0)
        draw_text("press SPACEBAR to change ",50,640,100)
        draw_text("the lane of the road ",50,640,150)
        pygame.display.update()
        time.sleep(2)

        gameDisplay.blit(background,(0,0))
        draw_text("3",100,640,100)
        gameDisplay.blit(carImg, (x,y))
        pygame.display.update()
        time.sleep(1)

        gameDisplay.blit(background,(0,0))
        draw_text("2",100,640,100)  
        gameDisplay.blit(carImg, (x,y))
        pygame.display.update()
        time.sleep(1)

        gameDisplay.blit(background,(0,0))
        draw_text("1",100,640,100)
        gameDisplay.blit(carImg, (x,y))
        pygame.display.update()
        time.sleep(1)

        gameDisplay.blit(background,(0,0))  
        draw_text("GO",100,640,100)
        gameDisplay.blit(carImg, (x,y)) 
        pygame.display.update()
        time.sleep(1)
        speed=10



        while not crashed:

               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                   
                    if event.key== pygame.K_SPACE:
                        if(y==510):
                            y-=50;
                
                        else:
                            y+=50;
                     

            gameDisplay.blit(background, (0,0))
            gameDisplay.blit(obcar, (ox,oy))
            gameDisplay.blit(obcar2, (ox2,oy2))
            gameDisplay.blit(obcar3,(ox3,oy3))

            gameDisplay.blit(carImg, (x,y))

            draw_text('score='+str(int(count/10)),50,1100,10)
            if ox<=-100:
                ox=1300
                n=randint(1,2)
                if n==1:
                    oy=460
                else:
                    oy=510
            if ox2<=-100:
                ox2=1300
                n=randint(1,2)
                if n==1:
                    oy2=460
                else:
                    oy2=510
            if ox3<=-100:
                ox3=1300
                n=randint(1,2)
                if n==1:
                    oy3=460
                else:
                    oy3=510

            if( (ox  <=150 and ox>=50) and (oy == y )or((ox2  <=150 and ox2>=50) and (oy2 == y ))or ((ox3  <=150 and ox3>=50) and (oy3 == y ))):

                pygame.mixer.Sound.stop(move1)
                pygame.mixer.Sound.stop(move2)
                pygame.mixer.Sound.stop(move3)
                pygame.mixer.Sound.stop(move4)
                pygame.mixer.Sound.stop(move5)
                pygame.mixer.Sound.stop(move6)
                
                pygame.mixer.Sound.play(crash_sound)
              
                draw_text('CRASHED!',200,640,200)
                pygame.display.update()
              
                time.sleep(2)
                crashed=True
               

            if count%300==0:
                speed+=4


            ox-=speed
            ox2-=speed
            ox3-=speed
            pygame.display.update()

            count+=1
