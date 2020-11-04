# coding: utf-8
from sympy.printing.dot import dotprint
import os

def dotexport(expr, fname):
    txt = str(dotprint(expr))

    name = os.path.splitext(fname)[0]

    f = open('{}.dot'.format(name), 'w')
    f.write(txt)
    f.close()

    cmd = 'dot {name}.dot -Tpng -o {name}.png'.format(name=name)
    os.system(cmd)

from sympy.abc import x,y
expr = x**2 + x*y
dotexport(expr, 'graph1.png')
