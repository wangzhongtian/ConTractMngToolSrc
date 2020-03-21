#-*- coding: UTF8
from __future__ import print_function

def classifyAcoount( datasObjDictionary1):
#     print( datasObjDictionary1.__class__ )
    for  a  in datasObjDictionary1:
       a.合同大类 , unitname , a.合同子类  = a.关联销售合同名称.split("-")
       # print( a.合同大类, a.合同子类 ,a.关联销售合同名称 )

       #  self.OrgObj.关联销售合同名称 = self.value关联销售合同名称.get()
       #  self.OrgObj.合同大类,unitname , self.OrgObj.合同子类 = self.OrgObj.关联销售合同名称.split("-")   
 