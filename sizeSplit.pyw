import PyPDF2
import os
import glob
import wx
'''11"x17" = 792x1224 points'''

class WINDOWCLASS(wx.Frame):
    """To do Doc String"""

    def __init__(self, parent, *args, **kwargs):
        """To do Doc String"""
        wx.Frame.__init__(self, parent)

        self.panel = wx.Panel(self)

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.st1 = wx.StaticText(self.panel, label='Files to split location')
        self.hbox1.Add(self.st1, flag=wx.RIGHT, border=8)
        self.tc1 = wx.TextCtrl(self.panel)
        self.hbox1.Add(self.tc1, proportion=1)
        self.vbox.Add(self.hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.tc1.SetValue('C:\\Apps\\TEST Folder\\splitter test')
        self.location = self.tc1.GetValue()
        self.vbox.Add((-1, 10))

        '''self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st2 = wx.StaticText(self.panel, label='Split location')
        self.hbox2.Add(self.st2, flag=wx.RIGHT, border=8)
        self.tc2 = wx.TextCtrl(self.panel)
        self.hbox2.Add(self.tc2, proportion=1)
        self.vbox.Add(self.hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.tc2.SetValue('C:\\Users\\as$646\\Desktop\\EVEN')
        self.vbox.Add((-1, 10))'''

        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.st3 = wx.StaticText(self.panel, label='Processed')
        self.hbox3.Add(self.st3)
        self.vbox.Add(self.hbox3, flag=wx.CENTER | wx.TOP, border=10)
        self.vbox.Add((-1, 10))

        self.hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc4 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.hbox4.Add(self.tc4, proportion=1, flag=wx.EXPAND)
        self.vbox.Add(self.hbox4, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)
        self.vbox.Add((-1, 10))

        '''self.hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc5 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.hbox4.Add(self.tc5, proportion=1, flag=wx.EXPAND)
        self.vbox.Add(self.hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)
        self.vbox.Add((-1, 10))'''
        
        self.buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.okbutton = wx.Button(self.panel, label='Process', size=(70, 30))
        self.okbutton.Bind(wx.EVT_BUTTON, self.split)
        self.buttons.Add(self.okbutton)
        self.closebutton = wx.Button(self.panel, label='Close', size=(70, 30))
        self.closebutton.Bind(wx.EVT_BUTTON, self.OnClose)
        self.buttons.Add(self.closebutton, flag=wx.LEFT|wx.BOTTOM, border=5)
        self.vbox.Add(self.buttons, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        self.panel.SetSizer(self.vbox)

        self.SetSize((250, 500))
        self.SetTitle('PDF size splitter')
        self.Centre()
        self.Show(True)


    def OnClose(self, e):
        self.Close(True)

    def split(self, e):
        self.location = self.tc1.GetValue()
        #print(self.location)
        location = self.location
        try:
            os.makedirs(self.location + '\\Large Format')
            os.makedirs(self.location + '\\Small Format')
        except:
            pass
        
        lf = []
        sf = []
        g = glob.glob(location + '\\*pdf')

        for pdf in g:
            #print(pdf)
            pdfread = PyPDF2.PdfFileReader(open(pdf, 'rb'))

            for pages in range(0, pdfread.numPages):
                pagesize = pdfread.getPage(pages).mediaBox
                psize1 = pagesize[2]/72
                psize2 = pagesize[3]/72
                #print(psize1, psize2)

                if pagesize[2] > 792 or pagesize[3] > 1224:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    lf.append(pages)
                    

                    for page in lf:
                        pdf_pages = pdfread.getPage(page)
                        pdf_writer.addPage(pdf_pages)
                    
                    pdf_output_file = open(self.location + '\\large format\\' + os.path.basename(pdf), 'wb')
                    pdf_writer.write(pdf_output_file)
                   

                    pdf_output_file.close()
                    
                    
                else:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    sf.append(pages)
                    

                    for page in sf:
                        pdf_pages = pdfread.getPage(page)
                        pdf_writer.addPage(pdf_pages)
                    
                    pdf_output_file = open(location + '\\small format\\' + os.path.basename(pdf), 'wb')
                    pdf_writer.write(pdf_output_file)
                   

                    pdf_output_file.close()
                self.tc4.AppendText(os.path.basename(pdf))
                self.tc4.AppendText(' - ' + str(psize1) + 'X' + str(psize2) + '\n')
            
            del lf[:]
            del sf[:]

if __name__ == '__main__':
    app = wx.App()
    WINDOWCLASS(None)
    app.MainLoop()
