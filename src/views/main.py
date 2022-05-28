from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDateTime, QTimer

# from openssl_lib import OpenSSLLib
from .set_csr import SetCSRView


class CSRData:
    def __init__(self):
        self.country_name = ''
        self.state_name = ''
        self.locality_name = ''
        self.org_name = ''
        self.org_unit_name = ''
        self.common_name = ''
        self.email = ''


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI Component Init
        self.pfx_path = QLineEdit()
        self.crt_path = QLineEdit()
        self.key_path = QLineEdit()
        self.cert_contents = QTextEdit()

        # Variable
        self.csr_data = CSRData()

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
        self.setWindowTitle('Certificates Tool(Developed by jsh152169@gmail.com)')
        self.resize(700, 600)
        self.move_to_center()
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.show()

    def set_current_time(self):
        current_date = QDateTime.currentDateTime()
        self.datetime_label = f"Date : {current_date.toString('yyyy-MM-dd HH:mm:ss')}"
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

        grid.addWidget(self.create_csr_group_layout(), 0, 0, 1, 6)

        grid.addWidget(QLabel('PFX file : '), 1, 0, 1, 1)
        grid.addWidget(QLabel('Crt file : '), 2, 0, 1, 1)
        grid.addWidget(QLabel('Key file : '), 3, 0, 1, 1)
        grid.addWidget(QLabel('Content : '), 4, 0, 1, 1)

        self.pfx_path.setReadOnly(True)
        self.crt_path.setReadOnly(True)
        self.key_path.setReadOnly(True)
        self.cert_contents.setReadOnly(True)

        grid.addWidget(self.pfx_path, 1, 1, 1, 4)
        grid.addWidget(self.crt_path, 2, 1, 1, 4)
        grid.addWidget(self.key_path, 3, 1, 1, 4)
        grid.addWidget(self.cert_contents, 6, 1, 1, 4)

        pfx_file_btn = QPushButton('File Select', self)
        pfx_file_btn.clicked.connect(self.onclick_crt_file_open_btn)
        crt_file_btn = QPushButton('File Select', self)
        crt_file_btn.clicked.connect(self.onclick_crt_file_open_btn)
        key_file_btn = QPushButton('File Select', self)
        key_file_btn.clicked.connect(self.onclick_key_file_open_btn)

        grid.addWidget(pfx_file_btn, 1, 5, 1, 1)
        grid.addWidget(crt_file_btn, 2, 5, 1, 1)
        grid.addWidget(key_file_btn, 3, 5, 1, 1)

        return

    def create_csr_group_layout(self):
        groupbox = QGroupBox('CSR Setting')

        hbox = QHBoxLayout()

        set_csr_btn = QPushButton('Set CSR Attributes')
        set_csr_btn.clicked.connect(self.onclick_set_csr_btn)
        hbox.addWidget(set_csr_btn)

        save_csr_btn = QPushButton('Save CSR')
        hbox.addWidget(save_csr_btn)
        groupbox.setLayout(hbox)

        return groupbox

    def move_to_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onclick_set_csr_btn(self):
        set_csr_view = SetCSRView()
        res = set_csr_view.show_modal()
        if res:
            self.csr_data.country_name = set_csr_view.country_name.text()
            self.csr_data.state_name = set_csr_view.state_name.text()
            self.csr_data.locality_name = set_csr_view.locality_name.text()
            self.csr_data.org_name = set_csr_view.org_name.text()
            self.csr_data.org_unit_name = set_csr_view.org_unit_name.text()
            self.csr_data.common_name = set_csr_view.common_name.text()
            self.csr_data.email = set_csr_view.email.text()

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
