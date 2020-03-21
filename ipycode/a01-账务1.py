#-*- coding: UTF-8 -*-
from __future__ import print_function
import os
import imp
##############################################################################
from datas import *
import datas

imp.reload(datas)
a= datas.update()
print( len( a.container ));


a.get合同利润();
a.get净现金流();
#gloProc.get供应商合同支付余额()
a.get费用总额();
a.get发票信息();
a.outXlsx( os.path.join("1report","xlsxName.xls") )


