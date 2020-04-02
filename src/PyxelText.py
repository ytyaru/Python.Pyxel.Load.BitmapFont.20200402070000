#!/usr/bin/env python3
# coding: utf8
from PIL import Image, ImageFont, ImageDraw
import pyxel, PyxelSpec

class PyxelText:
    def __init__(self, font, img=0, col=7, colkey=0):
        self.__font = font
        self.__img = img
        self.__col = col
        self.__colkey = colkey
        self.__load()
    def __load(self):
        img_bank = pyxel.image(self.__img)
        for y in range(PyxelSpec.Image.Size[1]):
            for x in range(PyxelSpec.Image.Size[0]):
                img_bank.set(x, y, self.__col if self.__font.Data[y][x] else 0) 
    def draw(self, x, y, s):
        w, h = self.__font.Size
        left = x
        for ch in s:
            if ch == '\n':
                x = left
                y += h
                continue
            if ch == ' ':
                x += w
                continue
            if ch in self.__font.Coords.keys():
                u, v = self.__font.Coords[ch]
                pyxel.blt(x, y, self.__img, u, v, w, h, self.__colkey)
#             for y_ in range(h):
#                 for x_ in range(w):
#                     if self.__font.Data[v+y_, u+x_]:
#                         pyxel.pix(x+x_, y+y_, col)
            x += w


