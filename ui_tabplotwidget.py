# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabplotwidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tabPlotWidget(object):
    def setupUi(self, tabPlotWidget):
        tabPlotWidget.setObjectName("tabPlotWidget")
        tabPlotWidget.resize(714, 563)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(tabPlotWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(tabPlotWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboType = QtWidgets.QComboBox(tabPlotWidget)
        self.comboType.setObjectName("comboType")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.horizontalLayout_4.addWidget(self.comboType)
        self.desvestBox = QtWidgets.QCheckBox(tabPlotWidget)
        self.desvestBox.setObjectName("desvestBox")
        self.horizontalLayout_4.addWidget(self.desvestBox)
        self.lineplotBox = QtWidgets.QCheckBox(tabPlotWidget)
        self.lineplotBox.setObjectName("lineplotBox")
        self.horizontalLayout_4.addWidget(self.lineplotBox)
        self.multicolorCB = QtWidgets.QCheckBox(tabPlotWidget)
        self.multicolorCB.setObjectName("multicolorCB")
        self.horizontalLayout_4.addWidget(self.multicolorCB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(tabPlotWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.filenameBox = QtWidgets.QLineEdit(tabPlotWidget)
        self.filenameBox.setObjectName("filenameBox")
        self.horizontalLayout_3.addWidget(self.filenameBox)
        self.browseBtn = QtWidgets.QPushButton(tabPlotWidget)
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout_3.addWidget(self.browseBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.normalizedCB = QtWidgets.QComboBox(tabPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalizedCB.sizePolicy().hasHeightForWidth())
        self.normalizedCB.setSizePolicy(sizePolicy)
        self.normalizedCB.setObjectName("normalizedCB")
        self.normalizedCB.addItem("")
        self.normalizedCB.addItem("")
        self.normalizedCB.addItem("")
        self.horizontalLayout_5.addWidget(self.normalizedCB)
        self.doubleCB = QtWidgets.QCheckBox(tabPlotWidget)
        self.doubleCB.setObjectName("doubleCB")
        self.horizontalLayout_5.addWidget(self.doubleCB)
        self.label_14 = QtWidgets.QLabel(tabPlotWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.convertYline = QtWidgets.QLineEdit(tabPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convertYline.sizePolicy().hasHeightForWidth())
        self.convertYline.setSizePolicy(sizePolicy)
        self.convertYline.setObjectName("convertYline")
        self.horizontalLayout_5.addWidget(self.convertYline)
        self.label_15 = QtWidgets.QLabel(tabPlotWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.convertY2line = QtWidgets.QLineEdit(tabPlotWidget)
        self.convertY2line.setObjectName("convertY2line")
        self.horizontalLayout_5.addWidget(self.convertY2line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(tabPlotWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.xlabel1line = QtWidgets.QLineEdit(self.groupBox)
        self.xlabel1line.setObjectName("xlabel1line")
        self.horizontalLayout_2.addWidget(self.xlabel1line)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.ylabel1line = QtWidgets.QLineEdit(self.groupBox)
        self.ylabel1line.setObjectName("ylabel1line")
        self.horizontalLayout_2.addWidget(self.ylabel1line)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.ylabel2line = QtWidgets.QLineEdit(self.groupBox)
        self.ylabel2line.setObjectName("ylabel2line")
        self.horizontalLayout_2.addWidget(self.ylabel2line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(tabPlotWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.xlimitline = QtWidgets.QLineEdit(self.groupBox_2)
        self.xlimitline.setObjectName("xlimitline")
        self.horizontalLayout_6.addWidget(self.xlimitline)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.y1limitline = QtWidgets.QLineEdit(self.groupBox_2)
        self.y1limitline.setObjectName("y1limitline")
        self.horizontalLayout_6.addWidget(self.y1limitline)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.y2limitline = QtWidgets.QLineEdit(self.groupBox_2)
        self.y2limitline.setObjectName("y2limitline")
        self.horizontalLayout_6.addWidget(self.y2limitline)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(tabPlotWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.xaxislocator = QtWidgets.QLineEdit(self.groupBox_3)
        self.xaxislocator.setObjectName("xaxislocator")
        self.horizontalLayout.addWidget(self.xaxislocator)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.y1axislocator = QtWidgets.QLineEdit(self.groupBox_3)
        self.y1axislocator.setObjectName("y1axislocator")
        self.horizontalLayout.addWidget(self.y1axislocator)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.y2axislocator = QtWidgets.QLineEdit(self.groupBox_3)
        self.y2axislocator.setObjectName("y2axislocator")
        self.horizontalLayout.addWidget(self.y2axislocator)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(tabPlotWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.legend1CB = QtWidgets.QComboBox(tabPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.legend1CB.sizePolicy().hasHeightForWidth())
        self.legend1CB.setSizePolicy(sizePolicy)
        self.legend1CB.setObjectName("legend1CB")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.legend1CB.addItem("")
        self.gridLayout.addWidget(self.legend1CB, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(tabPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.legendline = QtWidgets.QLineEdit(tabPlotWidget)
        self.legendline.setObjectName("legendline")
        self.gridLayout.addWidget(self.legendline, 2, 1, 1, 2)
        self.legend2CB = QtWidgets.QComboBox(tabPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.legend2CB.sizePolicy().hasHeightForWidth())
        self.legend2CB.setSizePolicy(sizePolicy)
        self.legend2CB.setObjectName("legend2CB")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.legend2CB.addItem("")
        self.gridLayout.addWidget(self.legend2CB, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(tabPlotWidget)
        QtCore.QMetaObject.connectSlotsByName(tabPlotWidget)

    def retranslateUi(self, tabPlotWidget):
        _translate = QtCore.QCoreApplication.translate
        tabPlotWidget.setWindowTitle(_translate("tabPlotWidget", "Form"))
        self.label.setText(_translate("tabPlotWidget", "Plot type"))
        self.comboType.setItemText(0, _translate("tabPlotWidget", "LinePlot"))
        self.comboType.setItemText(1, _translate("tabPlotWidget", "DotPlot"))
        self.comboType.setItemText(2, _translate("tabPlotWidget", "TafelPlot"))
        self.comboType.setItemText(3, _translate("tabPlotWidget", "SpectroAD"))
        self.comboType.setItemText(4, _translate("tabPlotWidget", "MultiSpectra"))
        self.comboType.setItemText(5, _translate("tabPlotWidget", "Image"))
        self.comboType.setItemText(6, _translate("tabPlotWidget", "pH"))
        self.comboType.setItemText(7, _translate("tabPlotWidget", "CalPlot"))
        self.comboType.setItemText(8, _translate("tabPlotWidget", "SpectraEvo"))
        self.desvestBox.setText(_translate("tabPlotWidget", "Desvest"))
        self.lineplotBox.setText(_translate("tabPlotWidget", "Line"))
        self.multicolorCB.setText(_translate("tabPlotWidget", "MulticolorDots"))
        self.label_2.setText(_translate("tabPlotWidget", "Filename"))
        self.browseBtn.setText(_translate("tabPlotWidget", "Browse"))
        self.normalizedCB.setItemText(0, _translate("tabPlotWidget", "Non-normalized"))
        self.normalizedCB.setItemText(1, _translate("tabPlotWidget", "Normalized by max"))
        self.normalizedCB.setItemText(2, _translate("tabPlotWidget", "Normalized by first"))
        self.doubleCB.setText(_translate("tabPlotWidget", "DoubleAxis"))
        self.label_14.setText(_translate("tabPlotWidget", "Convert y"))
        self.label_15.setText(_translate("tabPlotWidget", "Convert y2"))
        self.groupBox.setTitle(_translate("tabPlotWidget", "Labels"))
        self.label_3.setText(_translate("tabPlotWidget", "x Label 1"))
        self.label_6.setText(_translate("tabPlotWidget", "y Label 1"))
        self.label_5.setText(_translate("tabPlotWidget", "y Label 2"))
        self.groupBox_2.setTitle(_translate("tabPlotWidget", "Limits"))
        self.label_8.setText(_translate("tabPlotWidget", "x limit"))
        self.label_9.setText(_translate("tabPlotWidget", "y1 limit"))
        self.label_10.setText(_translate("tabPlotWidget", "y2 limit"))
        self.groupBox_3.setTitle(_translate("tabPlotWidget", "MultipleLocator"))
        self.label_11.setText(_translate("tabPlotWidget", "Xaxis"))
        self.label_12.setText(_translate("tabPlotWidget", "Y1axis"))
        self.label_13.setText(_translate("tabPlotWidget", "Y2axis"))
        self.label_4.setText(_translate("tabPlotWidget", "Locations"))
        self.legend1CB.setItemText(0, _translate("tabPlotWidget", "best"))
        self.legend1CB.setItemText(1, _translate("tabPlotWidget", "upper right"))
        self.legend1CB.setItemText(2, _translate("tabPlotWidget", "upper left"))
        self.legend1CB.setItemText(3, _translate("tabPlotWidget", "lower right"))
        self.legend1CB.setItemText(4, _translate("tabPlotWidget", "lower left"))
        self.legend1CB.setItemText(5, _translate("tabPlotWidget", "right"))
        self.legend1CB.setItemText(6, _translate("tabPlotWidget", "center left"))
        self.legend1CB.setItemText(7, _translate("tabPlotWidget", "center right"))
        self.legend1CB.setItemText(8, _translate("tabPlotWidget", "lower center"))
        self.legend1CB.setItemText(9, _translate("tabPlotWidget", "upper center"))
        self.legend1CB.setItemText(10, _translate("tabPlotWidget", "center"))
        self.label_7.setText(_translate("tabPlotWidget", "Legends"))
        self.legend2CB.setItemText(0, _translate("tabPlotWidget", "best"))
        self.legend2CB.setItemText(1, _translate("tabPlotWidget", "upper right"))
        self.legend2CB.setItemText(2, _translate("tabPlotWidget", "upper left"))
        self.legend2CB.setItemText(3, _translate("tabPlotWidget", "lower right"))
        self.legend2CB.setItemText(4, _translate("tabPlotWidget", "lower left"))
        self.legend2CB.setItemText(5, _translate("tabPlotWidget", "right"))
        self.legend2CB.setItemText(6, _translate("tabPlotWidget", "center left"))
        self.legend2CB.setItemText(7, _translate("tabPlotWidget", "center right"))
        self.legend2CB.setItemText(8, _translate("tabPlotWidget", "lower center"))
        self.legend2CB.setItemText(9, _translate("tabPlotWidget", "upper center"))
        self.legend2CB.setItemText(10, _translate("tabPlotWidget", "center"))

