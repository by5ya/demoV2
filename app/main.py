import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from database import Database

from pathlib import Path

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Database()

        self.base_path = Path(__file__).parent.parent / "import"

        self.setMinimumSize(600, 800)
        self.frame_container = QStackedWidget()
        self.setCentralWidget(self.frame_container)

        from login_page import LoginPage
        self.switch_frame(LoginPage)



    def switch_frame(self, target, **kwargs):
        goal = target(self, **kwargs)
        if isinstance(goal,QDialog):
            return goal.exec()
        else:
            self.frame_container.addWidget(goal)
            self.frame_container.setCurrentWidget(goal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_path = Path(__file__).parent.parent
    app.setWindowIcon(QPixmap(str(base_path/"import"/"Icon.png")))
    app.setFont("Times New Roman")

    main = MainWin()
    main.show()

    sys.exit(app.exec())
