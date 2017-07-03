__author__ = 'zyl'

from tkinter import*
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
import os
import chardet


filename = ''
gfind = ''


#Help
def aboutNotepad():
	messagebox.showinfo('About Notepad', '一页书')

def viewHelp():
	messagebox.showinfo('About Notepad', '百世经纶')

#File defaultextension='.txt', 
def openFile(enent=None):
	global filename
	filename = filedialog.askopenfilename(filetypes=(("All files", "*.txt"),), title='open')
	root.title(os.path.basename(filename)+' - Notepad')
	if filename:
	# 	fs = open(filename, 'rb')
	# 	fb= fs.read() #fb <class 'bytes'>
	# 	encoding = chardet.detect(fb).get('encoding', 'utf8') #detect type of code and get(default: 'utf8')
	# 	#print(chardet.detect(fb), 'encoding:', encoding)
	# 	text.delete(1.0, END)
	# 	text.insert(END, str(fb, encoding=encoding)) #<class 'bytes'> => <class 'str'>
	# 	fs.close()
		with open(filename, 'rb') as fs:
			fb = fs.read()
			encoding = chardet.detect(fb).get('encoding', 'utf8')or'utf8'
			text.delete(1.0, END)
			text.insert(END, str(fb, encoding=encoding))


#new file
def newFile(enent=None):
	global filename
	filename = ''
	root.title('untitled - Notepad')
	#text.delete(1.0, END)
	text.tag_add('sel', 1.0, 1.2)


#save as File
def saveAsFile(enent=None):
	global filename
	filename = filedialog.asksaveasfilename(filetypes=(("All files", "*.txt"),), initialfile = 'untitled.txt', defaultextension='.txt',  title='save as')
	print(filename)
	if filename:
		with open(filename, 'wb') as fs:
			contents = text.get(1.0, END)
			fs.truncate()
			fs.write(contents.encode('utf8'))
		root.title(filename+" - Notepad")

#Save File
def saveFile(event=None):
	global filename

	if os.path.exists(filename):
		print('filename: ', filename)
		contents = text.get(1.0, END)
		#print(type(contents))
		with open(filename, 'wb') as fs:
			fs.truncate()  
			fs.write(contents.encode('utf8')) #new document encode:'utf8'
	else:
		saveAsFile()


#edit
def undo():
	text.event_generate('<<Undo>>')


def cut():
	text.event_generate('<<Cut>>')


def copy():
	text.event_generate('<<Copy>>')


def paste():
	text.event_generate('<<Paste>>')


def selectAll():
	text.event_generate('<<SelectAll>>')
	# text.tag_add('sel', 1.0, END)
	# text.see(INSERT)
	# text.focus()


def delete():
	text.event_generate('<<Clear>>')


def find(event=None):
	def findAll():
		global gfind
		start = 1.0
		gfind = entry1.get()
		print('current pos： ',start)
		while 1:
			pos = text.search(find, start, stopindex=END)
			if not pos:
				break
			print('start: ', start)
			print('pos: ', pos)
			where1 = str(pos).split('.')
			sele_end_col = str(int(where1[1])+len(entry1.get()))
			sele = where1[0] + '.' + sele_end_col
			text.tag_add('sel', pos, sele)
			text.mark_set(INSERT, sele)
			start = pos + "+1c"
		search.destroy()


	def findword():
		global gfind
		start = text.index('insert')
		gfind = entry1.get()
		print('current pos： ',start)
		pos = text.search(entry1.get(), start, stopindex=END)
		if pos:
			print('pos: ', pos)
			where1 = str(pos).split('.')
			sele_end_col = str(int(where1[1])+len(entry1.get()))
			sele = where1[0] + '.' + sele_end_col
			text.tag_add('sel', pos, sele)
			text.mark_set(INSERT, sele)
		search.destroy()

	search = Toplevel(root)
	search.geometry('250x50+200+200')
	label1 = Label(search, text='Find')
	label1.grid(row=0, column=0, padx=5)
	entry1 = Entry(search, width=20)
	entry1.grid(row=0, column=1, padx=5)
	button1 = Button(search, text='find', command=findword)
	button1.grid(row=0, column=2)
	button2 = Button(search, text='find all', command=findAll)
	button2.grid(row=1, column=2)
	label2 = Label(search, text='find result')
	label2.grid(row=1, column=1, padx=5)
	#search.destroy()


