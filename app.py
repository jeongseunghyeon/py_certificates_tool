import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDateTime


class CertificateToolView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.datetime = QDateTime.currentDateTime()
        self.init_ui()

    def init_ui(self):
        self.init_menu_bar()
        self.init_input_interface()

        # Status Bar #
        self.statusBar().showMessage('Created by jsh152169')

        # Window #
        self.setWindowTitle('Certificate Tool')
        self.resize(500, 600)
        self.move_to_center()
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.show()

    def init_menu_bar(self):
        # Top Menu Init #
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)
        return

    def init_input_interface(self):
        self.setCentralWidget(QWidget())
        cw = self.centralWidget()
        grid = QGridLayout()
        cw.setLayout(grid)

        grid.addWidget(QLabel('crt file : '), 0, 0)
        grid.addWidget(QLabel('key file : '), 1, 0)
        grid.addWidget(QLabel('chain1 file : '), 2, 0)
        grid.addWidget(QLabel('chain2 file : '), 3, 0)
        grid.addWidget(QLabel('root ca file : '), 4, 0)
        grid.addWidget(QLabel('Content : '), 5, 0)

        crt_file_path = QLineEdit()
        crt_file_path.setReadOnly(True)
        key_file_path = QLineEdit()
        key_file_path.setReadOnly(True)
        chain1_file_path = QLineEdit()
        chain1_file_path.setReadOnly(True)
        chain2_file_path = QLineEdit()
        chain2_file_path.setReadOnly(True)
        rootca_file_path = QLineEdit()
        rootca_file_path.setReadOnly(True)
        certificate_contents = QTextEdit()
        certificate_contents.setReadOnly(True)
        grid.addWidget(crt_file_path, 0, 1)
        grid.addWidget(key_file_path, 1, 1)
        grid.addWidget(chain1_file_path, 2, 1)
        grid.addWidget(chain2_file_path, 3, 1)
        grid.addWidget(rootca_file_path, 4, 1)
        grid.addWidget(certificate_contents, 5, 1)

        crt_file_btn = QPushButton('File Open', self)
        crt_file_btn.resize(crt_file_btn.sizeHint())
        crt_file_show_btn = QPushButton('Show', self)
        crt_file_show_btn.resize(crt_file_show_btn.sizeHint())
        key_file_btn = QPushButton('File Open', self)
        key_file_btn.resize(crt_file_btn.sizeHint())
        chain1_file_btn = QPushButton('File Open', self)
        chain1_file_btn.resize(crt_file_btn.sizeHint())
        chain2_file_btn = QPushButton('File Open', self)
        chain2_file_btn.resize(crt_file_btn.sizeHint())
        rootca_file_btn = QPushButton('File Open', self)
        rootca_file_btn.resize(crt_file_btn.sizeHint())
        grid.addWidget(crt_file_btn, 0, 2)
        grid.addWidget(crt_file_show_btn, 0, 3)
        grid.addWidget(key_file_btn, 1, 2)
        grid.addWidget(chain1_file_btn, 2, 2)
        grid.addWidget(chain2_file_btn, 3, 2)
        grid.addWidget(rootca_file_btn, 4, 2)

        return

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CertificateToolView()
    sys.exit(app.exec_())
