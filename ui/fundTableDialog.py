# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fundTableDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FundTableDialog(object):
    def setupUi(self, FundTableDialog):
        FundTableDialog.setObjectName("FundTableDialog")
        FundTableDialog.resize(519, 313)
        self.gridLayout = QtWidgets.QGridLayout(FundTableDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fundTable = QtWidgets.QTableWidget(FundTableDialog)
        self.fundTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fundTable.setAlternatingRowColors(True)
        self.fundTable.setWordWrap(False)
        self.fundTable.setObjectName("fundTable")
        self.fundTable.setColumnCount(5)
        self.fundTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fundTable.setHorizontalHeaderItem(4, item)
        self.fundTable.horizontalHeader().setHighlightSections(False)
        self.fundTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.fundTable, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.okBtn = QtWidgets.QPushButton(FundTableDialog)
        self.okBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.okBtn.setObjectName("okBtn")
        self.gridLayout.addWidget(self.okBtn, 1, 3, 1, 1)
        self.moreBtn = QtWidgets.QPushButton(FundTableDialog)
        self.moreBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.moreBtn.setObjectName("moreBtn")
        self.gridLayout.addWidget(self.moreBtn, 1, 0, 1, 1)
        self.refreshBtn = QtWidgets.QPushButton(FundTableDialog)
        self.refreshBtn.setMinimumSize(QtCore.QSize(0, 25))
        self.refreshBtn.setObjectName("refreshBtn")
        self.gridLayout.addWidget(self.refreshBtn, 1, 1, 1, 1)

        self.retranslateUi(FundTableDialog)
        self.okBtn.clicked.connect(FundTableDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(FundTableDialog)

    def retranslateUi(self, FundTableDialog):
        _translate = QtCore.QCoreApplication.translate
        FundTableDialog.setWindowTitle(_translate("FundTableDialog", "Dialog"))
        item = self.fundTable.verticalHeaderItem(0)
        item.setText(_translate("FundTableDialog", "新建行"))
        item = self.fundTable.verticalHeaderItem(1)
        item.setText(_translate("FundTableDialog", "新建行"))
        item = self.fundTable.verticalHeaderItem(2)
        item.setText(_translate("FundTableDialog", "新建行"))
        item = self.fundTable.verticalHeaderItem(3)
        item.setText(_translate("FundTableDialog", "新建行"))
        item = self.fundTable.horizontalHeaderItem(0)
        item.setText(_translate("FundTableDialog", "新建列"))
        item = self.fundTable.horizontalHeaderItem(1)
        item.setText(_translate("FundTableDialog", "新建列"))
        item = self.fundTable.horizontalHeaderItem(2)
        item.setText(_translate("FundTableDialog", "新建列"))
        item = self.fundTable.horizontalHeaderItem(3)
        item.setText(_translate("FundTableDialog", "新建列"))
        item = self.fundTable.horizontalHeaderItem(4)
        item.setText(_translate("FundTableDialog", "新建列"))
        self.okBtn.setText(_translate("FundTableDialog", "确定"))
        self.moreBtn.setText(_translate("FundTableDialog", "更多"))
        self.refreshBtn.setText(_translate("FundTableDialog", "刷新"))
