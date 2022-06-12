
import wx
app = wx.App()
frame = wx.Frame(None,title = "这是一个简单的文本阅读器",
        pos = (100,200),size = (600,400))
panel = wx.Panel(frame)
remind_path = wx.StaticText(panel,label = "输入地址:",pos = (5,35))
get_path = wx.TextCtrl(panel,pos = (70,30),size = (350,24))
output_text = wx.TextCtrl(panel,pos = (70,70),
              size = (600,350),style = wx.TE_MULTILINE)


def openfile(event):
    path = get_path.GetValue()
    result = []
    for line in open(path,"r",encoding="utf8"):
        result.append(line)
    content = "".join(result)
    output_text.SetValue(content)

button = wx.Button(panel,label="打开",pos = (450,30))
button.Bind(wx.EVT_BUTTON,openfile)

frame.Show()
app.MainLoop()
