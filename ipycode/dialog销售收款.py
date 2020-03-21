#-*- coding: UTF8
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 

class 销售收款Dialog(dialogtest.Dialog_account):
    def body(self):
        width =0
        super(销售收款Dialog,self).body()
        return None # initial focus
   
    def getfileNameBase(self):
        return  self.getbaseFilename("xj","S")     
      
class 销售收款_EditDialog( 销售收款Dialog ):
    def init( self,OrgObj ):
        super(销售收款_EditDialog,self).init(OrgObj )

        return 
    def Gen_save2File(self):
        super(销售收款_EditDialog,self).Gen_save2File()
        self.OrgObj.税率 = 0.0        
        self.OrgObj.write2File()

        return


class 销售收款_NewDialog( 销售收款_EditDialog ):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj = 现金流收款Cls()
            self.OrgObj.序号 = getNewFileName("xj","s" )
            self.kongjian序号.set( self.OrgObj.序号) 
        return
