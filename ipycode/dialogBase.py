#-*- coding: UTF8
import clr

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import os
import datetime
import re

from  名称定义 import *
from System.Windows.Forms import Form,Button,Screen
from System.Windows.Forms import DataGridView
from System.Windows.Forms import DataGridViewContentAlignment
from System.Windows.Forms import Application
from System.Windows.Forms import Control,FormWindowState
from System.Windows.Forms import Clipboard,FormStartPosition
from System.Windows.Forms import DataFormats,MenuStrip,ToolStripMenuItem,ToolStripMenuItem
from System.Windows.Forms import DataObject,Panel,DockStyle

from System.Drawing import Point
from System.Drawing import Size
from System.Drawing import Font
from System.Drawing import FontStyle
from System.Drawing import Color
import datetime
import random
import imp
from  账务处理Lib  import *
import tips
from BasicWidgets import *
def getbaseFilename(prefix,direction):
        today1 = datetime.date.today()
        rndID =random.randint(1,999999)
        filename= "{}-{:04d}{:02d}{:02d}-{}{:06d}.{}".format(\
          prefix,today1.year,today1.month,today1.day,direction,rndID,"py1")
        print(filename)
        return filename
def getNewFileName(prefix,direction):
    dataDic = getdataDic() #账务处理Lib.getdataDic() 
    fn=""
    isExist = False
    while( True ):
        isExist = False        
        fn = getbaseFilename(prefix,direction)
        for v in dataDic :
            # print( v.序号)
            if v.序号 == fn :
                isExist =True
                continue;
        if isExist == False:
            break

    return fn
   
class DialogMain( Form ):
    def __init__(self,title=None,OrgObj=None):
        self.AutoScroll =True
        self.Font =getFont()
        screenSize =Screen.GetWorkingArea(self)
        maxsize1 =Size(screenSize.Width /3*2 , screenSize.Height  )
        self.Text =title
        self._Height=60
        self.OrgObj = OrgObj
        self.Posy=0
        self.Size = Size(maxsize1.Width,maxsize1.Height)
        self.WindowState = FormWindowState.Normal
        self.result = None
        self.create_menu()        
        self.body()
        self.buttonbox()
        self.bodyShowTree()        
        self.init(OrgObj )


    def create_menu(self):
        pass
    def bodyShowTree(self):
        pass
    def body(self):
        pass
    def init( self,OrgObj ):
        pass
    def buttonbox(self):
        splitPadsize =20
        buttonHeight =40 
        buttonwidth =200

        Width_pad = self.ClientSize.Width - splitPadsize*2 -buttonwidth*3  
        Width_pad /=2
        posx=  Width_pad

        w = Button()
        w.Text = "刷新余额数据"
        w.Location = Point(posx, self.Posy)
        w.Height = buttonHeight
        w.Width = buttonwidth
        w.ForeColor = Color.Blue
        w.Click += self.刷新余额数据
        w.Parent =self

        posx += buttonwidth+splitPadsize;     
        w1 = Button()
        w1.Text = "刷新筛选结果" 
        w1.Location = Point(posx, self.Posy)
        w1.Height = buttonHeight
        w1.Width = buttonwidth
        w1.ForeColor = Color.Blue
        w1.Click += self.刷新筛选结果
        w1.Parent =self

        posx += buttonwidth+splitPadsize   ;     

        w2 = Button()
        w2.Text = "退出系统"
        w2.Location = Point(posx, self.Posy)
        w2.Height = buttonHeight
        w2.Width = buttonwidth
        w2.ForeColor = Color.Blue
        w2.Click += self.退出系统
        w2.Parent =self
        
        self.Posy += buttonHeight
    def 计算项目数据(self, event=None):
        pass
    
    def 刷新筛选结果(self, sender, event):
        print("刷新筛选结果")
        if not self.validate():
            return
    def 退出系统(self, sender, event):
        print("exit out ")
        self.Close()
        # self.destroy()
    def 刷新余额数据(self, sender, event):
        print( "刷新余额数据 ")
        pass
    def validate(self):
        return 1 # override
    def apply(self):
        pass # override



class Dialog(Form):
    def __init__(self,parent, title = None,OrgObj=None):
        self.AutoScroll =True
        self.Font =getFont()
        maxsize1 =Screen.GetWorkingArea(self)
        size1 = Size(maxsize1.Width/3,maxsize1.Height-10 )
        self.Size = Size(size1.Width,size1.Height)
        self.WindowState = FormWindowState.Normal
        self.width1=self.ClientSize.Width-10
        self.OrgObj = OrgObj

        self.Text = title
        self.Posy= 0

        if title:
            self.Text = title

        self.result = None

        self.body()
        self.buttonbox()

        self.init(OrgObj )
    def body(self):
        pass
    def init( self,OrgObj ):
        pass
    def buttonbox(self):
        posx= 10
        buttonHeight =40 
        buttonwidth =200
        w = Button()
        w.Text = "保存"
        w.Location = Point(posx, self.Posy)
        w.Size= Size(buttonwidth,buttonHeight )
        w.ForeColor = Color.Blue
        w.Click += self.ok
        w.Parent =self

        posx = w.Right+20;        
        w1 = Button()
        w1.Text = "退出" 
        w1.Location = Point(posx, self.Posy)
        w1.Size= Size(buttonwidth,buttonHeight )        
        w1.ForeColor = Color.Blue
        w1.Click += self.cancel
        w1.Parent =self
        self.Posy = w1.Bottom
    def ok(self, sender ,event=None):
        if not self.validate():
            ret= MessageBox.Show ('数据输入不全，或者格式不正确，请完善后再行保存。', '输入数据存在问题', MessageBoxButtons.RetryCancel);
            if DialogResult.Retry  != ret :
                self.Close()
        else:
            self.apply()

    def cancel(self,sender , event=None):
        self.Close()

    def validate(self):
        return 1 # override
    def apply(self):
        pass # override
