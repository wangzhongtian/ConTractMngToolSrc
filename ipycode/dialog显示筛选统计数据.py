import dialogtest
from tkinter import *
# import tkinter.ttk as ttk1
from  dialogBase import *
import  dialogBase 
import dialog显示项目数据

class 显示筛选统计数据Dialog( dialog显示项目数据.显示项目数据Dialog ):
    def __init__(self, master, title, dataOBJ= None ):
        self.DataObj =dataOBJ
        dialog显示项目数据.显示项目数据Dialog.__init__(self, master,  title )

    def body(self):
        self.tree1= ttk.Treeview(master,show="headings", columns=('col1','col2'))
        # colwidth =180
        self.showdata()
        self.tree1.column('col1', width=130, anchor='w')
        self.tree1.column('col2', width=190, anchor='w')
        self.tree1.pack(ipady=150)
        # print("+++++++++++++++++++++++++")

    def showdata(self):  
        # self.DataObj.cal() 
        keys =sorted (self.DataObj.__dict__.keys()  )
        keysDisplay  =[]
        # print(keys )
        for i in keys:
            if i[3:4] == "_":
                keysDisplay += [ i ]

        self.tree1.heading('col1' , text= "科目" )      
        col=2
        self.tree1.heading('col{:}'.format(col ), text= "筛选条件统计结果金额"   )

        cnt=1
        aobj = self.DataObj
        for key in keysDisplay:
            values =( key ,)
            cnt+=1
            cmdstr =  'aobj.{key}'.format(key=key )
            value =eval( cmdstr )
            if key[:1] =="A":
                values += ( str( value  ),  )
            else:
                values += ( "{:0.2f}".format( value  )  , )
            self.tree1.insert('',cnt,values= values)





         