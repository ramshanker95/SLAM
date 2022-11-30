from turtle import position
import env, sensor
import pygame
import math


environment = env.buildenviroment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensor.LaserSensor(200,environment.originalMap,uncertainty=(0.5,0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()

running = True
while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if pygame.mouse.get_focused():
            sensorON = True
        elif pygame.mouse.get_focused():
            sensorON = False
    if sensorON:
        position = pygame.mouse.get_pos() 
        laser.position = position
        # print(position)
        sensor_data=laser.sense_obsticles()
        # print(sensor_data)
        environment.datastorage(sensor_data)
        environment.showsensordata()
    environment.map.blit(environment.infomap, (0,0))
    pygame.display.update()