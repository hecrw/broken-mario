import pygame as py
from settings import *
from level import Level
from sys import exit

py.init()
window = py.display.set_mode((width, height))
clock = py.time.Clock()
level = Level(window, level_map1)
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.MOUSEBUTTONDOWN:
            print(py.mouse.get_pos())
    window.fill("black")
    level.run()
    py.display.update()
    clock.tick(60)