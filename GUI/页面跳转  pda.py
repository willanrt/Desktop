# -*- coding: utf-8 -*-
"""
页面跳转方法处理.
"""

import wx

class TestFrame(wx.Frame): 
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'登陆',size=(470,280),style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX)  
        self.SetBackgroundColour('white')  
        self.button1 = wx.Button(self,-1,u'按钮1',pos = (80,180))  
        self.button1.Bind(wx.EVT_BUTTON,self.OnButtonClick1)  
        self.button2 = wx.Button(self,-1,u'按钮2',pos = (180,180))  
        self.button2.Bind(wx.EVT_BUTTON,self.OnButtonClick2)  #Button1显示组件 
        self.button3 = wx.Button(self,-1,u'按钮3',pos = (280,180))  
        self.button3.Bind(wx.EVT_BUTTON,self.OnButtonClick3)  #Button1显示组件 
        self.text1 = None  
        self.textc1 = None  #Button2显示组件  
        self.text2 = None  
        self.textc2 = None 
    def OnButtonClick1(self,event):  
        if not self.text1:
            self.text1 = wx.StaticText(self,-1,u'用户名',(70,73),(50,-1),wx.ALIGN_CENTER)
            self.text1.SetBackgroundColour('black')#设置背景颜色
            self.text1.SetForegroundColour('white')#设置文本颜色  
        if not self.textc1:
            self.textc1 = wx.TextCtrl(self,pos=(140,70))
        if self.text2:   
            self.text2.Destroy()  
        if self.textc2:   
            self.textc2.Destroy()
    def OnButtonClick2(self,event):  
        if self.text1:   
            self.text1.Destroy() 
        if self.textc1:  
            self.textc1.Destroy()  
        if not self.text2:
            self.text2 = wx.StaticText(self,-1,u'密码',(70,123),(50,-1),wx.ALIGN_CENTER)   
            self.text2.SetBackgroundColour('black')#设置背景颜色   
            self.text2.SetForegroundColour('white')#设置文本颜色  
        if not self.textc2:   
            self.textc2 = wx.TextCtrl(self,pos=(140,120), style=wx.TE_PASSWORD)

#新的窗体转换
    def OnButtonClick3(self,event):
        if __name__ == '__main__':
            app = wx.App()
            frame2 = MyFrame2(parent=None, id=-1)
            frame2.Show()
            app.MainLoop() 
                
class MyFrame2(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent,id, title="我的小软件",pos=(100,100),size=(400, 300))
        #创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label='请输入用户名和密码')
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.title.SetFont(font)    
        
        self.label_user = wx.StaticText(panel,label='用户名')
        self.text_user = wx.TextCtrl(panel,style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel,label='密码')
        self.text_password = wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        
        self.bt_confirm = wx.Button(panel,label='确定')
        #self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,label='取消')
        #self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)

        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)

        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=1, flag=wx.ALIGN_CENTER, border=5)
        
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                        border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)  


if __name__ == "__main__": 
    app = wx.App() 
    frame = TestFrame() 
    frame.Show() 
    app.MainLoop()