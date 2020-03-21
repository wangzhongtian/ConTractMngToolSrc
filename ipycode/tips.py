#-*- coding: UTF8
from __future__ import print_function

import os
import  账务处理Lib
def getAllPossible(colname , key ):
    # print(colname,key )
    colname = colname.strip()
    key = key.strip() 
    a = dict()
    dataObjArrary = 账务处理Lib.getdataDic()
    for v in dataObjArrary :
        if colname in v.__dict__:
            val = v.__dict__[ colname  ] 
            # print( val ) 
            if key in val :
                a[ val.strip() ] =""
    b=()
    for item in a.keys():
        b = b + ( item ,)
    return b

    





