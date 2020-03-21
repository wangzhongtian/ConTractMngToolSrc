#-*- coding: UTF-8
from __future__ import print_function
import copy
import os
from  名称定义 import *
import imp
from  xlsProLib import *
import glbcfg
class Basic财务数据1():
    def __init__(self):
        self.销售合同额=0.0
        self.销售合同收入=0.0

        self.采购合同额=0.0  
        self.采购合同成本=0.0      

        self.销售开票额=0.0          
        self.销售开票收入=0.0  

        self.采购收票额=0.0          
        self.采购收票成本=0.0  

        self.销售收款额=0.0  

        self.采购支出额=0.0   

        self.费用计划额=0.0          
        self.费用支付额=0.0  
        self.D15_销售待开票 = 0
        self.D16_销售应收款 = 0
        self.D17_销售待收款 = 0



        self.B11_采购待收票 = 0
        self.B12_采购应付款 = 0
        self.B13_采购待付款 = 0

        self.C11_费用待支额 =0 

        self.C12_应收管理费 = 0.0 


        self.C13_已收管理费 = 0.0 
         


        self.S11_增值税额 = 0
        self.S12_发票税额 = 0
        self.S13_待纳增值税额 =0

        self.F10_增值附加税费 =0                 
        self.F11_发票附加税费 = 0
        self.F12_待纳附加税费额 =0

        self.X10_现金流余额=0
        self.L10_现有利润额= 0
        self.L11_项目利润额= 0
#############
        self.D01_销售合同额=0
        self.D02_销售开票额=0         
        self.D03_销售收款额=0
        self.D04_销售合同收入=0
        self.D05_销售开票收入=0  

        self.B01_采购合同额=0
        self.B02_采购收票额= 0       
        self.B03_采购支出额=0 
        self.B04_采购合同成本=0   
        self.B05_采购收票成本=0  

        self.C01_费用计划额=0       
        self.C02_费用支付额=0

    def cal(self):
        管理费系数 = glbcfg.管理费系数
        附加税费系数 = glbcfg.附加税费系数


        self.D15_销售待开票 = self.销售合同额 - self.销售开票额
        self.D16_销售应收款 = self.销售开票额 - self.销售收款额
        self.D17_销售待收款 = self.销售合同额 - self.销售收款额



        self.B11_采购待收票 = self.采购合同额 - self.采购收票额
        self.B12_采购应付款 = self.采购收票额 - self.采购支出额
        self.B13_采购待付款 = self.采购合同额 - self.采购支出额

        self.C11_费用待支额 = self.费用计划额 - self.费用支付额  

        self.C12_应收管理费 = 0.0 
        try:
            if self.记账方 == glbcfg.管理费收取企业名称:
                self.C12_应收管理费 = 管理费系数 * self.销售合同额
        except:
            pass

        self.C13_已收管理费 = 0.0 
        try:
            if self.记账方 == glbcfg.管理费收取企业名称:
                self.C13_已收管理费 =  管理费系数 * self.销售开票额
        except:
            pass       


        self.S11_增值税额 = self.销售合同额- self.销售合同收入  \
                 - (  self.采购合同额 -  self.采购合同成本 )
        self.S12_发票税额 = self.销售开票额- self.销售开票收入  \
                 - (  self.采购收票额 -  self.采购收票成本 )
        self.S13_待纳增值税额 = self.S11_增值税额  - self.S12_发票税额

        self.F10_增值附加税费 = self.S11_增值税额 * 附加税费系数                 
        self.F11_发票附加税费 = self.S12_发票税额 * 附加税费系数 
        self.F12_待纳附加税费额 = self.F10_增值附加税费 - self.F11_发票附加税费

        self.X10_现金流余额=self.销售收款额 - self.采购支出额 - self.费用支付额 - \
             self.S12_发票税额  - self.F11_发票附加税费 -self.C13_已收管理费


        self.L10_现有利润额= self.销售开票收入 - self.采购收票成本 - self.费用支付额  \
          -self.F11_发票附加税费 -self.C13_已收管理费 #L10_现有利润额
        
        self.L11_项目利润额= self.销售合同收入 - self.采购合同成本 - self.费用计划额 - \
             self.F10_增值附加税费 -self.C12_应收管理费
#############
        self.D01_销售合同额=self.销售合同额
        self.D02_销售开票额= self.销售开票额          
        self.D03_销售收款额=self.销售收款额  
        self.D04_销售合同收入=self.销售合同收入
        self.D05_销售开票收入=self.销售开票收入  

        self.B01_采购合同额=self.采购合同额 
        self.B02_采购收票额= self.采购收票额          
        self.B03_采购支出额=self.采购支出额  
        self.B04_采购合同成本=self.采购合同成本   
        self.B05_采购收票成本=self.采购收票成本  

        self.C01_费用计划额=self.费用计划额          
        self.C02_费用支付额=self.费用支付额
    def guiyi条件字段(self):
        self.A04_记账方=self.记账方 
        self.A02_关联销售合同名称=self.关联销售合同名称 
        self.A05_对方=self.对方
        try:
            self.A01_财务分类=self.财务分类 
        except:
            pass
