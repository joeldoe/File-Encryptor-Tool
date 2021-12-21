'''
BTECH MAJOR PROJECT (2021-2022)

GROUP MEMBERS:
JOEL ELDOE
ARNAV ANAND
VIDYA LAD
'''

from tkinter import *                   # Importing tkinter module to create a GUI application
from tkinter import messagebox          # Importing messagebox from tkinter to show notifications
import tkinter.font as tkFont           # Importing tkinter font
import xor_file_encryptor               # Importing the module defined for XOR cipher
import aes_file_encryptor               # Importing the module defined for AES cipher
import os

class File_Encryptor:
    # Validates the inputs, checks for file existence and password 
    def input_validation(self, filename, password):
        flag = True
        if(len(password) >= 8 and len(password) <= 255):
            if not(os.path.isfile(filename)):
                flag = False
                messagebox.showerror("ERROR", "This file doesn't exist in this directory!")
        else:
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

                messagebox.showinfo("RESULT", "File has been encrypted successfully!")

            except Exception as e:
                messagebox.showerror("ERROR", "File type not supported for encryption!")

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

                messagebox.showinfo("RESULT", "File has been decrypted successfully!")

            except Exception as e:
                messagebox.showerror("ERROR", "Invalid file type or incorrect password!")

# Main program
fe = File_Encryptor()

# GUI
app = Tk()
app.geometry("500x500")
app.title("FILE ENCRYPTOR")

# Welcome message
messagebox.showinfo("WELCOME", "Keep your data safe with us!")

# Defining font
font_style = tkFont.Font(family="Verdana", size="12")

# Heading section
heading = Label(app,text="DATA SECURITY USING FILE ENCRYPTION",fg="black",bg="powderblue",width="500",height="2",font="Helvetica 14 bold")
heading.pack()

# Body section
# Defining labels
filename_text = Label(app,text="FILE NAME :", font=font_style)
password_text = Label(app,text="PASSWORD :", font=font_style)
filename_text.place(x=100,y=70)
password_text.place(x=100,y=150)

# Defining the text entry
file_name_entry = Entry(app, width="30", font=font_style)
password_entry = Entry(app, width="30", font=font_style)
file_name_entry.place(x=100,y=100, height="35")
password_entry.place(x=100,y=180, height="35")

# Defining the buttons
button1 = Button(app,text="ENCRYPT FILE",command=fe.encrypt,width="30",height="2",bg="WHITE", font=font_style)
button1.place(x=100,y=250)

button2 = Button(app,text="DECRYPT FILE",command=fe.decrypt,width="30",height="2",bg="WHITE", font=font_style)
button2.place(x=100,y=310)

button3 = Button(app,text="EXIT",command=app.quit,width="30",height="2",bg="WHITE", font=font_style)
button3.place(x=100,y=370)

# Running the app
app.mainloop()

# Deleting temporary files
if(os.path.isfile('./temp.txt')):
    os.system('rm ./temp.txt')

# Exit message
messagebox.showinfo("BYE", "Have a good day!")

# End of program