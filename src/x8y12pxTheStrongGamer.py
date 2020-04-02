#!/usr/bin/env python3
# coding: utf8
import os, string, BitmapFontMapper, BitmapFont
class x8y12pxTheStrongGamer(BitmapFontMapper.BitmapFontMapper):
    def __init__(self, base_dir=''):
        super(x8y12pxTheStrongGamer, self).__init__(base_dir=base_dir)
    @property
    def W(self): return 8
    @property
    def H(self): return 12

