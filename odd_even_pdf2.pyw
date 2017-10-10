#!/usr/bin/env python3
"""Scans odd folder and creates even numbered pdf's in even folder."""


import os
import shutil
import ctypes
import glob
import PyPDF2
import wx

class WINDOWCLASS(wx.Frame):
    """To do Doc String"""

    def __init__(self, parent, *args, **kwargs):
        """To do Doc String"""
        wx.Frame.__init__(self, parent)

        self.panel = wx.Panel(self)

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        '''self.oddbox = wx.BoxSizer(wx.HORIZONTAL)
        self.oddtext = wx.StaticText(panel, label='Odd File Location')
        self.oddbox.Add(oddtext, flag=wx.RIGHT, border=8)
        self.oddtextbox = wx.TextCtrl(panel)
        self.oddbox.Add(oddtextbox, proportion=1)
        self.vbox.Add(oddbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.oddtextbox.SetValue('C:\\Users\\as$646\\Desktop\\ODD')
        self.oddtextbox.SetValue(oddtextbox.GetValue())
        self.vbox.Add((-1, 10))

        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st2 = wx.StaticText(panel, label='Even File Location')
        self.hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.tc2 = wx.TextCtrl(panel)
        self.hbox2.Add(tc2, proportion=1)
        self.vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
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

        self.hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc5 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.hbox4.Add(self.tc5, proportion=1, flag=wx.EXPAND)
        self.vbox.Add(self.hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)
        self.vbox.Add((-1, 10))
        
        self.buttons = wx.BoxSizer(wx.HORIZONTAL)
        
        self.okbutton = wx.Button(self.panel, label='Process', size=(70, 30))
        self.okbutton.Bind(wx.EVT_BUTTON, self.Convert)
        self.buttons.Add(self.okbutton)
        self.closebutton = wx.Button(self.panel, label='Close', size=(70, 30))
        self.closebutton.Bind(wx.EVT_BUTTON, self.OnClose)
        self.buttons.Add(self.closebutton, flag=wx.LEFT|wx.BOTTOM, border=5)
        
        self.vbox.Add(self.buttons, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        self.panel.SetSizer(self.vbox)

        self.SetSize((250, 500))
        self.SetTitle('Odd to Even pdf Converter')
        self.Centre()
        self.Show(True)

    def OnClose(self, e):
        self.Close(True)

    def Convert(self, e):
        #CHANGE TO WORK WITH PANNEL
        odd_box = wx.TextEntryDialog(None,
                                     'Location of odd files?',
                                     'odd',
                                     'C:\\Users\\as$646\\Desktop\\odd')
        odd_box_input = odd_box.GetValue()
        odd_box.Destroy()

        even_box = wx.TextEntryDialog(None,
                                      'Location to convere even file to?',
                                      'even',
                                      'C:\\Users\\as$646\\Desktop\\even')
        even_box_input = even_box.GetValue()
        even_box.Destroy()

        files = os.listdir
        odd = odd_box_input
        even = even_box_input
        blank = os.path.join('C:\\', 'apps', 'blank.pdf')
        file_list = []

        try:
            for file in files(odd):
                pdf = (odd + '\\' + file)
                pdf_scan = open(pdf, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_scan)#1
                pages = pdf_reader.numPages
                file_list.append(file)

                if pages %2 == 0:
                    shutil.copy(pdf, even)
                    pdfeven = (file + ' - File copied.')
                    print(pdfeven)
                    self.tc4.AppendText(pdfeven + '\n')
                    
                else:
                    pdfodd = (file + ' - Page added.')
                    pdfblank = PyPDF2.PdfFileReader(open(blank, 'rb'))#2
                    pdf_writer = PyPDF2.PdfFileWriter()
                    #file.addBlankPage()

                    for page_num in range(pdf_reader.numPages):
                        pdf_pages = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(pdf_pages)


                    for page_num in range(pdfblank.numPages):
                        pdf_pages = pdfblank.getPage(page_num)
                        pdf_writer.addPage(pdf_pages)

                    pdf_output_file = open(even + '\\' + file, 'wb')
                    pdf_writer.write(pdf_output_file)

                    print(pdfodd)
                    self.tc5.AppendText(pdfodd + '\n')                   

                    pdf_output_file.close()
                pdf_scan.close()
          

        except:
            ctypes.windll.user32.MessageBoxW(0, 'Check. ' + file, "Error", 0)

        nfiles = (len(file_list))

        '''odd_files = glob.glob(odd + '\\*')
        for filename in odd_files:
            os.remove(filename)'''

        ctypes.windll.user32.MessageBoxW(0, 'Converted - ' + str(nfiles) + ' files.', "Done", 0)




if __name__ == '__main__':
    app = wx.App()
    WINDOWCLASS(None)
    app.MainLoop()
