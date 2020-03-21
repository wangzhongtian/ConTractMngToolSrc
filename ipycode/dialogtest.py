#-*- coding: UTF8
from __future__ import print_function
import dialogBase
import os
import datetime
import random
from BasicWidgets import *
from basicLib import *
def mkdirs(pathname):
    dirname = os.path.dirname( pathname)
    #print( pathname,dirname)
    if not os.path.exists(dirname) :
        print( dirname," created!!!")
        os.makedirs( dirname )

class Dialog_Base(dialogBase.Dialog):
    def __init__(self, parent,title = None,OrgObj=None):
        self._Height =50        
        super(Dialog_Base,self).__init__(parent,title = title ,OrgObj=OrgObj)
    def add纸媒单据编号(self,row,fieldname="纸媒单据编号"):
        title=fieldname
        hight = self._Height
        posy =self.Posy+3 
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue = "无"
        self.kongjian纸媒单据编号= generalEntry(posx,posy,hight,width,title,curvlaue,name )
        self.kongjian纸媒单据编号.Parent = self
        self.Posy = self.kongjian纸媒单据编号.Bottom

    def add交易货名(self,row,fieldname="交易货名"):
        title=fieldname
        hight = self._Height

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue = "无"
        # print(values,"-----------------")
        self.kongjian交易货名= generalEntry(posx,posy,hight,width,title,curvlaue,name )
        self.kongjian交易货名.Parent = self
        self.Posy = self.kongjian交易货名.Bottom

    def add业务内容(self,row):
        fieldname="业务内容"
        title="业务内容"
        hight = self._Height

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue = "无"

        self.kongjian业务内容= generalEntry(posx,posy,hight,width,title,curvlaue,name )
        self.kongjian业务内容.Parent = self
        self.Posy = self.kongjian业务内容.Bottom
    def add记账方(self,width1,row):
        title="记账方"

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= "记账方"
        curvlaue=""
        values=("-",); 

        self.kongjian记账方= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian记账方.Parent = self  
        self.Posy = self.kongjian记账方.Bottom 
    def add备注(self,row):
        fieldname="备注"
        title="备注"
        hight = self._Height*3

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue = "无"

        self.kongjian备注= generalMultiLineEntry(posx,posy,hight,width,title,curvlaue,name )
        self.kongjian备注.Parent = self
        self.Posy = self.kongjian备注.Bottom        
    def add项目主类(self,width1,row):
        title="合同大类"

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= "合同大类"
        curvlaue=""
        values=dialogBase.合同大类; 

        self.kongjian合同大类= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian合同大类.Parent = self
        self.Posy = self.kongjian合同大类.Bottom

    def add费用分类(self,width1,row):
        title="费用分类"

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= "费用分类"
        curvlaue=""
        values=dialogBase.全局费用子类s

        self.kongjian费用分类= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian费用分类.Parent = self
        self.Posy = self.kongjian费用分类.Bottom
    def add签署方式(self,width1,row,fieldname="签署方式"):
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= dialogBase.合同签署方式;

        self.kongjian签署方式= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian签署方式.Parent = self
        self.Posy = self.kongjian签署方式.Bottom

    def add税率(self,width1,row,fieldname="税率"):
        title=fieldname
        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= dialogBase.合同税率;

        self.kongjian税率= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian税率.Parent = self
        self.Posy = self.kongjian税率.Bottom
    def add金额(self,row,fieldname = "金额"):
        title=fieldname
        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=0
        hight=self._Height

        self.kongjian金额=金额Entry(posx,posy,hight,width,title,curvlaue,name)
        self.kongjian金额.Parent = self
        self.Posy = self.kongjian金额.Bottom

    def add项目主类(self,width,row):
        fieldname= "合同大类"
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= dialogBase.合同大类;

        self.kongjian合同大类= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian合同大类.Parent = self
        self.Posy = self.kongjian合同大类.Bottom
    def add合同子类(self,width,row,fieldname="项目子类"):
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= dialogBase.合同大类;

        self.kongjian合同子类= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian合同子类.Parent = self
        self.Posy = self.kongjian合同子类.Bottom
    def add开票类型(self,width,row):
        fieldname= "开票类型"
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= dialogBase.合同票别;

        self.kongjian开票类型= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian开票类型.Parent = self
        self.Posy = self.kongjian开票类型.Bottom        
    def add签署日期(self,row,fieldname = "签署日期"):
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""

        self.kongjian签署日期 = 日期Entry(posx,posy,self._Height,width,title,curvlaue,name)
        self.kongjian签署日期.Parent = self
        self.Posy = self.kongjian签署日期.Bottom        
    def add状态(self,width,row):
        fieldname= "状态"
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= dialogBase.状态类别;

        self.kongjian状态= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian状态.Parent = self
        self.Posy = self.kongjian状态.Bottom

    def add财务分类(self,width,row,财务类型):
        fieldname= "财务分类"
        title=fieldname

        posy =self.Posy+3          
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=财务类型
        values= self.财务分类s;

        self.kongjian财务分类= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian财务分类.Parent = self
        self.Posy = self.kongjian财务分类.Bottom

    def add序号(self,row):
        fieldname= "序号"        
        title=fieldname
        hight = self._Height

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue = "无"

        self.kongjian序号= generalEntry(posx,posy,hight,width,title,curvlaue,name )
        self.kongjian序号.Parent = self
        self.Posy = self.kongjian序号.Bottom

    def add关联销售合同名称(self,row,width1,fieldname="关联销售合同名称"):
        title="关联销售合同"
        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= (" ",);
        self.kongjian关联销售合同名称= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian关联销售合同名称.Parent = self
        self.Posy = self.kongjian关联销售合同名称.Bottom


    def add对方(self,width1,row):
        fieldname= "对方"
        title=fieldname

        posy =self.Posy+3         
        posx = 0  
        width=self.width1
        name= fieldname
        curvlaue=""
        values= (" ",);

        self.kongjian对方= SelectEditEntry(posx,posy,self._Height,width,title,curvlaue,values,name,colname1 =name )
        self.kongjian对方.Parent = self
        self.Posy = self.kongjian对方.Bottom

    def 费用记账方变化(self,*args):
        pass
        return True

    def validateAll(self):
        pass
    def 采购记账方变化(self,*args):
        return True
    
    def 项目主类变化(self,*args):
        return True
 
    def body(self):
        return###################
    def apply(self):
        idx =0
        try:
            self.fileData=""
            self.Gen_save2File(); idx+=1
            MessageBox.Show ('保存文件成功', '提示', MessageBoxButtons.OK);
        except:
            print(" 保存到文件失败,idx=:",idx)
            MessageBox.Show ('保存文件失败', '错误', MessageBoxButtons.OK);
            pass


    def Gen_save2File(self):
       pass

       
    def Save2File(self,filename):
        try :
            if filename ==None:
                return 
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

