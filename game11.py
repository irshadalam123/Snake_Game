import pygame
import time 
import random

pygame.init()

pygame.mixer.init()

# colors
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green=(0,255,50)
blue=(0,0,255)

s_width=800
s_height=400

font=pygame.font.SysFont(None,30)
def text_score(text,color,x,y):
    score_text=font.render(text,True,color)
    gameWindow.blit(score_text,[x,y])

def plot_snake(gameWindow,color,snk_list,size):
    for x,y in snk_list:
        pygame.draw.ellipse(gameWindow,color,[x,y,size+4,size])
        

gameWindow=pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Snake Game")
# End Image
bg_img=pygame.image.load("snake_image.jpg")
bg_img=pygame.transform.scale (bg_img,(s_width,s_height)).convert_alpha()

# background image
bgimg=pygame.image.load("bg_image.jpg")
bgimg=pygame.transform.scale (bgimg,(s_width,s_height)).convert_alpha()

pygame.display.update()

clock=pygame.time.Clock()

def game_loop():
    snake_x=50 
    snake_y=60
    size=10
    fps=30 
    velocity_x=0 
    velocity_y=0
    score=0
    food_x=random.randint(20,s_width-50)
    food_y=random.randint(60,s_height-50)
    exit_game=False
    game_over=False
    snk_list=[]
    snk_length=1    

    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(bg_img,(0,0))
            text_score(f"Your High Score:{score*5}",red,250,70) 
            text_score("Game Over! Prees Enter To continue",red,200,110)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game_loop()

        else:    
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            velocity_x=7
                            velocity_y=0
                        if event.key==pygame.K_LEFT:
                            velocity_x=-7
                            velocity_y=0
                        if event.key==pygame.K_UP:
                            velocity_y=-7
                            velocity_x=0
                        if event.key==pygame.K_DOWN:
                            velocity_y=7
                            velocity_x=0            
                                        
                            
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                food_x=random.randint(20,s_width-50)
                food_y=random.randint(20,s_height-50)
                score +=1
                snk_length +=5
                pygame.mixer.music.load("filling.mp3")
                pygame.mixer.music.play()


            gameWindow.fill(green)
            gameWindow.blit(bgimg,(0,0))
            text_score("Score:"+str(score*5),blue,5,5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("Loud.mp3")
                pygame.mixer.music.play()
                time.sleep(3)    

            if snake_x<0 or snake_x>s_width or snake_y<0 or snake_y>s_height:
                game_over=True
                pygame.mixer.music.load("Loud.mp3")
                pygame.mixer.music.play()
                time.sleep(3)
               

            plot_snake(gameWindow,black,snk_list,size)
            pygame.draw.circle(gameWindow,red,[food_x,food_y],size//2)
                        
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
game_loop()                            