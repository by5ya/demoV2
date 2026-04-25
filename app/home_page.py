from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main import MainWin

class HomePage(QFrame):
    def __init__(self, controller: MainWin, user: dict):
        super().__init__()
        self.controller = controller
        self.db = self.controller.db
        self.user = user

        self.setupUi(self)
        self.controller.setWindowTitle("Каталог товаров")

        self.fio_label.setText(self.user['fio'])

        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.addStretch()
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_layout.setSpacing(10)

        self.refresh()
        self.logout_pushButton.clicked.connect(self.logount)

    def logount(self):
        from login_page import LoginPage
        self.controller.switch_frame(LoginPage)

    def refresh(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        products = self.db.get_products()
        print(products)
        if products:
            for product in products:
                from product_card import ProductCard
                product_card_item = ProductCard(self.controller, product)
                self.scroll_layout.addWidget(product_card_item)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(869, 589)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:rgb(127, 255, 0)")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logout_pushButton = QPushButton(self.widget)
        self.logout_pushButton.setObjectName(u"logout_pushButton")
        self.logout_pushButton.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.horizontalLayout.addWidget(self.logout_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.fio_label = QLabel(self.widget)
        self.fio_label.setObjectName(u"fio_label")

        self.horizontalLayout.addWidget(self.fio_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.order_pushButton_2 = QPushButton(self.widget)
        self.order_pushButton_2.setObjectName(u"order_pushButton_2")
        self.order_pushButton_2.setVisible(False) if self.user['role'] in ['Гость', "Авторизаванный клиент"] else self.order_pushButton_2.setVisible(True)
        self.order_pushButton_2.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.horizontalLayout_2.addWidget(self.order_pushButton_2)

        self.add_pushButton_3 = QPushButton(self.widget)
        self.add_pushButton_3.setVisible(False) if self.user['role'] in ['Гость', "Авторизаванный клиент"] else self.add_pushButton_3.setVisible(True)
        self.add_pushButton_3.setObjectName(u"add_pushButton_3")
        self.add_pushButton_3.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.horizontalLayout_2.addWidget(self.add_pushButton_3)

        self.filt_comboBox = QComboBox(self.widget)
        self.filt_comboBox.setObjectName(u"filt_comboBox")
        self.filt_comboBox.setVisible(False) if self.user['role'] in ['Гость', "Авторизаванный клиент"] else self.filt_comboBox.setVisible(True)
        self.filt_comboBox.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.horizontalLayout_2.addWidget(self.filt_comboBox)

        self.sort_comboBox_2 = QComboBox(self.widget)
        self.sort_comboBox_2.setObjectName(u"sort_comboBox_2")
        self.sort_comboBox_2.setVisible(False) if self.user['role'] in ['Гость', "Авторизаванный клиент"] else self.sort_comboBox_2.setVisible(True)
        self.sort_comboBox_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.horizontalLayout_2.addWidget(self.sort_comboBox_2)

        self.search_lineEdit = QLineEdit(self.widget)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.search_lineEdit.setVisible(False) if self.user['role'] in ['Гость', "Авторизаванный клиент"] else self.search_lineEdit.setVisible(True)
        self.search_lineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.horizontalLayout_2.addWidget(self.search_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.widget)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 847, 495))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logout_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.fio_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.order_pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.add_pushButton_3.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
    # retranslateUi

