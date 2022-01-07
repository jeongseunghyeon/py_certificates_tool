from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QDateTime, QTimer


class SetCSRView(QDialog):
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
        self.setWindowIcon(QIcon('./image/icon.png'))

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

        set_btn = QPushButton('Set')
        set_btn.clicked.connect(self.onclick_create_btn)
        grid.addWidget(set_btn, 8, 0, 1, 3)
        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.onclick_cancel_btn)
        grid.addWidget(cancel_btn, 8, 3, 1, 3)

        self.setWindowTitle('Set CSR(Certificate Signing Request) Attributes')
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
