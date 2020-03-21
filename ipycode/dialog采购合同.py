#-*- coding: UTF8
# import dialogtest
from __future__ import print_function
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
from    dialogBase import *
import  dialogBase 


class 采购合同Dialog(dialogtest.Dialog_account):
    def body(self):
        super(采购合同Dialog,self).body()
        w=0
        self.add签署方式(w,self.row,fieldname="合同签署形式"); self.row= self.row+1
        self.add开票类型(w,self.row); self.row = self.row+1 
        self.add税率(w,self.row); self.row = self.row+1     
        return None # initial focus
   
    def getfileNameBase(self):
        return  self.getbaseFilename("ht","c")    
    # def validate(self):
    #     return True        
class 采购合同_EditDialog( 采购合同Dialog):
    def init( self,OrgObj ):
        super(采购合同_EditDialog,self).init(OrgObj )

        self.kongjian开票类型.set( OrgObj.开票类型  )
        self.kongjian税率.set( get合同税率(OrgObj.税率  )   )           
        # self.value费用分类.set( OrgObj.费用子类 ) 
        return 
    def Gen_save2File(self):
        super(采购合同_EditDialog,self).Gen_save2File()
        shuilv = self.kongjian税率.get().replace("%","*1.0").strip()
        self.OrgObj.税率 ="{:}".format(shuilv  )
 
        self.OrgObj.开票类型 =  "{:}".format( self.kongjian开票类型.get())   
        self.OrgObj.签署方式 =   self.kongjian签署方式.get().strip() 
        # print("pppp采购合同_EditDialog")           
        self.OrgObj.write2File()
        return

class 采购合同_NewDialog( 采购合同_EditDialog):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =合同采购Cls()
            self.OrgObj.序号 = getNewFileName("ht","c" )
            self.kongjian序号.set( self.OrgObj.序号) 
        return
        pass   

