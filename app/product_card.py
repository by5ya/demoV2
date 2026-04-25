from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main import MainWin

class ProductCard(QFrame):
    def __init__(self, controller: MainWin, product: dict):
        super().__init__()
        self.controller = controller
        self.db = self.controller.db
        self.product = product

        self.setupUi(self)
        self.pic_label_8.setScaledContents(True)
        self.pic_label_8.setMaximumSize(200, 300)
        image = str( self.controller.base_path / str(self.product['photo']) )
        print(image)
        self.pic_label_8.setPixmap(QPixmap(str( self.controller.base_path / self.product['photo'] )))

        self.name_label.setText(f"{self.product['category']} | {self.product['name']}")
        self.producer_label_3.setText(f"Производитель: {self.product['producer']}")
        self.seller_label_4.setText(f"Поставщик: {self.product['seller']}")
        self.desc_label_2.setText(f"Описание товара: {self.product['description']}")
        self.unit_label_6.setText(f"Единица измерения: {self.product['unit']}")
        self.discount_label_9.setText(f"Действующая скидка: {self.product['discount']}%")
        self.quantity_label_7.setText(f"Количество на складе: {str(self.product['quantity'])}")

        price = float(self.product['price'])
        final_price = price - price * (float(self.product['discount']) / 100)
        self.price_label_5.setText(f"Цена: <s style='color: red;'>{price:.2f}</s> <span style='color: black; font-weight: bold;'>{final_price}</span>")

        if int(self.product['quantity']) == 0:
            self.quantity_label_7.setStyleSheet(u"background-color:blue")

        if int(self.product['discount']) > 15:
            self.setStyleSheet(u"background-color:#2E8B57")

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(778, 398)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pic_label_8 = QLabel(self.widget)
        self.pic_label_8.setObjectName(u"pic_label_8")

        self.horizontalLayout.addWidget(self.pic_label_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")

        self.verticalLayout.addWidget(self.name_label)

        self.desc_label_2 = QLabel(self.widget)
        self.desc_label_2.setObjectName(u"desc_label_2")

        self.verticalLayout.addWidget(self.desc_label_2)

        self.producer_label_3 = QLabel(self.widget)
        self.producer_label_3.setObjectName(u"producer_label_3")

        self.verticalLayout.addWidget(self.producer_label_3)

        self.seller_label_4 = QLabel(self.widget)
        self.seller_label_4.setObjectName(u"seller_label_4")

        self.verticalLayout.addWidget(self.seller_label_4)

        self.price_label_5 = QLabel(self.widget)
        self.price_label_5.setObjectName(u"price_label_5")

        self.verticalLayout.addWidget(self.price_label_5)

        self.unit_label_6 = QLabel(self.widget)
        self.unit_label_6.setObjectName(u"unit_label_6")

        self.verticalLayout.addWidget(self.unit_label_6)

        self.quantity_label_7 = QLabel(self.widget)
        self.quantity_label_7.setObjectName(u"quantity_label_7")

        self.verticalLayout.addWidget(self.quantity_label_7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.discount_label_9 = QLabel(self.widget)
        self.discount_label_9.setObjectName(u"discount_label_9")

        self.horizontalLayout.addWidget(self.discount_label_9)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pic_label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.desc_label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.producer_label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.seller_label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.price_label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.unit_label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.quantity_label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.discount_label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi


