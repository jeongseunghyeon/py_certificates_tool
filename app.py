import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QTextEdit, QFileDialog, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDateTime, QTimer


class CertificateToolView(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI Component Init
        self.create_csr_btn = QPushButton('Create CSR')
        self.crt_path = QLineEdit()
        self.key_path = QLineEdit()
        self.chain1_path = QLineEdit()
        self.chain2_path = QLineEdit()
        self.rootca_path = QLineEdit()
        self.cert_contents = QTextEdit()

        self.datetime = QDateTime.currentDateTime()
        self.datetime_label = ''
        self.init_ui()

    def init_ui(self):
        self.init_menu_bar()
        self.init_widget()

        # Status Bar #
        self.set_current_time()
        qtimer = QTimer(self)
        qtimer.timeout.connect(self.set_current_time)
        qtimer.start(1000)

        # Window #
        self.setWindowTitle('Certificate Tool(Created by jsh152169@gmail.com)')
        self.resize(700, 600)
        self.move_to_center()
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.show()

    def set_current_time(self):
        qdate = QDateTime.currentDateTime()
        self.datetime_label = qdate.toString('yyyy-MM-dd HH:mm:ss')
        self.statusBar().showMessage(self.datetime_label)

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

    def init_widget(self):
        self.setCentralWidget(QWidget())
        cw = self.centralWidget()

        grid = QGridLayout()
        cw.setLayout(grid)

        grid.addWidget(self.create_csr_btn, 0, 0, 1, 3)

        grid.addWidget(QLabel('crt file : '), 1, 0)
        grid.addWidget(QLabel('key file : '), 2, 0)
        grid.addWidget(QLabel('chain1 file : '), 3, 0)
        grid.addWidget(QLabel('chain2 file : '), 4, 0)
        grid.addWidget(QLabel('root ca file : '), 5, 0)
        grid.addWidget(QLabel('Content : '), 6, 0)

        self.crt_path.setReadOnly(True)
        self.key_path.setReadOnly(True)
        self.chain1_path.setReadOnly(True)
        self.chain2_path.setReadOnly(True)
        self.rootca_path.setReadOnly(True)
        self.cert_contents.setReadOnly(True)

        grid.addWidget(self.crt_path, 1, 1)
        grid.addWidget(self.key_path, 2, 1)
        grid.addWidget(self.chain1_path, 3, 1)
        grid.addWidget(self.chain2_path, 4, 1)
        grid.addWidget(self.rootca_path, 5, 1)
        grid.addWidget(self.cert_contents, 6, 1)

        crt_file_btn = QPushButton('File Open', self)
        crt_file_btn.clicked.connect(self.onclick_crt_file_open_btn)

        key_file_btn = QPushButton('File Open', self)
        key_file_btn.clicked.connect(self.onclick_key_file_open_btn)
        chain1_file_btn = QPushButton('File Open', self)
        chain1_file_btn.resize(crt_file_btn.sizeHint())
        chain2_file_btn = QPushButton('File Open', self)
        chain2_file_btn.resize(crt_file_btn.sizeHint())
        rootca_file_btn = QPushButton('File Open', self)
        rootca_file_btn.resize(crt_file_btn.sizeHint())

        grid.addWidget(crt_file_btn, 1, 2)
        grid.addWidget(key_file_btn, 2, 2)
        grid.addWidget(chain1_file_btn, 3, 2)
        grid.addWidget(chain2_file_btn, 4, 2)
        grid.addWidget(rootca_file_btn, 5, 2)

        return

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onclick_crt_file_open_btn(self):
        file_name = QFileDialog.getOpenFileName(self)
        if file_name[0]:
            self.crt_path.setText(file_name[0])
            f = open(file_name[0], 'r')
            with f:
                data = f.read()
                self.cert_contents.setText(data)

    def onclick_key_file_open_btn(self):
        file_name = QFileDialog.getOpenFileName(self)
        if file_name[0]:
            self.key_path.setText(file_name[0])
            f = open(file_name[0], 'r')
            with f:
                data = f.read()
                self.cert_contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CertificateToolView()
    sys.exit(app.exec_())

