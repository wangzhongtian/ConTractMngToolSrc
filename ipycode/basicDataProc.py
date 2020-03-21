#-*- coding: UTF-8
from __future__ import print_function
import copy
import os
from  名称定义 import *
import imp
import basicLib
from  xlsProLib import *
import glbcfg
import basicLib  
import swaplib    
from  财务统计计算 import *
from  caiwuBasic统计 import *
doSwap= True ;

isDirty = True #global
datasObj = None #global
dataDic = [] #global   

titles= '''#-*- coding: UTF-8
##############################################################################
#print( len( gloProc.container ));
#gloProc.push(aobj);
# from 账务处理Lib import *
# from 名称定义 import *
# 万元=10000.0
# import re


from 账务处理Lib import *
from 名称定义 import *
万元=10000.0
import re
# def update():
gloProc = hcXlsProc (); 
'''
import shutil 
def savePickle(dbname=glbcfg.Py1fileRootFolder+"/Gened/pickleDB"):
    return
    print("Start, Save to Pickle:",dbname )
    global datasObj
    global dataDic
    import pickle
    print("write to pickle DB")
    with basicLib.openfile( dbname ,"wb") as fileobj:
        print( fileobj ,"write ....")
        pickle.dump(dataDic, fileobj, pickle.HIGHEST_PROTOCOL)
    print("End, Save to Pickle:",dbname )
