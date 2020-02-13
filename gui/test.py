#!/usr/bin/env python3
# Copyright (c) 2019 Connor Tozer (JavaIsNotMagic), Caleb Horton (scoutchorton)

#
#	Imports
#
import os
import platform
import pip
import tkinter as tk



#
#	Variables
#
cwd = os.path.dirname(os.path.realpath(__file__))	#Gets the folder the file is in: https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python



#
#	tkHTML installer
#
#Special instructions need to be made for Linux. See https://wxpython.org/pages/downloads/index.html for more detail about the Linux command.
print('Checking for wxPython package...')
if pip.main(['show','-q','wxPython']):	#If pip gives an error/non-zero exit code:
	print('Installing wxPython via pip...')
	if platform.system() == 'Linux':	#Checks if on Linux
		pip.main(['install','-U','-f',f'https://extras.wxpython.org/wxPython4/extras/linux/gtk3/{platform.linux_distribution()[0].lower()}-{platform.linux_distribution()[1]}','wxPython'])	#Specific installation for Linux from https://wxpython.org/pages/downloads/index.html
	else:	#Non-Linux
		pip.main(['install', 'wxPython'])	#Install wxPython regularly
	print('Installed!')
else:
	print('Already installed.')
import wx, wx.html2



#
#	wx code
#
app = wx.App()

#frame = wx.Frame(None, title='Python Minecraft Launcher')
#frame.Show()

#https://stackoverflow.com/questions/10358998/wxpython-webview-example
class HTMLRender(wx.Dialog):
	def __init__(self, *args, **kwargs):
		wx.Dialog.__init__(self, *args, **kwargs)
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.browser = wx.html2.WebView.New(self)
		sizer.Add(self.browser, 1, wx.EXPAND, 10)
		self.SetSizer(sizer)
		self.SetSize((700, 700))
		self.Bind(wx.EVT_CLOSE, self.OnQuit)
	def OnQuit(self, event):
		self.Destroy()
		return wx.ID_CANCEL

launcher = HTMLRender(None, -1)
print(f'file://{cwd}/static/index.html')
launcher.browser.LoadURL(f'file://{cwd}/static/index.html')
launcher.Show()
app.MainLoop()

#SIDE NOTE:
#Eventually implement a WebSocket server from the main Python script, and connect using JavaScript to communicate events and transmit data. Alternatively implement an HTTP server and use GET/POST. wxPython doesn't seem to have event listeners between JavaScript and Python. If it does, I'm too lazy to learn the code for it. I will just take the more complex route and make a WebSocket server and communicate that way.