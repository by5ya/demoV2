from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main import MainWin

class OrderPage(QDialog):
    def __init__(self, controller: MainWin, user: dict):
        super().__init__()
        self.controller = controller
        self.db = self.controller.db
        self.user = user

        self.setupUi(self)
        self.setWindowTitle("Заказы")

        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.addStretch()
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_layout.setSpacing(10)
        self.refresh()
        self.add_order_pushButton_2.clicked.connect(self.create_order)
        self.back_pushButton.clicked.connect(lambda : self.accept())

    def refresh(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        orders = self.db.get_orders()
        if orders:
            for order in orders:
                from order_card import OrderCard
                order_card_item = OrderCard(self.controller, order)
                self.scroll_layout.addWidget(order_card_item)
                order_card_item.clicked.connect(self.edit_order)

    def edit_order(self, order):
        if self.user['role'] == 'Администратор':
            from edit_create_order import EditCreateOrderPage
            result = self.controller.switch_frame(EditCreateOrderPage, order=order)
            if result == QDialog.Accepted:
                self.refresh()

    def create_order(self):
        from edit_create_order import EditCreateOrderPage
        result = self.controller.switch_frame(EditCreateOrderPage)
        if result == QDialog.Accepted:
            self.refresh()


    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(757, 513)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:rgb(127, 255, 0)")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_pushButton = QPushButton(self.widget)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.horizontalLayout.addWidget(self.back_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_order_pushButton_2 = QPushButton(self.widget)
        self.add_order_pushButton_2.setObjectName(u"add_order_pushButton_2")
        self.add_order_pushButton_2.setStyleSheet(u"background-color:rgb(0, 250, 154)")
        self.add_order_pushButton_2.setVisible(True) if self.user['role'] == 'Администратор' else  self.add_order_pushButton_2.setVisible(False)

        self.horizontalLayout.addWidget(self.add_order_pushButton_2)


        self.verticalLayout.addWidget(self.widget)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 735, 456))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.add_order_pushButton_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
    # retranslateUi



