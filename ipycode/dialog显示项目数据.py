import dialogtest
from tkinter import *
import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 
class 显示项目数据Dialog(dialogtest.Dialog_accountBase):
    def body(self):
        self.row=0
        width=16
        self.tree1= ttk.Treeview(master,show="headings", columns=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13','col14'))
        colwidth =80
        self.tree1.column('col1', width=130, anchor='w')
        self.tree1.column('col2', width=colwidth, anchor='w')
        self.tree1.column('col3', width=colwidth, anchor='w')
        self.tree1.column('col4', width=colwidth, anchor='w')
        self.tree1.column('col5', width=colwidth, anchor='w')
        self.tree1.column('col6', width=colwidth, anchor='w')
        self.tree1.column('col7', width=colwidth, anchor='w')        
        self.tree1.column('col8', width=colwidth, anchor='w')    
        self.tree1.column('col9', width=colwidth, anchor='w') 
        self.tree1.column('col10', width=colwidth, anchor='w') 
        self.tree1.column('col11', width=colwidth, anchor='w') 
        self.tree1.column('col12', width=colwidth, anchor='w') 
        self.tree1.column('col13', width=colwidth, anchor='w') 
        self.tree1.pack(ipady=140)
        self.showdata()

    def showdata(self):  
        import  账务处理Lib     
        dataObjArrary = 账务处理Lib.getdataDic()

        dataobjs   = 账务处理Lib.基本账务统计(dataObjArrary)
        # print( len( dataobjs ))
        for u in dataobjs:
            u.guiyi条件字段()
        keys =sorted (dataobjs[0].__dict__.keys()  )
        keysDisplay  =[]
        for i in keys:
            if i[3:4] == "_":
                keysDisplay += [ i ]
        
        # print( keysDisplay )

        self.tree1.heading('col1' , text= "科目" )       
        col=2
        for aobj in dataobjs:
          self.tree1.heading('col{:}'.format(col ), text= aobj.记账方 +"-"+ aobj.对方 + "-"+aobj.合同大类   )
          col+=1

        str1= ""
        cnt=1
        for key in keysDisplay:
            values =( key ,)
            cnt+=1
            for aobj in dataobjs:
                cmdstr =  'aobj.{key}'.format(key=key )
                value =eval( cmdstr )
                if key[:1] =="A":
                    values += ( str( value  ),  )
                else:
                    values += ( "{:0.2f}".format( value  )  , )
            self.tree1.insert('',cnt,values= values)






         