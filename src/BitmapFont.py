#!/usr/bin/env python3
# coding: utf8
from PIL import Image, ImageFont, ImageDraw
import os, numpy, PyxelSpec
class BitmapFont:
    def __init__(self, file, size, letters):
        self.__file = file
        self.__size = size
        self.__letters = letters
        self.__coords = None
        self.__data = None
        if   '.ttf' == os.path.splitext(self.__file)[1]: self.__export_png()
        elif '.png' == os.path.splitext(self.__file)[1]: self.load_from_png()
#        else: print('引数エラー。Fontクラスに渡すfipeは拡張子がttfかpngのパスであるべき。'); exit 1;
    def __export_png(self):
        # px_w, px_h = size
        # pt_w, pt_h = (int(n * 0.75) for n in meta['size']) # 96 dpi
        # font = ImageFont.truetype(file, size=px_h) # it must be pt_h, but px_h brings better result
        font = ImageFont.truetype(self.__file, size=self.__size[1]) # it must be pt_h, but px_h brings better result
        img = Image.new('1', size=PyxelSpec.Image.Size)
        draw = ImageDraw.Draw(img)
        self.__load(draw, font)
        self.__data = numpy.array(img.getdata()).reshape(PyxelSpec.Image.Size[0], PyxelSpec.Image.Size[1])
        self.__img = img
        self.__img.save(os.path.splitext(self.__file)[0] + '.png')
    def __load(self, draw=None, font=None):
        coords = {}
        x, y = 0, 0
        for c in self.__letters:
            if x + self.__size[0] > PyxelSpec.Image.Size[0]:
                x = 0
                y += self.__size[1]
            if draw: draw.text((x, y), c, font=font, fill=1)
            coords[c] = (x, y)
            x += self.__size[0]
        self.__coords = coords
    def load_from_png(self):
        self.__load()
        img = Image.open(self.__file)
        self.__data = numpy.array(img.getdata()).reshape(PyxelSpec.Image.Size[0], PyxelSpec.Image.Size[1])
    @property
    def FilePath(self): return self.__file
    @property
    def Size(self): return self.__size
    @property
    def Letters(self): return self.__letters
    @property
    def Coords(self): return self.__coords
    @property
    def Data(self): return self.__data

