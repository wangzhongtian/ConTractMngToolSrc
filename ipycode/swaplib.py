#-*- coding: UTF8
from __future__ import print_function
import glbcfg
def needSwap(记账方,对方):
    if (记账方 == glbcfg.swap记账方 and glbcfg.swap对方 == 对方) or  ( 对方 == glbcfg.swap记账方 and glbcfg.swap对方 == 记账方   ):
        return True;
    else:
        return False