class Basic财务数据():
    def transferData(self,caiwuBaseCls1Obj):
        self.D15_销售待开票 =caiwuBaseCls1Obj.get_D15_销售待开票()
        self.D16_销售应收款 = caiwuBaseCls1Obj.get_D16_销售应收款()
        self.D17_销售待收款 = caiwuBaseCls1Obj.get_D17_销售待收款()



        self.B11_采购待收票 = caiwuBaseCls1Obj.get_B11_采购待收票()
        self.B12_采购应付款 = caiwuBaseCls1Obj.get_B12_采购应付款()
        self.B13_采购待付款 = caiwuBaseCls1Obj.get_B13_采购待付款()

        self.C11_费用待支额 = caiwuBaseCls1Obj.get_C11_费用待支额() 

        self.C12_应收管理费 = caiwuBaseCls1Obj.get_C12_应收管理费()


        self.C13_已收管理费 = caiwuBaseCls1Obj.get_C13_已收管理费()
         


        self.S11_增值税额 =caiwuBaseCls1Obj.get_S11_增值税额()
        self.S12_发票税额 =caiwuBaseCls1Obj.get_S12_发票税额()
        self.S13_待纳增值税额 =caiwuBaseCls1Obj.get_S13_待纳增值税额()

        self.F10_增值附加税费 =caiwuBaseCls1Obj.get_F10_增值附加税费()                
        self.F11_发票附加税费 = caiwuBaseCls1Obj.get_F11_发票附加税费()
        self.F12_待纳附加税费额 = caiwuBaseCls1Obj.get_F12_待纳附加税费额() 

        self.X10_现金流余额= caiwuBaseCls1Obj.get_X10_现金流余额()
        self.L10_现有利润额= caiwuBaseCls1Obj.get_L10_现有利润额()
        self.L11_项目利润额= caiwuBaseCls1Obj.get_L11_项目利润额()
#############
        self.D01_销售合同额= caiwuBaseCls1Obj.get_D01_销售合同额()
        self.D02_销售开票额= caiwuBaseCls1Obj.get_D02_销售开票额()         
        self.D03_销售收款额= caiwuBaseCls1Obj.get_D03_销售收款额()
        self.D04_销售合同收入= caiwuBaseCls1Obj.get_D04_销售合同收入()
        self.D05_销售开票收入= caiwuBaseCls1Obj.get_D05_销售开票收入()  

        self.B01_采购合同额= caiwuBaseCls1Obj.get_B01_采购合同额()
        self.B02_采购收票额= caiwuBaseCls1Obj.get_B02_采购收票额()       
        self.B03_采购支出额= caiwuBaseCls1Obj.get_B03_采购支出额() 
        self.B04_采购合同成本= caiwuBaseCls1Obj.get_B04_采购合同成本()   
        self.B05_采购收票成本= caiwuBaseCls1Obj.get_B05_采购收票成本() 

        self.C01_费用计划额= caiwuBaseCls1Obj.get_C01_费用计划额()      
        self.C02_费用支付额= caiwuBaseCls1Obj.get_C02_费用支付额()        
    def __init__(self):
        self.销售合同额=0.0
        self.销售合同收入=0.0

        self.采购合同额=0.0  
        self.采购合同成本=0.0      

        self.销售开票额=0.0          
        self.销售开票收入=0.0  

        self.采购收票额=0.0          
        self.采购收票成本=0.0  

        self.销售收款额=0.0  

        self.采购支出额=0.0   

        self.费用计划额=0.0          
        self.费用支付额=0.0  
        self.D15_销售待开票 = 0
        self.D16_销售应收款 = 0
        self.D17_销售待收款 = 0



        self.B11_采购待收票 = 0
        self.B12_采购应付款 = 0
        self.B13_采购待付款 = 0

        self.C11_费用待支额 =0 

        self.C12_应收管理费 = 0.0 


        self.C13_已收管理费 = 0.0 
         


        self.S11_增值税额 = 0
        self.S12_发票税额 = 0
        self.S13_待纳增值税额 =0

        self.F10_增值附加税费 =0                 
        self.F11_发票附加税费 = 0
        self.F12_待纳附加税费额 =0

        self.X10_现金流余额=0
        self.L10_现有利润额= 0
        self.L11_项目利润额= 0
#############
        self.D01_销售合同额=0
        self.D02_销售开票额=0         
        self.D03_销售收款额=0
        self.D04_销售合同收入=0
        self.D05_销售开票收入=0  

        self.B01_采购合同额=0
        self.B02_采购收票额= 0       
        self.B03_采购支出额=0 
        self.B04_采购合同成本=0   
        self.B05_采购收票成本=0  

        self.C01_费用计划额=0       
        self.C02_费用支付额=0

    def cal(self):
        pass

    def guiyi条件字段(self):
        pass
