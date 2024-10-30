from Crypto.Random import  get_random_bytes
from Crypto.Protocol.KDF import PBKDF2 #anahtar üretme fonksiyonudur.import

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#Generate a key
# simple_key =get_random_bytes(32)
# print(simple_key) #basit bir anahtar oluşturduk

salt = b'\xd9\xc7\x06:\xa1q<gR\xf2\xef!\xcc\xf0\xb6\xf2\xaf\xca\x19\\\x83\x1f\x9b\xdf<\x0b{\x14\xa5/CZ'
password = "sifre123"

key = PBKDF2(password, salt, dkLen = 32)

with open("encrypted.bin", "rb") as f :
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)