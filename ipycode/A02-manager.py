#-*- coding:utf8 -*-
#-*- coding: UTF8
from __future__ import print_function
import sys
import os
sys.path.append( os.path.abspath("../xlsProLib") )
sys.path.append(os.path.abspath("../") )

for i in sys.path:
     print(i)
import os
print(os.curdir)   

import glbcfg

import os

from  dialogBase import *
import  dialogShowList

import  账务处理Lib

import dialog分类显示

title = "项目账务处理系统" +" : "+os.path.abspath(glbcfg.Py1fileRootFolder)
formMain = dialog分类显示.分类显示Dialog(  title )
# formMain.Font =getFont()
# print( Application.CurrentCulture.Name )
Application.Run(formMain)
     

