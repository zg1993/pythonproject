# pythonproject

studying...

note:一个简单的文本编辑器

oct.py:3D-OCT项目的脚本


pyinstaller的使用：

1.pip install pyinstaller 安装

2.pyinstaller -F -w -i d:\tmp\main.ico main.py

参数说明：

-F 表示生成单个可执行文件

-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！

-p 表示你自己自定义需要加载的类路径，一般情况下用不到

-i 表示可执行文件的图标


出现链接问题：原因是因为pyinstaller版本和python的版本不兼容

解决：网上下载pyinstaller的包

