# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_quicksearch.ui'
#
# Created: Sat Mar 14 22:10:22 2009
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LeoQuickSearchWidget(object):
    def setupUi(self, LeoQuickSearchWidget):
        LeoQuickSearchWidget.setObjectName("LeoQuickSearchWidget")
        LeoQuickSearchWidget.resize(868,572)
        self.verticalLayout_2 = QtGui.QVBoxLayout(LeoQuickSearchWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtGui.QLineEdit(LeoQuickSearchWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.listWidget = QtGui.QListWidget(LeoQuickSearchWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(LeoQuickSearchWidget)
        QtCore.QMetaObject.connectSlotsByName(LeoQuickSearchWidget)

    def retranslateUi(self, LeoQuickSearchWidget):
        LeoQuickSearchWidget.setWindowTitle(QtGui.QApplication.translate("LeoQuickSearchWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

