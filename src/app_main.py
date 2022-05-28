from PyQt5.QtWidgets import QApplication
import sys

from views.main import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainView()
    sys.exit(app.exec_())

