from src.openssl_lib import OpenSSLLib

if __name__ == '__main__':
    osl = OpenSSLLib()
    osl.generate_private_key()
    osl.create_csr(country='KR', org='jsh152169', cn='shsh.test.com')
    osl.create_certificates(period_day=365 * 3)

    osl.save_privatekey_pem(filename='key.pem', passphrase='testPW')
    osl.save_certificates_pem(filename='test_cert.pem')

    print(osl.get_csr_dump())
    print(osl.get_certificates_dump())

    exit()
