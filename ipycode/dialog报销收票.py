#-*- coding: UTF8
from __future__ import print_function
import dialogtest
from  dialogBase import *
import  dialogBase 

class 报销收票Dialog(dialogtest.Dialog_account):
    def body(self):
        self.width =0
        super(报销收票Dialog,self).body()
        self.add开票类型(self.width,self.row); self.row = self.row+1 
        self.add税率(self.width,self.row); self.row = self.row+1     
        return None # initial focus
    def getfileNameBase(self):
        return  self.getbaseFilename("fp","bx")      
       
class 报销收票_EditDialog( 报销收票Dialog):
    def init( self,OrgObj ):
        super(报销收票_EditDialog,self).init(OrgObj )
        self.kongjian开票类型.set( OrgObj.开票类型.strip()  )
        self.kongjian税率.set( get合同税率(OrgObj.税率  )   )    #.strip()       

        return 
    def Gen_save2File(self):
        
        super(报销收票_EditDialog,self).Gen_save2File()
        # print("-------------Gen_save2File-------- 2 Gen_save2File---------------")
        shuilv = self.kongjian税率.get().replace("%","*1.0").strip()
        self.OrgObj.税率 ="{:}".format(shuilv  )
 
        self.OrgObj.开票类型 =  "{:}".format( self.kongjian开票类型.get().strip())       
        # print("-------------Gen_save2File---------- 3-------------")
        self.OrgObj.write2File()

        return


class 报销收票_NewDialog( 报销收票_EditDialog):
    def init( self,OrgObj ):
        if OrgObj == None:
            self.OrgObj =报销发票收Cls()
            self.OrgObj.序号 = getNewFileName("fp","bx" )
            self.kongjian序号.set( self.OrgObj.序号) 


