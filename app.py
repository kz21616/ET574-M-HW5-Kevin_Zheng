import wx
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

FEATURE_X = "Wine"
FEATURE_Y = "Quality"

 class Chart(wx.Frame):
    def __init__(self, parent=None, title="Wine Quality"):
        super().__init__(parent, title=title,size=(820,520))
        self.SetMinSize((760,480))
        panel = wx.panel(self)

        open_btn = wx.Button(panel, label="Open Wine Quality")
        font = open_btn.GetFont()
        font.PointSize += 2
        open_btn.SetFont(font)
        open_btn.Bind(wx.EVT_BUTTON, self.on_open)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(open_btn,0,wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.AddStretchSpacer(2)
        panel.SetSizer(sizer)

        self.Centre()
        self.Show()



        