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


    def on_open(self, _evt):
        with wx.FileDialog(
            self,
            "Open Wine Quality",
            wildcard="CSV Files(*.csv|*.csv",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dlg:
            if dlg.ShowModal() != wx.ID_ok:
                return
            path = dlg.GetPath()

        try:
            df = pd.read_csv(path)
            want = ["Wine", "Wine Quality"]

            df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
            if df.shape[1] ==5 and not set(want).issubset(df.columns):
                df.columns = want

            for c in ["Wine", "Wine Quality"]:
                if c not in df.columns:
                    raise ValueError("CSV must contain 2 features.")
                
            # plt.figure(figsize=(7.5,5.0))
            # for sp, sub in df.groupby("")


        except Exception as e:
            wx.MessageBox(f"Could not load/plot file: \n{e}", "Error", wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = wx.APP(False)
    Chart()
    app.MainLoop()