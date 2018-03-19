# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ASUSarturo\Desktop\RnD\maya_rigging_skinsWeightsExporter\skinWeights_UI\resources\skinWeights_ui_v001.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_window_skinWeights(object):
    def setupUi(self, window_skinWeights):
        window_skinWeights.setObjectName("window_skinWeights")
        window_skinWeights.resize(491, 308)
        self.centralwidget = QtWidgets.QWidget(window_skinWeights)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.widget_tabs.setObjectName("widget_tabs")
        self.tab_export = QtWidgets.QWidget()
        self.tab_export.setObjectName("tab_export")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_export)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lyt_grid_mainExport = QtWidgets.QGridLayout()
        self.lyt_grid_mainExport.setObjectName("lyt_grid_mainExport")
        self.lyt_vertical_horizontal_btnExport = QtWidgets.QVBoxLayout()
        self.lyt_vertical_horizontal_btnExport.setObjectName("lyt_vertical_horizontal_btnExport")
        self.btn_export = QtWidgets.QPushButton(self.tab_export)
        self.btn_export.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_export.setObjectName("btn_export")
        self.lyt_vertical_horizontal_btnExport.addWidget(self.btn_export)
        self.lyt_grid_mainExport.addLayout(self.lyt_vertical_horizontal_btnExport, 4, 0, 1, 1)
        self.chkbox_screenshot = QtWidgets.QCheckBox(self.tab_export)
        self.chkbox_screenshot.setObjectName("chkbox_screenshot")
        self.lyt_grid_mainExport.addWidget(self.chkbox_screenshot, 3, 0, 1, 1)
        self.lyt_vertical_pathExport = QtWidgets.QHBoxLayout()
        self.lyt_vertical_pathExport.setObjectName("lyt_vertical_pathExport")
        self.txt_exportPath = QtWidgets.QLineEdit(self.tab_export)
        self.txt_exportPath.setObjectName("txt_exportPath")
        self.lyt_vertical_pathExport.addWidget(self.txt_exportPath)
        self.btn_browseExport = QtWidgets.QPushButton(self.tab_export)
        self.btn_browseExport.setObjectName("btn_browseExport")
        self.lyt_vertical_pathExport.addWidget(self.btn_browseExport)
        self.lyt_grid_mainExport.addLayout(self.lyt_vertical_pathExport, 2, 0, 1, 1)
        self.lyt_horizontal_radiobtns = QtWidgets.QVBoxLayout()
        self.lyt_horizontal_radiobtns.setObjectName("lyt_horizontal_radiobtns")
        self.lyt_vertical_radiobtns = QtWidgets.QHBoxLayout()
        self.lyt_vertical_radiobtns.setObjectName("lyt_vertical_radiobtns")
        self.rdbtn_sel = QtWidgets.QRadioButton(self.tab_export)
        self.rdbtn_sel.setObjectName("rdbtn_sel")
        self.lyt_vertical_radiobtns.addWidget(self.rdbtn_sel)
        self.rdbtn_all = QtWidgets.QRadioButton(self.tab_export)
        self.rdbtn_all.setObjectName("rdbtn_all")
        self.lyt_vertical_radiobtns.addWidget(self.rdbtn_all)
        self.lyt_horizontal_radiobtns.addLayout(self.lyt_vertical_radiobtns)
        self.lyt_grid_mainExport.addLayout(self.lyt_horizontal_radiobtns, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.lyt_grid_mainExport)
        self.widget_tabs.addTab(self.tab_export, "")
        self.tab_import = QtWidgets.QWidget()
        self.tab_import.setObjectName("tab_import")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_import)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lyt_horizontal_main = QtWidgets.QVBoxLayout()
        self.lyt_horizontal_main.setObjectName("lyt_horizontal_main")
        self.lyt_horizontal_images = QtWidgets.QVBoxLayout()
        self.lyt_horizontal_images.setObjectName("lyt_horizontal_images")
        self.lyt_horizontal_main.addLayout(self.lyt_horizontal_images)
        self.lyt_vertical_path = QtWidgets.QHBoxLayout()
        self.lyt_vertical_path.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.lyt_vertical_path.setObjectName("lyt_vertical_path")
        self.txt_importPath = QtWidgets.QLineEdit(self.tab_import)
        self.txt_importPath.setObjectName("txt_importPath")
        self.lyt_vertical_path.addWidget(self.txt_importPath)
        self.btn_importPath = QtWidgets.QPushButton(self.tab_import)
        self.btn_importPath.setObjectName("btn_importPath")
        self.lyt_vertical_path.addWidget(self.btn_importPath)
        self.lyt_horizontal_main.addLayout(self.lyt_vertical_path)
        self.lyt_horizontal_import = QtWidgets.QVBoxLayout()
        self.lyt_horizontal_import.setObjectName("lyt_horizontal_import")
        self.btn_import = QtWidgets.QPushButton(self.tab_import)
        self.btn_import.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_import.setObjectName("btn_import")
        self.lyt_horizontal_import.addWidget(self.btn_import)
        self.lyt_horizontal_main.addLayout(self.lyt_horizontal_import)
        self.verticalLayout_3.addLayout(self.lyt_horizontal_main)
        self.widget_tabs.addTab(self.tab_import, "")
        self.verticalLayout.addWidget(self.widget_tabs)
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setObjectName("lbl_status")
        self.verticalLayout.addWidget(self.lbl_status)
        window_skinWeights.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_skinWeights)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")
        window_skinWeights.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_skinWeights)
        self.statusbar.setObjectName("statusbar")
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

