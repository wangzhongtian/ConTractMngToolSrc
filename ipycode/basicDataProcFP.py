#-*- coding: UTF-8
from __future__ import print_function
from basicDataProc import *
import basicDataProc 
import glbcfg
import swaplib

# import basicLib
class 发票开Cls (发票Cls):
    def swap(self ):    
        # if (self.记账方 == jizhang and duifang == self.对方  ) :

        if swaplib.needSwap( self.记账方 ,self.对方):
            newObject = 发票收Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None
    def cal(self):
        super(发票开Cls,self).cal()
        # print( "calend ....")
        self.税率 = eval( str(self.税率) )
        # print( "calend ....",self.税率)
        # self.发票含税总额 = eval( str(self.发票含税总额) )
        # self.归一金额=  self.发票含税总额/10000.0;
        self.发票收入=self.归一金额/(1+ self.税率 / 100.0) 
        self.发票税额=  self.归一金额 -self.发票收入 


    def get_D02_销售开票额(self ):        
        return self.归一金额 * self.getguiyixishu();      

    def get_D05_销售开票收入(self ):
        self.税率 = eval( str(self.税率) )    
        # if( self.开票类型 == "专票"):
        收入=self.get_D02_销售开票额()/(1+ self.税率 / 100.0) 
        # else:
        #     发票收入=self.归一金额*self.getguiyixishu()        
        return 收入;  

    def get_C13_已收管理费(self ):
        if self.记账方 == glbcfg.管理费收取企业名称:
            val =self.get_D02_销售开票额() * glbcfg.管理费系数
            return val;
        else:
            return 0.0  
    # def get_L10_现有利润额(self ):
    #     return self.get_D05_销售开票收入() - self.get_C13_已收管理费();   

    def get_S12_发票税额(self ):
        val = self.get_D02_销售开票额()    - self.get_D05_销售开票收入()
        return val
    # def get_F11_发票附加税费(self ):  
    #     val =self.get_S12_发票税额() *glbcfg.附加税费系数
    #     return val  ;

    # def get_S13_待纳增值税额(self ):                 
    #     return sel.get_S12_发票税额();      

    # def getBasic财务数据(self):
    #     aobj = Basic财务数据()
    #     # aobj.transferData(self)
    #     # return aobj
    #     aobj.销售合同额=0.0
    #     aobj.销售合同收入=0.0

    #     aobj.采购合同额=0.0  
    #     aobj.采购合同成本=0.0      

    #     aobj.销售开票额=self.归一金额          
    #     aobj.销售开票收入=self.发票收入    

    #     aobj.采购收票额=0.0          
    #     aobj.采购收票成本=0.0  

    #     aobj.销售收款额=0.0  

    #     aobj.采购支出额=0.0   

    #     aobj.费用计划额=0.0          
    #     aobj.费用支付额=0.0  
    #     return aobj         
    def getguiyixishu(self):
        return 1.0                   
    def get归一金额(self,数据类型) :
        if 数据类型 =="原始数据":
            return self.归一金额
        elif 数据类型 =="财务收益分析":
            return self.发票收入
        return 0.0

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "发票开具"    
    def get金额(self):
        return self.归一金额    
    def is名附实(self):
        if "KJ" in self.序号.upper():
            return True
        return False 
    def getFNstr(self):
        return  "销售开票"
           
class 发票收Cls (发票Cls):
    def swap(self ):     
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方):    
            newObject = 发票开Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None
    def cal(self):
        super(发票收Cls,self).cal()
        self.税率 = eval( str(self.税率) )
				
        if( self.开票类型 == "专票"):
            self.发票成本=self.归一金额/(1+ self.税率 / 100.0) 
        else:
            self.发票成本=self.归一金额              
        self.发票税额=  self.发票成本- self.归一金额 


    def get_B02_采购收票额(self ):
        return self.归一金额*self.getguiyixishu() ;  

    def get_B05_采购收票成本(self ): 
        self.税率 = eval( str(self.税率) )    
        if( self.开票类型 == "专票"):
            发票成本 = self.get_B02_采购收票额()/(1+ self.税率 / 100.0) 
        else:
            发票成本 = self.get_B02_采购收票额()       
        return 发票成本;

    def get_S12_发票税额(self ):
        val = self.get_B02_采购收票额() - self.get_B05_采购收票成本()
        return val *self.getguiyixishu()    

    # def getBasic财务数据(self):

    #     aobj = Basic财务数据()

    #     aobj.销售合同额=0.0
    #     aobj.销售合同收入=0.0

    #     aobj.采购合同额=0.0  
    #     aobj.采购合同成本=0.0      

    #     aobj.销售开票额=    0.0     
    #     aobj.销售开票收入= 0.0

    #     aobj.采购收票额=self.归一金额    *-1.0       
    #     aobj.采购收票成本=self.发票成本  *-1.0

    #     aobj.销售收款额=0.0  

    #     aobj.采购支出额=0.0   

    #     aobj.费用计划额=0.0          
    #     aobj.费用支付额=0.0  
    #     return aobj   

    def get归一金额(self,数据类型) :
        if 数据类型 =="原始数据":
            return self.归一金额
        elif 数据类型 =="财务收益分析":
            return self.发票成本
        return 0.0

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "发票收"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        if "JS" in self.序号.upper():
            return True
        return False 

    def getFNstr(self):
        return  "采购收票"
    def getguiyixishu(self):
        return -1.0         
           
