# import dialogtest
from __future__ import print_function
from tkinter import *
import tkinter.ttk as ttk1
from  dialogBase import *
import dialogBase
import  dialogShowList
import dialog销售合同
import dialog销售开票
import dialog销售收款

import  dialog采购合同
import  dialog采购支付
import  dialog采购收票

import  dialog费用合同
import  dialog费用支出

import os

import  账务处理Lib

##############################################################################
class 供应商统计Dialog(dialogShowList.Dialog_ShowList):
    def body(self):
        self.root= master
        row =0
        width=80

        self.财务分类s  =dialogBase.全局财务分类s; # ("销售合同",)  #
        self.add财务分类(width,row,"销售合同"); row= row+1 #"销售合同"

        self.记账方s = dialogBase.全局记账方s;   # 设置下拉列表的值
        self.add记账方(width,row); row= row+1

        # self.对方s= dialogBase.中电销售合同对方s;
        self.add对方(width,row); row= row+1  
        
        self.add项目主类(width,row); row= row+1

        self.add合同子类(width,row); row= row+1     
        # body0.grid( row=0)

        # self.项目主类变化("初始关联")
        # self.记账方变化("初始关联")
        
        return None # initial focus
    def bodyShowTree(self,body2):
        self.tree = ttk.Treeview(body2,show="headings", columns=('col1','col2','col3','col4','col5','col6','col7','col8'))
        self.tree.column('col1', width=100, anchor='center')
        self.tree.column('col2', width=100, anchor='center')
        self.tree.column('col3', width=100, anchor='center')
        self.tree.column('col4', width=100, anchor='center')
        self.tree.column('col5', width=100, anchor='center')
        self.tree.column('col6', width=100, anchor='center')
        self.tree.column('col7', width=100, anchor='center')        
        self.tree.column('col8', width=100, anchor='center')    
        self.tree.heading('col1', text='合同大类')
        self.tree.heading('col2', text='合同子类')
        self.tree.heading('col3', text='记帐方')               
        self.tree.heading('col4', text='对方')
        self.tree.heading('col5', text='日期')
        self.tree.heading('col6', text='财务分类')
        self.tree.heading('col7', text='金额')
        self.tree.heading('col8', text='ID') 

        self.tree.bind("<Double-1>", self.onDBClick)
        self.tree.pack(ipady=130)

    def cond(self,dataObj):
        cond =True
        if( self.记账方 != None):
            cond = cond and dataObj.记账方   ==  self.记账方 
        if( self.对方 != None):
            cond = cond and dataObj.对方  == self.对方
        if( self.合同大类 != None):
            cond = cond and dataObj.合同大类  == self.合同大类
        if( self.合同子类 != None):
            cond = cond and dataObj.合同子类  == self.合同子类
        if(self.财务分类 != None):
            cond = cond and isinstance(  dataObj, self.财务分类  )
        return cond               
    def getConditions(self):
        self.记账方 ="" 
        self.对方 =""
        self.合同大类 =""
        self.合同子类 =""
        self.财务分类 =""
        try:
            self.记账方 = self.value记账方.get().strip()
            # self.记账方 = eval("记账单位Cls."+ self.value记账方.get() )

        except:
            pass

        try:
            self.对方 = self.value对方.get().strip()
            # self.对方 = eval("对方单位Cls."+ self.value对方.get())
        except:
            pass

        # try:
        #     self.合同大类= eval("合同主类Cls."+ self.value合同大类.get() )
        # except:
        #     pass 

        # try:
        #     self.合同子类= eval("合同子类Cls."+ self.value合同子类.get())
        # except:
        #     pass

        try:
            self.财务分类 =  self.value财务分类.get() 
        except:
            pass   

    def ok(self, event=None):  # 更新系统数据库，并刷新显示搜索数据到tree grid

        self.getConditions()
        # Clear datas in tree grid
        for item in self.tree.get_children():
            self.tree.delete( item )

        dataObjArrary = 账务处理Lib.getdataDic()
        # self.dataDic  = dataObjArrary
        self.dataDic  = 账务处理Lib.数据统计CLs.condsatisify(dataObjArrary,self.财务分类,self.记账方,self.对方,self.合同大类,self.合同子类)        
        # dicLen = len( self.dataDic )
        cnt =0       
        for v in self.dataDic :
                对方 = 对方单位Cls.mapping[v.对方] 
                a= 对方.split(".")
                jine = "{:0.2f}".format( v.get金额()  )
                values= ( v.合同大类,v.合同子类,v.记账方,a[1] ,v.get日期(),v.get财务类型() , jine,v.序号+"?"+str(cnt) )
                self.tree.insert('',cnt,values= values)
                cnt=cnt+1 



    def onDBClick(self,event):
        item  = self.tree.selection()[0]
        fname = self.tree.set(item, column='col8')  

        print( fname )
        diaolgtype=fname[:2].upper()
        fangxiang = fname[ 12:13].upper()
        a,idx = fname.split("?")
        idx1 = int(idx)

        # self.dataDic = 账务处理Lib.getdataDic()
        print( len( self.dataDic))
        currentObj =self.dataDic[idx1]
 
        if diaolgtype == "HT"  and fangxiang == "C" :
            currentObj =self.find符实Obj( a )
            print( "合同",diaolgtype, fangxiang,idx )
            dialog采购合同.采购合同_EditDialog(self.root,"采购合同",  OrgObj =currentObj )
            return
        if diaolgtype == "HT"  and fangxiang == "X" :
            currentObj =self.find符实Obj( a )
            print( "合同",diaolgtype, fangxiang,idx )
            dialog销售合同.销售合同_EditDialog(self.root,"销售合同",  OrgObj =currentObj )
            return           

        if diaolgtype == "XJ"  and fangxiang == "S" :
            currentObj =self.find符实Obj( a )
            dialog销售收款.销售收款_EditDialog(self.root,"销售收款",  OrgObj =currentObj )
            print( "现金流",diaolgtype, fangxiang,idx )
            return            
        if diaolgtype == "XJ"  and fangxiang == "F" :
            currentObj =self.find符实Obj( a )
            dialog采购支付.采购支付_EditDialog(self.root,"采购支付",  OrgObj =currentObj )
            print( "现金流",diaolgtype, fangxiang,idx )
            return  

        if diaolgtype == "HT"  and fangxiang == "F" :
            dialog费用合同.费用合同_EditDialog(self.root,"费用合同",  OrgObj =currentObj )
            print( "费用合同",diaolgtype, fangxiang,idx ) 
            return   

        if diaolgtype == "FY"  and fangxiang == "F" :
            print( "feiyong zhichu ",diaolgtype, fangxiang,idx )
            dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return  

        if diaolgtype == "FP"  and fangxiang == "J" :
            print( "发票收到 ",diaolgtype, fangxiang,idx )
            dialog采购收票.采购收票_EditDialog(self.root,"采购收票",  OrgObj =currentObj )
            # dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return  

        if diaolgtype == "FP"  and fangxiang == "K" :
            print( "销售开票 ",diaolgtype, fangxiang,idx )
            dialog销售开票.销售开票_EditDialog(self.root,"销售开票",  OrgObj =currentObj )
            # dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return  

    def find符实Obj(self, filename):
        for v in self.dataDic :
            if v.序号 == filename:
                if v.is名附实( ):
                    return v

    def 计算项目数据(self, event=None):
        import dialog显示项目数据
        d = dialog显示项目数据.显示项目数据Dialog(self.root,"显示项目财务数据")
        return

    def 计算筛选数据(self):
        print(" 计算筛选数据 ,显示筛选结果")
        # print("--------------")
        import dialog显示筛选统计数据
        self.getConditions()
        dataObjArrary = 账务处理Lib.getdataDic()
        财务分类=""
        dataObj = 账务处理Lib.数据统计CLs.get财务数据( dataObjArrary ,财务分类,self.记账方,self.对方,self.合同大类,self.合同子类 )

        if self.记账方 =="":
            dataObj.记账方= "所有"
        else:
            dataObj.记账方= 记账单位Cls.get友好名(self.记账方)  

        if self.对方 =="":
            dataObj.对方= "所有"
        else:
            dataObj.对方= 对方单位Cls.get友好名(self.对方)


        if self.合同大类 =="":
            dataObj.合同大类= "所有"
        else:
            dataObj.合同大类= 合同主类Cls.get友好名(self.合同大类) 
        
        if self.合同子类 =="":
            dataObj.合同子类= "所有"
        else:
            dataObj.合同子类= 合同子类Cls.get友好名(self.合同子类) 
        

        dataObj.财务分类= "所有"
         
        # dataObj.cal()
        # print("-------------",dataObj.财务分类)
        d = dialog显示筛选统计数据.显示筛选统计数据Dialog(self.root, "显示筛选的财务数据",dataOBJ = dataObj)
        pass
