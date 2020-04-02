#!/usr/bin/env python3
# coding: utf8
import os, string, BitmapFont
class BitmapFontMapper:
    def __init__(self, base_dir=''):
        self.__base_dir = base_dir
        self.__font = None
        self.Font
    @property
    def Letters(self):
        ascii_chars = string.punctuation + string.digits + string.ascii_letters
        hira = "".join(chr(c) for c in range(ord('ぁ'), ord('ゔ')+1))+"ー"
        kata = "".join(chr(c) for c in range(ord('ァ'), ord('ヶ')+1))+"ー"
        # hankata = "".join(chr(c) for c in range(ord('ｧ')-6, ord('ﾞ')+2))
        return ascii_chars + hira + kata + "、。「」"
    @property
    def W(self): return 8
    @property
    def H(self): return 12
    def __ttf2png(self):
        self.__font = BitmapFont.BitmapFont(self.TtfPath, (self.W, self.H), self.Letters)
    @property
    def Font(self):
        if self.__font: return self.__font
        if not os.path.isfile(self.PngPath): self.__ttf2png()
        self.__font = BitmapFont.BitmapFont(self.PngPath, (self.W, self.H), self.Letters)
        return self.__font
    @property
    def BaseDir(self): return self.__base_dir
    @property
    def ClassName(self): return self.__class__.__name__
    @property
    def TtfPath(self): return os.path.join(self.BaseDir, self.ClassName + '.ttf')
    @property
    def PngPath(self): return os.path.join(self.BaseDir, self.ClassName + '.png')

    """
    def __init__(self):
        self.__sizes = {
            'x8y12pxTheStrongGamer': (8, 12),
            'x12y16pxLineLinker': (12, 16),
            'x16y32pxGridGazer': (16, 32),
            'x12y20pxScanLine': (12, 20),
            'x14y20pxScoreDozer': (14, 20),
            'x14y24pxHeadUpDaisy': (14, 24),
            'x12y16pxLineLinker': (12, 16),
        }
    @property
    def Sizes(self): return self.__sizes
    """

