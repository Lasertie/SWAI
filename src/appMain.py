# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'appMain.ui'
# Created by: PyQt5 UI code generator 5.9.2
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 695)
        MainWindow.setMinimumSize(QtCore.QSize(792, 695))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(560, 30, 20, 131))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(10, 180, 771, 441))
        self.MplWidget.setAutoFillBackground(False)
        self.MplWidget.setStyleSheet("")
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(590, 40, 151, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_davy = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_davy.setStyleSheet("")
        self.checkBox_davy.setObjectName("checkBox_davy")
        self.gridLayout.addWidget(self.checkBox_davy, 0, 0, 1, 1)
        self.checkBox_sharp = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_sharp.setObjectName("checkBox_sharp")
        self.gridLayout.addWidget(self.checkBox_sharp, 1, 0, 1, 1)
        self.checkBox_ISO = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ISO.setObjectName("checkBox_ISO")
        self.gridLayout.addWidget(self.checkBox_ISO, 2, 0, 1, 1)
        self.checkBox_paredsimple = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_paredsimple.setObjectName("checkBox_paredsimple")
        self.gridLayout.addWidget(self.checkBox_paredsimple, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 30, 20, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(80, 10, 281, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 80, 51, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 10, 61, 16))
        self.label.setObjectName("label")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 10, 21, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 160, 801, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 121, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 80, 56, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.largeur = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.largeur.setAlignment(QtCore.Qt.AlignCenter)
        self.largeur.setObjectName("largeur")
        self.verticalLayout.addWidget(self.largeur)
        self.epeseur = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.epeseur.setAlignment(QtCore.Qt.AlignCenter)
        self.epeseur.setObjectName("epeseur")
        self.verticalLayout.addWidget(self.epeseur)
        self.hauteur = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hauteur.setAlignment(QtCore.Qt.AlignCenter)
        self.hauteur.setObjectName("hauteur")
        self.verticalLayout.addWidget(self.hauteur)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(430, 10, 151, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(221, 50, 101, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(680, 10, 121, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 40, 160, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_procesar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_procesar.setPalette(palette)
        self.pushButton_procesar.setObjectName("pushButton_procesar")
        self.verticalLayout_4.addWidget(self.pushButton_procesar)
        self.pushButton_exportar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_exportar.setPalette(palette)
        self.pushButton_exportar.setObjectName("pushButton_exportar")
        self.verticalLayout_4.addWidget(self.pushButton_exportar)
        self.pushButton_borrar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_borrar.setObjectName("pushButton_borrar")
        self.verticalLayout_4.addWidget(self.pushButton_borrar)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 161, 16))
        self.label_2.setObjectName("label_2")
        self.materiel = QtWidgets.QComboBox(self.centralwidget)
        self.materiel.setGeometry(QtCore.QRect(40, 80, 121, 22))
        self.materiel.setObjectName("materiel")
        self.pushButton_cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cerrar.setGeometry(QtCore.QRect(700, 630, 75, 23))
        self.pushButton_cerrar.setObjectName("pushButton_cerrar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_borrar.clicked.connect(self.hauteur.clear)
        self.pushButton_borrar.clicked.connect(self.epeseur.clear)
        self.pushButton_borrar.clicked.connect(self.largeur.clear)
        self.pushButton_borrar.clicked['bool'].connect(self.checkBox_paredsimple.setChecked)
        self.pushButton_borrar.clicked['bool'].connect(self.checkBox_ISO.setChecked)
        self.pushButton_borrar.clicked['bool'].connect(self.checkBox_sharp.setChecked)
        self.pushButton_borrar.clicked['bool'].connect(self.checkBox_davy.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_davy.setText(_translate("MainWindow", "Davy"))
        self.checkBox_sharp.setText(_translate("MainWindow", "Sharp"))
        self.checkBox_ISO.setText(_translate("MainWindow", "ISO"))
        self.checkBox_paredsimple.setText(_translate("MainWindow", "Pared simple"))
        self.label_6.setText(_translate("MainWindow", "Largeur:"))
        self.label_8.setText(_translate("MainWindow", "Epeseur:"))
        self.label_7.setText(_translate("MainWindow", "hauteur:"))
        self.label.setText(_translate("MainWindow", "Fonctions"))
        self.label_3.setText(_translate("MainWindow", "Possibilites"))
        self.label_4.setText(_translate("MainWindow", "Materiau"))
        self.label_5.setText(_translate("MainWindow", "Dimensions [m]:"))
        self.pushButton_procesar.setText(_translate("MainWindow", "Calculer"))
        self.pushButton_exportar.setText(_translate("MainWindow", "Exporter"))
        self.pushButton_borrar.setText(_translate("MainWindow", "Supprimer"))
        self.label_2.setText(_translate("MainWindow", "Méthode de calcul"))
        self.pushButton_cerrar.setText(_translate("MainWindow", "Fermer"))

from mplwidget import MplWidget