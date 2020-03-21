#-*- coding: UTF8
from __future__ import print_function
# import pickle
import  basicDataProc
from basicDataProcHT import * 
from basicDataProcFY import * 
from basicDataProcXJ import * 
from basicDataProcFP import * 
import shutil       
import sub合同分类
from basicLib import *

##############################################################################

def getdataDic1():
    # global isDirty ,datasObj,dataDic  
    if basicDataProc.isDirty == False:
        print( "isDirty  is False ,return Buffered dataDIc .=================")   
        return basicDataProc.dataDic 
    import fileSplit
    fileSplit.合并()    
    basicDataProc.dataDic =[]
    try:
        import  datas  
    except:
        print("Pro data  base ERROR")
        return basicDataProc. dataDic
        pass

    imp.reload(datas)
    basicDataProc.datasObj = datas.update()
    basicDataProc.dataDic = datas.gloProc.container
    
    basicDataProc.isDirty = False
    return basicDataProc.dataDic
    
def getdatasObj():
    # global isDirty ,datasObj,dataDic
    if basicDataProc.datasObj !=None:
        return basicDataProc.datasObj
    if basicDataProc.isDirty == False   :
        print( "isDirty is False ,return Buffered datasObj.=================")   
        return basicDataProc.datasObj
    # import fileSplit
    # fileSplit.合并()

    basicDataProc.datasObj= None
    try:
        print(" load dataDb into mem begin ..")
        if os.path.exists(glbcfg.Py1fileRootFolder+"Gened/dataDb.py"):
            shutil.copyfile( glbcfg.Py1fileRootFolder+"Gened/dataDb.py",glbcfg.Py1fileRootFolder+"Gened/datas.py")
        sys.path.append(glbcfg.Py1fileRootFolder+"Gened")
        import  datas  
        print(" load dataDb into mem end ,ok ..")
    except   :
        print("Pro data  base ERROR in getdatasObj"  )
        return basicDataProc.datasObj

    try:        
        # imp.reload(datas)
        basicDataProc.datasObj =  datas.gloProc #update()

    except:
        print("Re load  data  base ERROR")
        return basicDataProc.datasObj
    basicDataProc.dataDic = datas.gloProc.container
    basicDataProc.isDirty = False
    sub合同分类.classifyAcoount( basicDataProc.dataDic )
    return basicDataProc.datasObj

def getdataDic():
    # print("Test Here@")
    basicDataProc.readpickle()
    getdatasObj()
    return  basicDataProc.dataDic
    # basicDataProc.dataDic = basicDataProc.datasObj.container
    
