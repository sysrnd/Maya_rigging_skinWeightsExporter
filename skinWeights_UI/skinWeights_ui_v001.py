# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ASUSarturo\Desktop\RnD\maya_rigging_skinsWeightsExporter\skinWeights_UI\resources\skinWeights_ui_v001.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window_skinWeights(object):
    def setupUi(self, window_skinWeights):
        window_skinWeights.setObjectName(_fromUtf8("window_skinWeights"))
        window_skinWeights.resize(491, 308)
        self.centralwidget = QtGui.QWidget(window_skinWeights)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_tabs = QtGui.QTabWidget(self.centralwidget)
        self.widget_tabs.setObjectName(_fromUtf8("widget_tabs"))
        self.tab_export = QtGui.QWidget()
        self.tab_export.setObjectName(_fromUtf8("tab_export"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_export)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lyt_grid_mainExport = QtGui.QGridLayout()
        self.lyt_grid_mainExport.setObjectName(_fromUtf8("lyt_grid_mainExport"))
        self.lyt_vertical_horizontal_btnExport = QtGui.QVBoxLayout()
        self.lyt_vertical_horizontal_btnExport.setObjectName(_fromUtf8("lyt_vertical_horizontal_btnExport"))
        self.btn_export = QtGui.QPushButton(self.tab_export)
        self.btn_export.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_export.setObjectName(_fromUtf8("btn_export"))
        self.lyt_vertical_horizontal_btnExport.addWidget(self.btn_export)
        self.lyt_grid_mainExport.addLayout(self.lyt_vertical_horizontal_btnExport, 4, 0, 1, 1)
        self.chkbox_screenshot = QtGui.QCheckBox(self.tab_export)
        self.chkbox_screenshot.setObjectName(_fromUtf8("chkbox_screenshot"))
        self.lyt_grid_mainExport.addWidget(self.chkbox_screenshot, 3, 0, 1, 1)
        self.lyt_vertical_pathExport = QtGui.QHBoxLayout()
        self.lyt_vertical_pathExport.setObjectName(_fromUtf8("lyt_vertical_pathExport"))
        self.txt_exportPath = QtGui.QLineEdit(self.tab_export)
        self.txt_exportPath.setObjectName(_fromUtf8("txt_exportPath"))
        self.lyt_vertical_pathExport.addWidget(self.txt_exportPath)
        self.btn_browseExport = QtGui.QPushButton(self.tab_export)
        self.btn_browseExport.setObjectName(_fromUtf8("btn_browseExport"))
        self.lyt_vertical_pathExport.addWidget(self.btn_browseExport)
        self.lyt_grid_mainExport.addLayout(self.lyt_vertical_pathExport, 2, 0, 1, 1)
        self.lyt_horizontal_radiobtns = QtGui.QVBoxLayout()
        self.lyt_horizontal_radiobtns.setObjectName(_fromUtf8("lyt_horizontal_radiobtns"))
        self.lyt_vertical_radiobtns = QtGui.QHBoxLayout()
        self.lyt_vertical_radiobtns.setObjectName(_fromUtf8("lyt_vertical_radiobtns"))
        self.rdbtn_sel = QtGui.QRadioButton(self.tab_export)
        self.rdbtn_sel.setObjectName(_fromUtf8("rdbtn_sel"))
        self.lyt_vertical_radiobtns.addWidget(self.rdbtn_sel)
        self.rdbtn_all = QtGui.QRadioButton(self.tab_export)
        self.rdbtn_all.setObjectName(_fromUtf8("rdbtn_all"))
        self.lyt_vertical_radiobtns.addWidget(self.rdbtn_all)
        self.lyt_horizontal_radiobtns.addLayout(self.lyt_vertical_radiobtns)
        self.lyt_grid_mainExport.addLayout(self.lyt_horizontal_radiobtns, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.lyt_grid_mainExport)
        self.widget_tabs.addTab(self.tab_export, _fromUtf8(""))
        self.tab_import = QtGui.QWidget()
        self.tab_import.setObjectName(_fromUtf8("tab_import"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_import)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lyt_horizontal_main = QtGui.QVBoxLayout()
        self.lyt_horizontal_main.setObjectName(_fromUtf8("lyt_horizontal_main"))
        self.lyt_horizontal_images = QtGui.QVBoxLayout()
        self.lyt_horizontal_images.setObjectName(_fromUtf8("lyt_horizontal_images"))
        self.lyt_horizontal_main.addLayout(self.lyt_horizontal_images)
        self.lyt_vertical_path = QtGui.QHBoxLayout()
        self.lyt_vertical_path.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.lyt_vertical_path.setObjectName(_fromUtf8("lyt_vertical_path"))
        self.txt_importPath = QtGui.QLineEdit(self.tab_import)
        self.txt_importPath.setObjectName(_fromUtf8("txt_importPath"))
        self.lyt_vertical_path.addWidget(self.txt_importPath)
        self.btn_importPath = QtGui.QPushButton(self.tab_import)
        self.btn_importPath.setObjectName(_fromUtf8("btn_importPath"))
        self.lyt_vertical_path.addWidget(self.btn_importPath)
        self.lyt_horizontal_main.addLayout(self.lyt_vertical_path)
        self.lyt_horizontal_import = QtGui.QVBoxLayout()
        self.lyt_horizontal_import.setObjectName(_fromUtf8("lyt_horizontal_import"))
        self.btn_import = QtGui.QPushButton(self.tab_import)
        self.btn_import.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_import.setObjectName(_fromUtf8("btn_import"))
        self.lyt_horizontal_import.addWidget(self.btn_import)
        self.lyt_horizontal_main.addLayout(self.lyt_horizontal_import)
        self.verticalLayout_3.addLayout(self.lyt_horizontal_main)
        self.widget_tabs.addTab(self.tab_import, _fromUtf8(""))
        self.verticalLayout.addWidget(self.widget_tabs)
        self.lbl_status = QtGui.QLabel(self.centralwidget)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.verticalLayout.addWidget(self.lbl_status)
        window_skinWeights.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(window_skinWeights)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window_skinWeights.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window_skinWeights)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window_skinWeights.setStatusBar(self.statusbar)

        self.retranslateUi(window_skinWeights)
        self.widget_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(window_skinWeights)

    def retranslateUi(self, window_skinWeights):
        window_skinWeights.setWindowTitle(_translate("window_skinWeights", "Skin Weights Handler", None))
        self.btn_export.setText(_translate("window_skinWeights", "Export", None))
        self.chkbox_screenshot.setText(_translate("window_skinWeights", "Take screenshots of vertices", None))
        self.btn_browseExport.setText(_translate("window_skinWeights", "Browse", None))
        self.rdbtn_sel.setText(_translate("window_skinWeights", "Selected geometry", None))
        self.rdbtn_all.setText(_translate("window_skinWeights", "All geometry", None))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_export), _translate("window_skinWeights", "Export Skin Weights", None))
        self.btn_importPath.setText(_translate("window_skinWeights", "Browse", None))
        self.btn_import.setText(_translate("window_skinWeights", "Import", None))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_import), _translate("window_skinWeights", "Import Skin Weights", None))
        self.lbl_status.setText(_translate("window_skinWeights", "//", None))