class 报销发票收Cls (发票收Cls):
    def swap(self ):     
        # if (self.记账方 == jizhang and duifang == self.对方  ) :
        if swaplib.needSwap( self.记账方 ,self.对方):    
            newObject = 发票开Cls( self )
            newObject.记账方=self.对方
            newObject.对方= self.记账方
            return newObject;
        else:
            return None
    def cal(self):
        super(报销发票收Cls,self).cal()
        self.税率 = eval( str(self.税率) )
				
        if( self.开票类型 == "专票"):
            self.发票成本=self.归一金额/(1+ self.税率 / 100.0) 
        else:
            self.发票成本=self.归一金额              
        self.发票税额=  self.发票成本- self.归一金额 


    def get_B02_采购收票额(self ):
        return 0;
        return  self.归一金额*self.getguiyixishu() ;  

    def get_B05_采购收票成本(self ): 
        return 0;
        self.税率 = eval( str(self.税率) )    
        if( self.开票类型 == "专票"):
            发票成本 = self.get_B02_采购收票额()/(1+ self.税率 / 100.0) 
        else:
            发票成本 = self.get_B02_采购收票额()       
        return 发票成本;

    def get_S12_发票税额(self ):
        self.税率 = eval( str(self.税率) )    
        票额 = self.归一金额*self.getguiyixishu() 
        if( self.开票类型 == "专票"):
            发票成本 = 票额/(1+ self.税率 / 100.0) 
        else:
            发票成本 = 票额
        val = 票额 - 发票成本

        return val *self.getguiyixishu()    

    # def getBasic财务数据(self):

    #     aobj = Basic财务数据()

    #     aobj.销售合同额=0.0
    #     aobj.销售合同收入=0.0

    #     aobj.采购合同额=0.0  
    #     aobj.采购合同成本=0.0      

    #     aobj.销售开票额=    0.0     
    #     aobj.销售开票收入= 0.0

    #     aobj.采购收票额=self.归一金额    *-1.0*0       
    #     aobj.采购收票成本=self.发票成本  *-1.0*0

    #     aobj.销售收款额=0.0  

    #     aobj.采购支出额=0.0   

    #     aobj.费用计划额=0.0          
    #     aobj.费用支付额=0.0  
    #     return aobj   

    def get归一金额(self,数据类型) :
        if 数据类型 =="原始数据":
            return self.归一金额
        elif 数据类型 =="财务收益分析":
            return 0.0 #self.发票成本
        return 0.0

    def get日期(self):
        return self.发生日期
    def get财务类型(self):
        return "报销收票"    
    def get金额(self):
        return self.归一金额  
    def is名附实(self):
        return True
        if "BX" in self.序号.upper():
            return True
        return False 

    def getFNstr(self):
        return  "报销收票"
    def getguiyixishu(self):
        return -1.0         
    def get_B11_采购待收票(self ):
        return 0;
        # val =    self.get_B01_采购合同额(  ) - self.get_B02_采购收票额()   
        # return val;
    def get_B12_采购应付款(self ): 
        # val =   self.get_B02_采购收票额() -  self.get_B03_采购支出额(  )  
        # return val;
        return 0;
    # def get_B13_采购待付款(self ):   
    #     # val =   self.get_B01_采购合同额() -  self.get_B03_采购支出额(  )              
    #     # return val; 
    #     return 0;        
    def get_L10_现有利润额(self ):
        v1 = super(报销发票收Cls,self).get_L10_现有利润额( )
        return v1- self.get_S12_发票税额()    