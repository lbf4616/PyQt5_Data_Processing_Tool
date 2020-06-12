from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Mainwindow(QWidget):
    def __init__(self):
        super(Mainwindow, self).__init__()
        #设置窗口初始位置和大小
        self.setGeometry(0,0,800,600)
        self.center()
        self.setWindowTitle('Data_Processing_Tools')
        # self.status = self.statusBar()
        # self.status.showMessage('我是状态栏', 5000)
        # icon = QIcon()
        # icon.addPixmap(QPixmap("icon.png"), QIcon.Normal, QIcon.Off)
        # self.setWindowIcon(icon)

        #创建列表窗口，添加条目
        # self.leftlist = QListWidget()
        # self.leftlist.insertItem(0,'Delet JPG with JSON')
        # self.leftlist.insertItem(1,'Delet JPG with label')
        # self.leftlist.insertItem(2,'Comming soon...')

        #创建三个小控件
        self.stack0 = QWidget()
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        
        #在QStackedWidget对象中填充了三个子控件
        self.stack = QStackedWidget(self)

        self.stack.addWidget(self.stack0)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        #水平布局，添加部件到布局中
        HBox = QHBoxLayout()
        # HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)
        self.display(0)
        # self.leftlist.currentRowChanged.connect(self.display)
        self.stack0UI()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

    def stack0UI(self):
        pushButton = QPushButton(self.stack0)
        pushButton2 = QPushButton(self.stack0)
        pushButton3 = QPushButton(self.stack0)
        pushButton.setText('Delet JPG with \n JSON')
        pushButton2.setText('Delet JPG with \n label')
        pushButton3.setText('Comming soon...')
        pushButton.setGeometry(QRect(120, 140, 130, 130))
        pushButton2.setGeometry(QRect(335, 140, 130, 130))
        pushButton3.setGeometry(QRect(550, 140, 130, 130))
        pushButton.setStyleSheet("        background-color: rgb(37, 121, 255);\n"
"        color: white;\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;")
        pushButton2.setStyleSheet("        background-color: rgb(37, 121, 255);\n"
"        color: white;\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;")
        pushButton3.setStyleSheet("        background-color: rgb(37, 121, 255);\n"
"        color: white;\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;")
        pushButton.clicked.connect(lambda:self.display(1))
        pushButton2.clicked.connect(lambda:self.display(2))
        pushButton3.clicked.connect(lambda:self.display(3))
        # self.stack0.setLayout(layout)

    # Delet JPG with JSON
    def stack1UI(self):
        pushButton = QPushButton(self.stack1)
        pushButton2 = QPushButton(self.stack1)
        pushButton.setText('OK')
        pushButton2.setText('Menu')
        pushButton2.setStyleSheet("        background-color: rgb(37, 121, 255);\n"
"        color: white;\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;")

        pushButton.setGeometry(QRect(680, 500, 80, 30))
        pushButton2.setGeometry(QRect(10, 10, 80, 30))
        pushButton.clicked.connect(lambda:self.display(0))

    def stack2UI(self):
        pushButton = QPushButton(self.stack2)
        pushButton2 = QPushButton(self.stack2)
        pushButton.setText('OK')
        pushButton2.setText('Menu')
        pushButton2.setStyleSheet("        background-color: rgb(37, 121, 255);\n"
"        color: white;\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;")

        pushButton.setGeometry(QRect(680, 500, 80, 30))
        pushButton2.setGeometry(QRect(10, 10, 80, 30))
        pushButton.clicked.connect(lambda:self.display(0))

    def stack3UI(self):
        pushButton = QPushButton(self.stack3)
        pushButton2 = QPushButton(self.stack3)
        pushButton.setText('OK')
        pushButton2.setText('Menu')
        pushButton2.setStyleSheet("        background-color: rgb(37, 121, 255);\n"
"        color: white;\n"
"        border-radius: 10px;  border: 2px groove gray;\n"
"        border-style: outset;")

        pushButton.setGeometry(QRect(680, 500, 80, 30))
        pushButton2.setGeometry(QRect(10, 10, 80, 30))
        pushButton.clicked.connect(lambda:self.display(0))

    def display(self, i):
        #设置当前可见的选项卡的索引
        print(i)
        self.stack.setCurrentIndex(i)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        print(int(newLeft),int(newTop))
        self.move(int(newLeft),int(newTop))