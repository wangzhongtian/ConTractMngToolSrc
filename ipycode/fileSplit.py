#!/usr/bin/python3
#-*- coding: UTF-8
from __future__ import print_function
import os
import glbcfg
import basicLib
def fileSplit( filename ,title,tgrRoot,map1 ):
    ID=0
    map0 =[]
    for i in map1:
        j = i.replace( " ","");
        # print(j)
        map0 += [j]
    curfile=None
    ofilename=""
    for line in basicLib.openfile(filename,"rt",encoding="UTF8"):
        line1 = line.replace(" ","").replace("\r\n","").replace("\n","")
        # if line1 == map0[ 0 ]  or line1 == map0[1 ] :
        #     print(line1 ,map0[0 ])
        if line1 == map0[ 0 ]:
            ID = ID+1
            ofilename= "{:}{:}/{}{}{:04d}.py1".format(tgrRoot,map0[1],title,map0[2]  ,ID)
            if curfile != None:
                curfile.close()
            curfile=basicLib.openfile( ofilename ,"wt",encoding="UTF8")
        if line1 == map0[3]:
            ID = ID+1
            ofilename= "{:}{:}/{}{}{:04d}.py1".format(tgrRoot,map0[4],title,map0[5],ID)
            if curfile != None:
                curfile.close()
            curfile=basicLib.openfile( ofilename ,"wt",encoding="UTF8") 
        #print(ofilename,curfile)

        if  curfile != None:
            if "aObj=" in line1 or "gloProc.push(" in line1 or "aObj.状态=" in line1  or "aObj.序号=" in line1:
                pass
            else:
                line2=line.replace("\r\n","").replace("\n","")
                print(line2,file=curfile )

################################ Split  ##########################
def SplitFiles():
    ################合同
    filename = "../1账务处理V50/hetong已签.py"
    title="ht-"
    tgrRoot= glbcfg.Py1fileRootFolder+"完成/"
    map1=["aObj =  合同采购Cls();","采购合同","20180815-c","aObj =  合同销售Cls();","销售合同","20180815-x"]
    fileSplit( filename ,title,tgrRoot,map1 )

    filename = "../1账务处理V50/hetong待签.py"
    title="ht-"
    tgrRoot=glbcfg.Py1fileRootFolder+"计划/"
    map1=["aObj =  合同采购Cls();","采购合同","20180816-c","aObj =  合同销售Cls();","销售合同","20180816-x"]
    fileSplit( filename ,title,tgrRoot,map1 )

    ################ 发票
    filename = "../1账务处理V50/fapiao已执.py"
    title="fp-"
    tgrRoot=glbcfg.Py1fileRootFolder+"完成/"
    map1=["aObj =  发票开Cls();","销售开票","20180815-F","aObj =  发票收Cls();","采购收票","20180815-S"]
    fileSplit( filename ,title,tgrRoot,map1 )

    filename = "../1账务处理V50/fapiao待执.py"
    title="fp-"
    tgrRoot=glbcfg.Py1fileRootFolder+"计划/"
    map1=["aObj =  发票开Cls();","销售开票","20180816-F","aObj =  发票收Cls();","采购收票","20180816-S"]
    #fileSplit( filename ,title,tgrRoot,map1 )

    ################现金
    filename = "../1账务处理V50/xianjin已执.py"
    title="xj-"
    tgrRoot=glbcfg.Py1fileRootFolder+"完成/"
    map1=["aObj =  现金支付Cls();","采购支出","20180815-F","aObj =  现金收款Cls();","销售收款","20180815-S"]
    fileSplit( filename ,title,tgrRoot,map1 )


    filename = "../1账务处理V50/xianjin待执.py"
    title="xj-"
    tgrRoot=glbcfg.Py1fileRootFolder+"计划/"
    map1=["aObj =  现金支付Cls();","采购支出","20180815-F","aObj =  现金收款Cls();","销售收款","20180815-S"]
    fileSplit( filename ,title,tgrRoot,map1 )



    ################费用
    filename = "../1账务处理V50/feiyong记录.py"
    title="fy-"
    tgrRoot=glbcfg.Py1fileRootFolder+"完成/"
    map1=["aObj =  费用支出Cls();","费用支出","20180815-F","xxxxx","xxxxxx","xxxxxx"]
    fileSplit( filename ,title,tgrRoot,map1 )

    filename = "../1账务处理V50/feiyong计划.py"
    title="fy-"
    tgrRoot=glbcfg.Py1fileRootFolder+"计划/"
    map1=["aObj =  费用支出Cls();","费用支出","20180816-F","xxxxx","xxxxxx","xxxxxx"]
    fileSplit( filename ,title,tgrRoot,map1 )

################################ Combines  ##########################
################合同


