import rsa
import os

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo cặp khóa RSA
        (public_key, private_key) = rsa.newkeys(2048)  # Sử dụng RSA với độ dài khóa 2048 bit

        # Lưu khóa riêng và khóa công khai vào các tệp
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1())  # Lưu khóa riêng dưới dạng PEM

        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1())  # Lưu khóa công khai dưới dạng PEM

    def load_keys(self):
        # Kiểm tra nếu khóa không tồn tại, tạo lại
        if not os.path.exists('cipher/rsa/keys/privateKey.pem') or not os.path.exists('cipher/rsa/keys/publicKey.pem'):
            self.generate_keys()  # Tạo cặp khóa nếu không tìm thấy

        # Đọc và tải khóa công khai và khóa riêng từ tệp PEM
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())  # Đọc khóa riêng

        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())  # Đọc khóa công khai

        return private_key, public_key

    def encrypt(self, message, public_key):
        # Mã hóa dữ liệu bằng khóa công khai
        encrypted_message = rsa.encrypt(message.encode('ascii'), public_key)
        return encrypted_message

    def decrypt(self, encrypted_message, private_key):
        # Giải mã dữ liệu bằng khóa riêng
        decrypted_message = rsa.decrypt(encrypted_message, private_key).decode('ascii')
        return decrypted_message

    # def sign(self, message, private_key):
    #     # Ký dữ liệu bằng khóa riêng
    #     signature = rsa.sign(message.encode('ascii'), private_key, 'SHA-1')
    #     return signature
    
    def sign(self, message, private_key):
        # Ký dữ liệu bằng khóa riêng (private_key)
        signature = rsa.sign(message.encode('ascii'), private_key, 'SHA-1')
        return signature


    def verify(self, message, signature, public_key):
        # Xác minh chữ ký bằng khóa công khai
        try:
            rsa.verify(message.encode('ascii'), signature, public_key)
            return True
        except rsa.VerificationError:
            return False
