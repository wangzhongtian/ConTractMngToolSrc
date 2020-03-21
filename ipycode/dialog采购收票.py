#-*- coding: UTF8
# import dialogtest
from __future__ import print_function
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 


class 采购收票Dialog(dialogtest.Dialog_account):
    def body(self):
        w1=0
        super(采购收票Dialog,self).body()
        self.add开票类型(w1,self.row); self.row = self.row+1 
        self.add税率(w1,self.row); self.row = self.row+1     
        # self.add费用分类(self.width,self.row); self.row = self.row+1  
        return None # initial focus
   
    def getfileNameBase(self):
        return  self.getbaseFilename("fp","js")      
    # def validate(self):
    #     return True        
class 采购收票_EditDialog( 采购收票Dialog):
    def init( self,OrgObj ):
        super(采购收票_EditDialog,self).init(OrgObj )

        self.kongjian开票类型.set( OrgObj.开票类型.strip()  )
        self.kongjian税率.set( get合同税率(OrgObj.税率  )   )    #.strip()       

        return 
    def Gen_save2File(self):
        # print("-------------Gen_save2File---- 1-------------------")
        super(采购收票_EditDialog,self).Gen_save2File()
        # print("-------------Gen_save2File-------- 2 Gen_save2File---")
        shuilv = self.kongjian税率.get().replace("%","*1.0").strip()
        self.OrgObj.税率 ="{:}".format(shuilv  )
 
        self.OrgObj.开票类型 =  "{:}".format( self.kongjian开票类型.get().strip())       
        # print("-------------Gen_save2File---------- 3-")
        self.OrgObj.write2File()

        return


class 采购收票_NewDialog( 采购收票_EditDialog):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =发票收Cls()
            self.OrgObj.序号 = getNewFileName("fp","js" )
            self.kongjian序号.set( self.OrgObj.序号) 
            print("==============================")
        return
        pass   

#############################
