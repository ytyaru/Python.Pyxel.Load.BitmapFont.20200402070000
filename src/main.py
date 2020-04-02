#!/usr/bin/env python3
# coding: utf8
import os, pyxel, PyxelSpec, x8y12pxTheStrongGamer, PyxelText
class App:
    def __init__(self):
        pyxel.init(PyxelSpec.Window.Size[0], PyxelSpec.Window.Size[1], caption="PNGフォント")
        self.font = x8y12pxTheStrongGamer.x8y12pxTheStrongGamer(self.ResDir)
        self.pyxtext = PyxelText.PyxelText(self.font.Font)
        pyxel.run(self.update, self.draw)
    @property
    def ResDir(self):
        this = os.path.abspath(__file__)
        here = os.path.dirname(this)
        parent = os.path.dirname(here)
        return os.path.join(parent, 'res')
    def update(self): pass
    def draw(self):
        pyxel.cls(0)
        self.pyxtext.draw(0, 0, """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
みにくいよりうつくしいほうがいい。
Explicit is better than implicit.
あんじするよりめいじするほうがいい。
Simple is better than complex.
ふくざつであるよりはへいいであるほうがいい。
Complex is better than complicated.
それでも、こみいっているよりはふくざつであるほうがまし。
Flat is better than nested.
ネストはあさいほうがいい。
Sparse is better than dense.
みっしゅうしているよりはすきまがあるほうがいい。
Readability counts.
よみやすいことはぜんである。
Special cases aren't special enough to break the rules.
とくしゅであることはルールをやぶるりゆうにならない。
Although practicality beats purity.
しかし、じつようせいをもとめるとじゅんすいさがうしなわれることが
ある。""".strip())

if __name__ == '__main__':
    App()

