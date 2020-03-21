#-*- coding: UTF8
from __future__ import print_function
import dialogtest
# from tkinter import *
# import tkinter.ttk as ttk1
import  dialogBase 
from    dialogBase import *
# import  dialogBase 


      

class 销售合同Dialog(dialogtest.Dialog_account):
    def __init__(self, parent, title = None,OrgObj=None):

        super(销售合同Dialog,self).__init__(parent, title = title ,OrgObj=OrgObj)  
        
    def body(self):
        w=1000
        # print("Dial------------------og_Base") 
        super(销售合同Dialog,self).body()
        # print("Dial------------------og_Base") 
        self.add签署方式(w,self.row,fieldname="合同签署形式"); self.row= self.row+1
        # print("Dial------------------og_Base") 
        self.add开票类型(w,self.row); self.row = self.row+1 
        # print("Dial------------------og_Base")         
        self.add税率(w,self.row); self.row = self.row+1     
        # print("Dial------------------og_Base") 
        return None # initial focus
   
    def getfileNameBase(self):
        return  self.getbaseFilename("ht","x")  
    # def validate(self):
    #     return True        
class 销售合同_EditDialog( 销售合同Dialog):
    def init( self,OrgObj ):
        super(销售合同_EditDialog,self).init(OrgObj )
        self.kongjian开票类型.set( OrgObj.开票类型.strip()  )
        self.kongjian税率.set( get合同税率(OrgObj.税率)    )      #.strip()      
        # self.value费用分类.set( OrgObj.费用子类 ) 
        return 
    def Gen_save2File(self):
        print("-------------Gen_save2File---- 1-------------------")
        super(销售合同_EditDialog,self).Gen_save2File()

        print("-------------Gen_save2File-------- 2 Gen_save2File---------------")
        shuilv = self.kongjian税率.get().replace("%","*1.0").strip()
        self.OrgObj.税率 ="{:}".format(shuilv  )
        print( self.OrgObj.税率)
        self.OrgObj.签署方式 =   self.kongjian签署方式.get().strip()
        self.OrgObj.开票类型 =  "{:}".format( self.kongjian开票类型.get().strip() )       
        print("-------------Gen_save2File---------- 3-------------")
        self.OrgObj.write2File()

        return
class 销售合同_NewDialog( 销售合同_EditDialog):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =合同销售Cls()
            self.OrgObj.序号 = getNewFileName("ht","x" )
            self.kongjian序号.set( self.OrgObj.序号) 
            # print("==============================")
        return
        pass   