class  数据统计CLs(object):
    map1={ "采购合同" :合同采购Cls,"销售合同" :合同销售Cls , 
        "销售开票":发票开Cls,  "采购收票": 发票收Cls , "报销收票": 报销发票收Cls ,
        "采购支出":现金流支付Cls,  "销售收款":现金流收款Cls ,"直接采购支出":直接采购支出Cls,"代赋税支出":代赋税支出Cls,
        "费用支出":现金流费用支付Cls, "费用合同":费用合同Cls,"报销采购支出" :报销采购支出Cls    }

    outputdatas =[]

    @classmethod
    def is财务分类Obj( cls,dataObj,财务分类=""):
        if 财务分类=="" or 财务分类=="所有":
             return True
        财务分类cls =cls.map1[ 财务分类 ]

        a= isinstance(  dataObj, 财务分类cls )
        # print( "---",财务分类, 财务分类cls,type(dataObj),a )
        return a
    @classmethod        
    def cond关联销售合同(cls,dataObj,关联销售合同名称 ):
        # print(关联销售合同名称 )
        str1 = 关联销售合同名称.strip()
        str1 = str1.replace("，",",")
        str1 = str1.replace(";",",")
        str1 = str1.replace("；",",")
        str1 = str1.replace(" ",",") 

        conds = str1.strip().split(",")
        if len(conds) == 0 or  "所有" in conds :
            return True
        for con in conds:
            if con  in dataObj.关联销售合同名称 :
                return True
        return False 
        # if( 关联销售合同名称 == ""  or 关联销售合同名称 == "所有"):
        #     pass
        # else:              
        #     cond1 =  关联销售合同名称 in dataObj.关联销售合同名称 
        #     if cond1 == False:
        #         return False
        # return True
    @classmethod        
    def cond财务分类(cls,dataObj,财务分类条件):
        # print( 财务分类条件 )
        str1 = 财务分类条件.strip()
        str1 = str1.replace("，",",")
        str1 = str1.replace(";",",")
        str1 = str1.replace("；",",")
        str1 = str1.replace(" ",",") 

        conds = str1.strip().split(",")
        if len(conds) == 0 or "所有" in conds :
            return True

        for 财务分类 in conds:
            # cond1 = cls.is财务分类Obj( dataObj,财务分类)
            cond1= 财务分类 in  dataObj.getFNstr()
            if cond1 == True:
                return True  
        return False 
    @classmethod         
    def cond对方(cls,dataObj,对方):
        str1 = 对方.strip()
        str1 = str1.replace("，",",")
        str1 = str1.replace(";",",")
        str1 = str1.replace("；",",")
        str1 = str1.replace(" ",",") 

        conds = str1.strip().split(",")
        # for u in conds: print(u)
        if len(conds) == 0 or  "所有" in conds :
            return True

        for 对方1 in conds:
            
            if 对方1 in dataObj.对方  :
                # print( dataObj.对方,对方1 )
                return True  
        return False 

    @classmethod         
    def cond记账方(cls,dataObj,记账方):
        # print(记账方)
        str1 = 记账方.strip()
        str1 = str1.replace("，",",")
        str1 = str1.replace(";",",")
        str1 = str1.replace("；",",")
        str1 = str1.replace(" ",",") 

        conds = str1.strip().split(",")
        # for u in conds: print(u)
        if len(conds) == 0 or  "所有" in conds :
            return True

        for 记账方1 in conds:
            if 记账方1 in dataObj.记账方  :
                # print( dataObj.记账方,记账方1 )
                return True  
        return False 


    @classmethod  
    def condDate(cls,dataObj,startDate,endDate ):
        # print("condDate --------------------------------")
        startDate = startDate.strip()
        endDate = endDate.strip()

        date1 = dataObj.发生日期

        cond1 =  True if len(startDate) == 0   else  date1 >= startDate 
        cond2 =  True if len(endDate) == 0   else  date1 <= endDate         
        return cond1 and cond2
    @classmethod        
    def cond(cls,dataObj,财务分类,记账方,对方,关联销售合同名称,startDate,endDate ):
        cond1 =True

        if not cls.cond财务分类( dataObj,财务分类) :
            return False 

        if not cls.cond记账方( dataObj,记账方) :
            return False 

        if not cls.cond对方( dataObj,对方) :
            return False 


        if not cls.cond关联销售合同( dataObj,关联销售合同名称) :
            return False 

        if not cls.condDate( dataObj,startDate,endDate) :
            return False 

        return True
    @classmethod          
    def cal财务数据(cls, orgDatas) :
        财务统计数组= []
        for data in orgDatas:
            财务统计结果 = data.getBasic财务数据()
            for k in  ["合同子类","合同大类","对方","记账方"]: #,"财务分类"
                exec( "财务统计结果.{0}=data.{0}".format( k) )
            财务统计数组 += [ 财务统计结果 ]
        财务统计结果=  Basic财务数据()  
        # key_basic = ()# 财务统计结果.__dict__.keys()
        key_caled =None   
        for jisuan in 财务统计数组:
            jisuan.cal()########### wangzht
            if  key_caled == None:
                key_caled =jisuan.__dict__.keys()
            for k in   tuple(key_caled):#key_caled) +
                # print(k)
                if "_" in k  and "A" != k[:1]:
                    try:
                        exec( "财务统计结果.{0}=jisuan.{0}+财务统计结果.{0}".format( k) )
                    except:
                        exec( "财务统计结果.{0}=0.0".format( k) )
                        pass

        return 财务统计结果
    @classmethod     ####### extern function   
    def condsatisify(cls,dataObjArrary,财务分类="",记账方="",对方="",关联销售合同名称="",startDate="",endDate=""):
        # self.dataDic = 账务处理Lib.getdataDic()
        # print("@@@@@@@@@@@ condsatisify @@@@@@@@@@@@@@@@@")
        cls.outputdatas=[]
        for  dataObj in dataObjArrary:
            # print(dataObj.记账方, 记账方 )
            if  cls.cond( dataObj,财务分类,记账方,对方,关联销售合同名称,startDate,endDate ):
                 cls.outputdatas += [ dataObj ]
        return  cls.outputdatas

    @classmethod  ####### extern function     
    def get财务数据(cls ,dataObjArrary,财务分类="",记账方="",对方="",关联销售合同名称="" ,startDate="",endDate=""):
       orgdatasObj =  cls.condsatisify ( dataObjArrary,财务分类,记账方,对方,关联销售合同名称 ,startDate,endDate )
       return cls.cal财务数据(orgdatasObj )



