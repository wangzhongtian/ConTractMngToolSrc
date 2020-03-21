#-*- coding: UTF8
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 

class 采购支付Dialog(dialogtest.Dialog_account):
    def body(self):
        super(采购支付Dialog,self).body()
        # self.add费用分类(self.width,self.row); self.row = self.row+1  
        return None # initial focus
   
    def getfileNameBase(self):
        return  self.getbaseFilename("xj","F")    

    def validate(self):
        return True        
class 采购支付_EditDialog( 采购支付Dialog  ):
    def init( self,OrgObj ):
        super(采购支付_EditDialog,self).init(OrgObj )

        return 
    def Gen_save2File(self):
        # print("-------------Gen_save2File---- 1-------------------")
        super(采购支付_EditDialog,self).Gen_save2File()
        # print("-------------Gen_save2File-------- 2 Gen_save2File---------------")

        self.OrgObj.税率 = 0.0        
        # print("-------------Gen_save2File---------- 3-------------")
        self.OrgObj.write2File()

        return

class 采购支付_NewDialog( 采购支付_EditDialog):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =现金流支付Cls()
            self.OrgObj.序号 = getNewFileName("xj","f" )
            self.kongjian序号.set( self.OrgObj.序号) 
            print("==============================")
        return
        pass   
      