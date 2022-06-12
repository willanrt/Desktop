import wx

app = wx.App()

frame = wx.Frame(None,-1,title = "用户登录",pos=(100,100),size = (700,400))
panel = wx.Panel(frame)

title = wx.StaticText(panel,label = "请用户输入用户和密码")

user = wx.StaticText(panel,label = "用户名:")
in_user = wx.TextCtrl(panel,style = wx.TE_LEFT)   ###文本居左

password = wx.StaticText(panel,label = "密  码:")
in_password = wx.TextCtrl(panel,style = wx.TE_PASSWORD)

confirm_button = wx.Button(panel,label = "确认")
cancel_button = wx.Button(panel,label = "取消")

################################添加容器
####first 横向
col_box_first = wx.BoxSizer(wx.HORIZONTAL)
col_box_first.Add(user,flag = wx.ALL,proportion = 0 ,border = 5)
col_box_first.Add(in_user,flag = wx.ALL,proportion = 1 ,border = 5)
####second
col_box_second = wx.BoxSizer(wx.HORIZONTAL)
col_box_second.Add(password,flag = wx.ALL,proportion = 0 ,border = 5)
col_box_second.Add(in_password,flag = wx.ALL,proportion = 1 ,border = 5)

####third
col_box_third = wx.BoxSizer(wx.HORIZONTAL)
col_box_third.Add(confirm_button,flag = wx.ALIGN_CENTER,proportion = 0 ,border = 5)
col_box_third.Add(cancel_button,flag = wx.ALIGN_CENTER,proportion = 0 ,border = 5)

##################将横向的box加载到一个竖向的盒子
row_box = wx.BoxSizer(wx.VERTICAL)
row_box.Add(title,proportion = 0 ,flag = wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
row_box.Add(col_box_first , proportion = 0 , flag = wx.EXPAND|wx.LEFT|wx.RIGHT,border = 45)
row_box.Add(col_box_second , proportion = 0 , flag = wx.EXPAND|wx.LEFT|wx.RIGHT,border = 45)
row_box.Add(col_box_third , proportion = 0 , flag = wx.ALIGN_CENTER|wx.TOP,border = 15)

panel.SetSizer(row_box)

frame.Show()
app.MainLoop()







