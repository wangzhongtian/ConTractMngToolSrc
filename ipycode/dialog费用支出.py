#-*- coding: UTF8
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 

class 费用支出Dialog(dialogtest.Dialog_account):
    def body(self):
        width =0
        super(费用支出Dialog,self).body()
        self.add费用分类(width,self.row); self.row = self.row+1  
        return None # initial focus
    # def Gen_save2File(self):
    #     return 
   
    def getfileNameBase(self):
        return  self.getbaseFilename("fy","f")  
        # return self.getbaseFilename("ht","fy")   
    # def validate(self):
    #     return True        


class 费用支出_EditDialog( 费用支出Dialog  ):
    def init( self,OrgObj ):
        super(费用支出_EditDialog,self).init(OrgObj )
        self.kongjian费用分类.set( OrgObj.费用子类.strip() ) 
        return 
    def Gen_save2File(self):
        # print("-------------Gen_save2File-----------------------")
        super(费用支出_EditDialog,self).Gen_save2File()
        # print("-------------Gen_save2File-----------------------")
        self.OrgObj.费用子类 =  self.kongjian费用分类.get().strip() 
        self.OrgObj.税率 =0.0        
        print("-------------Gen_save2File-----------------------")
        self.OrgObj.write2File()
        return
                  
class 费用支出_NewDialog( 费用支出_EditDialog ):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj = 现金流费用支付Cls()
            self.OrgObj.序号 = getNewFileName("fy","f" )
            self.kongjian序号.set( self.OrgObj.序号) 
            print("==============================")
        return
        pass           