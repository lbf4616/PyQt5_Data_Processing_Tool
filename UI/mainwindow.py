# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Data_tools.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):

        self.resize(1000, 800)
        self.desktopWidth = QApplication.desktop().width()  # 获取当前桌面的宽
        self.desktopHeight = QApplication.desktop().height()  # 获取当前桌面的高

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.init_left()  # 初始化左侧空间
        self.init_right()  # 初始化右侧空间

        # 将初始化完成的左侧、右侧空间加入整体空间的网格布局
        self.main_layout.addWidget(self.left_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.right_widget1, 0, 1, 1, 6)

        #self.main_layout.addWidget(self.right_widget2, 0, 1, 1, 6)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # MainWindow.setObjectName("MainWindow")
        
        # MainWindow.resize(800, 600)
        # self.centralWidget = QtWidgets.QWidget(MainWindow)
        # self.centralWidget.setObjectName("centralWidget")
        # self.retranslateUi(MainWindow)
        # self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        # self.pushButton.setGeometry(QtCore.QRect(120, 140, 130, 130))
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton.setText("Delet JPG with\n JSON")
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(335, 140, 130, 130))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.setText("Delet JPG with \n label")

        # self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(550, 140, 130, 130))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.setText("Comming \n soon...")
        # MainWindow.setCentralWidget(self.centralWidget)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # self.pushButton.clicked.connect(self.on_pushButton1_clicked)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data_Tools"))
    
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        print(int(newLeft),int(newTop))
        self.move(int(newLeft),int(newTop))

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')

    windowList = []

    def init_left(self):
        '''
        初始化左侧布局
        '''
        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')  # 左侧部件对象命名
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.left_widget.setLayout(self.left_layout)  # 将左侧部件设置为网格布局
      	# 接下来添加按钮控件等...，细节略  

    def init_right(self):
        '''
        初始化右侧布局
        '''
        self.right_widget1 = QWidget()  # 创建右侧界面1
        self.right_layout1 = QGridLayout()  # 创建网格布局对象1
        self.right_widget1.setLayout(self.right_layout1)  # 设置右侧界面1的布局为网格布局
        self.Button1 = QPushButton() # 加一个用来界面跳转的button1
        self.Button1.setText("进入界面2")
        self.right_layout1.addWidget(self.Button1)
        
        self.right_widget2 = QWidget()  # 创建右侧界面2
        self.right_layout2 = QGridLayout()  # 创建网格布局对象2
        self.right_widget2.setLayout(self.right_layout2)  # 设置右侧界面2的布局为网格布局
        self.Button2 = QPushButton() # 加一个用来界面跳转的button2
        self.Button2.setText("进入界面1")
        self.right_layout2.addWidget(self.Button2)
        
        # 把切换界面的button和两个跳转函数绑定
        self.Button1.clicked.connect(self.clicked_1)
        self.Button2.clicked.connect(self.clicked_2)


    def clicked_1(self):
        self.right_widget1.hide() # 隐藏界面1
        self.right_widget2.show() # 显示界面2

    def clicked_2(self):
        self.right_widget2.hide() # 隐藏界面2
        self.right_widget1.show() # 显示界面1




class SecondWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Data_Tools")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 140, 130, 130))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Delet JPG with\n JSON")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 140, 130, 130))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Comming \n soon...")
        MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.back_MainWindow)

        # 窗口最大化
        # self.showMaximized()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        print(int(newLeft),int(newTop))
        self.move(int(newLeft),int(newTop))

    ###### 重写关闭事件，回到第一界面
    windowList = []
    def back_MainWindow(self):
        the_window = Ui_MainWindow()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()
        the_window.center()
        
        # event.accept()