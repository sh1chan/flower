#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳

class LC():
    end = '\033[0m' #-----#
    blue = '\033[94m' #---#
    purple = '\033[35m' #-#
    vermelho = '\033[31m' #

flo = '''
{0}...............................................
....＊..＊......＊..＊＊.....................................
....＊....＊....＊.{1}希信{0}..............................
.....{1}仰愛{0}.＊{3}..........{0}＊........................................
....＊＊{3}......{2}｢{3}...{0}＊＊....................
...........{2}㉡{3}＊{2}㉠{0}..............................
......＊＊{3}...{2}｣{3}......{0}＊＊...............................
....＊{3}..........{0}＊.{1}幸運{0}.....................
.......{1}望{0}.＊....＊....＊...............................
....＊＊..＊..{1}＊{0}..＊..＊.............................................
..............{1}＊{0}..............................
..............{1}＊{0}..........................................
....{2}____{0}_6_{2}__{0}..{1}＊{0}.......................................
....{2}___{0}__6__{2}__{0}..{1}＊{0}.......................
....{2}__{0}___6___{2}__{0}..{1}＊{0}................................
..................{1}＊{0}...........................
...................{1}＊{0}....................................
.{2}kira@-築城院.真鍳{0}..........................『{2}言葉無限欺{0}』..........{3}
'''.format(LC.vermelho, LC.purple, LC.blue, LC.end)

print(flo)