def fileGen( curfile ,pathcur1,curfilename,map1,状态,财务类型):
    if curfilename[-4:] != ".py1":
        return
    # print( curfilename )        
    print("","\r\n",file=curfile )
    print("######################","\r\n",file=curfile )
    print("    ",end="",file=curfile )
    if 财务类型 == map1[1] :
        print(map1[0],file=curfile )
        #print(财务类型,map1[0])
    elif 财务类型 == map1[3] :
        print(map1[2],file=curfile );#print(财务类型,map1[2])
    elif 财务类型 == map1[5] :
        print(map1[4],file=curfile );#print(财务类型,map1[4])
    elif 财务类型 == map1[7] :
        print(map1[6],file=curfile );#print(财务类型,map1[6])
    elif 财务类型 == map1[9] :
        print(map1[8],file=curfile );#print(财务类型,map1[8])
    elif 财务类型 == map1[11] :
        print(map1[10],file=curfile ) ;#print(财务类型,map1[10])                           
    elif 财务类型 == map1[13] :
        print(map1[12],file=curfile ) ;#print(财务类型,map1[12])
    elif 财务类型 == map1[15] :
        print(map1[14],file=curfile ) ;#print(财务类型,map1[12])
    elif 财务类型 == map1[17] :
        print(map1[16],file=curfile ) ;#print(财务类型,map1[12])  
    elif 财务类型 == map1[19] :
        print(map1[18],file=curfile ) ;#print(财务类型,map1[12])         
    elif 财务类型 == map1[21] :
        print(map1[20],file=curfile ) ;#print(财务类型,map1[12]) 
    elif 财务类型 == map1[23] :
        print(map1[22],file=curfile ) ;#print(财务类型,map1[12]) 
    else:

        print(财务类型 )
        ##Error
        pass

    print("    aObj.状态 ='{}'".format(状态),file=curfile ) 
    print("    aObj.序号 ='{}'".format(curfilename),file=curfile ) 
    folder = os.path.abspath(pathcur1)
    print("    aObj.folder =r'''{}'''".format( folder.replace("\\","/") ),file=curfile )
    # print("    aObj.folder ='{}'".format( folder ) )    
    # print(folder)
    for line in basicLib.openfile(pathcur1,"rt", encoding="UTF8"):
        line1 = line.replace("\r\n","").replace("\n","").replace(" ","")
        if line1 !="":
            specialHead= "aObj.税率="
            l1 = len(specialHead )
            if line1[:l1] == specialHead : #and line1[l1:l1+1].isnumeric():
                税率str= line1[l1:]
                税率str= 税率str.replace("/","*1.0/").replace("'","").replace("\r","").replace("\n","") #+ "'"
                # print("-{:};".format(税率str))
                税率 = float( str(eval(税率str)) )

                line= specialHead +""+str(税率)+"\n"
                # print( line1,税率str,税率,"=>",line )
            print("    "+line,end="",file=curfile )
    print("    gloProc.push( aObj); ",file=curfile )

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
import glbcfg
def update():
    gloProc = hcXlsProc (); 
'''

def iterSubs(tgrRoot1,subfolder,map1,curfile):
    if subfolder == "":
        tgrRoot =tgrRoot1
    else:
        tgrRoot =os.path.join( tgrRoot1,subfolder)
    for root1,paths1,files1 in os.walk(tgrRoot, topdown=True, onerror=None, followlinks=False) :
        for 状态 in paths1:
            if "模板" in 状态  or  "临时" in 状态 or  "Gened" in 状态:
                continue
            print(状态," status in ",root1 ) 
            pathcur =os.path.join( root1, 状态)
            for root2,paths2,files2 in os.walk(pathcur, topdown=True, onerror=None, followlinks=False) :
                for  财务类型 in paths2:
                    print(财务类型,"财务类型 in ",root2)
                    pathcur1 =os.path.join( root2, 财务类型)
                    for root3,paths3,files3 in os.walk(pathcur1, topdown=True, onerror=None, followlinks=False):  
                        for  curfilename in files3:
                            pathcur2 =os.path.join(root3, curfilename)  
                            # print(curfilename,"\r\n")
                            # 状态1= root2.replace( tgrRoot1,"")
                            folder1 = os.path.abspath( os.path.join(root3,"../" ) )
                            # .split()[1]
                            状态1 = os.path.split( folder1)[1]
                            # print("-----",状态1)
                            fileGen( curfile ,pathcur2,curfilename,map1,状态1,财务类型)
                        break
                break
            # break
        break



def files(tgrRoot,tgrFileName,map1,subfolders=[]):
    curfile= basicLib.openfile( tgrFileName ,"wt" ,encoding="UTF8")
    print(titles, file=curfile )
    if len(subfolders) == 0:
        iterSubs(tgrRoot,"",map1,curfile)
    for subfolder in subfolders:
        iterSubs(tgrRoot,subfolder,map1,curfile)


    print("    return gloProc\n",file =curfile )
    print("gloProc=update()\n",file =curfile )
    
    curfile.close()                 


#SplitFiles()

def 合并( tgrFileName  , tgrRoot):
    map1=["aObj =  合同采购Cls();","采购合同","aObj =  合同销售Cls();","销售合同"]
    map1 +=["aObj =  发票开Cls();","销售开票","aObj =  发票收Cls();","采购收票"]
    map1 +=["aObj =  现金流支付Cls();","采购支出","aObj =  现金流收款Cls();","销售收款"]
    map1 +=["aObj =  现金流费用支付Cls();","费用支出","aObj =  费用合同Cls();","费用合同"]
    map1 +=["aObj =  报销发票收Cls();","报销收票","aObj = 报销采购支出Cls();","报销采购支出"]
    map1 +=["aObj =  直接采购支出Cls();","直接采购支出","aObj = 代赋税支出Cls();","代赋税支出"]      
    # print(map1)

    a=os.listdir(tgrRoot)
    subs =[]
    for a0 in a:
        a1=os.path.join(tgrRoot,a0)
        if os.path.isdir(a1):
            if "datas" in a0:
                print(a1 )
                subs= subs +[a0,]
        else:
            print(a1," is file")
    for i in subs:
        print("Subfolder is:",i)

    files(tgrRoot,tgrFileName,map1,subs)

