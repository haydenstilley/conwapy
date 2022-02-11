import pygame
import stage

class Node: #object representing individual cells/pixels

    onoff = False
    
    ns = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def pos(self,x,y):  #assign neighbors
        self.x = x
        self.y = y
        self.n1 = [x,(y-1)]
        self.n2 = [(x+1),(y-1)]
        self.n3 = [(x+1),y]
        self.n4 = [(x+1),(y+1)]
        self.n5 = [x,(y+1)]
        self.n6 = [(x-1),(y+1)]
        self.n7 = [(x-1),y]
        self.n8 = [(x-1),(y-1)]
        
    def nCount(self): #neighbor counter
        self.ns = 0
        counter = {
            True: 1,
            False: 0
        }
        try:
            self.ns += counter[stage.stage1.bg[self.n1[0]][self.n1[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n2[0]][self.n2[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n3[0]][self.n3[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n4[0]][self.n4[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n5[0]][self.n5[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n6[0]][self.n6[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n7[0]][self.n7[1]].onoff]
        except IndexError as error:
            pass
        try:
            self.ns += counter[stage.stage1.bg[self.n8[0]][self.n8[1]].onoff]
        except IndexError as error:
            pass
        if (self.ns > 4):
            self.ns = 4
        if (self.ns == 2):
            if (self.onoff == True):
                self.ns = 3
        return self.ns

    onImg = pygame.image.load("#####.png")   #single-pixel images for on/off status of cells (not currently included)
    offImg = pygame.image.load("#####.png")
