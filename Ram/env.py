import math
import pygame



class buildenviroment:
    def __init__(self,MapDimension) :
        pygame.init()
        self.externalMap=pygame.image.load('map1.png')
        self.maph,self.mapw = MapDimension
        self.mapWindow = 'RRT path plannning'
        pygame.display.set_caption(self.mapWindow)
        self.map = pygame.display.set_mode((self.mapw,self.maph))
        self.map.blit(self.externalMap,(0,0))
        self.black = (0,0,0)
        self.gray = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.red = (255,0,0)
        self.white = (255,255,255)
        self.pointCloud = []

    def AD2pos (self,distance,angle,robotPosition):
        x = distance*math.cos(angle)+robotPosition[0]
        y = -distance*math.sin(angle)+robotPosition[1]
        return(int(x),int(y))


    def datastorage(self,data):
        # print(len(self.pointCloud))
        if data:
            for element in data:
                point = self.AD2pos(element[0],element[1],element[2])
                if point not in self.pointCloud :
                    self.pointCloud.append(point)

    def showsensordata (self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255,0,0))


