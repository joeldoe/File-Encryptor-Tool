from Crypto.Cipher import AES   # Importing AES object from pycrypto module
import hashlib                  # Importing hashlib module to use SHA-256 function

# Padding the file bytes to make it a multiple of 16 because AES is a block cipher which takes 16 bytes(128-bit) as input
def pad_input(file_bytes):
    while(len(file_bytes) % 16 != 0):
        file_bytes += b'0'            # Padding null bytes at the end
    return file_bytes

# Implements AES encryption on the file bytes
def encrypt(data, password):
    # To create a 256-bit key (14 rounds in AES)
    key = hashlib.sha256(password.encode()).digest()

    # Initializing the AES cipher
    mode = AES.MODE_CBC
    IV = "MAJORPROJECT2021"              # Initialization Vector is also of 16 bytes
    aes_cipher = AES.new(key, mode, IV)
    
    padded_data = pad_input(data.encode())
    encrypted_data  = aes_cipher.encrypt(padded_data)

    return encrypted_data

# Implements AES decryption on the file bytes
def decrypt(data, password):
    # To create a 256-bit key (14 rounds in AES)
    key = hashlib.sha256(password.encode()).digest()

    # Initializing the AES cipher
    mode = AES.MODE_CBC
    IV = "MAJORPROJECT2021"              # Initialization Vector is also of 16 bytes
    aes_cipher = AES.new(key, mode, IV)

    decrypted_data = aes_cipher.decrypt(data)
    decrypted_data = decrypted_data.rstrip(b'0')

    return decrypted_data
