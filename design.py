from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.source_image = None
        self.target_image = None
        self.result_image = None
        self.temp_result = None
        self.temp_target = None
        self.temp_source = None
        self.color_space = 'RGB'
        self.future_color = 'RGB'
        self.solo_list = [-1, 0, 1, 2]
        self.colors = ["RGB", "HLS", "HSV", "Lab"]
        self.color_list = {('RGB', 'Lab'): cv2.COLOR_RGB2Lab, ('Lab', 'RGB'): cv2.COLOR_Lab2RGB,
                           ('RGB', 'HLS'): cv2.COLOR_RGB2HLS_FULL, ('HLS', 'RGB'): cv2.COLOR_HLS2RGB_FULL,
                           ('RGB', 'HSV'): cv2.COLOR_RGB2HSV_FULL, ('HSV', 'RGB'): cv2.COLOR_HSV2RGB_FULL,
                            ('RGB', 'RGB'):None}
        self.target_solo = -1
        self.source_solo = -1
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(909, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 151, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 0, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 261, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QLabel(self.verticalLayoutWidget) #111
        self.widget.setStyleSheet("background-color: \"white\"")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(320, 70, 261, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.widget_2.setStyleSheet("background-color: \"white\"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(610, 70, 261, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.widget_3.setStyleSheet("background-color: \"white\"")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3.addWidget(self.widget_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 30, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 30, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 30, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 380, 261, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.widget_4.setStyleSheet("background-color: \"white\"")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4.addWidget(self.widget_4)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 560, 261, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.widget_6.setStyleSheet("background-color: \"white\"")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5.addWidget(self.widget_6)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 470, 261, 80))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_5 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.widget_5.setStyleSheet("background-color: \"white\"")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6.addWidget(self.widget_5)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(320, 560, 261, 80))
        self.verticalLayoutWidget_7.setStyleSheet("background-color: \"white\"")
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_9 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.widget_9.setStyleSheet("background-color: \"white\"")
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_7.addWidget(self.widget_9)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(320, 470, 261, 80))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_8 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.widget_8.setStyleSheet("background-color: \"white\"")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8.addWidget(self.widget_8)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(320, 380, 261, 80))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_7 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.widget_7.setStyleSheet("background-color: \"white\"")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_9.addWidget(self.widget_7)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(610, 380, 261, 80))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_10 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.widget_10.setStyleSheet("background-color: \"white\"")
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_10.addWidget(self.widget_10)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(610, 470, 261, 80))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_11 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.widget_11.setStyleSheet("background-color: \"white\"")
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_11.addWidget(self.widget_11)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(610, 560, 261, 80))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_12 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.widget_12.setStyleSheet("background-color: \"white\"")
        self.widget_12.setObjectName("widget_12")
        self.widget_14 = QtWidgets.QWidget(self.widget_12)
        self.widget_14.setGeometry(QtCore.QRect(-370, -480, 259, 229))
        self.widget_14.setObjectName("widget_14")
        self.widget_15 = QtWidgets.QWidget(self.widget_12)
        self.widget_15.setGeometry(QtCore.QRect(-80, -170, 259, 78))
        self.widget_15.setObjectName("widget_15")
        self.widget_16 = QtWidgets.QWidget(self.widget_12)
        self.widget_16.setGeometry(QtCore.QRect(-80, -80, 259, 78))
        self.widget_16.setObjectName("widget_16")
        self.widget_17 = QtWidgets.QWidget(self.widget_12)
        self.widget_17.setGeometry(QtCore.QRect(-80, -480, 259, 229))
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_12.addWidget(self.widget_12)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 340, 131, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 310, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 131, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 30, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 310, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 310, 131, 21))
        self.label_3.setObjectName("label_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(780, 310, 73, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 310, 131, 21))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.add_source_image)
        self.pushButton_2.clicked.connect(self.add_target_image)
        self.pushButton_5.clicked.connect(self.image_convert)
        self.comboBox.activated.connect(self.color_pick)
        self.comboBox_3.activated.connect(self.target_solo_img)
        self.comboBox_2.activated.connect(self.source_solo_img)
        self.comboBox_4.activated.connect(self.result_solo_img)
        self.pushButton_4.clicked.connect(self.draw_hist)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def draw_hist(self):

        #temp_source = cv2.cvtColor(self.source_image, self.color_list[('RGB', self.future_color)])
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_source[:, :, 0].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\x0.png', dpi=100)
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_source[:, :, 1].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\x1.png', dpi=100)
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_source[:, :, 2].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\x2.png', dpi=100)
        pixmap = QPixmap(r'D:\tmpimages\x0.png')
        self.widget_4.setPixmap(pixmap)
        pixmap = QPixmap(r'D:\tmpimages\x1.png')
        self.widget_5.setPixmap(pixmap)
        pixmap = QPixmap(r'D:\tmpimages\x2.png')
        self.widget_6.setPixmap(pixmap)

        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_target[:, :, 0].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\y0.png', dpi=100)
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_target[:, :, 1].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\y1.png', dpi=100)
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_target[:, :, 2].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\y2.png', dpi=100)
        pixmap = QPixmap(r'D:\tmpimages\y0.png')
        self.widget_7.setPixmap(pixmap)
        pixmap = QPixmap(r'D:\tmpimages\y1.png')
        self.widget_8.setPixmap(pixmap)
        pixmap = QPixmap(r'D:\tmpimages\y2.png')
        self.widget_9.setPixmap(pixmap)

        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_result[:, :, 0].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\z0.png', dpi=100)
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_result[:, :, 1].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\z1.png', dpi=100)
        plt.figure(figsize=(2.59, 0.78), dpi=100)
        plt.hist(self.temp_result[:, :, 2].ravel(), bins=255)
        plt.savefig(r'D:\tmpimages\z2.png', dpi=100)
        pixmap = QPixmap(r'D:\tmpimages\z0.png')
        self.widget_10.setPixmap(pixmap)
        pixmap = QPixmap(r'D:\tmpimages\z1.png')
        self.widget_11.setPixmap(pixmap)
        pixmap = QPixmap(r'D:\tmpimages\z2.png')
        self.widget_12.setPixmap(pixmap)

    def result_solo_img(self, color):
        self.result_solo = self.solo_list[color]
        self.temp_result = cv2.cvtColor(self.result_image.astype('float32'), self.color_list[('RGB', self.future_color)])
        for i in range(3):
            if self.result_solo == -1:
                break
            if i == self.result_solo:
                continue
            self.temp_result[:, :, i] = np.zeros_like(self.temp_result[:,:,i])
        temp_result = cv2.cvtColor(self.temp_result, self.color_list[(self.future_color, 'RGB')])
        cv2.imwrite('color_result.bmp', temp_result)
        self.temp_result = cv2.imread('color_result.bmp')
        pixmap = QPixmap('color_result.bmp')
        heighti, widthi = pixmap.height(), pixmap.width()
        if heighti < widthi:
            width = self.widget.width()
            pixmap = pixmap.scaledToWidth(width)
        else:
            height = self.widget.height()
            pixmap = pixmap.scaledToHeight(height)
        self.widget_3.setPixmap(pixmap)

    def source_solo_img(self, color):
        self.source_solo = self.solo_list[color]
        self.temp_source = cv2.cvtColor(self.source_image, self.color_list[('RGB', self.future_color)])
        for i in range(3):
            if self.source_solo == -1:
                break
            if i == self.source_solo:
                continue
            self.temp_source[:, :, i] = np.zeros_like(self.temp_source[:,:,i])
        temp_source = cv2.cvtColor(self.temp_source.astype("uint8"), self.color_list[(self.future_color, 'RGB')])
        cv2.imwrite('source_one_color.bmp', temp_source)
        self.temp_source = cv2.imread('source_one_color.bmp')

        pixmap = QPixmap('source_one_color.bmp')
        heighti, widthi = pixmap.height(), pixmap.width()
        if heighti < widthi:
            width = self.widget.width()
            pixmap = pixmap.scaledToWidth(width)
        else:
            height = self.widget.height()
            pixmap = pixmap.scaledToHeight(height)
        self.widget.setPixmap(pixmap)

    def target_solo_img(self, color):
        self.target_solo = self.solo_list[color]
        self.temp_target = cv2.cvtColor(self.target_image, self.color_list[('RGB', self.future_color)])
        for i in range(3):
            if self.target_solo == -1:
                break
            if i == self.target_solo:
                continue
            self.temp_target[:, :, i] = np.zeros_like(self.temp_target[:,:,i])
        temp_target = cv2.cvtColor(self.temp_target.astype("uint8"), self.color_list[(self.future_color, 'RGB')])
        cv2.imwrite('Target_one_color.bmp', temp_target)
        self.temp_target = cv2.imread('Target_one_color.bmp')
        pixmap = QPixmap('Target_one_color.bmp')
        heighti, widthi = pixmap.height(), pixmap.width()
        if heighti < widthi:
            width = self.widget.width()
            pixmap = pixmap.scaledToWidth(width)
        else:
            height = self.widget.height()
            pixmap = pixmap.scaledToHeight(height)
        self.widget_2.setPixmap(pixmap)

    def color_pick(self, color):
        self.future_color = self.colors[color]
        if self.future_color == 'RGB':
            _translate = QtCore.QCoreApplication.translate
            self.comboBox_4.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_4.setItemText(1, _translate("MainWindow", "Blue"))
            self.comboBox_4.setItemText(2, _translate("MainWindow", "Green"))
            self.comboBox_4.setItemText(3, _translate("MainWindow", "Red"))
            self.comboBox_3.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_3.setItemText(1, _translate("MainWindow", "Blue"))
            self.comboBox_3.setItemText(2, _translate("MainWindow", "Green"))
            self.comboBox_3.setItemText(3, _translate("MainWindow", "Red"))
            self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_2.setItemText(1, _translate("MainWindow", "Blue"))
            self.comboBox_2.setItemText(2, _translate("MainWindow", "Green"))
            self.comboBox_2.setItemText(3, _translate("MainWindow", "Red"))
        elif self.future_color == 'HLS':
            _translate = QtCore.QCoreApplication.translate
            self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_2.setItemText(1, _translate("MainWindow", "H"))
            self.comboBox_2.setItemText(2, _translate("MainWindow", "L"))
            self.comboBox_2.setItemText(3, _translate("MainWindow", "S"))
            self.comboBox_3.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_3.setItemText(1, _translate("MainWindow", "H"))
            self.comboBox_3.setItemText(2, _translate("MainWindow", "L"))
            self.comboBox_3.setItemText(3, _translate("MainWindow", "S"))
            self.comboBox_4.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_4.setItemText(1, _translate("MainWindow", "H"))
            self.comboBox_4.setItemText(2, _translate("MainWindow", "L"))
            self.comboBox_4.setItemText(3, _translate("MainWindow", "S"))
        elif self.future_color == 'HSV':
            _translate = QtCore.QCoreApplication.translate
            self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_2.setItemText(1, _translate("MainWindow", "H"))
            self.comboBox_2.setItemText(2, _translate("MainWindow", "S"))
            self.comboBox_2.setItemText(3, _translate("MainWindow", "V"))
            self.comboBox_3.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_3.setItemText(1, _translate("MainWindow", "H"))
            self.comboBox_3.setItemText(2, _translate("MainWindow", "S"))
            self.comboBox_3.setItemText(3, _translate("MainWindow", "V"))
            self.comboBox_4.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_4.setItemText(1, _translate("MainWindow", "H"))
            self.comboBox_4.setItemText(2, _translate("MainWindow", "S"))
            self.comboBox_4.setItemText(3, _translate("MainWindow", "V"))
        elif self.future_color == 'Lab':
            _translate = QtCore.QCoreApplication.translate
            self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_2.setItemText(1, _translate("MainWindow", "L"))
            self.comboBox_2.setItemText(2, _translate("MainWindow", "a"))
            self.comboBox_2.setItemText(3, _translate("MainWindow", "b"))
            self.comboBox_3.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_3.setItemText(1, _translate("MainWindow", "L"))
            self.comboBox_3.setItemText(2, _translate("MainWindow", "a"))
            self.comboBox_3.setItemText(3, _translate("MainWindow", "b"))
            self.comboBox_4.setItemText(0, _translate("MainWindow", "All"))
            self.comboBox_4.setItemText(1, _translate("MainWindow", "L"))
            self.comboBox_4.setItemText(2, _translate("MainWindow", "a"))
            self.comboBox_4.setItemText(3, _translate("MainWindow", "b"))

    def add_source_image(self):
        file, _ = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        if file:
            pixmap = QPixmap(file)

            self.source_image = cv2.imread(file)
            self.temp_source = self.source_image.copy()
            heighti, widthi = pixmap.height(), pixmap.width()

            if heighti < widthi:
                width = self.widget.width()
                pixmap = pixmap.scaledToWidth(width)
            else:
                height = self.widget.height()
                pixmap = pixmap.scaledToHeight(height)
            self.widget.setPixmap(pixmap)
    def add_target_image(self):
        file, _ = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        if file:
            pixmap = QPixmap(file)

            self.target_image = cv2.imread(file)
            self.temp_target = self.target_image.copy()
            heighti, widthi = pixmap.height(), pixmap.width()
            if heighti < widthi:
                width = self.widget.width()
                pixmap = pixmap.scaledToWidth(width)
            else:
                height = self.widget.height()
                pixmap = pixmap.scaledToHeight(height)
            self.widget_2.setPixmap(pixmap)
    def save_img(self):
        cv2.imwrite('result.bmp', self.result_image)

    def image_convert(self):
        self.color_space_change()
        self.result_image = np.zeros_like(self.target_image)
        if self.temp_source is None:
            self.temp_source = self.source_image.copy()
        if self.temp_target is None:
            self.temp_target = self.target_image.copy()

        E_t = np.mean(self.temp_target, axis=(0, 1))
        D_t = np.std(self.temp_target, axis=(0, 1))
        E_s = np.mean(self.temp_source, axis=(0, 1))
        D_s = np.std(self.temp_source, axis=(0, 1))

        self.result_image = (E_s + (self.temp_target - E_t) * D_s / D_t)

        self.color_space_change()
        self.temp_result = self.result_image.copy()
        cv2.imwrite("tmp.bmp", self.result_image)
        cv2.imwrite('color_result.bmp', self.result_image)
        pixmap = QPixmap("tmp.bmp")

        heighti, widthi = pixmap.height(), pixmap.width()

        if heighti < widthi:
            width = self.widget.width()
            pixmap = pixmap.scaledToWidth(width)
        else:
            height = self.widget.height()
            pixmap = pixmap.scaledToHeight(height)
        self.widget_3.setPixmap(pixmap)

    def color_space_change(self):
        if self.color_space != 'RGB' or self.future_color != 'RGB':
            self.temp_source = cv2.cvtColor(self.temp_source, self.color_list[(self.color_space, self.future_color)])
            self.temp_target = cv2.cvtColor(self.temp_target, self.color_list[(self.color_space, self.future_color)])
            self.result_image = cv2.cvtColor(self.result_image.astype("uint8"), self.color_list[(self.color_space, self.future_color)])
            self.color_space, self.future_color = self.future_color, self.color_space


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Colorchanger"))
        self.label.setText(_translate("MainWindow", "Choose color space"))
        self.comboBox.setItemText(0, _translate("MainWindow", "RGB"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HLS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "HSV"))
        self.comboBox.setItemText(3, _translate("MainWindow", "LAB"))
        self.pushButton.setText(_translate("MainWindow", "Add source img"))
        self.pushButton_2.setText(_translate("MainWindow", "Add target img"))
        self.pushButton_3.setText(_translate("MainWindow", "Save result"))
        self.pushButton_4.setText(_translate("MainWindow", "Show histograms"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Blue"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Red"))
        self.label_2.setText(_translate("MainWindow", "Choose color channel"))
        self.pushButton_5.setText(_translate("MainWindow", "Result"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Blue"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Red"))
        self.label_3.setText(_translate("MainWindow", "Choose target color"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Blue"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Red"))
        self.label_4.setText(_translate("MainWindow", "Choose color channel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
