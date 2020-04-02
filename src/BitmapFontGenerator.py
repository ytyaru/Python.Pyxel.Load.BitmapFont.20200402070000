#!/usr/bin/env python3
# coding: utf8
import string, os, BitmapFont, BitmapFontMapper

class BitmapFontGenerator:
    def __init__(self, fontfile='x8y12pxTheStrongGamer.ttf', w=8, h=12):
        self.__fontfile = os.path.abspath(fontfile)
        self.__letter_size = (w, h)
        self.__font = BitmapFont.BitmapFont(self.__fontfile, self.__letter_size, BitmapFontMapper.BitmapFontMapper().Letters)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='ビットマップフォント作成（.ttfから.pngを出力）', 
        add_help=False, 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--fontfile', default='x8y12pxTheStrongGamer.ttf', help='ttf形式ファイルパス')
    parser.add_argument('-w', '--width', type=int, default=8, help='png出力時における1字あたりのピクセル幅')
    parser.add_argument('-h', '--height', type=int, default=12, help='png出力時における1字あたりのピクセル高さ')
    parser.add_argument('--help', action='help', help='ヘルプ表示する')
    args = parser.parse_args()
    BitmapFontGenerator(args.fontfile, args.width, args.height)

