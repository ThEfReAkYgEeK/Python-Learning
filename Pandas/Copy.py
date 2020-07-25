# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:55:26 2020

@author: Sureshkumar R
"""

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets



#Configuring LogInWndow
class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(530, 247)
        self.centralwidget = QtWidgets.QWidget(LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(430, 170, 75, 23))
        self.LoginButton.setObjectName("LoginButton")
        self.UserIDInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UserIDInput.setGeometry(QtCore.QRect(330, 50, 171, 21))
        self.UserIDInput.setObjectName("UserIDInput")
        self.DepartmentInput = QtWidgets.QComboBox(self.centralwidget)
        self.DepartmentInput.setGeometry(QtCore.QRect(330, 90, 171, 22))
        self.DepartmentInput.setObjectName("DepartmentInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(330, 130, 171, 21))
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.UserIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserIDLabel.setGeometry(QtCore.QRect(190, 50, 91, 20))
        self.UserIDLabel.setObjectName("UserIDLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(190, 130, 91, 20))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(20, 70, 141, 51))
        self.LogoLabel.setText("")
        self.LogoLabel.setPixmap(QtGui.QPixmap("Logo.PNG"))
        self.LogoLabel.setObjectName("LogoLabel")
        self.DeptLabel = QtWidgets.QLabel(self.centralwidget)
        self.DeptLabel.setGeometry(QtCore.QRect(190, 90, 91, 20))
        self.DeptLabel.setObjectName("DeptLabel")
        self.InfoOutput = QtWidgets.QLabel(self.centralwidget)
        self.InfoOutput.setGeometry(QtCore.QRect(26, 170, 371, 20))
        self.InfoOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.InfoOutput.setText("")
        self.InfoOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoOutput.setObjectName("InfoOutput")
        LogInWindow.setCentralWidget(self.centralwidget)
        
        for Department,Department_df in GroupedLoginDetails:
            self.DepartmentInput.addItem(Department)
        
        self.LoginButton.clicked.connect(self.LoginButtonPressed)
        
        
        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

    def retranslateUi(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "LogInWindow"))
        self.LoginButton.setText(_translate("LogInWindow", "Login"))
        self.UserIDLabel.setText(_translate("LogInWindow", "Enter User ID"))
        self.PasswordLabel.setText(_translate("LogInWindow", "Enter Password"))
        self.DeptLabel.setText(_translate("LogInWindow", "Department"))
        self.InfoOutput.setText(_translate("LogInWindow", "Enter Login Crentials"))

    def LoginButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        ValidUser=0
        EnteredUserID = self.UserIDInput.text()
        SelectedDepartment = self.DepartmentInput.currentText()
        EnteredPassword = self.PasswordInput.text()
        for index, row in AllLoginDetails.iterrows():
            if row.UserID==EnteredUserID:
                ValidUser=1
                if row.Department==SelectedDepartment:
                    if str(row.Password)==EnteredPassword:
                        self.InfoOutput.setText(_translate("LogInWindow","Loggin In..."))
                        if row.Department=="Admin":
                            AdminOptions.show()
                            LogInWindow.close() 
                        else:
                            RequestWindow.show()
                            LogInWindow.close()
                    else:
                        self.InfoOutput.setText(_translate("LogInWindow", 
                                "Enter a valid Password for the mentioned User!!!"))
                else:
                    self.InfoOutput.setText(_translate("LogInWindow",
                                "Entered user is not available in Selected Department!!!"))
        if ValidUser==0:
            self.InfoOutput.setText(_translate("LogInWindow","Enter a valid user ID!!!"))
            print("Enter a valid username")

#Configuring AdminOptions
class Ui_AdminOptions(object):
    def setupUi(self, AdminOptions):
        AdminOptions.setObjectName("AdminOptions")
        AdminOptions.resize(391, 164)
        self.centralwidget = QtWidgets.QWidget(AdminOptions)
        self.centralwidget.setObjectName("centralwidget")
        self.AddStockButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddStockButton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.AddStockButton.setObjectName("AddStockButton")
        self.ViewRequestButton = QtWidgets.QPushButton(self.centralwidget)
        self.ViewRequestButton.setGeometry(QtCore.QRect(140, 50, 91, 23))
        self.ViewRequestButton.setObjectName("ViewRequestButton")
        self.StockDetailsButton = QtWidgets.QPushButton(self.centralwidget)
        self.StockDetailsButton.setGeometry(QtCore.QRect(280, 50, 91, 23))
        self.StockDetailsButton.setObjectName("StockDetailsButton")
        self.LogoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogoutButton.setGeometry(QtCore.QRect(140, 90, 91, 23))
        self.LogoutButton.setObjectName("LogoutButton")
        AdminOptions.setCentralWidget(self.centralwidget)

        self.AddStockButton.clicked.connect(self.AddStockButtonPressed)
        self.ViewRequestButton.clicked.connect(self.ViewRequestButtonPressed)
        self.StockDetailsButton.clicked.connect(self.StockDetailsButtonPressed)
        self.LogoutButton.clicked.connect(self.LogoutButtonPressed)

        self.retranslateUi(AdminOptions)
        QtCore.QMetaObject.connectSlotsByName(AdminOptions)

    def retranslateUi(self, AdminOptions):
        _translate = QtCore.QCoreApplication.translate
        AdminOptions.setWindowTitle(_translate("AdminOptions", "AdminOptions"))
        self.AddStockButton.setText(_translate("AdminOptions", "AddStock"))
        self.ViewRequestButton.setText(_translate("AdminOptions", "View Requests"))
        self.StockDetailsButton.setText(_translate("AdminOptions", "Stock Details"))
        self.LogoutButton.setText(_translate("AdminOptions", "Logout"))

        
    def AddStockButtonPressed(self):
        AddWindow.show()
        AdminOptions.close()
        
    def ViewRequestButtonPressed(self):
        ViewRequestWindow.show()
        AdminOptions.close()
        
    def StockDetailsButtonPressed(self):
        StockDetailsWindow.show()
        AdminOptions.close()
        
    def LogoutButtonPressed(self):
        LogInWindow.show()
        AdminOptions.close()

#Configuring AddWindow
class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(493, 397)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MaerialLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaerialLabel.setGeometry(QtCore.QRect(100, 100, 51, 21))
        self.MaerialLabel.setObjectName("MaerialLabel")
        self.NumberLablel = QtWidgets.QLabel(self.centralwidget)
        self.NumberLablel.setGeometry(QtCore.QRect(100, 140, 47, 13))
        self.NumberLablel.setObjectName("NumberLablel")
        self.PartNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PartNoLabel.setGeometry(QtCore.QRect(100, 180, 61, 16))
        self.PartNoLabel.setObjectName("PartNoLabel")
        self.DateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DateLabel.setGeometry(QtCore.QRect(100, 60, 61, 16))
        self.DateLabel.setObjectName("DateLabel")
        self.DeptLabel = QtWidgets.QLabel(self.centralwidget)
        self.DeptLabel.setGeometry(QtCore.QRect(100, 220, 61, 16))
        self.DeptLabel.setObjectName("DeptLabel")
        self.MaterialInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MaterialInput.setGeometry(QtCore.QRect(200, 100, 113, 20))
        self.MaterialInput.setObjectName("MaterialInput")
        self.NumberInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NumberInput.setGeometry(QtCore.QRect(200, 140, 113, 20))
        self.NumberInput.setObjectName("NumberInput")
        self.PartNoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PartNoInput.setGeometry(QtCore.QRect(200, 180, 113, 20))
        self.PartNoInput.setObjectName("PartNoInput")
        self.DeptInput = QtWidgets.QLineEdit(self.centralwidget)
        self.DeptInput.setGeometry(QtCore.QRect(200, 220, 113, 20))
        self.DeptInput.setObjectName("DeptInput")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(330, 300, 61, 23))
        self.AddButton.setObjectName("AddButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(260, 300, 61, 23))
        self.BackButton.setObjectName("BackButton")
        self.UnitLabel = QtWidgets.QLabel(self.centralwidget)
        self.UnitLabel.setGeometry(QtCore.QRect(350, 240, 21, 16))
        self.UnitLabel.setObjectName("UnitLabel")
        self.QuantityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.QuantityInput.setGeometry(QtCore.QRect(200, 260, 113, 20))
        self.QuantityInput.setObjectName("QuantityInput")
        self.QuantityLabel = QtWidgets.QLabel(self.centralwidget)
        self.QuantityLabel.setGeometry(QtCore.QRect(100, 260, 61, 16))
        self.QuantityLabel.setObjectName("QuantityLabel")
        self.UnitInput = QtWidgets.QComboBox(self.centralwidget)
        self.UnitInput.setGeometry(QtCore.QRect(330, 260, 61, 21))
        self.UnitInput.setObjectName("UnitInput")
        self.UnitInput.addItem("")
        self.UnitInput.addItem("")
        self.UnitInput.addItem("")
        self.DateInput = QtWidgets.QDateEdit(self.centralwidget)
        self.DateInput.setGeometry(QtCore.QRect(200, 60, 111, 22))
        self.DateInput.setObjectName("DateInput")
        AddWindow.setCentralWidget(self.centralwidget)

        self.AddButton.clicked.connect(self.AddButtonPressed)
        self.BackButton.clicked.connect(self.BackButtonPressed)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "AddWindow"))
        self.MaerialLabel.setText(_translate("AddWindow", "Material"))
        self.NumberLablel.setText(_translate("AddWindow", "Number"))
        self.PartNoLabel.setText(_translate("AddWindow", "Part Number"))
        self.DateLabel.setText(_translate("AddWindow", "Date"))
        self.DeptLabel.setText(_translate("AddWindow", "Supplier"))
        self.AddButton.setText(_translate("AddWindow", "Add"))
        self.UnitLabel.setText(_translate("AddWindow", "Unit"))
        self.QuantityLabel.setText(_translate("AddWindow", "Quantity"))
        self.UnitInput.setItemText(0, _translate("AddWindow", "Kgs"))
        self.UnitInput.setItemText(1, _translate("AddWindow", "Litres"))
        self.UnitInput.setItemText(2, _translate("AddWindow", "Nos"))
        self.BackButton.setText(_translate("MainWindow", "Back"))

    def AddButtonPressed(self):
        print("Add Button Pressed")
    
    def BackButtonPressed(self):
        AdminOptions.show()
        AddWindow.close()

#Configuring StockDetailsWindow        
class Ui_StockDetailsWindow(object):
    def setupUi(self, StockDetailsWindow):
        StockDetailsWindow.setObjectName("StockDetailsWindow")
        StockDetailsWindow.resize(296, 213)
        self.centralwidget = QtWidgets.QWidget(StockDetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MaerialLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaerialLabel.setGeometry(QtCore.QRect(50, 40, 51, 21))
        self.MaerialLabel.setObjectName("MaerialLabel")
        self.PartNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PartNoLabel.setGeometry(QtCore.QRect(50, 120, 61, 16))
        self.PartNoLabel.setObjectName("PartNoLabel")
        self.NumberLablel = QtWidgets.QLabel(self.centralwidget)
        self.NumberLablel.setGeometry(QtCore.QRect(50, 80, 47, 13))
        self.NumberLablel.setObjectName("NumberLablel")
        self.MaterialInput = QtWidgets.QComboBox(self.centralwidget)
        self.MaterialInput.setGeometry(QtCore.QRect(150, 40, 111, 22))
        self.MaterialInput.setObjectName("MaterialInput")
        self.NumberInput = QtWidgets.QComboBox(self.centralwidget)
        self.NumberInput.setGeometry(QtCore.QRect(150, 80, 111, 22))
        self.NumberInput.setObjectName("NumberInput")
        self.PartNoInput = QtWidgets.QComboBox(self.centralwidget)
        self.PartNoInput.setGeometry(QtCore.QRect(150, 120, 111, 22))
        self.PartNoInput.setObjectName("PartNoInput")
        self.ProceedButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProceedButton.setGeometry(QtCore.QRect(190, 160, 75, 23))
        self.ProceedButton.setObjectName("ProceedButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.BackButton.setObjectName("BackButton")
        StockDetailsWindow.setCentralWidget(self.centralwidget)

        self.ProceedButton.clicked.connect(self.ProceedButtonPressed)
        self.BackButton.clicked.connect(self.BackButtonPressed)
        
        for Materials in AllStock["Material"]:
            self.MaterialInput.addItem(Materials)
        
        self.retranslateUi(StockDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(StockDetailsWindow)

    def retranslateUi(self, StockDetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        StockDetailsWindow.setWindowTitle(_translate("StockDetailsWindow", "StockDetailsWindow"))
        self.MaerialLabel.setText(_translate("StockDetailsWindow", "Material"))
        self.PartNoLabel.setText(_translate("StockDetailsWindow", "Part Number"))
        self.NumberLablel.setText(_translate("StockDetailsWindow", "Number"))
        self.ProceedButton.setText(_translate("StockDetailsWindow", "Proceed"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        
    def ProceedButtonPressed(self):
        print("ProceedButtonPressed")
    
    def BackButtonPressed(self):
        AdminOptions.show()
        StockDetailsWindow.close()

#Configuring ViewRequestWindow        
class Ui_ViewRequestWindow(object):
    def setupUi(self, ViewRequestWindow):
        ViewRequestWindow.setObjectName("ViewRequestWindow")
        ViewRequestWindow.resize(540, 295)
        self.centralwidget = QtWidgets.QWidget(ViewRequestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MaterialLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaterialLabel.setGeometry(QtCore.QRect(30, 50, 61, 20))
        self.MaterialLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MaterialLabel.setObjectName("MaterialLabel")
        self.MaterialDisplay = QtWidgets.QLabel(self.centralwidget)
        self.MaterialDisplay.setGeometry(QtCore.QRect(30, 90, 61, 20))
        self.MaterialDisplay.setText("")
        self.MaterialDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.MaterialDisplay.setObjectName("MaterialDisplay")
        self.NumberDiasplay = QtWidgets.QLabel(self.centralwidget)
        self.NumberDiasplay.setGeometry(QtCore.QRect(110, 90, 51, 16))
        self.NumberDiasplay.setText("")
        self.NumberDiasplay.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberDiasplay.setObjectName("NumberDiasplay")
        self.NumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumberLabel.setGeometry(QtCore.QRect(110, 50, 51, 16))
        self.NumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NumberLabel.setObjectName("NumberLabel")
        self.PartNoDisplay = QtWidgets.QLabel(self.centralwidget)
        self.PartNoDisplay.setGeometry(QtCore.QRect(180, 90, 61, 16))
        self.PartNoDisplay.setText("")
        self.PartNoDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.PartNoDisplay.setObjectName("PartNoDisplay")
        self.PartNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PartNoLabel.setGeometry(QtCore.QRect(180, 50, 61, 16))
        self.PartNoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PartNoLabel.setObjectName("PartNoLabel")
        self.ReqQtyDisplay = QtWidgets.QLabel(self.centralwidget)
        self.ReqQtyDisplay.setGeometry(QtCore.QRect(270, 90, 101, 16))
        self.ReqQtyDisplay.setText("")
        self.ReqQtyDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.ReqQtyDisplay.setObjectName("ReqQtyDisplay")
        self.ReqQtyLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReqQtyLabel.setGeometry(QtCore.QRect(270, 50, 101, 16))
        self.ReqQtyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ReqQtyLabel.setObjectName("ReqQtyLabel")
        self.AvlQtyDisplay = QtWidgets.QLabel(self.centralwidget)
        self.AvlQtyDisplay.setGeometry(QtCore.QRect(400, 90, 101, 16))
        self.AvlQtyDisplay.setText("")
        self.AvlQtyDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.AvlQtyDisplay.setObjectName("AvlQtyDisplay")
        self.AvlQtyLabel = QtWidgets.QLabel(self.centralwidget)
        self.AvlQtyLabel.setGeometry(QtCore.QRect(400, 50, 101, 16))
        self.AvlQtyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AvlQtyLabel.setObjectName("AvlQtyLabel")
        self.AppQtyInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AppQtyInput.setGeometry(QtCore.QRect(300, 200, 71, 20))
        self.AppQtyInput.setObjectName("AppQtyInput")
        self.AppQtyLabel = QtWidgets.QLabel(self.centralwidget)
        self.AppQtyLabel.setGeometry(QtCore.QRect(280, 180, 101, 16))
        self.AppQtyLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AppQtyLabel.setObjectName("AppQtyLabel")
        self.ApproveButton = QtWidgets.QPushButton(self.centralwidget)
        self.ApproveButton.setGeometry(QtCore.QRect(420, 200, 75, 23))
        self.ApproveButton.setObjectName("ApproveButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(30, 190, 75, 23))
        self.BackButton.setObjectName("BackButton")
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setGeometry(QtCore.QRect(300, 140, 61, 23))
        self.NextButton.setObjectName("NextButton")
        self.PrevButton = QtWidgets.QPushButton(self.centralwidget)
        self.PrevButton.setGeometry(QtCore.QRect(170, 140, 61, 23))
        self.PrevButton.setObjectName("PrevButton")
        self.Progress = QtWidgets.QLabel(self.centralwidget)
        self.Progress.setGeometry(QtCore.QRect(240, 140, 51, 21))
        self.Progress.setText("")
        self.Progress.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress.setObjectName("Progress")
        self.ApprovePartlyRB = QtWidgets.QRadioButton(self.centralwidget)
        self.ApprovePartlyRB.setGeometry(QtCore.QRect(161, 180, 111, 20))
        self.ApprovePartlyRB.setObjectName("ApprovePartlyRB")
        self.ApproveFullyRB = QtWidgets.QRadioButton(self.centralwidget)
        self.ApproveFullyRB.setGeometry(QtCore.QRect(161, 200, 111, 20))
        self.ApproveFullyRB.setObjectName("ApproveFullyRB")
        ViewRequestWindow.setCentralWidget(self.centralwidget)

        self.BackButton.clicked.connect(self.BackButtonPressed)
        self.NextButton.clicked.connect(self.NextButtonPressed)
        self.PrevButton.clicked.connect(self.PrevButtonPressed)
        self.ApproveButton.clicked.connect(self.ApproveButtonPressed)
        
        Requests=pd.read_csv("Requests.csv")
        nrows=Requests.shape[0]
        #print(nrows)
        nrowsstr=str(nrows)
        if nrows==0:
            self.Progress.setText("0/0")
            self.MaterialDisplay.setText("")
            self.NumberDiasplay.setText("")
            self.PartNoDisplay.setText("")
            self.ReqQtyDisplay.setText("")
            self.AvlQtyDisplay.setText("")
            
        #print(nrowsstr)    
        for index, row in Requests.iterrows():
            if index==0:
                indexstr=str(index+1)
                #print(indexstr)
                #print(indexstr+"/"+nrowsstr)
                self.Progress.setText(indexstr+"/"+nrowsstr)
        self.MaterialDisplay.setText("")
        
        
        self.retranslateUi(ViewRequestWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewRequestWindow)

    def retranslateUi(self, ViewRequestWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewRequestWindow.setWindowTitle(_translate("ViewRequestWindow", "ViewRequestWindow"))
        self.MaterialLabel.setText(_translate("ViewRequestWindow", "Material"))
        self.NumberLabel.setText(_translate("ViewRequestWindow", "Number"))
        self.PartNoLabel.setText(_translate("ViewRequestWindow", "Part Number"))
        self.ReqQtyLabel.setText(_translate("ViewRequestWindow", "Requested Quantity"))
        self.AvlQtyLabel.setText(_translate("ViewRequestWindow", "Available Quantity"))
        self.AppQtyLabel.setText(_translate("ViewRequestWindow", "Approve  Quantity"))
        self.ApproveButton.setText(_translate("ViewRequestWindow", "Approve"))
        self.BackButton.setText(_translate("ViewRequestWindow", "Back"))
        self.NextButton.setText(_translate("ViewRequestWindow", "Next"))
        self.PrevButton.setText(_translate("ViewRequestWindow", "Prev"))
        self.ApprovePartlyRB.setText(_translate("MainWindow", "Approve Partly"))
        self.ApproveFullyRB.setText(_translate("MainWindow", "Approve Fully"))

    def BackButtonPressed(self):
        AdminOptions.show()
        ViewRequestWindow.close()
    
    def NextButtonPressed(self):
        print("NextButtonPressed")
    
    def PrevButtonPressed(self):
        print("PrevButtonPressed")
    
    def ApproveButtonPressed(self):
        if self.ApprovePartlyRB.isChecked():
            print("Part")
        elif self.ApproveFullyRB.isChecked():
            print("Full")
        #print("ApproveButtonPressed")    

#Configuring RequestWindow  
class Ui_RequestWindow(object):
    def setupUi(self, RequestWindow):
        RequestWindow.setObjectName("RequestWindow")
        RequestWindow.resize(520, 350)
        self.centralwidget = QtWidgets.QWidget(RequestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DateLabel = QtWidgets.QLabel(self.centralwidget)
        self.DateLabel.setGeometry(QtCore.QRect(80, 50, 61, 16))
        self.DateLabel.setObjectName("DateLabel")
        self.DateInput = QtWidgets.QDateEdit(self.centralwidget)
        self.DateInput.setGeometry(QtCore.QRect(180, 50, 111, 22))
        self.DateInput.setObjectName("DateInput")
        self.MaerialLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaerialLabel.setGeometry(QtCore.QRect(80, 90, 51, 21))
        self.MaerialLabel.setObjectName("MaerialLabel")
        self.NumberInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NumberInput.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.NumberInput.setObjectName("NumberInput")
        self.NumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.NumberLabel.setGeometry(QtCore.QRect(80, 130, 51, 21))
        self.NumberLabel.setObjectName("NumberLabel")
        self.PartNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PartNoLabel.setGeometry(QtCore.QRect(80, 170, 61, 21))
        self.PartNoLabel.setObjectName("PartNoLabel")
        self.PartNoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PartNoInput.setGeometry(QtCore.QRect(180, 170, 113, 20))
        self.PartNoInput.setText("")
        self.PartNoInput.setObjectName("PartNoInput")
        self.QuantityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.QuantityInput.setGeometry(QtCore.QRect(180, 210, 113, 20))
        self.QuantityInput.setObjectName("QuantityInput")
        self.QuantityLabel = QtWidgets.QLabel(self.centralwidget)
        self.QuantityLabel.setGeometry(QtCore.QRect(80, 210, 61, 16))
        self.QuantityLabel.setObjectName("QuantityLabel")
        self.RequestButton = QtWidgets.QPushButton(self.centralwidget)
        self.RequestButton.setGeometry(QtCore.QRect(230, 280, 61, 23))
        self.RequestButton.setObjectName("RequestButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(80, 280, 61, 23))
        self.BackButton.setObjectName("BackButton")
        self.MaterialInput = QtWidgets.QComboBox(self.centralwidget)
        self.MaterialInput.setGeometry(QtCore.QRect(180, 90, 111, 22))
        self.MaterialInput.setObjectName("MaterialInput")
        self.UnitLabel = QtWidgets.QLabel(self.centralwidget)
        self.UnitLabel.setGeometry(QtCore.QRect(80, 240, 211, 21))
        self.UnitLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UnitLabel.setObjectName("UnitLabel")
        self.UpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateButton.setGeometry(QtCore.QRect(160, 280, 61, 23))
        self.UpdateButton.setObjectName("UpdateButton")
        RequestWindow.setCentralWidget(self.centralwidget)
        
        for Materials in AllStock["Material"]:
            self.MaterialInput.addItem(Materials)
                
        self.BackButton.clicked.connect(self.BackButtonPressed)
        self.RequestButton.clicked.connect(self.RequestButtonPressed)
        self.UpdateButton.clicked.connect(self.UpdateButtonPressed)
        
        self.retranslateUi(RequestWindow)
        QtCore.QMetaObject.connectSlotsByName(RequestWindow)

    def retranslateUi(self, RequestWindow):
        _translate = QtCore.QCoreApplication.translate
        RequestWindow.setWindowTitle(_translate("RequestWindow", "RequestWindow"))
        self.DateLabel.setText(_translate("RequestWindow", "Date"))
        self.MaerialLabel.setText(_translate("RequestWindow", "Material"))
        self.NumberLabel.setText(_translate("RequestWindow", "Number"))
        self.PartNoLabel.setText(_translate("RequestWindow", "Part Number"))
        self.UnitLabel.setText(_translate("RequestWindow", "Click Update after selecting Material"))
        self.QuantityLabel.setText(_translate("RequestWindow", "Quantity"))
        self.RequestButton.setText(_translate("MainWindow", "Request"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.UpdateButton.setText(_translate("MainWindow", "Update"))
        
    def BackButtonPressed(self):
        LogInWindow.show()
        RequestWindow.close()
        
    def UpdateButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.SelectedMaterial = self.MaterialInput.currentText()
        for index, row in AllStock.iterrows():
            if row.Material==self.SelectedMaterial:
                self.UnitLabel.setText(row.Units)
                self.NumberInput.setText(_translate("MainWindow", str(row.Number)))
                self.PartNoInput.setText(_translate("MainWindow", str(row.PartNumber)))
                
        
    def RequestButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        self.SelectedMaterial = self.MaterialInput.currentText()
        self.EnteredQuantity = self.QuantityInput.text()
        self.SelectedDate = str(self.DateInput.date())
        #print(self.SelectedDate[19:-1])
        Requests=pd.read_csv("Requests.csv")
        for index, row in AllStock.iterrows():
            if row.Material==self.SelectedMaterial:
                Requests=Requests.append({'Date': self.SelectedDate[19:-1], 
                                              'Material': row.Material,
                                              'Number': row.Number,
                                              'PartNumber' : row.PartNumber,
                                              'Quantity' : self.EnteredQuantity,
                                              'Units' : row.Units}, ignore_index=True)
                Requests.to_csv("Requests.csv",index=False)
                self.UnitLabel.setText("Click Update after selecting Material")
                self.NumberInput.setText(_translate("MainWindow", ""))
                self.PartNoInput.setText(_translate("MainWindow", ""))
                

if __name__ == "__main__":
    AllLoginDetails=pd.read_excel("input.xlsx","Login")
    GroupedLoginDetails=AllLoginDetails.groupby("Department")
    AllStock=pd.read_excel("input.xlsx","Stock")
    AllRequest=pd.read_excel("input.xlsx","Requests")
    #AvailableStocks=
    #print(GroupedLoginDetails[["Password"]].get_group('Lab'))
    #for Department,Department_df in GroupedLoginDetails:
    #    print(Department)
    #    print(Department_df)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogInWindow = QtWidgets.QMainWindow()
    ui1 = Ui_LogInWindow()
    ui1.setupUi(LogInWindow)
    AddWindow = QtWidgets.QMainWindow()
    ui2 = Ui_AddWindow()
    ui2.setupUi(AddWindow)
    AdminOptions = QtWidgets.QMainWindow()
    ui3 = Ui_AdminOptions()
    ui3.setupUi(AdminOptions)
    StockDetailsWindow = QtWidgets.QMainWindow()
    ui4 = Ui_StockDetailsWindow()
    ui4.setupUi(StockDetailsWindow)
    ViewRequestWindow = QtWidgets.QMainWindow()
    ui5 = Ui_ViewRequestWindow()
    ui5.setupUi(ViewRequestWindow)
    RequestWindow = QtWidgets.QMainWindow()
    ui6 = Ui_RequestWindow()
    ui6.setupUi(RequestWindow)
    LogInWindow.show()
    sys.exit(app.exec_())