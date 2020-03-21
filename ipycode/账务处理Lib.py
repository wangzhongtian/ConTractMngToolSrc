#-*- coding: UTF8
from __future__ import print_function
# import pickle
import basicDataProc
from basicDataProcHT import * 
from basicDataProcFY import * 
from basicDataProcXJ import * 
from basicDataProcFP import * 
import shutil       
import sub合同分类
import fieldsname  
from basicLib import *
class tgrContainer(object):
    def __init__(self):
        self.container  =[]
    def push(self , aobj  ):
        aobj.cal();
        self.container +=[aobj]
        if doSwap == True:
            nobj = aobj.swap( ) 
            if nobj != None:
                nobj.cal();
                self.container +=[nobj]
    def get合同利润( self):
        合同成本=0.0;合同抵税=0.0
        合同收入=0.0;合同纳税=0.0
        合同毛利润=0.0
        for d1 in self.container :
            if isinstance( d1 ,合同采购Cls ):
                合同成本 += d1.合同成本;
                合同抵税 += d1.税额;
                continue;
            if  isinstance( d1 ,合同销售Cls):
                合同收入 += d1.合同收入;
                合同纳税 += d1.税额;
                continue;
        合同毛利润 = 合同收入 + 合同成本
        print( """
        合同分析
            合同成本 = {: ,.2f};
            合同抵税 = {: ,.2f};
            合同收入={: ,.2f};
            合同纳税={: ,.2f};
            合同毛利润={: ,.2f};
            应缴税款={: ,.2f};""".format( 合同成本, 合同抵税 ,合同收入 ,-1.0*合同纳税 ,合同毛利润,-1.0*合同纳税 + 合同抵税 ) );

    def get发票信息( self):
        应收=0.0;抵税=0.0
        应付=0.0;纳税=0.0
        for d1 in self.container :
            if isinstance( d1 ,发票收Cls ):
                应付 += d1.归一金额;
                抵税 += d1.发票税额;
                continue;
            if  isinstance( d1 , 发票开Cls):
                应收 += d1.归一金额;
                纳税 += d1.发票税额;
                continue;
        # 合同毛利润 = 合同收入 + 合同成本
        print( """
        发票分析：
            应付 = {: ,.2f};
            抵税 = {: ,.2f};
            应收={: ,.2f};
            纳税={: ,.2f};
            应缴税款={: ,.2f};""".format( 应付, 抵税 ,应收 ,-1.0*纳税 , -1.0*纳税 +  抵税 ) );            
    def get净现金流( self):
        收款=0.0;支出=0.0
        for d1 in self.container :
            if isinstance( d1 ,现金流支付Cls ):
                支出 += d1.归一金额;
                continue;
            if  isinstance( d1 , 现金流收款Cls):
                收款 += d1.归一金额;
                continue;
        print( """
        现金流分析：
            支出= {: ,.2f};
            收款={: ,.2f};
            净现金流={: ,.2f}""".format( 支出, 收款 ,支出+收款  ));
    def get供应商合同支付余额( self):
        for key,value in 对方单位Cls.__dict__.items():
            if key in ( "mapping","typename") or "__" == key[:2]:
                continue
            
            print( key ,value)


            合同额=0.0;支付额=0.0
            for d1 in self.container :
                if isinstance( d1 ,现金流支付Cls ):
                    支出 += d1.归一金额;
                    continue;
                if  isinstance( d1 , 现金流收款Cls):
                    收款 += d1.归一金额;
                    continue;
            print( """
            现金流分析：
                支出= {: ,.2f};
                收款={: ,.2f};
                净现金流={: ,.2f}""".format( 支出, 收款 ,支出+收款  ));

    def get费用总额( self):
        支出=0.0
        费用合同额=0.0
        for d1 in self.container :
            if isinstance( d1 ,现金流费用支付Cls ):
                支出 += d1.归一金额;
                continue;
        for d1 in self.container :
            if isinstance( d1 ,费用合同Cls ):
                费用合同额 += d1.归一金额;
                continue;
        
        print( """
        费用分析：
            费用支出= {: ,.2f};
            费用计划= {: ,.2f};
            """.format( 支出 ,费用合同额 ));