def readpickle(dbname= glbcfg.Py1fileRootFolder+"/Gened/pickleDB"):
    return 
    data1=[]
    import pickle
    with basicLib.openfile(dbname, 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        data1 = pickle.load(f)
    print( "data count in pickle >..",len(data1 ))
def Save2DataDB( filename =glbcfg.Py1fileRootFolder+"/Gened/datadb.py"):
    global dataDic
    pass
    print(" Save2DataDB  ")  
    tempfile=glbcfg.Py1fileRootFolder+"Gened/oooooooooo.py"  
    try:
        with basicLib.openfile( tempfile ,"wt",encoding="UTF8") as fileobj:
            print( titles,file= fileobj)
            for dataobj in dataDic:
                if  dataobj.is名附实():
                    str1 = dataobj.getbasicdataStr()
                    # print(str1 ,"++++++++++++++++++++++++tempfile++++++++++++++--------1--------",tempfile ,dataobj.__class__.__name__)
                    print( str1, file= fileobj)   
                    # print(str1 ,"++++++++++++++++++++++++tempfile++++++++++++++--------1.1--------")                             
                    str1 = dataobj.toStr() 
                    # print(str1 ,"++++++++++++++++++++++++++++++++++++++--------2--------")
                    print( str1, file= fileobj)
                    str1 ="gloProc.push( aObj);"+ "\n"
                    # print(str1 ,"++++++++++++++++++++++++++++++++++++++--------3--------")
                    print( str1, file= fileobj)

                # print(dataobj.__class__.__name__,"++++++++++++++++++++++++++++++++++++++OK?? 4")
                # return 
    except:
        pass
        print("Save db file Error",tempfile)
        return 
    finally:
        pass
        # fileobj.close()
    try:
        if os.path.exists( filename):
            os.remove( filename )
        os.rename( tempfile,filename )
    except:
        print("Error happened")   
    savePickle()         
def supermkdirs(pathname):
    # print( pathname)
    dirname = os.path.dirname( pathname)
    # print( "_mkdirs:----",pathname,dirname)
    if not os.path.exists(dirname) :
        print( dirname," created!!!")
        os.makedirs( dirname )
def DateStrReg( strdate):
    strdate = strdate.replace("-",".")
    strdate = strdate.replace("_",".")
    strdate = strdate.replace("/",".")
    strdate = strdate.replace("年",".")
    strdate = strdate.replace("月",".")
    strdate = strdate.replace("日","")

    a = strdate.split(".")
    if (len(a) == 3 ):
        strdate1 ="{:0>4}.{:0>2}.{:0>2}".format(a[0],a[1],a[2])
        return strdate1
    else:
        return "1969.11.16"


class AccountBaseCls(caiwuBaseCls1):
    keystrs ="""
序号 
关联销售合同名称 
记账方 
对方 
合同大类 
合同子类 

发票含税总额
交易总金额
发票总金额
金额 
税率

交易日期
发票日期
签署日期

状态

业务内容 
纸媒单据编号 
发票单据编号
交易货名
费用分类 
开票类型

签署方式
备注 
        """


    displaykeystrs ="""
序号 
关联销售合同名称
记账方 
对方 
合同大类 
合同子类 

状态
费用子类 

业务内容 
纸媒单据编号 
发票单据编号
交易货名

开票类型
税率
签署方式
备注 
        """        
    paichuFields="""
        发票含税总额
交易总金额
发票总金额
金额 
税率

交易日期
发票日期
签署日期
        """
    keys = keystrs.split()
    displaykeys  = displaykeystrs.split()
    def __init__( self,obj=None):
        if obj ==None:
            return ;
        for k,v in obj.__dict__.items():
            self.__dict__[ k ] =v 
    def writeOut(self,tgrObj):
        pass
    def swap(self ): 
        #      if swaplib.needSwap( self.记账方 ,self.对方): 
        return None
    def get归一金额(self,数据类型="原始数据") : # 原始数据  财务收益分析
        return 0
    def cal(self):
        # print(str(self.金额 ),"  ;;;;")
        self.金额 = eval( str(self.金额 ) )
        self.归一金额 = self.getguiyixishu()*self.金额/10000.0;  
    def getguiyixishu(self):
        return 1.0       
    def get发生日期(self):
        fdict =self.__dict__
        return fdict["发生日期" ] #交易日期

    def get日期(self):
        return "2050.12.31"  
    def get财务类型(self):
        return ""    
    def get金额(self):
        return self.金额  
    def write2File(self):
        pass
    # def getBasic财务数据(aobj):
    #     return (0,)
    def getFNstr(self):
        return  None

    def Save2Filepy1(self,str1):
        global isDirty
        try :
            fullname = self.folder
        except:
            self.folder =""
            fullname = os.path.join( glbcfg.Py1fileRootFolder,"新增datas",self.状态,self.getFNstr(), self.序号)
        print("::",fullname,"--",self.folder)
        # fullname = self.folder
        supermkdirs(fullname)
        with basicLib.openfile( fullname,"wt",encoding="UTF8") as fo:            
            print( str1,file= fo )
        pass         
        isDirty = True  
        print(" Save to file ok:", fullname)
        self.Save2MemDict()
        print(" Save to Mem Dicr ok:")
        isDirty = False 
        Save2DataDB()
    def getFieldStrRe(self,FieldName):
        # fieldname = "签署方式"
        # print(FieldName)
        try:
            if  FieldName in  self.__dict__.keys():
                v0 = self.__dict__[FieldName]
                v1=str( v0 )
                str1  ="aObj.{:} =  '''{:}'''".format(FieldName,v1.strip() ) +"\n" 
                # print(str1)
                return str1
            else:
                return ""
        except:
            print("ERORR.. in getFieldStrRe()..")
    def toStrBase(self):
        str1= ""
        # print("----------0.0------------")
        try:
            str1 +="aObj.关联销售合同名称 =  '''{:}'''".format( self.__dict__["关联销售合同名称"].strip() )+"\n"
            # print("----------0.011------------")
        except:
            # print("----------0.01------------")
            print("except in 关联销售合同名称,in FY基本合同Cls" ,self.__dict__["序号"].strip() )
        # print("----------0.02------------")
        str1 +="aObj.记账方 = '''{:}''' ".format(  self.__dict__["记账方"].strip()  )+"\n"
        str1 +="aObj.对方 =  '''{:}''' ".format(  self.__dict__["对方"].strip() ) + "\n"  
        try:
            str1 +="aObj.纸媒单据编号 = '''{:}'''".format(self.__dict__["纸媒单据编号"].strip() )+"\n"
        except:
            str1 +="aObj.纸媒单据编号 = '''{:}'''".format("无")+"\n"
        # print("----------0.1------------")

        str1 +="aObj.备注 = '''{:}'''".format(self.__dict__["备注"].strip()   ) +"\n"

        str1 +="aObj.交易货名 = '''{:}'''".format(self.__dict__["交易货名"].strip() )+"\n"

        str1 +="aObj.业务内容 =  '''{:}'''".format( self.__dict__["业务内容"].strip() )+"\n"

        # print("----------1-----------")
        fieldname = "签署方式";str1 += self.getFieldStrRe(fieldname ) 

        fieldname = "发生日期";str1 += self.getFieldStrRe(fieldname )
        # fieldname = "发票日期";str1 += self.getFieldStrRe(fieldname )

        fieldname = "开票类型";str1 += self.getFieldStrRe(fieldname ) 
        fieldname = "费用子类";str1 += self.getFieldStrRe(fieldname )  
 
        fieldname = "税率";str1 += self.getFieldStrRe(fieldname )         

        fieldname = "金额fn";str1 += self.getFieldStrRe(fieldname )
        fieldname = "金额";str1 += self.getFieldStrRe(fieldname )  
        
        fieldname = "发票单据编号";str1 += self.getFieldStrRe(fieldname ) 
        fieldname = "folder";str1 += self.getFieldStrRe(fieldname ) 
        #  aObj.folder


        return str1
    def write2File(self):
        
        str1 = self.toStr()
        # print(str1) 
        self.Save2Filepy1(str1)
        print("Save2Filepy1,DB ,Mem ok")
    def Save2MemDict(self):
        global dataDic ,datasObj,isDirty
        len1 = len( dataDic)-1
        for idx in range( len1,-1,-1 ):
            if idx == -1:
                print( "-1 reached ,stop")
                break
            if dataDic[ idx].序号 == self.序号:
                del dataDic[ idx]
        print(" delete edited objext -------------------") 
        # datasObj.push(self)
        self.cal();
        print("Cal Ok")
        dataDic +=[self]
        if True:# doSwap == True:
            nobj = self.swap( ) 
            if nobj != None:
                nobj.cal();
                dataDic += [nobj]
                print("Swap Ok")
         
        print(" Added edited objext -------------------") 
    def getbasicdataStr(self):
        str0= "aObj =  {:}();".format( self.__class__.__name__ )+"\n"
        str0 += "aObj.序号 = '{:}' ".format(self.序号 )+"\n"
        str0 +="aObj.状态 = '{:}'".format(self.状态)+"\n"
        # str0 +="gloProc.push( aObj);"+ "\n"
        return str0 


class 现金Cls(AccountBaseCls ):
    pass  
    def toStr(self):   
        str11 ="""#aObj = 现金流收款Cls() ; """+"\n"
        str12= super(现金Cls,self).toStrBase()
        return str11 +str12       
 
       
class 费用Cls(AccountBaseCls ):
    pass   
    def toStr(self):
        str11 ="""#aObj = 现金流费用支付Cls() ; """+"\n"

        str12= super(费用Cls,self).toStrBase()

        return str11 +str12 # + str10   
    def get_C02_费用支付额(self ):                
        return  self.getguiyixishu() * self.归一金额;  
    # def get_C11_费用待支额(self ):
    #     return self.get_C02_费用支付额() ;        
class 合同Cls(AccountBaseCls ):
    pass    
    def toStr(self):   
        str11 ="""#aObj = 合同采购Cls() ;OrgObj =aObj """+"\n"
        str12= super(合同Cls,self).toStrBase()

        return str11 +str12   

     
class FY基本合同Cls(AccountBaseCls ):
    def toStr(self):
        str11 ="""#aObj = 费用合同Cls() ; """+"\n"
        # print( str11 )
        str12=super(FY基本合同Cls,self).toStrBase()
        # print( str12 )
        return str11 +str12 #+ str10   

    def get_C01_费用计划额(self ):
        return self.getguiyixishu() * self.归一金额;
    # def get_C11_费用待支额(self ):
    #     return self.get_C01_费用计划额() ;         
class 发票Cls(AccountBaseCls ):
    pass
    def toStr(self):   
        str11 ="""#aObj = 发票收Cls() ;OrgObj =aObj """+"\n"
        str12= super(发票Cls,self).toStrBase()
        return str11 +str12    
        # return str1
