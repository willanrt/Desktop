import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'用户登录',size = (400,300))
        self.panel = wx.Panel(self)
        self.account = wx.TextCtrl(self.panel,pos = (120,20),size = (150,30))
        self.button = wx.Button(self.panel,label="account",pos=(20,20))
        self.button.Bind(wx.EVT_BUTTON,self.login_event)
    def login_event(self,event):
        account = self.account.GetValue()
        if account == "123":
            self.Destroy()         #######事件停止后是否删除顶层窗口
            frame = wx.Frame(None,title="这是一个文本阅读器",pos=(100,200),size=(600,400))
            self.panel = wx.Panel(frame)
            self.title = wx.StaticText(self.panel,label = "这是一个简单的文本阅读器",pos = (160,5))
            self.remind_text = wx.StaticText(self.panel,label = "输入地址：",pos = (5,35))
            self.input_path = wx.TextCtrl(self.panel,pos = (70,30),size= (350,24))
            self.open_Button = wx.Button(self.panel,label = "打开",pos=(450,30))
            self.open_Button.Bind(wx.EVT_BUTTON,self.openfile)
            self.output_text = wx.TextCtrl(self.panel,pos = (70,70),size= (600,350),style = wx.TE_MULTILINE)
            frame.Show()
        else:
            message = "error!"
            wx.MessageBox(message)
    def openfile(self,event):
        try:
            path = self.input_path.GetValue()
            content = []
            for line in open(path,"r",encoding="utf8"):
                content.append(line)
            self.output_text.SetValue("".join(content))
        except:
            message = "path error!"
            wx.MessageBox(message)
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None,-1,)
    frame.Show()
    app.MainLoop()
    
    
    
    
    
    
    
    


