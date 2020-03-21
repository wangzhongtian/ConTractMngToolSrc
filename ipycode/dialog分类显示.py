#-*- coding: UTF8
from __future__ import print_function

import dialogBase
import dialogShowList
import dialog销售合同
import dialog销售开票
import dialog销售收款

import dialog采购合同
import dialog采购支付
import dialog采购收票
import  dialog报销采购支出
import  dialog直接采购支出
import  dialog代赋税支出
import dialog报销收票

import dialog费用合同
import dialog费用支出
from   名称定义      import *
from   BasicWidgets import *
import os
import  账务处理Lib
import glbcfg
##############################################################################
class 分类显示Dialog(dialogShowList.Dialog_ShowList):
    def body(self):
        sizeA =self.ClientRectangle
        print(sizeA)
        self.Posy = sizeA.Top       

        self.SetupMenus()
        # self.root= master
        row =0

        width=sizeA.Width

        self.财务分类s  =dialogBase.全局财务分类s; # ("销售合同",)  #
        self.add财务分类(width,row,"销售合同"); row= row+1 #"销售合同"

        self.记账方s = dialogBase.全局记账方s;   # 设置下拉列表的值
        self.add记账方(width,row); row= row+1

        # self.对方s= dialogBase.中电销售合同对方s;
        self.add对方(width,row); row= row+1  
        self.add关联销售合同名称(row,width,fieldname="关联销售合同名称")    
        self.ctrlstartDate = self.add签署日期( row ,width ,fieldname="起始日期") 
        self.ctrlendDate =  self.add签署日期( row ,width ,fieldname="截至日期") 
        self.ctrlstartDate.set("")
        self.ctrlendDate.set("")
        self.row =row

        return None # initial focus
    def bodyShowTree(self):
        margin =10
        ColumnWidth =( self.ClientSize.Width-margin) /3
        self.row +=1
        seeRows=10
        posy=self.Posy        
        height = self.ClientSize.Height -posy -3

        posx=10

        width=ColumnWidth*2
        self.Dg1Ctrl = DataGridEntry(posx,posy,height,width )
        self.Dg1Ctrl.formatheaders(["关联销售合同名称","对方","记帐方","日期","财务分类","金额","ID"])
        self.Dg1Ctrl.Parent = self
        self.Dg1Ctrl.ToParet = self.onDBClick
        posx=self.Dg1Ctrl.Right +margin

        width=ColumnWidth -margin 

        self.Dg1Ctr2=DataGridEntry(posx,posy,height,width )
        self.Dg1Ctr2.formatheaders(["科目","筛选条件统计结果金额"])
        self.Dg1Ctr2.Parent = self 
        self.Posy=  self.Dg1Ctr2.Bottom
    def show余额统计data(self,DataObj):  
        self.Dg1Ctr2.Clear() 
        if DataObj ==None:
            return 
        keys = sorted (DataObj.__dict__.keys()  )
        keysDisplay  =[]
        for i in keys:
            if i[3:4] == "_":
                keysDisplay += [ i ]
                # print(i)

        cnt=0
        aobj = DataObj
 
        cnt+=1;
        self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=("记账方",aobj.记账方)) 
        cnt+=1;
        self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=("对方",aobj.对方)) 
        cnt+=1;
        self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=("关联销售合同",aobj.关联销售合同名称)) 
        cnt+=1;
        self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=("财务分类",aobj.财务分类)) 
        cnt+=1;
        self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=("起始日期",aobj.startDate)) 
        cnt+=1;
        self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=("截至日期",aobj.endDate))         
        for key in keysDisplay:
            values =( key ,)
            cnt+=1
            cmdstr =  'aobj.{key}'.format(key=key )
            value =eval( cmdstr )
            if key[:1] =="A":
                values += ( str( value  ),  )
            else:
                values += ( "{:0,.6f}".format( value*1.0  )  , )

            self.Dg1Ctr2.addRowdata(rowtitle=str(cnt),datas=values)     

              
    def getConditions(self):
        self.记账方 ="" 
        self.对方 =""
        self.关联销售合同名称 =""
        self.财务分类 =""
        self.startDate=""
        self.endDate=""
        try:
            self.记账方 =  self.ctrl记账方.get().strip()
        except:
            pass

        try:
            self.对方 =   self.ctrl对方.get().strip()
        except:
            pass

        try:
            self.关联销售合同名称 = self.ctrl关联销售合同名称.get() # eval("合同子类Cls."+ self.value关联销售合同名称.get())
        except:
            pass

        try:
            self.财务分类 =  self.ctrl财务分类.get()
        except:
            pass  
        try:
            self.startDate =  self.ctrlstartDate.get()
        except:
            pass 
        try:
            self.endDate =  self.ctrlendDate.get()
        except:
            pass         


    def 刷新筛选结果(self, sender, event):# 更新系统数据库，并刷新显示搜索数据到tree grid
        self.getConditions()
        self.Dg1Ctrl.Clear() 
        # print("刷新筛选结果:{},{},{},{}".format(self.财务分类, self.关联销售合同名称 ,self.记账方,self.对方) ,"将被汇总统计。" )        
        dataObjArrary = 账务处理Lib.getdataDic()
        print(" OK ,显示筛选结果")
        self.dataObjArrary  = dataObjArrary
        self.dataDic  = 账务处理Lib.数据统计CLs.condsatisify(dataObjArrary,self.财务分类,self.记账方,self.对方,self.关联销售合同名称,self.startDate,self.endDate )      

        cnt =0       
        for v in self.dataDic :
                jine = "{:0,.2f}".format( v.get金额()*10000.0 )
                t=v.get财务类型() 
                d= v.get日期()
                values= ( v.关联销售合同名称,v.对方,v.记账方 ,d , t , jine,v.序号+"?"+str(cnt) ) #v.合同大类,
                self.Dg1Ctrl.addRowdata(rowtitle=str(cnt),datas=values) 
                cnt=cnt+1 

    def 刷新余额数据(self, sender, event):  
        dataObj = None
        try:     
            dataObj = self.计算筛选余额统计(); 
        except:
            print("刷新余额数据,cal Error:计算筛选余额统计")
            pass

        # print("||||||||")
        try:
            self.show余额统计data(dataObj)
        except:
            pass
    def 计算筛选余额统计(self):
        self.getConditions()
        dataObjArrary = 账务处理Lib.getdataDic()
        财务分类=""
        print("处理如下条件的筛选结果：财务分类:{},记账方:{},对方:{},关联销售合同:{}.".format(财务分类,self.记账方,self.对方,self.关联销售合同名称 ) )
        dataObj = 账务处理Lib.数据统计CLs.get财务数据( dataObjArrary ,财务分类,self.记账方,self.对方,self.关联销售合同名称,self.startDate,self.endDate )
        print("计算筛选余额统计,获取相关条件的数据成功")
        if self.记账方 ==""  or self.记账方== "所有" :
            dataObj.记账方= "所有"
        else:
            dataObj.记账方= self.记账方 #记账单位Cls.get友好名(self.记账方)  

        if self.对方 =="" or self.对方== "所有":
            dataObj.对方= "所有"
        else:
            dataObj.对方= self.对方#对方单位Cls.get友好名(self.对方)
       
        if self.关联销售合同名称 == "" or  self.关联销售合同名称 == "所有"  :
            dataObj.关联销售合同名称 = "所有"
        else:
            dataObj.关联销售合同名称 = self.关联销售合同名称  

        dataObj.财务分类= "所有"

        # self.startDate,self.endDate 
        if self.startDate == "" or  self.startDate == "所有"  :
            dataObj.startDate = "所有"
        else:
            dataObj.startDate = self.startDate 

        if self.endDate == "" or  self.endDate == "所有"  :
            dataObj.endDate = "所有"
        else:
            dataObj.endDate = self.endDate             



        dataObj.guiyi条件字段()
        return dataObj


    def onDBClick(self,sender,rowtitle):
        print(sender,rowtitle)
        rowobj =sender.getCurRowObj()
        fname = rowobj.Cells[6].Value
        print("onDBClick:", fname )
        
        diaolgtype=fname[:2].upper()
        fangxiang = fname[ 12:13].upper()
        a,idx = fname.split("?")
        idx1 = int(idx)


        # print( "Access： len is: ",len( self.dataDic) ,"Current id is ",idx1 )

        currentObj =self.find符实Obj( a )
        if diaolgtype == "HT"  and fangxiang == "C" :
            dialogForm =dialog采购合同.采购合同_EditDialog(self,"采购合同",  OrgObj =currentObj )
            dialogForm.Show()              
            return
        if diaolgtype == "HT"  and fangxiang == "X" :
            dialogForm = dialog销售合同.销售合同_EditDialog(self,title="销售合同",  OrgObj =currentObj )
            dialogForm.Show()
            return           

        if diaolgtype == "XJ"  and fangxiang == "S" :
            dialogForm =dialog销售收款.销售收款_EditDialog(self,"销售收款",  OrgObj =currentObj )
            # print( "现金流",diaolgtype, fangxiang,idx )
            dialogForm.Show()              
            return            
        if diaolgtype == "XJ"  and fangxiang == "F" :
            dialogForm =dialog采购支付.采购支付_EditDialog(self,"采购支付",  OrgObj =currentObj )
            # print( "现金流",diaolgtype, fangxiang,idx )
            dialogForm.Show()              
            return  

        if diaolgtype == "HT"  and fangxiang == "F" :
            dialogForm =dialog费用合同.费用合同_EditDialog(self,"费用合同",  OrgObj =currentObj )
            # print( "费用合同",diaolgtype, fangxiang,idx ) 
            dialogForm.Show()              
            return   

        if diaolgtype == "FY"  and fangxiang == "F" :
            dialogForm =dialog费用支出.费用支出_EditDialog(self,"费用支出",  OrgObj =currentObj )            
            dialogForm.Show()              
            return  

        if diaolgtype == "FP"  and fangxiang == "J" :
            dialogForm= dialog采购收票.采购收票_EditDialog(self,"采购收票",  OrgObj =currentObj )
            dialogForm.Show()           
            return  

        if diaolgtype == "FP"  and fangxiang == "K" :
            # print( "销售开票 ",diaolgtype, fangxiang,idx )
            dialogForm =dialog销售开票.销售开票_EditDialog(self,"销售开票",  OrgObj =currentObj )
            dialogForm.Show()              #            
            return  

        if diaolgtype == "XJ"  and fangxiang == "B" :
            # print( "报销采购支出 ",diaolgtype, fangxiang,idx )
            dialogForm =dialog报销采购支出.报销采购支出_EditDialog(self,"报销采购支出",  OrgObj =currentObj )
            dialogForm.Show() 
            # dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return 

        if diaolgtype == "XJ"  and fangxiang == "Z" :
            # print( "直接采购支出 ",diaolgtype, fangxiang,idx )
            dialogForm =dialog直接采购支出.直接采购支出_EditDialog(self,"直接采购支出",  OrgObj =currentObj )
            dialogForm.Show() 
            # dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return 

        if diaolgtype == "XJ"  and fangxiang == "D" :
            # print( "代赋税支出 ",diaolgtype, fangxiang,idx )
            dialogForm =dialog代赋税支出.代赋税支出_EditDialog(self,"代付税支出",  OrgObj =currentObj )
            dialogForm.Show() 
            # dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return           # 直接采购支出Cls
        if diaolgtype == "FP"  and fangxiang == "B" :
            # print( "报销采购收票 ",diaolgtype, fangxiang,idx )
            dialogForm =dialog报销收票.报销收票_EditDialog(self,"报销收票",  OrgObj =currentObj )
            dialogForm.Show() 
            # dialog费用支出.费用支出_EditDialog(self.root,"费用支出",  OrgObj =currentObj )            
            return              

    def find符实Obj(self, filename):
        for v in self.dataObjArrary :
            if v.序号 == filename:
                if v.is名附实( ):
                    return v
        print("CAN not  find the Org Log ,ERROR")
    def 计算项目数据(self, event=None):
        import dialog显示项目数据
        d = dialog显示项目数据.显示项目数据Dialog(self,"显示项目财务数据")
        return

    def 计算筛选数据(self):
        print(" 计算筛选数据 ,显示筛选结果")
        import dialog显示筛选统计数据
        dataObj = self.计算筛选余额统计();
        d = dialog显示筛选统计数据.显示筛选统计数据Dialog(self, "显示筛选的财务数据",dataOBJ = dataObj)
        pass


    def SetupMenus(self):
        ms = dialogBase.fontMenuStrip();
        # ms.Font= getFont()
        windowMenu =  dialogBase.ToolStripMenuItem("销售类记录");
        windowNewMenu1 =  dialogBase.fontToolStripMenuItem("新增销售合同" );
        windowNewMenu1.Click += self.say_hi销售合同
        windowNewMenu2 =  dialogBase.fontToolStripMenuItem("新增销售发票" );
        windowNewMenu2.Click += self.say_hi销售发票
        windowNewMenu3 =  dialogBase.fontToolStripMenuItem("新增销售收款" );
        windowNewMenu3.Click += self.say_hi销售收款

        windowMenu.DropDownItems.Add(windowNewMenu1);
        windowMenu.DropDownItems.Add(windowNewMenu2);
        windowMenu.DropDownItems.Add(windowNewMenu3);        
        windowMenu.DropDown.ShowImageMargin = False;
        windowMenu.DropDown.ShowCheckMargin = True;

        ms.Items.Add(windowMenu);


        Menu =  dialogBase.fontToolStripMenuItem("采购类记录");
        Menu1 =  dialogBase.fontToolStripMenuItem("新增采购合同" );
        Menu1.Click += self.say_hi采购合同
        Menu2 =  dialogBase.fontToolStripMenuItem("新增采购收票" );
        Menu2.Click += self.say_hi采购收票
        Menu3 =  dialogBase.fontToolStripMenuItem("新增采购支付" );
        Menu3.Click += self.say_hi采购支付
        Menu4 =  dialogBase.fontToolStripMenuItem("新增直接采购支付" );
        Menu4.Click += self.say_hi直接采购支付
        Menu5 =  dialogBase.fontToolStripMenuItem("新增待付税支付" );
        Menu5.Click += self.say_hi代赋税支付

        # menu2.add_command(label="新增直接采购支付", command=self. )
        # menu2.add_command(label="", command=self. )


        Menu.DropDownItems.Add(Menu1);
        Menu.DropDownItems.Add(Menu2);
        Menu.DropDownItems.Add(Menu3);   
        Menu.DropDownItems.Add(Menu4);   
        Menu.DropDownItems.Add(Menu5);                        
        Menu.DropDown.ShowImageMargin = False;
        Menu.DropDown.ShowCheckMargin = True;

        ms.Items.Add(Menu);

        Menu =  dialogBase.fontToolStripMenuItem("费用类记录");
        Menu1 =  dialogBase.fontToolStripMenuItem("新增费用合同(计划)" );
        Menu1.Click += self.say_hi费用合同
        Menu2 =  dialogBase.fontToolStripMenuItem("新增费用支出" );
        Menu2.Click += self.say_hi费用支出
        Menu3 =  dialogBase.fontToolStripMenuItem("新增报销采购支付" );
        Menu3.Click += self.say_hi报销采购支出        
        # menu3.add_command(label="", command=self. )
        Menu4 =  dialogBase.fontToolStripMenuItem("新增报销收票" );
        Menu4.Click += self.say_hi报销收票     

        Menu.DropDownItems.Add(Menu1);
        Menu.DropDownItems.Add(Menu2);
        Menu.DropDownItems.Add(Menu3); 
        Menu.DropDownItems.Add(Menu4);              
        Menu.DropDown.ShowImageMargin = False;
        Menu.DropDown.ShowCheckMargin = True;
        ms.Items.Add(Menu);

        Menu =  dialogBase.fontToolStripMenuItem("数据分析");
        Menu1 =  dialogBase.fontToolStripMenuItem("数据合并" );
        Menu1.Click += self.say_hi数据合并
        Menu2 =  dialogBase.fontToolStripMenuItem("数据统计并转出到Excel" );
        Menu2.Click += self.say_hi数据XLS
        Menu3 =  dialogBase.fontToolStripMenuItem("导出指定记账方的账务数据" );
        Menu3.Click += self.导出指定记账方的账务数据XLS
        Menu.DropDownItems.Add(Menu1);
        Menu.DropDownItems.Add(Menu2);
        Menu.DropDownItems.Add(Menu3);        
        Menu.DropDown.ShowImageMargin = False;
        Menu.DropDown.ShowCheckMargin = True;
        ms.Items.Add(Menu);



        Menu =  dialogBase.fontToolStripMenuItem("文件");
        Menu1 =  dialogBase.fontToolStripMenuItem("退出" );
        Menu1.Click += self.say_hiExit
        Menu.DropDownItems.Add(Menu1);
        Menu.DropDown.ShowImageMargin = False;
        Menu.DropDown.ShowCheckMargin = True;
        ms.Items.Add(Menu);

        ms.Dock = dialogBase.DockStyle.Top;

        self.MainMenuStrip = ms;  
        self.Controls.Add(ms);  
        self.Posy = self.MainMenuStrip.Bottom 
    def say_hi销售合同(self,sender,event):
        d = dialog销售合同.销售合同_NewDialog(self,title="销售合同")
        d.Show()

    def say_hi销售发票(self,sender,event):
        d = dialog销售开票.销售开票_NewDialog(self,"销售开票")
        d.Show()

    def say_hi销售收款(self,sender,event):
        d = dialog销售收款.销售收款_NewDialog(self,"销售收款")
        d.Show()     

    def say_hi采购合同(self,sender,event):
        d = dialog采购合同.采购合同_NewDialog(self,"采购合同")
        d.Show() 

    def say_hi采购收票(self,sender,event):
        d = dialog采购收票.采购收票_NewDialog(self,"采购收票")
        d.Show() 

    def say_hi采购支付(self,sender,event):
        d = dialog采购支付.采购支付_NewDialog(self,"采购支付")
        d.Show() 
    def say_hi费用合同(self,sender,event):
        d = dialog费用合同.费用合同_NewDialog(self,"费用合同")
        d.Show() 

    def say_hi费用支出(self,sender,event):
        d = dialog费用支出.费用支出_NewDialog(self,"费用支出")
        d.Show() 

    def say_hi分类显示(self,sender,event):
        d = dialog分类显示.分类显示Dialog(self,"分类显示")
        d.Show() 
    def ZD供应商统计(self,sender,event):
        d = dialog供应商统计.供应商统计Dialog(self,"ZD供应商统计")
        d.Show() 
    def say_hi报销收票(self,sender,event):
        d = dialog报销收票.报销收票_NewDialog(self,"报销收票")
        d.Show() 
    def say_hi(self,sender,event):
        d = dialog合同.销售合同Dialog(self,"销售合同")
        d.Show() 
    def say_hi数据合并(self,sender,event):
        # import fileSplit
        # fileSplit.合并()
        # basicDataProc.Save2DataDB()
        pass
    def 导出指定记账方的账务数据XLS(self,sender,event):
        import os
        记账方 =  self.ctrl记账方.get().strip()
        print("导出 '{:}' 记账方的数据到Excel文件中。".format(记账方) )        
        a= 账务处理Lib.getdatasObj()
        if a == None:
            print(" 没有任何数据")
        else:
            if 记账方 == "" or 记账方 == "所有":
                记账方 = ""
                gxlsxFilename = "所有公司"+ "_"+glbcfg.ReportFileName 
            else:
                gxlsxFilename = 记账方 + "_"+glbcfg.ReportFileName 
            print( gxlsxFilename )
            filepath =  os.path.join( glbcfg.reportRootFolder  ,gxlsxFilename )
            a.outXlsx( filepath ,记账方)

    def say_hi数据XLS(self,sender,event):
        print("导出所有记账方的数据到Excel文件中。")
        import os
        a= 账务处理Lib.getdatasObj()
        if a == None:
            print(" 没有任何数据")
        else:
            记账方 = ""
            filepath =  os.path.join( glbcfg.reportRootFolder  ,"所有公司_"+glbcfg.ReportFileName )
            print("导出全部数据到xls:",filepath)            
            a.outXlsx( filepath ,记账方)

    def say_hiExit(self,sender,event):
        self.Close()        

    def say_hi代赋税支付(self,sender,event):
        d = dialog代赋税支出.代赋税支出_NewDialog(self,"代赋税支出")
        d.Show() 
    def say_hi直接采购支付(self,sender,event):
        d = dialog直接采购支出.直接采购支出_NewDialog(self,"直接采购支出")
        d.Show() 
    def say_hi报销采购支出(self,sender,event):
        d = dialog报销采购支出.报销采购支出_NewDialog(self,"报销采购支出")    
        d.Show() 