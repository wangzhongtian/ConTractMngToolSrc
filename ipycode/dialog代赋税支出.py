#-*- coding: UTF8
# import dialogtest
from __future__ import print_function
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from    dialogBase import *
import  dialogBase 
#############################################################################################
class 代赋税支出Dialog(dialogtest.Dialog_account):
    def body(self):
        super(代赋税支出Dialog,self).body()
        return None # initial focus

   
    def getfileNameBase(self):
        return  self.getbaseFilename("xj","D")  

class 代赋税支出_EditDialog( 代赋税支出Dialog  ):
    def init( self,OrgObj ):
        super(代赋税支出_EditDialog,self).init(OrgObj )
        return 
    def Gen_save2File(self):
        super(代赋税支出_EditDialog,self).Gen_save2File()
        self.OrgObj.税率 =0.0        
        self.OrgObj.write2File()
        return
                  
class 代赋税支出_NewDialog( 代赋税支出_EditDialog ):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj = 代赋税支出Cls()
            self.OrgObj.序号 = getNewFileName("xj","d" )
            self.kongjian序号.set( self.OrgObj.序号) 
        return
