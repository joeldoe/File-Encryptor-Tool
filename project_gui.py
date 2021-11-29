'''
BTECH MAJOR PROJECT (2021-2022)

GROUP MEMBERS:
JOEL ELDOE
ARNAV ANAND
VIDYA LAD
'''

from tkinter import *
from tkinter import messagebox
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
            if not(os.path.isfile(filename)):
                flag = False
                print("This file doesn't exist in this directory!")
                messagebox.showerror("ERROR", "This file doesn't exist in this directory!")
        else:
            print(f"\n[{colors.RED}-{colors.RESET}] Error Occurred: Password length should be between 8-255!\n")
            flag = False
            messagebox.showwarning("WARNING", "Password length should be between 8-255!")

        return flag
    
    # Implements file encryption
    def encrypt(self):
        filename = file_name_entry.get()
        password = password_entry.get()

        if(fe.input_validation(filename, password)):
            try:                
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
                messagebox.showinfo("RESULT", f"'{filename+'.enc'}': encrypted file has been created successfully!")

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("ERROR", f"{e}")

    # Implements file decryption
    def decrypt(self):
        filename = file_name_entry.get()
        password = password_entry.get()

        if(fe.input_validation(filename, password)):
            try:
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
                messagebox.showinfo("RESULT", f"'{filename[:-4]+'.dec'}': decrypted file has been created successfully!")

            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror("ERROR", f"{e}")

# Main program
print("-----------------------------------------------------------------------")
print(f"------------------------- {colors.GREEN}FILE ENCRYPTOR TOOL{colors.RESET} -------------------------")
print("-----------------------------------------------------------------------\n")

# GUI
fe = File_Encryptor()

app = Tk()
app.geometry("500x500")
app.title("FILE ENCRYPTOR")

messagebox.showinfo("WELCOME", "Keep your data safe with us!")

heading = Label(app,text="DATA SECURITY USING FILE ENCRYPTION",fg="black",bg="powderblue",width="500",height="2",font="Helvetica 14 bold")
heading.pack()

filename_text = Label(app,text="FILE NAME :")
password_text = Label(app,text="PASSWORD :")
filename_text.place(x=15,y=70)
password_text.place(x=15,y=140)

file_name_entry = Entry(app,width="30")
password_entry = Entry(app,width="30")
file_name_entry.place(x=15,y=100)
password_entry.place(x=15,y=180)

button1 = Button(app,text="ENCRYPT FILE",command=fe.encrypt,width="30",height="2",bg="WHITE")
button1.place(x=15,y=250)

button2 = Button(app,text="DECRYPT FILE",command=fe.decrypt,width="30",height="2",bg="WHITE")
button2.place(x=15,y=300)

button3 = Button(app,text="EXIT",command=app.quit,width="30",height="2",bg="WHITE")
button3.place(x=15,y=350)

app.mainloop()

if(os.path.isfile('./temp.txt')):
    os.system('rm ./temp.txt')

messagebox.showinfo("BYE BYE", "Have a good day!")
