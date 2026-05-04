from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main import MainWin

class OrderCard(QFrame):
    clicked = Signal(dict)
    def __init__(self, controller: MainWin, order: dict):
        super().__init__()
        self.controller = controller
        self.db = self.controller.db
        self.order = order

        self.setupUi(self)

        self.articul_label.setText(f"Артикул заказа: {self.order['articul']}")
        self.status_label_2.setText(f"Статус заказа: {self.order['status']}")
        self.address_label_3.setText(f"Адрес пункта выдачи: {self.order['address']}")
        self.date_order_label_4.setText(f"Дата заказа: {self.order['date_order']}")
        self.date_deliv_label_5.setText(f"Дата доставки: {self.order['date_deliv']}")

    def mousePressEvent(self, event, /):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.order)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 332)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wid = QWidget(Form)
        self.wid.setObjectName(u"wid")
        self.wid.setStyleSheet(u"#wid{\n"
                               "border:3px solid;\n"
                               "}")
        self.horizontalLayout = QHBoxLayout(self.wid)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.articul_label = QLabel(self.wid)
        self.articul_label.setObjectName(u"articul_label")

        self.verticalLayout.addWidget(self.articul_label)

        self.status_label_2 = QLabel(self.wid)
        self.status_label_2.setObjectName(u"status_label_2")

        self.verticalLayout.addWidget(self.status_label_2)

        self.address_label_3 = QLabel(self.wid)
        self.address_label_3.setObjectName(u"address_label_3")

        self.verticalLayout.addWidget(self.address_label_3)

        self.date_order_label_4 = QLabel(self.wid)
        self.date_order_label_4.setObjectName(u"date_order_label_4")

        self.verticalLayout.addWidget(self.date_order_label_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.wid)

        self.date_deliv_label_5 = QLabel(Form)
        self.date_deliv_label_5.setObjectName(u"date_deliv_label_5")

        self.horizontalLayout_2.addWidget(self.date_deliv_label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.articul_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.status_label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.address_label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.date_order_label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.date_deliv_label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

