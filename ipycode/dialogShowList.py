#-*- coding: UTF8
from __future__ import print_function
import dialogBase
# from tkinter import *
# import tkinter.ttk as ttk1
import os
import datetime
import random
from basicLib import *
# import tkmessagebox 
from BasicWidgets import *
def mkdirs(pathname):
    dirname = os.path.dirname( pathname)
    #print( pathname,dirname)
    if not os.path.exists(dirname) :
        print( dirname," created!!!")
        os.makedirs( dirname )
class Dialog_ShowList(dialogBase.DialogMain):
    def add签署日期(self,row,width1,fieldname = "签署日期"):
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=width1
        name= fieldname
        curvlaue=""

        self.ctrl签署日期 = 日期Entry(posx,posy,self._Height,width,title,curvlaue,name)
        self.ctrl签署日期.Parent = self
        self.Posy = self.ctrl签署日期.Bottom 
         
        return  self.ctrl签署日期    
    def add关联销售合同名称(self,row,width1,fieldname="关联销售合同名称"):
        title="关联销售合同"
        posy= self.Posy
        posx = 0  
        width=width1
        name=  fieldname #"关联销售合同名称"
        curvlaue=""
        values=("",)
        # print(values,"-----------------")
        self.ctrl关联销售合同名称= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.ctrl关联销售合同名称.Parent = self
        self.Posy =self.ctrl关联销售合同名称.Bottom +3

    def add项目主类(self,width1,row):

        title="合同大类:"
        posy= self.Posy 
        posx = 0  
        width=width1
        name= "合同大类"
        curvlaue="所有"
        values=("所有","主合同和增项",) +dialogBase.合同大类; #("增补合同", "增项","主合同")  
        self.ctrl项目主类=SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 = name )
        # self.ctrl项目主类.Notify  = self.项目主类变化 ########
        self.ctrl项目主类.Parent = self
        self.Posy =self.ctrl项目主类.Bottom +3

    def add签署方式(self,width1,row,fieldname="签署方式"):

        title="签署方式:"
        posy= self.Posy
        posx = 0  
        width=width1
        name= "签署方式"
        curvlaue="所有"
        values=("所有",) +dialogBase.合同签署方式 #("增补合同", "增项","主合同")  
        self.ctrl签署方式=SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 = name )
        # self.ctrl签署方式.Notify  = self.项目主类变化 ########        
        self.ctrl签署方式.Parent = self   
        self.Posy =self.ctrl签署方式.Bottom +3
    def add合同子类(self,width1,row,fieldname="项目子类"):
        title="合同子类:"
        posy= self.Posy
        posx = 0  
        width=width1
        name= "项目子类"
        curvlaue="所有"
        values= ("所有",) +("二期维保", "一期维保","三期维保") 
        self.ctrl合同子类=SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 = name )
        self.ctrl合同子类.Parent = self
        self.Posy =self.ctrl合同子类.Bottom +3
    def add财务分类(self,width1,row,财务类型):

        title="财务分类:"
        posy= self.Posy
        posx = 0  
        width=width1
        name= "财务分类"
        curvlaue=财务类型
        values=("所有",) + self.财务分类s 
        # for i in values :
        #      print(  i,"/////////////////"  )
        self.ctrl财务分类=SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 = name )
        self.ctrl财务分类.Notify = self.记账方变化  
        # self.ctrl财务分类.cb.Enabled =False
        self.ctrl财务分类.Parent = self
        self.Posy =self.ctrl财务分类.Bottom +3

    def add对方(self,width1,row):

        title="对方:"
        # posx = row*self._Height 
        posy= self.Posy
        posx = 0  
        width=width1
        name= "对方"
        curvlaue="所有"
        values=("所有",) 
        self.ctrl对方=SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 = name )
        self.ctrl对方.Parent = self
        self.Posy =self.ctrl对方.Bottom +3


    def add记账方(self,width1,row):

        title="记账方:"
        posy= self.Posy
        posx = 0  
        width=width1
        name= "记账方"
        curvlaue="所有"
        values=("所有",) 
        self.ctrl记账方=SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 = name )
        self.ctrl记账方.Parent = self
        self.Posy =self.ctrl记账方.Bottom +3
##################################

    def 费用记账方变化(self,*args):
        return True
 


    def validateAll(self):
        pass

    def 记账方变化(self,*args):
        return True
 
    def 项目主类变化(self,*args):
        return

        
        a = self.ctrl合同大类.get()
        if a == "增补合同":
            rng = ("所有",) +dialogBase.增补合同子类s
            self.ctrl合同子类.cb.Items.AddRange(rng)
        elif a == "增项":
            rng = ("所有",) +dialogBase.主合同增项子类s
            self.ctrl合同子类.cb.Items.AddRange(rng)
        elif a == "主合同":
            rng = ("所有",) +dialogBase.主合同子类s
            self.ctrl合同子类.cb.Items.AddRange(rng)
        elif a == "所有":
            rng = ("所有",) +dialogBase.主合同子类s +\
                dialogBase.主合同增项子类s  +\
                dialogBase.增补合同子类s
            self.ctrl合同子类.cb.Items.AddRange(rng)

        self.ctrl合同子类.SelectedIndex = 0
        return True

    def body(self):
        return###################
    def apply(self):
        try:
            self.fileData=""
            self.Gen_save2File();

            filename = self.getFilename() 
            print(filename)           
            self.Save2File(filename);
        except:
            print(" 保存到文件失败\r\n")
            pass
    def Gen_save2File(self):
       pass

       
    def Save2File(self,filename):
        try :
            mkdirs( filename )
            fo = openfile(filename,"wt",encoding="UTF8")
            print(self.fileData,file=fo)
            fo.close()
        except:
            print("save to file Error")
            pass
    def getFilename(self):
        return None

    def getbaseFilename(self,prefix,direction):
        today1 = datetime.date.today()
        rndID =random.randint(1,999999)
        # print("ppppppppppppppp")
        filename= "{}-{:04d}{:02d}{:02d}-{}{:06d}.{}".format(prefix,today1.year,today1.month,today1.day,direction,rndID,"py1")
        return filename

