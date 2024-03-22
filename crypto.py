# crypto.py
from Crypto.Cipher import AES
import base64
import json

def pad(text, block_size=16):
    pad_size = block_size - (len(text) % block_size)
    return text + (chr(pad_size) * pad_size)

def unpad(padded_text):
    pad_size = ord(padded_text[-1])
    return padded_text[:-pad_size]

def encrypt(text, key, iv="0123456789abcdef"):
    cipher = AES.new(base64.b64decode(key), AES.MODE_CBC, iv.encode())
    padded_text = pad(text)
    encrypted_bytes = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(crypt, key, iv="0123456789abcdef"):
    cipher = AES.new(base64.b64decode(key), AES.MODE_CBC, iv.encode())
    encrypted_bytes = base64.b64decode(crypt)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return unpad(decrypted_bytes.decode())
