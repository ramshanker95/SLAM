import statistics
from turtle import color 
import pygame
import math
import numpy as np

def uncertainty_add(distance,angle,sigma):
    mean= np.array([distance,angle])
    statistics.covariance = np.diag(sigma ** 2)
    distance,angle = np.random.multivariate_normal(mean,statistics.covariance)
    distance = max(distance,0)
    angle = max(angle,0)
    return [distance, angle]



class LaserSensor:
    def __init__(self,Range,map,uncertainty):
        self.Range = Range
        self.map = map
        self.speed = 4  # round per Second
        self.sigma = np.array([uncertainty[0],uncertainty[1]])
        self.position = (0,0)
        self.w,self.h = pygame.display.get_surface().get_size()
        self.sensorobsticles = []

    def distance(self,obsticleposition):
        px = (obsticleposition[0]-self.position[0])**2
        py = (obsticleposition[1]-self.position[1])**2
        # print("PX", px, py)
        return math.sqrt(px+py)

    def sense_obsticles(self):
        data = []
        x1,y1 = self.position[0],self.position[1]
        # print("Zeroes", np.linspace(0.2*math.pi,60,60))
        for angle in np.linspace(0, 2*math.pi, 60, False):
            x2,y2 = (x1 + self.Range*math.cos(angle), y1 - self.Range*math.sin(angle))
            # print("First", x2, y2)
            for i in range(0, 100):
                u = i/100
                x = int(x2 * u+x1*(1-u))
                y = int(y2 * u+y1*(1-u))
                # print(x, y)
                if 0<x<self.w and 0<y<self.h :
                    color = self.map.get_at((x,y))
                    # print("Color: ", color)
                    if color[0]  == 0:
                        distance = self.distance((x,y))
                        output = uncertainty_add(distance,angle,self.sigma)
                        output.append(self.position)
                        # print("Output: " ,  output)

                        data.append(output)
                        break
        if len(data)>0:
            return data
        else :
            return False






    
