#-*- coding: UTF8
from __future__ import print_function

import glbcfg 
import 财务统计计算
class caiwuBaseCls1(object):
    def __init__(self):
        pass
    def __getattr__(self, name) :
        # for key in dir(self):
        #         print ("---",key)
        if name[:2]=="__" :
            raise AttributeError 
        if name[-2:]=="__" :
            raise AttributeError             
        exp ="get_"+name
        expression = "self."+exp+ "()"
        # print( "~~~????? :",name," ",expression )
        if exp in dir(self): 
            val =eval( expression)
            return val
        else:
            print("无法发现属性：",name)
            raise AttributeError
            # return None
#########################

    def get_D15_销售待开票(self ):
        val = self.get_D01_销售合同额() - self.get_D02_销售开票额()
        return val ;
    def get_D16_销售应收款(self ):         
        val = self.get_D02_销售开票额() - self.get_D03_销售收款额()
        return val ;
    def get_D17_销售待收款(self ):
        val = self.get_D01_销售合同额() - self.get_D03_销售收款额()
        return val ;

    def get_B11_采购待收票(self ):
        val =    self.get_B01_采购合同额(  ) - self.get_B02_采购收票额()   
        return val;
    def get_B12_采购应付款(self ): 
        val =   self.get_B02_采购收票额() -  self.get_B03_采购支出额(  )  
        return val;

    def get_B13_采购待付款(self ):   
        val =   self.get_B01_采购合同额() -  self.get_B03_采购支出额(  )              
        return val; 

    def get_S13_待纳增值税额(self ): 
        val =   self.get_S11_增值税额() - self.get_S12_发票税额()       
        return val;


    def get_F12_待纳附加税费额(self ):  
        val = self.get_F10_增值附加税费() -   self.get_F11_发票附加税费()
        return val ;
#############
    # def get_F11_发票附加税费(self ):  
    def get_F11_发票附加税费(self ):  
        val =self.get_S12_发票税额() *glbcfg.附加税费系数
        return val  ;
    def get_C11_费用待支额(self ):
        val =self.get_C01_费用计划额() -self.get_C02_费用支付额()

        return val;
#############

    def get_F10_增值附加税费(self ):
        val = self.get_S11_增值税额() *glbcfg.附加税费系数
        return val ;
############

    def get_D03_销售收款额(self ):              
        return 0;

    def get_D01_销售合同额(self ):
        return 0;   
    def get_C12_应收管理费(self ):
        return 0;    

    def get_D04_销售合同收入(self ):        
        return 0;
    
    def get_S11_增值税额(self):
        return 0
    def get_D02_销售开票额(self ):        
        return 0;          
    def get_D05_销售开票收入(self ):        
        return 0;
    def get_C13_已收管理费(self ):
        return 0;  

    def get_S12_发票税额(self ):
        return 0;

    def get_B03_采购支出额(self ):              
        return 0; 
    def get_B01_采购合同额(self ):
        return 0;
    def get_B04_采购合同成本(self ):        
        return 0;  

    def get_B02_采购收票额(self ):
        return 0;           
    def get_B05_采购收票成本(self ):         
        return 0;

    def get_C01_费用计划额(self ):
        return 0;
    def get_C02_费用支付额(self ):                
        return 0;

    def get_X10_现金流余额(self ):
        valout =  self.get_B03_采购支出额() +self.get_C02_费用支付额()+  \
            self.get_F11_发票附加税费()+ self.get_S12_发票税额()+ self.get_C13_已收管理费() 
        valin = self.get_D03_销售收款额()
            
        return valin - valout;

    def get_L10_现有利润额(self ):
        valout =  self.get_B05_采购收票成本() +self.get_C02_费用支付额() \
              + self.get_F11_发票附加税费() +self.get_C13_已收管理费() 
        valin = self.get_D05_销售开票收入()
            
        return valin - valout;

    def get_L11_项目利润额(self ):        
        valout =  self.get_B04_采购合同成本() +self.get_C01_费用计划额() \
              + self.get_F10_增值附加税费() +self.get_C12_应收管理费() 
        valin = self.get_D04_销售合同收入()
        return valin - valout;
    def get_账务分类(self):
        return self.getFNstr()
    def get_费用子类(self):
        return "NA"

    def get_签署方式(self):
        return "NA"   
    def getBasic财务数据(self):        
        aobj = 财务统计计算.Basic财务数据()
        aobj.transferData(self)
        return aobj       
def test():
    a= caiwuBaseCls1()
    # a.title ="qwewqe"
    print(a.titile)
    print(a.nameObj )
    print(a.D15_销售待开票)
    print("---")
    print(a.get_F10_增值附加税费())
    # print(a.__getstate__())
class caiwuBaseCls(object):
    pass
# test()    