import os
import wx
import pandas as pd 
import matplotlib.pyplot as plt 

FEATURE_X = "alcohol"
FEATURE_Y = "quality"
DATA_FILE = "Winequality.csv"

class Chart(wx.Frame):
    def __init__(self, parent=None, title="Wine Quality"):
        super().__init__(parent, title=title,size=(820,520))
        self.SetMinSize((760,480))
        panel = wx.Panel(self)

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
     
        try:
            data_path = os.path.join(os.path.dirname(__file__), DATA_FILE)
            data = pd.read_csv(data_path, sep=';', quotechar='"')

            if FEATURE_X not in data.columns or FEATURE_Y not in data.columns:
                raise ValueError(
                    f"CSV must contain columns '{FEATURE_X}' and '{FEATURE_Y}'. "
                    f"Found: {list(data.columns)}"
                )

            x_values = data[FEATURE_X]
            y_values = data[FEATURE_Y]

            plt.figure(figsize=(8, 5))
            plt.scatter(x_values, y_values, alpha=0.6)
            plt.title("Wine Alcohol vs Quality")
            plt.xlabel(FEATURE_X.capitalize())
            plt.ylabel(FEATURE_Y.capitalize())
            plt.tight_layout()
            plt.show()

        except Exception as e:
            wx.MessageBox(f"Could not load/plot file: \n{e}", "Error", wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = wx.App(False)
    Chart()
    app.MainLoop()