#-*- coding: UTF-8
from __future__ import print_function
from basicDataProc import *
import   basicDataProc
import   glbcfg   
import swaplib     
class 现金流支付Cls (现金Cls):
    def swap(self ):    
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方):    
            newObject = 现金流收款Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None

    def get归一金额(self,数据类型) :
        return self.归一金额
    def get_B03_采购支出额(self ):              
        return self.归一金额 *self.getguiyixishu(); 

      
 
    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "现金支付"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "F" in self.序号.upper():
            return True
        return False       
    def getguiyixishu(self):
        return -1.0  

    def getFNstr(self):
        return  "采购支出"                          
class 现金流收款Cls (现金Cls):
    def swap(self,jizhang="PT",duifang="ZD" ):     
        if (self.记账方 == jizhang and duifang == self.对方  ) :
            newObject = 现金流支付Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None

    def get归一金额(self,数据类型) :
        return self.归一金额

    def get_D03_销售收款额(self ):              
        return self.归一金额*self.getguiyixishu();

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "现金收款"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "S" in self.序号.upper():
            return True
        return False  
                          
    def getFNstr(self):
        return  "销售收款" 
    def getguiyixishu(self):
        return 1.0      

class 报销采购支出Cls (现金Cls):
    def swap(self ):    
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方) :   
            newObject = 现金流收款Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None

    def get归一金额(self,数据类型) :
        return self.归一金额
    # def get_B03_采购支出额(self ):              
    #     return self.归一金额 *self.getguiyixishu(); 
    def get_C02_费用支付额(self):
        return self.归一金额 *self.getguiyixishu(); 
    def get_C11_费用待支额(self ):
        return 0 
    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "报销采购支出"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "B" in self.序号.upper():
            return True
        return False       
    def getguiyixishu(self):
        return -1.0  

    def getFNstr(self):
        return  "报销采购支出" 

class 直接采购支出Cls (现金Cls):
    def swap(self ):    
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方):  
            newObject = 现金流收款Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None

    def get归一金额(self,数据类型) :
        return self.归一金额
    def get_B03_采购支出额(self ):              
        return self.归一金额 *self.getguiyixishu(); 
    def get_C11_费用待支额(self ):
        return 0 
    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "直接采购支出"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "Z" in self.序号.upper():
            return True
        return False       
    def getguiyixishu(self):
        return -1.0  

    def getFNstr(self):
        return  "直接采购支出" 
    def get_L10_现有利润额(self ):
        val1 = super(直接采购支出Cls,self).get_L10_现有利润额()
        return val1 + self.get归一金额("1")
    def get_L11_项目利润额(self ):  
        val1 = super(直接采购支出Cls,self).get_L11_项目利润额()
        return val1 + self.get归一金额("2")


    def get_B12_采购应付款(self ): 
        return 0;
        val =   self.get_B02_采购收票额() -  self.get_B03_采购支出额(  )  
        return val;

    def get_B13_采购待付款(self ): 
        return 0  ;
        val =   self.get_B01_采购合同额() -  self.get_B03_采购支出额(  )              
        return val;             
class 代赋税支出Cls (现金Cls):
    def get归一金额(self,数据类型) :
        return self.归一金额

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "代赋税支出"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "D" in self.序号.upper():
            return True
        return False       
    def getguiyixishu(self):
        return -1.0  

    def getFNstr(self):
        return  "代赋税支出" 

    def get_B03_采购支出额(self ):
        return self.归一金额 *self.getguiyixishu(); 
    def get_B05_采购收票成本(self ): 
        # print( self.归一金额 )        
        return self.归一金额 ; 

    def get_X10_现金流余额(self ):
        return  0; 

    def get_L10_现有利润额(self ):
        valout1 = self.get_B05_采购收票成本()
        valout =  valout1 +self.get_C02_费用支付额() \
              + self.get_F11_发票附加税费() +self.get_C13_已收管理费() 
        valin = self.get_D05_销售开票收入()

        return valin - valout;    
    def get_F11_发票附加税费(self ): 
        return 0
