# *-* coding=UTF8
import os
import basicLib
def fileGenHetong( curfile ,pathcur1,curfilename):
    for line in basicLib.openfile(pathcur1,"rt", encoding="UTF8"):
        line1 = line.replace("\r\n","").replace("\n","").replace(" ","")
        if line1 !="":
            if "aObj.合同子类" == line[:9]:
                line2= line.replace("aObj.合同子类 = 合同子类Cls.", "aObj.费用子类 = 费用子类Cls." )
                print(line2,end="",file=curfile)
                print("aObj.合同子类 = 合同子类Cls.主合同",end="\n",file=curfile) 
                continue
            if "发票总金额" ==  line[:5]:
                print( line  ,end="",file=curfile)            
                print( "aObj.发票总金额fn = 发票总金额",end="\n",file=curfile)
                continue
            print(line,end="",file=curfile) 

def fileGen支出( curfile ,pathcur1,curfilename):
    for line in basicLib.openfile(pathcur1,"rt", encoding="UTF8"):
        line1 = line.replace("\r\n","").replace("\n","").replace(" ","")
        if line1 !="":
            if "aObj.合同子类" == line[:9]:
                line2= line.replace("aObj.合同子类 = 合同子类Cls.", "aObj.费用子类 = 费用子类Cls." )
                print(line2,end="",file=curfile)
                print("aObj.合同子类 = 合同子类Cls.主合同",end="\n",file=curfile) 
                continue
            if "发票总金额" ==  line[:5]:
                print( line  ,end="",file=curfile)            
                print( "aObj.发票总金额fn = 发票总金额",end="\n",file=curfile)
                continue
            print(line,end="",file=curfile) 
 
def files(tgrRoot,fileGen=fileGenHetong):
    # print( tgrRoot )
    for root1,paths1,files1 in os.walk(tgrRoot, topdown=True, onerror=None, followlinks=False) :
        # print( files1 ,root1)
        for curfilename in files1:
            print(curfilename,"\r\n")            
            tgrFileName = curfilename .replace(".py2",".py1")
            tgrfn = os.path.join( root1, tgrFileName )
            curfileobj= basicLib.openfile( tgrfn ,"wt" ,encoding="UTF8")
            pathcur1 = os.path.join(root1, curfilename)  
            fileGen( curfileobj ,pathcur1,curfilename)
            curfileobj.close()  
        break

tgrRoot=glbcfg.Py1fileRootFolder+"完成/费用合同/"
files(tgrRoot, fileGen=fileGenHetong )
tgrRoot=glbcfg.Py1fileRootFolder+"完成/费用支出/"
files(tgrRoot, fileGen=fileGen支出 )