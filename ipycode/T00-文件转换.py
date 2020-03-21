# *-* coding=UTF8
import os
import basicLib
def files(tgrRoot,fileGen):
    print(tgrRoot )
    for root1,paths1,files1 in os.walk(tgrRoot, topdown=True, followlinks=False) :
        # print( root1 )
        roottgr = root1.replace("后期datas-test","后期datas")
        # print( roottgr )

        for curfilename in files1:
            # print(curfilename,"\r\n")         
            ext =   curfilename[-4:]    
            ext= ext.upper()
            # print( ext )
            if  ext == ".PY1":    
                tgrFileName = curfilename 
                tgrfn = os.path.join( roottgr, tgrFileName )
                curfileobj= basicLib.openfile( tgrfn ,"wt" ,encoding="UTF8")
                pathcur1 = os.path.join(root1, curfilename)  
                fileGen( curfileobj ,pathcur1,curfilename)
                curfileobj.close()  
                print( tgrFileName)

def fileGenHetong( curfile ,pathcur1,curfilename):
    for line in basicLib.openfile(pathcur1,"rt", encoding="UTF8"):
        line1 = line.replace("\r\n","").replace("\n","").replace(" ","")
        line1 = line1.replace("aObj.发票总金额","aObj.金额" )
        line1 = line1.replace("aObj.交易总金额","aObj.金额" )
        line1 = line1.replace("aObj.发票含税总额","aObj.金额" ) 
        
        line1 = line1.replace("aObj.签署日期","aObj.发生日期" )       
        line1 = line1.replace("aObj.发票日期","aObj.发生日期" ) 
        line1 = line1.replace("aObj.交易日期","aObj.发生日期" )                     

        line1 = line1.strip()


        print(line1,end="\n",file = curfile )       
        # print(line1 ) 

# tgrRoot="F:\\z\\2019files\\项目账务工具\\Log\datalib\\后期datas-test"
# files(tgrRoot,  fileGenHetong )
