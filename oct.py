
from tkinter import *
import winreg
import configparser
from tkinter import messagebox


#读取ini配置文件
config = configparser.ConfigParser()
a = config.read('DATABASE.INI')
sections1 = config.sections()[0]
sections2 = config.sections()[1]
xmlPath = config[sections2]['DatabaseXmlPath']
dbinfo = list()
#将读取的section1的内容放入列表里
for db in config[sections1]:
	db = config[sections1][db]
	dbinfo.append(tuple(db.split(';')))
	

#修改注册表（运行程序需要管理员权限）
def modifyRefXml(db):
	dbname, path = db
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
						 r'SOFTWARE\TOPCON\3DOCT-2000\1.00\DATABASE',
						 access=winreg.KEY_SET_VALUE					 
					)
	winreg.SetValueEx(key,
					'DBName',
					0,
					winreg.REG_SZ,
					dbname 
				)
	winreg.SetValueEx(key,
					'MeasurementDataPath',
					0,
					winreg.REG_SZ,
					path
				)
	winreg.CloseKey(key)
	key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
						 r'SOFTWARE\TOPCON\3DOCT-2000\1.00\DATABASE\MainSystem1',
						 access=winreg.KEY_SET_VALUE					 
					)
	winreg.SetValueEx(key,
					'DBName',
					0,
					winreg.REG_SZ,
					dbname 
				)
	winreg.SetValueEx(key,
					'MeasurementDataPath',
					0,
					winreg.REG_SZ,
					path 
				)
	winreg.CloseKey(key)
	#修改xml文件
	with open(xmlPath, 'r+') as f:
		flist = f.readlines()
		r = flist[1]
		flist[1] = flist[1].replace(r.split(';')[1], 'Initial Catalog='+dbname)
		#seek(offset[, whence])
		#offset：开始的偏移量
		#whence:可选，默认为0，0代表文件开头开始，1代表当前位置开始，2代表文件末尾开始
		f.seek(0, 0)
		#truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符
		# 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除
		f.truncate(0)
		f.writelines(flist)


#创建按钮
def fun(toolbar, db, index):
	b = Button(toolbar, text=db[0], width=15, command=lambda:modifyRefXml(db))
	b.pack(side=TOP, padx=10, pady=10)	


root = Tk()
root.title('OCT')
root.geometry('500x500+100+100')

#create a toolbar
toolbar = Frame(root, bg='light sea green')
#按钮个数为dbinfo的元素个数
for db in enumerate(dbinfo):
	index = db[0]
	db = db[1]
	#创建未知的控件个数这里要通过函数去创建控件 Pay attention!!!
	fun(toolbar, db, index)

toolbar.pack(side=TOP, fill=X)
root.mainloop()

