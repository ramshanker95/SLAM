import cv2
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from bresenham import bresenham

WIDTH = 64
HEIGHT = 64

# Creating a blank map
# rmap = np.ones((WIDTH, HEIGHT))

# Load map
rmap = cv2.imread("map.png", 0)

# class For path Finder
class PathFilnder:
    def __init__(self, ix=0, iy=0) :
        self.ix = ix
        self.iy = iy
        self.fx = 0
        self.fy = 0
        

    def load_map(self, img):
        self.img = img 

    def calculate_path(self, fx, fy):
        self.fx = fx
        self.fy = fy
        # Write path finding algorithm
        path_lst = list(bresenham(self.ix,self.iy,self.fx,self.fy))
        # print(path_lst)
        # path_lst = [[randint(0, 60), randint(0,60)] for _ in range(20)]
        self.ix = self.fx
        self.iy = self.fy
        return path_lst


# Class for Robot Move
class Robot:
    def __init__(self, ix=0, iy=0, p_in=0, a_in=1):
        self.ix = ix
        self.iy = iy
        self.fx = 0
        self.fy = 0
        self.a_intesity = a_in
        self.p_intesity = p_in
    
    def load_map(self, img):
        self.img = img

    def move(self, fx, fy):
        # move y direction 
        self.fx = fx
        self.fy = fy
        if (self.iy <= self.fy) and (self.ix <= self.fx):
            self.img[self.iy:self.fy, self.ix] = self.p_intesity
            self.img[self.fy, self.ix:self.fx+1] = self.p_intesity

        else:
            self.img[self.fy:self.iy, self.ix] = self.p_intesity
            self.img[self.fy, self.fx:self.ix+1] = self.p_intesity

        
        # Update initial Position
        self.ix = self.fx
        self.iy = self.fy
        return self.img



rob = Robot()
rob.load_map(rmap)
cal = PathFilnder()
cal.load_map(rmap)
my_list = [(10,5),(15,20),(20,25),(50,35),(30,40),(25,45),(20,55),(0,60)]
for j in my_list:
    # print (j)
    co_ordinate = cal.calculate_path(j[0],j[1])
    # print(co_ordinate[3])
    for cor in co_ordinate:
        # print(cor[0],cor[1])
        rmap = rob.move(cor[0],cor[1])

# rmap = rob.move(1,1)
# rmap = rob.move(2, 1)
# rmap = rob.move(3, 1)
# rmap = rob.move(4, 2)
# rmap = rob.move(5, 2)



# print(rmap)
plt.imshow(rmap, cmap='gray')
plt.show()