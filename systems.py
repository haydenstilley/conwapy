import pygame
import stage
import random

pygame.init()

win = pygame.Surface((100,100)) #surface for resizing

screen = pygame.display.set_mode((500,500)) #target surface

def ruleFilter(node):
    n = {
        0: False,
        1: False,
        2: False,
        3: True,
        4: False
    }
    node.onoff = n[node.ns]

def turn(bg,x=100,y=100): #advance the game one turn
    for i in range(x):
        for j in range(y):
            bg[i][j].nCount()
    for i in range(x):
        for j in range(y):
            ruleFilter(bg[i][j])
    for i in range(x):
        for j in range(y):
            if (bg[i][j].onoff == True):
                win.blit(bg[i][j].onImg,(i,j))
            else:
                win.blit(bg[i][j].offImg,(i,j))

run = True

stage.stage1.drawNodes()

for i in range(100):
    for j in range(100):
        x = random.randint(1,100)
        if (x<=40):
            stage.stage1.bg[i][j].onoff = True

while run==True: #primary loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    turn(stage.stage1.bg)
   
    win2 = pygame.transform.scale(win,(500,500)) #resized surface

    for x in range(100): #update screen surface
        for y in range(100):
            screen.blit(win2,(x,y))

    pygame.display.flip() #update screen

    pygame.time.delay(10) #delay before next turn

pygame.quit()
