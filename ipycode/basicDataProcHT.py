#-*- coding: UTF-8
from __future__ import print_function
from basicDataProc import *
import basicDataProc
import glbcfg
import swaplib    
class 合同采购Cls (合同Cls):
    def swap(self ):   
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方):            
            newObject =合同销售Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None
    def cal(self):
        super(合同采购Cls,self).cal()
        # print( "will cal shuilv")
        # for i in self.__dict__.keys():
        #  print(i)
        self.税率 = eval( str(self.税率) )
		#print('aobj.开票类型="专票" # 专票  普票' );					
        if( self.开票类型 == "专票"):
            self.合同成本=self.归一金额/(1+ self.税率 / 100.0) 
        else:
            self.合同成本=self.归一金额              
        self.税额=  self.合同成本- self.归一金额
    # def getBasic财务数据(self):
    #     aobj = Basic财务数据()
    #     aobj.采购合同额=self.归一金额*-1.0
    #     aobj.采购合同成本=self.合同成本*-1.0
    #     return aobj      
    def get归一金额(self,数据类型) :
        if 数据类型 =="原始数据":
            return self.归一金额
        elif 数据类型 =="财务收益分析":
            return self.合同成本
        return 0.0
    def get发生日期(self):
        return self.发生日期

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "采购合同"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "C" in self.序号.upper():
            return True
        return False 
    def getFNstr(self):
        return  "采购合同"       
    def getguiyixishu(self):
        return -1.0  

    # def get_B03_采购支出额(self ):              
    #     return self.归一金额;   
    def get_B01_采购合同额(self ):
        return self.归一金额* self.getguiyixishu();
    def get_B04_采购合同成本(self ):        
        self.税率 = eval( str(self.税率) )    
        if( self.开票类型 == "专票"):
            成本 = self.get_B01_采购合同额()/(1+ self.税率 / 100.0)
        else:
            成本 = self.get_B01_采购合同额()      
        return 成本 ;        
    def get_S11_增值税额(self ):
        税额 = self.get_B01_采购合同额() - self.get_B04_采购合同成本()      
        return 税额* self.getguiyixishu();   

    # def get_L11_项目利润额(self ):        
    #     return self.get_B04_采购合同成本(); 
    # def get_F10_增值附加税费(self ):
    #     val = self.get_S11_增值税额() *glbcfg.附加税费系数
    #     return val ; 

    # def get_S13_待纳增值税额(self ):                 
    #     return sel.get_S11_增值税额();    

class 合同销售Cls (合同Cls):
    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "销售合同"    
    def get金额(self):
        return self.归一金额  
    def swap(self): 
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方):            
            newObject = 合同采购Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None
    def cal(self):
        super(合同销售Cls,self).cal()
        self.税率 = eval( str(self.税率) ) 
        # self.发票总金额 = eval( str(self.发票总金额) )
        # # self.发票含税总额 = eval( str(self.发票含税总额) )                 
        # self.归一金额=  self.发票总金额/10000.0;
        self.合同收入=self.归一金额/(1+ self.税率 / 100.0) 
        self.税额=  self.归一金额 -self.合同收入

    def get_D01_销售合同额(self ):
        return self.归一金额*self.getguiyixishu();   
    def get_C12_应收管理费(self ):
        if self.记账方 == glbcfg.管理费收取企业名称:        
            val =self.归一金额 * glbcfg.管理费系数
            return val; 
        return 0.0    

    def get_D04_销售合同收入(self ):        
        self.税率 = eval( str(self.税率) )    
        # if( self.开票类型 == "专票"):
        收入=self.get_D01_销售合同额() /(1+ self.税率 / 100.0)
        # else:
        #     收入=self.get_D01_销售合同额()          
        return 收入;  
    def get_S11_增值税额(self ):
        税额 = self.get_D01_销售合同额() -self.get_D04_销售合同收入()      
        return 税额;  

    # def get_L11_项目利润额(self ):        
    #     return self.get_D04_销售合同收入();  

    # def get_F10_增值附加税费(self ):
    #     val = self.get_S11_增值税额() *glbcfg.附加税费系数
    #     return val ;
    # def get_S13_待纳增值税额(self ):                 
    #     return sel.get_S11_增值税额();   

    # def getBasic财务数据(self):
    #     aobj = Basic财务数据()
    #     aobj.销售合同额=self.归一金额
    #     aobj.销售合同收入=self.合同收入   
    #     return aobj          
    def get归一金额(self,数据类型) :
        if 数据类型 =="原始数据":
            return self.归一金额
        elif 数据类型 =="财务收益分析":
            return self.合同收入
        return 0.0
    def get发生日期(self):
        return self.发生日期
    def is名附实(self):
        if "X" in self.序号.upper():
            return True
        return False  
     
    def getFNstr(self):
        return  "销售合同"  
    def getguiyixishu(self):
        return 1.0          