class hcProc(tgrContainer):
    def __init__(self):
        self.file =sys.stdout
        super(hcProc,self).__init__()
        self.ID =0;
        self.row =None
        self.XuhaoHead="A{:04d}"
    def outHead(self,row):
           print("aObj = " ,end=" ",file=self.file )
           print( row.__class__ .__name__+"();" ,file=self.file )
    def outTail(self,row):
        print( "gloProc.push( aObj); ",file=self.file );
        print("##################################\r\n",file=self.file )
    def xuhaoGen(self):
        self.ID +=1;
        return  self.XuhaoHead.format(self.ID);

    def jizhanggongsimingtihuan(self,k1 , v1):
        newname= 记账单位Cls.revermapping( v1 )
        #a = "记账单位Cls.{:};".format( newname );  #format(self.row.__class__.__name__ )
        return newname;
    def duifanggongsimingtihuan(self,k1 , v1):
        newname = 对方单位Cls.revermapping( v1 )
        a = "对方单位Cls.{:};".format( newname );  #format(self.row.__class__.__name__ )
        return newname;     
    def hetongdaleitihuan(self,k1 , v1):
        newname = 合同主类Cls.revermapping( v1 )
        a = "合同主类Cls.{:};".format( newname );  #format(self.row.__class__.__name__ )
        return newname; 
    def hetongZileitihuan(self,k1 , v1):
        newname = 合同子类Cls.revermapping( v1 )
        a = "合同子类Cls.{:};".format( newname );  #format(self.row.__class__.__name__ )
        return newname; 
    def 签署方式tihuan(self,k1 , v1):
        newname = 签署方式Cls.revermapping( v1 )
        a = "签署方式Cls.{:};".format( newname );  #format(self.row.__class__.__name__ )
        return newname;     
         
    def outthedata(self,fileObj=None,fenxileixing=None):
        if fileObj != None:
            self.file= fileObj
        h=dict()
        for self.row  in self.container:
            if fenxileixing !=None and fenxileixing =="合同":
                if not  isinstance(self.row, 合同Cls ):
                    continue
            if fenxileixing !=None and fenxileixing =="发票":
                if not  isinstance( self.row,发票Cls ):
                    continue            
            if fenxileixing !=None and fenxileixing =="现金":
                if not isinstance( self.row,现金Cls ):
                    continue    
            if fenxileixing !=None and fenxileixing =="费用":
                if not  isinstance(self.row, 费用Cls ):
                    continue                        
            self.outHead( self.row  )
            for k,v in self.row .__dict__.items():
                if k not in self.row .keys:
                    h[ k ] ="not in keys"
                    continue 
                #continue
                if k == "序号":
                    v1= self.xuhaoGen()
                    print( "aObj.{:} = '''{:}'''".format( k,v1),file=self.file  )
                elif k== "记账方": 
                    v1 = self.jizhanggongsimingtihuan(k,v)
                    print( "aObj.{:} = {:}".format( k,v1),file=self.file  )
                elif k == "对方":
                    v1 = self.duifanggongsimingtihuan(k,v)
                    print( "aObj.{:} = {:}".format( k,v1),file=self.file  )
                elif k== "合同大类" :
                    v1 = self.hetongdaleitihuan(k,v)
                    print( "aObj.{:} = {:}".format( k,v1) ,file=self.file )
                elif k == "合同子类":
                    v1 = self.hetongZileitihuan(k,v)
                    print( "aObj.{:} = {:}".format( k,v1),file=self.file  )
                elif k == "签署方式":
                    v1=self.签署方式tihuan(k,v)
                    print( "aObj.{:} = {:}".format( k,v1) ,file=self.file )
                else:
                    v1=v
                    if "额" == k[-1:] or "率" ==  k[-1:] :
                        print( "aObj.{:} = {:}".format( k,v1),file=self.file  )
                    else:
                        print( "aObj.{:} = '''{:}'''".format( k,v1) ,file=self.file )

            self.outTail(self.row)

        # for k,v in h.items():
        #     print(k,v)
        print(self.ID )

