'''
BTECH MAJOR PROJECT (2021-2022)

GROUP MEMBERS:
JOEL ELDOE
ARNAV ANAND
VIDYA LAD
'''

import xor_file_encryptor               # Importing the module defined for XOR cipher
import aes_file_encryptor               # Importing the module defined for AES cipher
import os

# ANSI codes for font colors
class colors:
    GREEN = '\033[92m'  # GREEN COLOR
    YELLOW = '\033[93m' # YELLOW COLOR
    RED = '\033[91m'    # RED COLOR
    RESET = '\033[0m'   # RESET COLOR

class File_Encryptor:
    # Validates the inputs, checks for file existence and password 
    def input_validation(self, filename, password):
        flag = True
        if(len(password) >= 8 and len(password) <= 255):
            try:
                f = open(filename, 'rb')
            except OSError as e:
                print(f"\n[{colors.RED}-{colors.RESET}] Error Occurred: {e}\n")
                flag = False
        else:
            print(f"\n[{colors.RED}-{colors.RESET}] Error Occurred: Password length should be between 8-255!\n")
            flag = False

        return flag
    
    # Implements file encryption
    def encrypt(self, filename, password):
        # Converting the data from unicode to ASCII format
        os.system('touch temp.txt')
        f1 = open(filename, 'r')
        data = f1.read()
        f1.close()
        data = data.encode('utf-8').decode('utf-8')
        f2 = open('temp.txt', 'w')
        f2.write(data)
        f2.close()

        
        f = open('temp.txt', 'rb')
        file_bytes = f.read()
        f.close()

        key = len(password)

        xor_encrypted_file_bytes = xor_file_encryptor.xor_encrypt(file_bytes, key)
        aes_encrypted_file_bytes = aes_file_encryptor.encrypt(xor_encrypted_file_bytes, password)

        f = open(filename+'.enc', 'wb')
        f.write(aes_encrypted_file_bytes)
        f.close()

        print(f"[{colors.GREEN}+{colors.RESET}] '{colors.GREEN}{filename+'.enc'}{colors.RESET}': encrypted file has been created successfully!")

    # Implements file decryption
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

        print(f"[{colors.GREEN}+{colors.RESET}] '{colors.GREEN}{filename[:-4]+'.dec'}{colors.RESET}': decrypted file has been created successfully!")

# Main program
print("-----------------------------------------------------------------------")
print(f"------------------------- {colors.GREEN}FILE ENCRYPTOR TOOL{colors.RESET} -------------------------")
print("-----------------------------------------------------------------------\n")

fe = File_Encryptor()
filename = input(f"\nEnter the name of the file: {colors.YELLOW}")
print(colors.RESET)
password = input(f"Enter the password: {colors.YELLOW}")
print(colors.RESET)

if(fe.input_validation(filename,password)):
    try:
        choice = input(f"What action do you want to perform, encryption or decryption? (e|d): {colors.YELLOW}")
        print(colors.RESET)
        if(choice == 'e'):
            fe.encrypt(filename, password)
        elif(choice == 'd'):
            fe.decrypt(filename, password)
        else:
            print(f"\n[{colors.RED}-{colors.RESET}] Wrong choice!!!")
    except Exception as e:
        print(f"\n[{colors.RED}-{colors.RESET}] Error Occurred: {e}")
        print(f"[{colors.RED}-{colors.RESET}] Maybe you entered a wrong password!")
        print(f"[{colors.RED}-{colors.RESET}] Or maybe the file format isn't supported! (Only use '.txt' or '.csv' files)")
    finally:
        if(os.path.isfile('./temp.txt')):
            os.system('rm ./temp.txt')
        print(f"\n[{colors.GREEN}+{colors.RESET}] Exiting program\n")
else:
    pass

# End of program