def cal财务数据( orgDatas) :
    return 数据统计CLs.cal财务数据(orgDatas )

def loopCal( dataObjArrary ,A1 ):
    a=[]
    for  记账方1 in  A1[0]:
            for 对方1 in A1[1]:
             for 销售合同0 in A1[2]:
                # name =  记账方1+"_"+ 对方1  + "_" + 合同大类1
                if 销售合同0 == "所有":
                    销售合同1 =""
                else:
                    销售合同1 = 销售合同0+"-"
                
                # 合同大类 = 合同大类1.replace("所有","")
                对方 = 对方1.replace("所有","")
                记账方 =记账方1 .replace("所有","")
                aobj   = 数据统计CLs.get财务数据(dataObjArrary,财务分类="",记账方=记账方,对方=对方,关联销售合同名称=销售合同1 )
                # aobj.name =name
                exec(  "aobj.{0} ='{1}'".format("记账方" ,记账方1 )   )
                exec(  "aobj.{0} ='{1}'".format("对方" ,对方1 )   )
                exec(  "aobj.{0} = '{1}'".format("合同大类" ,销售合同0 )   )
                exec(  "aobj.{0} = '{1}'".format("财务分类" ,"所有" )   )
                exec(  "aobj.{0} = '{1}'".format("关联销售合同名称" ,"销售合同1" )   )

                a += [aobj]
    return a

def 基本账务统计_新(dataObjArrary,jizhangfang = ""):
    if jizhangfang =="":
        a=[]
        A1=  [   ["PPPP"],               ["所有"],                ["主合同","增项","增补合同","所有"]   ]
        a0= loopCal( dataObjArrary ,A1 )
        a+=a0[:-1]
        A1=  [   ["AAAA"],               ["PPPP","所有"],           ["主合同","增项","增补合同","所有"]   ]
        a1 =  loopCal( dataObjArrary ,A1 )
        a+=a1[ :-1] + a0[-1:]+a1[-1:]
        return a
    elif jizhangfang == "AAAA":
        a=[]

        A1=  [   ["AAAA"],               ["PPPP","所有"],           ["主合同","增项","增补合同","所有"]   ]
        a1 =  loopCal( dataObjArrary ,A1 )
        a+=a1[ :-1] +a1[-1:]
        return a
    else:
        a=[]
        A1=  [   [jizhangfang],               ["所有"],                ["主合同","增项","增补合同","所有"]   ]
        a0= loopCal( dataObjArrary ,A1 )
        a+=a0[:-1]+a0[-1:]

        return a
def 基本账务统计(dataObjArrary,jizhangfang = ""):
    return 基本账务统计_新(dataObjArrary,jizhangfang)
def MainFun(jizhangfang = ""):
    # import  账务处理Lib     
    dataObjArrary = getdataDic()
    # print("11111111111111111")    
    dataobjs   = 基本账务统计(dataObjArrary,jizhangfang )
    # print( len( dataobjs ))
    # print("11111111111111111")
    for u in dataobjs:
        u.guiyi条件字段()
    keys =sorted (dataobjs[0].__dict__.keys()  )
    keysDisplay  =[]
    for i in keys:
        if i[3:4] == "_":
            keysDisplay += [ i ]
            # print(i,"will be shown")
    values= [] 
    columnCnt= len( dataobjs ) +1
    values += [ columnCnt ] 
    values += [ "科目"]       
    for aobj in dataobjs:
        values += [aobj.记账方 +"-"+ aobj.对方 + "-"+aobj.合同大类]
    for key in keysDisplay:
        values +=[ key ]
        for aobj in dataobjs:
            cmdstr =  'aobj.{key}'.format(key=key )
            # print("--11111111111111111")
            value = eval( cmdstr )
            # print("+--11111111111111111",value)            
            if key[:1] =="A":
                values += [ str( value  )]
            else:
                value *=1.0
                values += ["{:0.6f}".format( value  )  ]
    return values