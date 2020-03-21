#-*- coding: UTF-8
from __future__ import print_function
from basicDataProc import *
import  basicDataProc      
import   glbcfg 
import swaplib      
class 现金流费用支付Cls (费用Cls):
    def swap(self ):     
            return None

    def get归一金额(self,shujuType) :
        return self.归一金额
    def getguiyixishu(self):
        return -1.0  

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "费用支出"    
    def get金额(self):
        return self.归一金额

  
    def is名附实(self):
        if "F" in self.序号.upper():
            return True
        return False               

    def getFNstr(self):
        return  "费用支出"  
            
class 费用合同Cls ( FY基本合同Cls):
    def swap(self ): 
        # if swaplib.needSwap( self.记账方 ,self.对方):                
            return None

    def get归一金额(self,shujuType) :
        return self.归一金额

    # def get_L11_项目利润额(self ):        
    #     return self.归一金额;  

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "费用合同"    
    def get金额(self):
        return self.归一金额   
  
    def is名附实(self):
        if "F" in self.序号.upper():
            return True
        return False         
    
    def getFNstr(self):
        return  "费用合同"            
    def getguiyixishu(self):
        return -1.0          
