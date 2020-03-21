#-*- coding:utf8 -*-
from __future__ import print_function
import sys
import os

sys.path.append( os.path.abspath("../xlsProLib") )
sys.path.append(os.path.abspath("../") )
for i in sys.path:
     print(i)
import os
print(os.curdir)   
import os

import  basicDataProc
import fileSplit
import glbcfg

fileSplit.合并( os.path.join(glbcfg.Py1fileRootFolder,"Gened/datas.py"),os.path.join(glbcfg.Py1fileRootFolder)  )

basicDataProc.datasObj= None
import sys

sys.path.append(os.path.join(glbcfg.Py1fileRootFolder,"Gened") )
import  datas  
print(" load dataDb into mem end ,ok ..")
basicDataProc.dataDic = datas.gloProc.container
basicDataProc.Save2DataDB()
pass
