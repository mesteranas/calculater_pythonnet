import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import *
from System.Drawing import Point
class mainScreen(Form):
    def __init__(self):
        Form.__init__(self)
        self.Text="calculator"
        self.label1=Label()
        self.label1.Text="type hear"
        self.Controls.Add(self.label1)
        self.textBox=TextBox()
        self.Controls.Add(self.textBox)
        self.calculate=Button()
        self.calculate.Text="calculate"
        self.calculate.Click+=self.onCalculate
        self.Controls.Add(self.calculate)
    def onCalculate(self,obj,evt):
        try:
            result=eval(self.textBox.Text)
        except:
            result="Error"
        MessageBox.Show(str(result),"result")
frm=mainScreen()
Application.Run(frm)