from Crypto.Cipher import AES # importing AES object from pycrypto module
import hashlib # importing hashlib module to use SHA-256 function

# Padding input to make it a multiple of 16 because AES input blocks are of 16 bytes (128 bit)
def pad_input(file):
    while(len(file) % 16 != 0):
        file += b'0' # Padding null bytes
    return file

#def encrypt(filename, password):
def encrypt(data, password):
    # Creating the AES cipher
    key = hashlib.sha256(password.encode()).digest() # to create a 256-bit key (14 rounds in AES)
    mode = AES.MODE_CBC
    IV = "MAJORPROJECT2021" # Initialization Vector is also of 16 bytes
    aes_cipher = AES.new(key, mode, IV)
    
    padded_data = pad_input(data.encode())
    encrypted_data  = aes_cipher.encrypt(padded_data)
    return encrypted_data

#def decrypt(filename, password)
def decrypt(data, password):
    key = hashlib.sha256(password.encode()).digest() # to create a 256-bit key (14 rounds in AES)
    mode = AES.MODE_CBC
    IV = "MAJORPROJECT2021" # Initialization Vector is also of 16 bytes
    aes_cipher = AES.new(key, mode, IV)

    decrypted_data = aes_cipher.decrypt(data)
    decrypted_data = decrypted_data.rstrip(b'0')
    return decrypted_data