class Dialog_accountBase(Dialog_Base):
    pass

 
class Dialog_account(Dialog_Base):
    def body(self):
        self.row=0
        self.add序号(self.row)
        self.row=self.row+1        
        # row =self.row
        w=1000
        self.add状态(w,self.row); self.row= self.row+1

        self.记账方s = dialogBase.全局记账方s;   # 设置下拉列表的值
        self.add记账方(w,self.row);self.row= self.row+1

        # self.对方s= dialogBase.费用合同对方zd;
        self.add对方(w,self.row); self.row= self.row+1 


        self.add金额(self.row,fieldname="总金额"); self.row= self.row+1
 
        self.add签署日期(self.row,fieldname = "发生日期") ; self.row= self.row+1
        self.add纸媒单据编号(self.row); self.row= self.row+1  
        self.add交易货名(self.row,fieldname="明细说明"); self.row= self.row+1  
        self.add业务内容(self.row); self.row= self.row+1 
        self.add备注(self.row); self.row= self.row+6  
        self.add关联销售合同名称(self.row,w)  ; self.row= self.row+1  
        # self.项目主类变化("init")    
        # 
        # self.Posy =   self.row *self._Height+10
        return None # initial focus
    def getfileNameBase(self):
        return  
    def getFilename(self):
        # print("=======================")
        filename1 = self.getfileNameBase()         
        rootfolder=glbcfg.Py1fileRootFolder
        # print("--------------------------")
        状态=self.kongjian状态.get()
        # print(状态)
        财务名称=self.kongjian财务分类.get()
        # print("rewewerer")
        return os.path.join( rootfolder,状态,财务名称,filename1)          

    def validate(self):
        keys = self.__dict__.keys() 
        IDS ="kongjian"
        ll = len(IDS)
        for k in keys:
            if IDS ==  k[0:ll]:
                cmdexpression = "self."+k+".validateText()"
                try:
                    a= eval( cmdexpression )
                    if a == False :
                        return False
                    # print("_",k,cmdexpression)
                except:
                    print( "Validate Exception !!!")
        return True

    def init( self,OrgObj ):
        self.OrgObj = OrgObj
        self.kongjian状态.set( OrgObj.状态.strip()  )
        self.kongjian记账方.set(  OrgObj.记账方.strip()  )
        self.kongjian对方.set( OrgObj.对方.strip()  )  
        try:
            self.kongjian纸媒单据编号.set( OrgObj.纸媒单据编号.strip()  )
        except:
            pass

        if "签署方式" in OrgObj.__dict__.keys():
            self.kongjian签署方式.set(OrgObj.签署方式.strip()  )
        else:
            pass
        try:
            self.kongjian交易货名.set( OrgObj.交易货名.strip()  )
        except:
            pass
        # print(OrgObj.发票总金额 )

        self.kongjian金额.set( self.OrgObj.金额fn.strip() )
             #     pass
        # print( self.kongjian签署日期.get())
        self.kongjian签署日期.set(OrgObj.发生日期.strip()  )        

        self.kongjian业务内容.set( OrgObj.业务内容.strip()  )
        self.kongjian备注.set( OrgObj.备注  )
    
        self.kongjian序号.set( OrgObj.序号.strip()) 
        # print( "--------------",OrgObj.关联销售合同名称 ) 
        self.kongjian关联销售合同名称.set( OrgObj.关联销售合同名称.strip() ) #######################
        pass   

    def Gen_save2File(self):
        # print("----------SUB -1--Gen_save2File-----------------------")
        self.OrgObj.序号 = self.kongjian序号.get().strip() 
        self.OrgObj.状态 = self.kongjian状态.get().strip() 
        self.OrgObj.对方 =  self.kongjian对方.get().strip() 
        self.OrgObj.记账方 = self.kongjian记账方.get().strip() 
        # print("----------SUB -2--Gen_save2File-----------------------")
        self.OrgObj.纸媒单据编号 = self.kongjian纸媒单据编号.get().strip()
        # print("----------SUB -2--Gen_save2File-----------------------")
        self.OrgObj.交易货名 ="{:}".format( self.kongjian交易货名.get().strip())
        # print("----------SUB -2--Gen_save2File-----------------------")
        self.OrgObj.业务内容 = "{:}".format( self.kongjian业务内容.get().strip() )      
        # print("----------SUB -2--Gen_save2File-----------------------")        
        self.OrgObj.备注 =  self.kongjian备注.get()  
        # print("----------SUB --3-Gen_save2File-----------------------")
        self.OrgObj.发生日期 = "{:}".format( self.kongjian签署日期.get().strip())

        print("----------SUB 4---Gen_save2File-----------------------")        
        self.OrgObj.金额fn  =  self.kongjian金额.get().strip()
        a=eval(re.sub("[^0-9.*+-/]","",self.OrgObj.金额fn.replace("%","/100")) )
        # self.fileData += "import re \r\n发票总金额 = '''{:}'''\n".format( 发票总金额 )
        self.OrgObj.金额 =  a 

        print("----------SUB -7 --Gen_save2File-----------------------")          
        self.OrgObj.关联销售合同名称 = self.kongjian关联销售合同名称.get().strip()
        # print("----------SUB 8---Gen_save2File-----------------------",self.OrgObj.关联销售合同名称,";;;" ) 
        self.OrgObj.合同大类,unitname , self.OrgObj.合同子类 = self.OrgObj.关联销售合同名称.split("-")  
        print("----------SUB --9-Gen_save2File-----------------------")  
