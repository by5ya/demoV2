import os

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main import MainWin
import shutil
from messages import *
from datetime import datetime


from pathlib import Path

class EditCreateOrderPage(QDialog):
    def __init__(self, controller: MainWin, order=None):
        super().__init__()
        self.controller = controller
        self.db = self.controller.db
        self.setupUi(self)
        if order:
            self.setWindowTitle("Редактирование заказа")
            self.order = order
            self.edit = True
        else:
            self.setWindowTitle("Создание заказа")
            self.order = None
            self.edit = False
            self.del_pushButton_4.setVisible(False)

        statuses = self.db.get_distinct("status", "orders")
        self.status_comboBox.addItems(statuses)

        self.order_items = []

        products = self.db.get_products()
        for prod in products:
            self.prod_comboBox_2.addItem(f"{prod['name']} | {prod['articul']}", prod)

        if self.edit:
            self.articul_lineEdit.setText(self.order['articul'])
            self.date_order_dateEdit.setDate(self.order['date_order'])
            self.date_deliv_dateEdit_2.setDate(self.order['date_deliv'])
            self.status_comboBox.setCurrentText(self.order['status'])
            self.address_lineEdit.setText(self.order['address'])
            self.get_oi()
        self.add_prod_pushButton_2.clicked.connect(self.create_oi)
        self.del_prod_pushButton.clicked.connect(self.delete_oi)
        self.tableWidget.cellChanged.connect(self.edit_oi)
        self.del_pushButton_4.clicked.connect(self.delete_order)
        self.back_pushButton_5.clicked.connect(lambda: self.reject())
        self.save_pushButton_3.clicked.connect(self.save)


    def create_oi(self):
        product = self.prod_comboBox_2.currentData()
        quantity = self.quantity_spinBox.value()

        existing_item = None
        for item in self.order_items:
            if item['product_articul'] == product['articul'] and item['flag'] != 'delete':
                existing_item = item
                break

        if existing_item is None:
            if product['articul'] not in self.order_items:
                self.order_items.append({
                    "flag": "new",
                    "quantity": quantity,
                    "product_name": product['name'],
                    "product_id": product['id'],
                    "product_articul": product['articul'],
                })

        self.set_order_items()

    def delete_oi(self):
        row = self.tableWidget.currentRow()
        product = self.order_items[row]
        if product['flag'] == 'new':
            self.order_items.remove(product)
        else:
            self.order_items.remove(product)
            product['flag'] = "delete"
        self.set_order_items()

    def edit_oi(self):
        row = self.tableWidget.currentRow()
        print(row)
        column = self.tableWidget.currentColumn()
        if column != 3:
            return

        product = self.order_items[row]
        product['quantity'] = int(str(self.tableWidget.currentItem().text()))
        if product['flag'] not in ['new', 'delete']:
            product['flag'] = 'edited'

        self.set_order_items()

    def generate_articul(self):
        articul = [f"{prod['product_articul']}, {prod['quantity']}" for prod in self.order_items]
        self.articul_lineEdit.setText(",".join(articul))

    def delete_order(self):
        if warn_yes_no("Вы действительно хотите удалить заказ?"):
            self.db.delete_order(self.order['id'])
            self.accept()

    def check(self):
        return all([self.address_lineEdit.text(), self.articul_lineEdit.text()])

    def save(self):
        if self.check():
            order = {
                "articul": self.articul_lineEdit.text(),
                "date_delivery": self.date_deliv_dateEdit_2.date().toPython(),
                "date_order": self.date_order_dateEdit.date().toPython(),
                "address": self.address_lineEdit.text(),
                "status": self.status_comboBox.currentText()
            }

            create_items = [oi for oi in self.order_items if oi['flag'] == 'new']
            delete_items = [oi for oi in self.order_items if oi['flag'] == 'delete']
            edit_items = [oi for oi in self.order_items if oi['flag'] == 'edited']
            if self.edit:
                id = self.order['id']
                self.db.update_order(order, id)
                info_ok("Заказ успешно обновлен")
            else:
                id = self.db.create_order(order)
                info_ok("Заказ успешно создан")

            for create_item in create_items:
                self.db.create_order_item(create_item, id)
            for delete_item in delete_items:
                self.db.delete_order_item(delete_item['id'])
            for edit_item in edit_items:
                self.db.update_order_item(edit_item, edit_item['id'])

            self.accept()


    def get_oi(self):
        self.order_items = self.db.get_order_items(self.order['id'])
        self.set_order_items()

    def set_order_items(self):
        self.tableWidget.setRowCount(len(self.order_items))

        self.tableWidget.blockSignals(True)

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Наименование', "Артикул", "Количество"])

        self.tableWidget.setColumnHidden(0, True)
        print(self.order_items)

        for row, item in enumerate(self.order_items):
            if item['flag'] != 'delete':
                if item.get('id'):
                    ceilId = QTableWidgetItem(str(item['id']))
                    self.tableWidget.setItem(row, 0, ceilId)

                ceilName = QTableWidgetItem(item['product_name'])
                ceilName.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.tableWidget.setItem(row, 1, ceilName)

                ceilArticul = QTableWidgetItem(item['product_articul'])
                ceilArticul.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.tableWidget.setItem(row, 2, ceilArticul)

                ceilQuantity = QTableWidgetItem(str(item['quantity']))
                self.tableWidget.setItem(row, 3, ceilQuantity)
        self.tableWidget.blockSignals(False)
        self.generate_articul()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(891, 810)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.articul_lineEdit = QLineEdit(Form)
        self.articul_lineEdit.setObjectName(u"articul_lineEdit")

        self.address_lineEdit = QLineEdit(Form)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.address_lineEdit)

        self.label_1234 = QLabel(Form)
        self.label_1234.setObjectName(u"label_4")
        self.label_1234.setText("Адрес")
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_1234)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.articul_lineEdit)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.status_comboBox = QComboBox(Form)
        self.status_comboBox.setObjectName(u"status_comboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.status_comboBox)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.date_order_dateEdit = QDateEdit(Form)
        self.date_order_dateEdit.setObjectName(u"date_order_dateEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.date_order_dateEdit)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.date_deliv_dateEdit_2 = QDateEdit(Form)
        self.date_deliv_dateEdit_2.setObjectName(u"date_deliv_dateEdit_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.date_deliv_dateEdit_2)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.wid1 = QWidget(Form)
        self.wid1.setObjectName(u"wid1")
        self.wid1.setStyleSheet(u"#wid1{background-color:rgb(127, 255, 0)}")
        self.verticalLayout_2 = QVBoxLayout(self.wid1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.wid1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prod_comboBox_2 = QComboBox(self.wid1)
        self.prod_comboBox_2.setObjectName(u"prod_comboBox_2")

        self.horizontalLayout_2.addWidget(self.prod_comboBox_2)

        self.quantity_spinBox = QSpinBox(self.wid1)
        self.quantity_spinBox.setObjectName(u"quantity_spinBox")

        self.horizontalLayout_2.addWidget(self.quantity_spinBox)

        self.add_prod_pushButton_2 = QPushButton(self.wid1)
        self.add_prod_pushButton_2.setObjectName(u"add_prod_pushButton_2")
        self.add_prod_pushButton_2.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.horizontalLayout_2.addWidget(self.add_prod_pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.wid1)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(4)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.del_prod_pushButton = QPushButton(self.wid1)
        self.del_prod_pushButton.setObjectName(u"del_prod_pushButton")
        self.del_prod_pushButton.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.horizontalLayout.addWidget(self.del_prod_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.wid1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.save_pushButton_3 = QPushButton(Form)
        self.save_pushButton_3.setObjectName(u"save_pushButton_3")
        self.save_pushButton_3.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout_3.addWidget(self.save_pushButton_3)

        self.del_pushButton_4 = QPushButton(Form)
        self.del_pushButton_4.setObjectName(u"del_pushButton_4")
        self.del_pushButton_4.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout_3.addWidget(self.del_pushButton_4)

        self.back_pushButton_5 = QPushButton(Form)
        self.back_pushButton_5.setObjectName(u"back_pushButton_5")
        self.back_pushButton_5.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout_3.addWidget(self.back_pushButton_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430 \u0432 \u0437\u0430\u043a\u0430\u0437", None))
        self.add_prod_pushButton_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.del_prod_pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.save_pushButton_3.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.del_pushButton_4.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.back_pushButton_5.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

