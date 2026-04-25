from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main import MainWin

class LoginPage(QFrame):
    def __init__(self, controller: MainWin, /):
        super().__init__()
        self.controller = controller
        self.db = self.controller.db

        self.setupUi(self)
        self.controller.setWindowTitle("Авторизация")
        self.pic_label_4.setPixmap(QPixmap(str(self.controller.base_path/"Icon.png")))
        self.pic_label_4.setMaximumSize(250, 250)

        self.entry_pushButton.clicked.connect(self.entry)
        self.entry_g_pushButton_2.clicked.connect(self.entry_g)


    def entry(self):
        login = self.login_lineEdit.text()
        password = self.password_lineEdit_2.text()

        user = self.db.login_user(login, password)
        if user:
            from home_page import HomePage
            self.controller.switch_frame(HomePage, user=user)
        else:
            pass

    def entry_g(self):
        user = {
            "fio": "Гость",
            "role": "Гость"
        }
        from home_page import HomePage
        self.controller.switch_frame(HomePage, user=user)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(647, 515)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pic_label_4 = QLabel(Form)
        self.pic_label_4.setObjectName(u"pic_label_4")
        self.pic_label_4.setScaledContents(True)
        self.pic_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.pic_label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:#7FFF00")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.login_lineEdit = QLineEdit(self.widget)
        self.login_lineEdit.setObjectName(u"login_lineEdit")
        self.login_lineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.login_lineEdit)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.password_lineEdit_2 = QLineEdit(self.widget)
        self.password_lineEdit_2.setObjectName(u"password_lineEdit_2")
        self.password_lineEdit_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.password_lineEdit_2)

        self.entry_pushButton = QPushButton(self.widget)
        self.entry_pushButton.setObjectName(u"entry_pushButton")
        self.entry_pushButton.setStyleSheet(u"background-color:rgb(0, 250, 154)")

        self.verticalLayout.addWidget(self.entry_pushButton)

        self.entry_g_pushButton_2 = QPushButton(self.widget)
        self.entry_g_pushButton_2.setObjectName(u"entry_g_pushButton_2")
        self.entry_g_pushButton_2.setStyleSheet(u"background-color:#00FA9A")

        self.verticalLayout.addWidget(self.entry_g_pushButton_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pic_label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.entry_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.entry_g_pushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c", None))
    # retranslateUi


