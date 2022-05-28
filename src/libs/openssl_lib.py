from OpenSSL.crypto import (
    dump_certificate,
    dump_certificate_request,
    dump_privatekey,
    FILETYPE_PEM,
    PKey,
    TYPE_RSA,
    X509,
    X509Req
)
import os
import random


class OpenSSLLib:
    def __init__(self):
        self._pk = PKey()
        self._x509_request = X509Req()
        self._x509 = X509()

    def init_variable(self):
        self._pk = PKey()
        self._x509_request = X509Req()
        self._x509 = X509()

    def generate_private_key(self):
        self._pk.generate_key(type=TYPE_RSA, bits=2048)

    def get_privatekey_dump(self, passphrase: str) -> str:
        assert passphrase, 'Empty Pass phrase'

        return dump_privatekey(type=FILETYPE_PEM, pkey=self._pk, cipher='aes-256-cbc',
                               passphrase=passphrase.encode('utf-8')).decode('utf-8')

    def save_privatekey_pem(self, filename: str, passphrase: str):
        assert filename, 'Empty Filename'
        assert passphrase, 'Empty Pass phrase'

        try:
            fp = open(file=f'certs/{filename}', mode='w', encoding='utf-8')
        except FileNotFoundError:
            os.makedirs('certs')
            fp = open(file=f'certs/{filename}', mode='w', encoding='utf-8')

        fp.write(self.get_privatekey_dump(passphrase=passphrase))
        fp.close()

    def create_csr(self, country, org, cn):
        assert country, 'Empty Country'
        assert org, 'Empty Organization'
        assert cn, 'Empty Common Name'

        self._x509_request.get_subject().countryName = country
        self._x509_request.get_subject().organizationName = org
        self._x509_request.get_subject().commonName = cn
        self._x509_request.set_pubkey(self._pk)

    def get_csr_dump(self) -> str:
        return dump_certificate_request(type=FILETYPE_PEM, req=self._x509_request).decode('utf-8')

    def save_csr_pem(self, filename: str):
        assert filename, 'Empty Filename'

        try:
            fp = open(file=f'certs/{filename}', mode='w', encoding='utf-8')
        except FileNotFoundError:
            os.makedirs('certs')
            fp = open(file=f'certs/{filename}', mode='w', encoding='utf-8')

        fp.write(self.get_csr_dump())
        fp.close()

    def create_certificates(self, period_day: int):
        assert isinstance(period_day, int), 'Invalid Period Day'

        self._x509.set_serial_number(random.randint(10 ** 8, 10 ** 9))

        # Set Certificates Period
        self._x509.gmtime_adj_notBefore(0)
        self._x509.gmtime_adj_notAfter(60 * 60 * 24 * period_day)

        # Set Attributes
        self._x509.set_subject(self._x509_request.get_subject())
        self._x509.set_issuer(self._x509.get_subject())
        self._x509.set_pubkey(self._x509_request.get_pubkey())
        self._x509.sign(pkey=self._pk, digest="sha256".encode('utf-8'))

    def get_certificates_dump(self) -> str:
        return dump_certificate(type=FILETYPE_PEM, cert=self._x509).decode('utf-8')

    def save_certificates_pem(self, filename: str):
        assert filename, 'Empty Filename'

        try:
            fp = open(file=f'certs/{filename}', mode='w', encoding='utf-8')
        except FileNotFoundError:
            os.makedirs('certs')
            fp = open(file=f'certs/{filename}', mode='w', encoding='utf-8')

        fp.write(self.get_certificates_dump())
        fp.close()