class hcXlsProc(hcProc):
    def __init__(self ):
        #super(hcXlsProc,self).__init__(self)
        super(hcXlsProc,self).__init__()
        self.row  = None
    def needxlsSave( self,fenxileixing  ):
        # print( "**************:",fenxileixing )
        if fenxileixing ==None:
            return False ;
        mappings =[ ("费用合同",FY基本合同Cls),("合同",合同Cls ),("发票",发票Cls ) , ("现金",现金Cls )   , ("费用",费用Cls ) ]
        for (type, clsName ) in mappings:
            if fenxileixing == type and isinstance(self.row, clsName) :
                return True
        return False 
    def outTitleCaled(self,xlsfile1,sheetname):
        titleStr=""
        cols =fieldsname.caledFields.split()
        for k1  in cols:
            titleStr += xlsfile1.getCell( "Title","String",k1)
        xlsfile1.addrow2table( sheetname , titleStr , -1)
        return True
    def outTitle(self,xlsfile1,sheetname):
        titleStr=""
        titleStr += xlsfile1.getCell( "Title","String","账务分类")
        titleStr += xlsfile1.getCell( "Title","String","发生日期")
        titleStr += xlsfile1.getCell( "Title","String","金额")
        
        for k  in self.row.displaykeys:
            titleStr += xlsfile1.getCell( "Title","String",k)
        
        xlsfile1.addrow2table( sheetname , titleStr , -1)
        return True
    
    def outRowCaled(self, xlsfile1,sheetname,数据类型,类型标记):
        cellsDta =""
        # cellsDta += xlsfile1.getCell( "Regular","String", self.row.__class__.__name__.replace("Cls",类型标记) )     
        # cellsDta += xlsfile1.getCell( "Regular","String", DateStrReg( self.row.get发生日期() )  )  
        # cellsDta += xlsfile1.getCell( "Regular","Number", self.row.get归一金额(数据类型) ) 

        cols =fieldsname.caledFields.split()
        for k1  in cols:
            k = k1.strip()
            if "_" in k :
                typeStr = "Number"
            else:
                typeStr = "String"
            exp = str( k )
            expfull= "self.row."+exp
            # print( expfull )
            v0= eval( expfull )
            # if "_" in k :

            #     if abs( v0 ) < 0.0000001:
            #         # print(" jixiaoshu :",v0 )
            #         v0 = "0.0" 

            v1 = str( v0 )
            # v1 =str(v0).strip("\r\n\t ")
            cellsDta += xlsfile1.getCell( "Regular",typeStr,v1)   
        xlsfile1.addrow2table( sheetname , cellsDta ,-1) 
    def outRow(self, xlsfile1,sheetname,数据类型,类型标记):
        cellsDta =""
        cellsDta += xlsfile1.getCell( "Regular","String", self.row.__class__.__name__.replace("Cls",类型标记) )     
        cellsDta += xlsfile1.getCell( "Regular","String", DateStrReg( self.row.get发生日期() )  )  

        cellsDta += xlsfile1.getCell( "Regular","Number", "{:0,.6f}".format(self.row.get归一金额(数据类型) *1.0 ) ) 
        for k  in self.row.displaykeys:
            try:
                v0=self.row.__dict__[ k ];
                v1 =str(v0).strip("\r\n\t ")

            except:

                v1= ""

            try:
                if v1 != "":
                    a= float(v1)*1.0
                    v1 ="{:0,.6f}".format(a)
            except:
                pass

            if "额" == k[-1:] or "率" ==  k[-1:] :
                typeStr = "Number"
                
                # v1 =
            else:
                typeStr = "String"
            cellsDta += xlsfile1.getCell( "Regular",typeStr,v1)  
            # if  "后期维保" in v1 :
            #     print( ";;"+v1+"___") 
        xlsfile1.addrow2table( sheetname , cellsDta ,-1)
    def outputTbls(self,xlsfile1,tblname1,数据类型,sheetname,类型标记):
        tblname =tblname1 
        titleOuted = False
        for self.row  in self.container:
            if self.jizhangfang == "" :
                合格记账方 = True
            elif self.jizhangfang   in  self.row.__dict__[ "记账方" ] :
                合格记账方 = True
            else:
                合格记账方 = False
            # 合格记账方 = and self.jizhangfang != "" 
            if not 合格记账方:
                continue
            if tblname1 == None:
                needSave =True
            else:
                needSave = self.needxlsSave( tblname  )
            if needSave == False:
                continue
            if  titleOuted == False  :
                self.outTitle(xlsfile1,sheetname)
                titleOuted = True
            self.outRow(  xlsfile1,sheetname,数据类型,类型标记)
    def outputCalTbls(self,xlsfile1,tblname1,数据类型,sheetname,类型标记):
        tblname =tblname1 
        titleOuted = False
        for self.row  in self.container:
            if self.jizhangfang == "" :
                合格记账方 = True
            elif self.jizhangfang   in  self.row.__dict__[ "记账方" ] :
                合格记账方 = True
            else:
                合格记账方 = False
            # 合格记账方 = and self.jizhangfang != "" 
            if not 合格记账方:
                continue
            # if tblname1 == None:
            needSave =True
            # else:
            #     needSave = self.needxlsSave( tblname  )
            # if needSave == False:
            #     continue
            if  titleOuted == False  :
                self.outTitleCaled(xlsfile1,sheetname)
                titleOuted = True
            self.outRowCaled(  xlsfile1,sheetname,数据类型,类型标记)                   
    def outStaticsinfo( self, xlsfile1,sheetname ,ColDataCnt , dataArrary  ):
        cnt = 0
        titleStr=""
        row = 1
        line = 0
        glbtitleLInes = 5
        for value in dataArrary:
            if line > glbtitleLInes and cnt % ColDataCnt != 0:
                titleStr += xlsfile1.getCell( "Regular","Number","{}".format(value) )
            else:
                try:
                    b=float(value)
                    titleStr += xlsfile1.getCell( "Regular","Number","{:0,.6f}".format(b*1.0) ) #
                except:
                     titleStr += xlsfile1.getCell( "Regular","String", value )
            if( cnt % ColDataCnt == ColDataCnt-1 ) :
                xlsfile1.addrow2table( sheetname , titleStr , -1)
                titleStr=""
            cnt += 1
            line = cnt / ColDataCnt            
        return True
    def outXlsx(self,xlsxName,jizhangfang=""):
        self.jizhangfang = jizhangfang
        self.xlsxFilename = xlsxName
        xlsfile1 =xlsFile(self.xlsxFilename )
        for sheetname in ("费用合同" ,"合同","发票","现金","费用","财务分析汇总","原始数据汇总","汇总","财务统计","财务计算" ):
            xlsfile1.addtable( sheetname )
        for tblname in ( "合同","发票" ):
            self.outputTbls(xlsfile1,tblname,"原始数据",tblname,"-原始")
            self.outputTbls(xlsfile1,tblname,"财务收益分析","财务分析汇总","-收成")
            self.outputTbls(xlsfile1,tblname,"原始数据","原始数据汇总","-原始")
        for tblname in (  "现金","费用"):
            self.outputTbls(xlsfile1,tblname,"原始数据",tblname,"-原始")
            self.outputTbls(xlsfile1,tblname,"财务收益分析","财务分析汇总","")
            self.outputTbls(xlsfile1,tblname,"原始数据","原始数据汇总","")

        for tblname in ( "合同","发票" ):
            self.outputTbls(xlsfile1,tblname,"原始数据","汇总","-原始")
            self.outputTbls(xlsfile1,tblname,"财务收益分析","汇总","-收成")
            #self.outputTbls(xlsfile1,tblname,"原始数据","原始数据汇总","-原始")
        for tblname in (  "现金","费用"):
            # self.outputTbls(xlsfile1,tblname,"原始数据",tblname,"-原始")
            self.outputTbls(xlsfile1,tblname,"财务收益分析","汇总","")
        for tblname in (  "费用合同", ):
            self.outputTbls(xlsfile1,tblname,"原始数据",tblname,"-原始")
            self.outputTbls(xlsfile1,tblname,"财务收益分析","财务分析汇总","-收成")
            self.outputTbls(xlsfile1,tblname,"原始数据","原始数据汇总","-原始")
        tblname = "财务计算"
        sheetname = "财务计算"
        类型标记 ="-计算" 
        数据类型 = "财务计算"
        self.outputCalTbls(xlsfile1,tblname,数据类型,sheetname,类型标记)
        # print("--bbbb-") 
        datas = MainFun(self.jizhangfang)    
        # print("--bbbb-")                
        ColDataCnt = datas[0]
        dataArrary = datas[1:]
        # print("--bbbb-")        
        self.outStaticsinfo( xlsfile1,"财务统计" , ColDataCnt , dataArrary  )
        # print("--bbbb-")
        xlsfile1.writeXlsFile()
        # print("---")




from out2Xls import *