#-*- coding: UTF8
# import dialogtest
from __future__ import print_function
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from    dialogBase import *
import  dialogBase 

#############################################################################################
class 报销采购支出Dialog(dialogtest.Dialog_account):
    def body(self):
        super(报销采购支出Dialog,self).body()
        return None 

   
    def getfileNameBase(self):
        return  self.getbaseFilename("xj","b")  
      


class 报销采购支出_EditDialog( 报销采购支出Dialog  ):
    def init( self,OrgObj ):
        super(报销采购支出_EditDialog,self).init(OrgObj )
        return 
    def Gen_save2File(self):
        super(报销采购支出_EditDialog,self).Gen_save2File()
        self.OrgObj.税率 =0.0        
        self.OrgObj.write2File()
        return
                  
class 报销采购支出_NewDialog( 报销采购支出_EditDialog ):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj = 报销采购支出Cls()
            self.OrgObj.序号 = getNewFileName("xj","b" )
            self.kongjian序号.set( self.OrgObj.序号) 
        return
        pass        