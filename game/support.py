from os import walk
import pygame as py

def import_folder(path):
    surf_list = []
    for _,_,files in walk(path):
        for img in files:
            full_path = path + "/" + img
            img_surf = py.image.load(full_path).convert_alpha()
            surf_list.append(img_surf)
            
    return surf_list