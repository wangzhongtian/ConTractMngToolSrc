import csv
import os
import sys
import basicLib
def procPy1File(datafolder,statusfolder,caiwuFolder,filename,Newstr):
    fullname = os.path.join( datafolder,statusfolder,caiwuFolder,filename )
    if not os.path.exists( fullname ):
        return 
    if filename[-3:].upper() == "PY1":
        py1_file =   basicLib.openfile(fullname,"a",encoding="utf-8-sig") 
        # UTF8fileObj = basicLib.openfile(TgrFilename,"w",encoding="utf-8-sig")
        # for line in py1_file:
        #     print(line)
        data = "aObj.关联销售合同名称"+ " ='" + Newstr + "'"
        print( data,file = py1_file )
        py1_file.close()
        ## read files
        py1_file =   basicLib.openfile(fullname,"r",encoding="utf-8-sig") 
        # UTF8fileObj = basicLib.openfile(TgrFilename,"w",encoding="utf-8-sig")
        for line in py1_file:
            print(line)
        # data = "aObj.关联销售合同名称"+ " ='" + Newstr + "'"
        # print( data,file=py1_file )
        py1_file.close() 
        



def readinCsvFile(rootfolder,SrcFile):
    fullname = os.path.join( rootfolder,SrcFile )
    csv_file= csv.reader( basicLib.openfile(fullname,"r") )
    # UTF8fileObj = basicLib.openfile(TgrFilename,"w",encoding="utf-8-sig")
    cnt=1
    for cols in csv_file:
        print(cols)
        # cols =line.split(  ",")
        procPy1File("D:\\Log\\datalib", cols[2],cols[0] ,cols[3] ,cols[1])
        cnt = cnt +1
        if cnt > 500000:
            sys.exit()
    # close(csv_file)

SrcFile="改变合同子类.csv"
rootfolder="./"
readinCsvFile(rootfolder,SrcFile)
