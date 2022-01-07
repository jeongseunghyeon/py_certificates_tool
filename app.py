import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDateTime, QTimer


class MainView(QMainWindow):
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

        # Variable
        self._csr_temp = ''

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

        self.create_csr_btn.clicked.connect(self.onclick_create_csr_btn)
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

    def onclick_create_csr_btn(self):
        win = CreateCSRView()
        res = win.show_modal()
        if res:
            country_name = win.country_name.text()
            state_name = win.state_name.text()
            locality_name = win.locality_name.text()
            org_name = win.org_name.text()
            org_unit_name = win.org_unit_name.text()
            common_name = win.common_name.text()
            email = win.email.text()
            print(f'{country_name} {state_name} {locality_name} {org_name} {org_unit_name} {common_name} {email}')

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


class CreateCSRView(QDialog):
    def __init__(self):
        super().__init__()

        # Init Component
        self.country_name = QLineEdit()
        self.country_name.setMaxLength(2)
        self.state_name = QLineEdit()
        self.locality_name = QLineEdit()
        self.org_name = QLineEdit()
        self.org_unit_name = QLineEdit()
        self.common_name = QLineEdit()
        self.email = QLineEdit()

        self.init_ui()
        self.move_to_center()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Country name(2 letters) : '), 1, 0, 1, 2)
        grid.addWidget(self.country_name, 1, 2, 1, 4)
        grid.addWidget(QLabel('State or Province Name : '), 2, 0, 1, 2)
        grid.addWidget(self.state_name, 2, 2, 1, 4)
        grid.addWidget(QLabel('Locality Name : '), 3, 0, 1, 2)
        grid.addWidget(self.locality_name, 3, 2, 1, 4)
        grid.addWidget(QLabel('Organization Name : '), 4, 0, 1, 2)
        grid.addWidget(self.org_name, 4, 2, 1, 4)
        grid.addWidget(QLabel('Organization Unit Name : '), 5, 0, 1, 2)
        grid.addWidget(self.org_unit_name, 5, 2, 1, 4)
        grid.addWidget(QLabel('Common Name(Domain) : '), 6, 0, 1, 2)
        grid.addWidget(self.common_name, 6, 2, 1, 4)
        grid.addWidget(QLabel('Email Address : '), 7, 0, 1, 2)
        grid.addWidget(self.email, 7, 2, 1, 4)

        create_btn = QPushButton('Create')
        create_btn.clicked.connect(self.onclick_create_btn)
        grid.addWidget(create_btn, 8, 0, 1, 3)
        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.onclick_cancel_btn)
        grid.addWidget(cancel_btn, 8, 3, 1, 3)

        self.setWindowTitle('Create CSR(Certificate Signing Request) File')
        self.resize(600, 400)

    def onclick_create_btn(self):
        self.accept()

    def onclick_cancel_btn(self):
        self.reject()

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_modal(self):
        return super().exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainView()
    sys.exit(app.exec_())

