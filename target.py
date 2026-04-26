# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_create_prod.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(845, 742)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:rgb(127, 255, 0)")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pic_label_11 = QLabel(self.widget)
        self.pic_label_11.setObjectName(u"pic_label_11")
        self.pic_label_11.setMaximumSize(QSize(300, 200))
        self.pic_label_11.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.pic_label_11.setScaledContents(True)
        self.pic_label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.pic_label_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.load_pushButton = QPushButton(self.widget)
        self.load_pushButton.setObjectName(u"load_pushButton")
        self.load_pushButton.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout.addWidget(self.load_pushButton)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.name_lineEdit = QLineEdit(Form)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.name_lineEdit)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.unit_lineEdit_2 = QLineEdit(Form)
        self.unit_lineEdit_2.setObjectName(u"unit_lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.unit_lineEdit_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.cat_comboBox = QComboBox(Form)
        self.cat_comboBox.setObjectName(u"cat_comboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cat_comboBox)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.prod_comboBox_2 = QComboBox(Form)
        self.prod_comboBox_2.setObjectName(u"prod_comboBox_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.prod_comboBox_2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.desc_plainTextEdit = QPlainTextEdit(Form)
        self.desc_plainTextEdit.setObjectName(u"desc_plainTextEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.desc_plainTextEdit)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.quant_spinBox = QSpinBox(Form)
        self.quant_spinBox.setObjectName(u"quant_spinBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.quant_spinBox)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.disc_spinBox_2 = QSpinBox(Form)
        self.disc_spinBox_2.setObjectName(u"disc_spinBox_2")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.disc_spinBox_2)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.price_doubleSpinBox = QDoubleSpinBox(Form)
        self.price_doubleSpinBox.setObjectName(u"price_doubleSpinBox")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.price_doubleSpinBox)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.seller_lineEdit_3 = QLineEdit(Form)
        self.seller_lineEdit_3.setObjectName(u"seller_lineEdit_3")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.seller_lineEdit_3)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.articul_lineEdit_4 = QLineEdit(Form)
        self.articul_lineEdit_4.setObjectName(u"articul_lineEdit_4")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.articul_lineEdit_4)

        self.id_label_12 = QLabel(Form)
        self.id_label_12.setObjectName(u"id_label_12")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.id_label_12)

        self.id_lineEdit_6 = QLineEdit(Form)
        self.id_lineEdit_6.setObjectName(u"id_lineEdit_6")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.id_lineEdit_6)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.save_pushButton = QPushButton(Form)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout_2.addWidget(self.save_pushButton)

        self.del_pushButton_3 = QPushButton(Form)
        self.del_pushButton_3.setObjectName(u"del_pushButton_3")
        self.del_pushButton_3.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout_2.addWidget(self.del_pushButton_3)

        self.back_pushButton_2 = QPushButton(Form)
        self.back_pushButton_2.setObjectName(u"back_pushButton_2")
        self.back_pushButton_2.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout_2.addWidget(self.back_pushButton_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pic_label_11.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.load_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f \u0441\u043a\u0438\u0434\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.id_label_12.setText(QCoreApplication.translate("Form", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440", None))
        self.save_pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.del_pushButton_3.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.back_pushButton_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

