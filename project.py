'''
BTECH MAJOR PROJECT (2021-2022)

GROUP MEMBERS:
JOEL ELDOE
ARNAV ANAND
VIDYA LAD
'''

# importing the defined modules for XOR and AES
import xor_file_encryptor
import aes_file_encryptor
from Crypto.Cipher import AES # importing AES object from pycrypto module
import hashlib # importing hashlib module to use SHA-256 function

class File_Encryptor:
    def input_validation(self, filename, password):
        flag = True
        if(len(password) >= 8 and len(password) <= 255):
            try:
                f = open(filename, 'rb')
            except OSError as e:
                print(f"\nError Occurred: {e}")
                flag = False
        else:
            print("\nError Occurred: Password length should be between 8-255!")
            flag = False

        return flag
    
    def encrypt(self, filename, password):
        f = open(filename, 'rb')
        file_bytes = f.read()
        f.close()

        key = len(password)

        xor_encrypted_file_bytes = xor_file_encryptor.xor_encrypt(file_bytes, key)
        aes_encrypted_file_bytes = aes_file_encryptor.encrypt(xor_encrypted_file_bytes, password)

        f = open(filename+'.enc', 'wb')
        f.write(aes_encrypted_file_bytes)
        f.close()

    def decrypt(self, filename, password):
        f = open(filename, 'rb')
        file_bytes = f.read()
        f.close()

        key = len(password)

        aes_decrypted_file_bytes = aes_file_encryptor.decrypt(file_bytes, password)
        xor_decrypted_file_bytes = xor_file_encryptor.xor_decrypt(aes_decrypted_file_bytes, key)

        f = open(filename[:-4]+'.dec', 'wb')
        f.write(xor_decrypted_file_bytes.encode())
        f.close()

# Main program
print("----- FILE ENCRYPTOR TOOL -----")

fe = File_Encryptor()
filename = input("\nEnter the name of the file: ")
password = input("Enter the password: ")

if(fe.input_validation(filename,password)):
    try:
        choice = input("What action do you want to perform? (e|d): ")
        if(choice == 'e'):
            fe.encrypt(filename, password)
        elif(choice == 'd'):
            fe.decrypt(filename, password)
        else:
            print("Wrong choice!!!")
    except Exception as e:
        print(f"\nError Occurred: {e}")
        print("Maybe you entered a wrong password!")
        print("Or maybe the file format isn't supported! (Only use '.txt' or '.csv' files)")
    finally:
        print("\nExiting program.")
else:
    pass