def findNext(event=None):
	global gfind
	start = text.index('insert')
	print('into findnext start: ', start, 'find: ', gfind)
	if gfind:
		print('find is true')
		pos = text.search(gfind, start, stopindex=END)
		if pos:
			where1 = str(pos).split('.')
			sele_end_col = str(int(where1[1])+len(gfind))
			sele = where1[0] + '.' + sele_end_col
			print('pos:', pos, 'sele', sele)
			text.tag_add('sel', pos, sele)
			#text.tag_config(entry1.get(),foreground='blue', underline=1)
			text.mark_set(INSERT, sele)
			#search.destroy()
		else: 
			messagebox.showinfo('Info', 'find end')
		#label2.config(text='Can not find %s'%entry1.get())
	# def findAll():
	# 	start = 1.0
	# 	print('current pos： ',start)
	# 	while 1:
	# 		pos = text.search(entry1.get(), start, stopindex=END)
	# 		if not pos:
	# 			break
	# 		print('start: ', start)
	# 		print('pos: ', pos)
	# 		where1 = str(pos).split('.')
	# 		sele_end_col = str(int(where1[1])+len(entry1.get()))
	# 		sele = where1[0] + '.' + sele_end_col
	# 		text.tag_add('sel', pos, sele)
	# 		text.mark_set(INSERT, sele)
	# 		start = pos + "+1c"
	# 	search.destroy()

	# search = Toplevel(root)
	# search.geometry('250x35+200+200')
	# label1 = Label(search, text='Find')
	# label1.grid(row=0, column=0, padx=5)
	# entry1 = Entry(search, width=20)
	# entry1.grid(row=0, column=1, padx=5)
	# button1 = Button(search, text='find all', command=findAll)
	# button1.grid(row=0, column=2)
	# start = 1.0
	# while 1:
	# 	pos = text.search('1', start, stopindex=END)
	# 	if not pos:
	# 		break
	# 	print(pos)
	# 	start = pos + "+1c"
	# 	print('start: ', start)
	# text.focus

def new():
	pass


root = Tk()
root.title('Notepad')
root.geometry('500x500+100+100')

#definition font
ft = font.Font(family = 'Fixdsys',size = 20,weight = 'bold')
font.families()

#create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', accelerator='Ctrl+N', command=newFile)
filemenu.bind_all("<Control-n>", newFile)
filemenu.add_command(label='Open', accelerator='Ctrl+O', command=openFile)
filemenu.bind_all("<Control-o>", openFile)
filemenu.add_command(label='Save', accelerator='Ctrl+S', command=saveFile)
filemenu.bind_all("<Control-s>", saveFile)
filemenu.add_command(label='Save as', accelerator='Ctrl+Shift+S', command=saveAsFile)
filemenu.add_command(label='Exit', command=new)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo', accelerator='Ctrl+Z', command=undo)
editmenu.add_command(label='Cut', accelerator='Ctrl+X', command=cut)
editmenu.add_command(label='Copy', accelerator='Ctrl+C', command=copy)
editmenu.add_command(label='Paste', accelerator='Ctrl+P', command=paste)
editmenu.add_command(label='Delete', accelerator='Ctrl+Delete', command=delete)
editmenu.add_command(label='Select All', accelerator='Ctrl+A', command=selectAll)
editmenu.add_separator()
editmenu.add_command(label='Find..,', accelerator='Ctrl+F', command=find)
editmenu.bind_all('<Control-f>', find)
editmenu.add_command(label='Find Next', accelerator='F3', command=findNext)
editmenu.bind_all('<F3>', findNext)

formatmenu = Menu(menu)
menu.add_cascade(label='Font', menu=formatmenu)
formatmenu.add_command(label='Font', command=new)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help', command=viewHelp)
helpmenu.add_command(label='About Notepad', command=aboutNotepad)

#create a toolbar
toolbar = Frame(root, bg='light sea green')
b = Button(toolbar, text='new', width=6, command=newFile)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text='open', width=6, command=openFile)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#create a status bars
class StatusBar(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.label = Label(master, text='ln20', bg='antique white', relief=RAISED, anchor=W)
		self.label.pack(fill=X)

	def set(self, format, *args):
		self.label.config(text=format % args)
		self.label.update_idletasks()

	def clear(self):
		self.label.config(text='')

status = StatusBar(root)
status.label.pack(side=BOTTOM, fill=X)

lnstatus = StatusBar(root)
lnstatus.label.pack(side=LEFT, fill=Y)
lnstatus.label.config(text='12')

#create a textedit
text = Text(root, undo=True)
text.pack(expand=YES, fill=BOTH)
text.config(font=ft)


#create a scrollbar
scrollbar = Scrollbar(text)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)


root.mainloop()