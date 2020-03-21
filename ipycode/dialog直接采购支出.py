#-*- coding: UTF8
# import dialogtest
from __future__ import print_function
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from    dialogBase import *
import  dialogBase 

#############################################################################################
class 直接采购支出Dialog(dialogtest.Dialog_account):
    def body(self):
        super(直接采购支出Dialog,self).body()
        return None # initial focus

   
    def getfileNameBase(self):
        return  self.getbaseFilename("xj","z")  

class 直接采购支出_EditDialog( 直接采购支出Dialog  ):
    def init( self,OrgObj ):
        super(直接采购支出_EditDialog,self).init(OrgObj )
        # self.value费用分类.set( OrgObj.费用子类.strip() ) 
        return 
    def Gen_save2File(self):
        super(直接采购支出_EditDialog,self).Gen_save2File()
        self.OrgObj.税率 =0.0        
        self.OrgObj.write2File()
        return
                  
class 直接采购支出_NewDialog( 直接采购支出_EditDialog ):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj = 直接采购支出Cls()
            self.OrgObj.序号 = getNewFileName("xj","z" )
            self.kongjian序号.set( self.OrgObj.序号) 
            # print("==============================")
        return
        pass        