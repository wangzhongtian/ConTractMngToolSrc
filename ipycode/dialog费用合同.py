#-*- coding: UTF8
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 

class 费用合同Dialog(dialogtest.Dialog_account):
    def body(self):
        width =11
        super(费用合同Dialog,self).body()
        self.add签署方式(width,self.row,fieldname="合同签署形式"); self.row= self.row+1

        # self.kongjian签署方式.current(0)        
        self.add费用分类(width,self.row); self.row = self.row+1  
        return None # initial focus
    # def Gen_save2File(self):
    #     return 
   
    def getfileNameBase(self):
        return self.getbaseFilename("ht","fy")   
    # def validate(self):

    #     return True        

class 费用合同_EditDialog( 费用合同Dialog  ):
    def init( self,OrgObj ):
        super(费用合同_EditDialog,self).init(OrgObj )
        self.kongjian费用分类.set( OrgObj.费用子类.strip() ) 

        return 
 
    def Gen_save2File(self):
        # print("-------------Gen_save2File-----------------------")
        super(费用合同_EditDialog,self).Gen_save2File()
        # print("-------------Gen_save2File-----------------------")
        self.OrgObj.费用子类 =  self.kongjian费用分类.get().strip()
        self.OrgObj.税率 =0.0   
        self.OrgObj.签署方式 =   self.kongjian签署方式.get().strip()     
        # print("-------------Gen_save2File-----------------------")
        self.OrgObj.write2File()
        return
class 费用合同_NewDialog( 费用合同_EditDialog ):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =费用合同Cls()
            self.OrgObj.序号 = getNewFileName("ht","f" )
            self.kongjian序号.set( self.OrgObj.序号) 
            print("==============================")
        return
        pass 
         