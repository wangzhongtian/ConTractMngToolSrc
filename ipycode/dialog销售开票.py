#-*- coding: UTF8
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 



class 销售开票Dialog(dialogtest.Dialog_account):
    def body(self):
        width =0
        super(销售开票Dialog,self).body()
        self.add开票类型(width,self.row); self.row = self.row+1 
        self.add税率(width,self.row); self.row = self.row+1     
        # self.add费用分类(self.width,self.row); self.row = self.row+1  
        return None # initial focus
   
    def getfileNameBase(self):
        return  self.getbaseFilename("fp","kj")      
    # def validate(self):
    #     return True        
class 销售开票_EditDialog( 销售开票Dialog):
    def init( self,OrgObj ):
        super(销售开票_EditDialog,self).init(OrgObj )

        self.kongjian开票类型.set( OrgObj.开票类型.strip()  )
        self.kongjian税率.set( get合同税率(OrgObj.税率  )   )           

        return 
    def Gen_save2File(self):
        # print("-------------Gen_save2File---- 1-------------------")
        super(销售开票_EditDialog,self).Gen_save2File()
        # print("-------------Gen_save2File-------- 2 Gen_save2File---------------")
        shuilv = self.kongjian税率.get().replace("%","*1.0").strip()
        self.OrgObj.税率 ="{:}".format(shuilv  )
 
        self.OrgObj.开票类型 =  "{:}".format( self.kongjian开票类型.get().strip())       
        # print("-------------Gen_save2File---------- 3-------------")
        self.OrgObj.write2File()

        return




class 销售开票_NewDialog( 销售开票_EditDialog):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =发票开Cls()
            self.OrgObj.序号 = getNewFileName("fp","kj" )
            self.kongjian序号.set( self.OrgObj.序号) 
            print("==============================")
        return
        pass                   