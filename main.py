import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb

import psutil


from cryptography.fernet import Fernet

import clipboard

import os

user_name = psutil.users()[0].name

toEncryptFilePath = None
keyFile = None

defaultExplorer = f"C:\\Users\\{user_name}\\Desktop"

def EnOrDe(event):
    selected_value = dropdown.get()

    if selected_value.lower() == "encrypt":
        selectFile.config(text="Select file to Encrypt")
        askToMakeAKeyFile.place(x=20, y=130)
        askCopyKey.place(x=20, y=160)
        buttonForEncrypt.place(x=20, y=250)

        selectKeyFile.place_forget()
        buttonToSelectKeyFile.place_forget()
        enterKeyManually.place_forget()
        keybox.place_forget()
        buttonForDecrypt.place_forget()

    if selected_value.lower() == "decrypt":
        selectFile.config(text="Select file to Decrypt")
        askToMakeAKeyFile.place_forget()
        askCopyKey.place_forget()
        buttonForEncrypt.place_forget()

        selectKeyFile.place(x=20,y=130)
        buttonToSelectKeyFile.place(x=200, y=130)
        enterKeyManually.place(x=20,y=160)
        if checkbox4.get() == 1:
            enterKeyManually.config(fg="#FFF200")
            keybox.place(x=30, y=185)
        buttonForDecrypt.place(x=20, y=250)


def openFile():
    global toEncryptFilePath
    global defaultExplorer

    toEncryptFilePath = filedialog.askopenfilename(initialdir=defaultExplorer,
                                          title="Select File")
    if toEncryptFilePath == "":

        return None

    button.config(text=os.path.basename(toEncryptFilePath))

    defaultExplorer = os.path.split(toEncryptFilePath)[0]


def needKeyFileOrNo():
    if checkbox1.get() == 1:
        askToMakeAKeyFile.config(fg="#FFF200")
    else:
        askToMakeAKeyFile.config(fg="#F1D4E5")

def copyKeyOrNo():
    if checkbox2.get() == 1:
        askCopyKey.config(fg="#FFF200")
    else:
        askCopyKey.config(fg="#F1D4E5")

def pathForSaveKey():
    global defaultExplorer
    filePath = filedialog.asksaveasfile(initialdir=defaultExplorer,
                                          title="Choose path to save encryption key",defaultextension=".key",filetypes=[
                                              ("KEY file",".key")
                                          ],mode='wb')

    if filePath == "":
        return None
    
    
    
    return filePath

def EnCrypt():
    global toEncryptFilePath

    if toEncryptFilePath is None:
        mb.showwarning("Choose File Warning","First select a file for encrypting")
        return

    key = Fernet.generate_key()

    if checkbox1.get() == 1:
        savekeyPath = pathForSaveKey()
        while savekeyPath is None:
            savekeyPath = pathForSaveKey()

        savekeyPath.write(key)
        savekeyPath.close()

    
    if checkbox2.get() == 1:
        clipboard.copy(str(key))

    if checkbox1.get() != 1 and checkbox2.get() != 1:
        mb.showwarning("Where should the encryption key saved?","There is no recovery option")
        return

    with open(toEncryptFilePath, 'rb') as file:
        original = file.read()

    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(original)

    with open(toEncryptFilePath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


    toEncryptFilePath = None
    button.config(text="Select File")

    mb.showinfo("File Encryptor","Successfully encrypted")

    return

def selectKeyFileExplorer():
    if checkbox3.get() == 1:
        selectKeyFile.config(fg="#FFF200")
        buttonToSelectKeyFile.place(x=200, y=130)

    else:
        selectKeyFile.config(fg="#F1D4E5")
        buttonToSelectKeyFile.place_forget()

def openKeyFile():
    global keyFile
    global defaultExplorer
    keyFile = filedialog.askopenfilename(initialdir=defaultExplorer,
                                          title="Select File", filetypes=[("KEY file","*.key")])
    if keyFile == "":

        return None
    
    defaultExplorer = os.path.split(keyFile)[0]
    buttonToSelectKeyFile.config(text=os.path.basename(keyFile))

def selectKeyManually():
    if checkbox4.get() == 1:
        enterKeyManually.config(fg="#FFF200")
        keybox.place(x=30, y=185)

    else:
        enterKeyManually.config(fg="#F1D4E5")
        keybox.place_forget()
        
def DeCrypt():
    global toEncryptFilePath
    global keyFile

    if toEncryptFilePath is None:
        mb.showwarning("Choose File Warning","First select a file for decrypting")
        return
    
    if keyFile is None and checkbox4.get() != 1:
        mb.showwarning("Provide a key","There is no key found")
        return
    
    if checkbox4.get() == 1:
        key = bytes((keybox.get("1.0", "end-1c").replace("b'","").replace("'","")), 'utf-8')
        
    if checkbox3.get() == 1:
        key = open(keyFile, "rb").read()

        
    fernet = Fernet(key)

    with open(toEncryptFilePath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(toEncryptFilePath, 'wb') as dec_file:
        dec_file.write(decrypted)
    

    toEncryptFilePath = None
    button.config(text="Select File")

    keyFile = None
    buttonToSelectKeyFile.config(text="Select File")

    mb.showinfo("File Encryptor","Successfully decrypted")


    return



window = Tk()
window.title("File Encryptor")
logo_image = tk.PhotoImage(file="./asset/dp.png")
window.iconphoto(True, logo_image)
window.resizable(0, 0)
window.config(bg="#26242f")
window.geometry("300x384")

Title = Label(window,
              text="File Encryptor", bg="#26242f", font=22, fg="#ffffff")
Title.place(anchor=CENTER, relx=.5, y=20)

style = ttk.Style()
style.theme_create('custom_style', parent='alt',
                   settings={'TCombobox': {'configure': {'selectbackground': 'white',
                                                         'selectforeground': 'black'}}})
style.theme_use('custom_style')

dropdown = ttk.Combobox(
    window, values=["Encrypt", "Decrypt"], state="readonly")
dropdown.set("Encrypt")
dropdown.bind("<<ComboboxSelected>>", EnOrDe)
dropdown.place(x=20, y=50)


selectFile = Label(window,
                   text="Select file to Encrypt", bg="#26242f", font=18,fg="#F1D4E5")
selectFile.place(x=20,y=80)

button = Button(text="Select File", command=openFile, bg="#26ff2f",width=10)
button.place(x=200, y=80)

checkbox1 = tk.IntVar()
askToMakeAKeyFile = tk.Checkbutton(window, text="Export encryption key", variable=checkbox1, command=needKeyFileOrNo, bg="#26242f",activebackground="#26242f",fg="#F1D4E5",font=18,activeforeground="#F1D4E5")
askToMakeAKeyFile.place(x=20, y=130)
askToMakeAKeyFile.select()
askToMakeAKeyFile.config(fg="#FFF200")


checkbox2 = tk.IntVar()
askCopyKey = tk.Checkbutton(window, text="Copy encryption key to clipboard", variable=checkbox2, command=copyKeyOrNo, bg="#26242f",activebackground="#26242f",fg="#F1D4E5",font=18,activeforeground="#F1D4E5")
askCopyKey.place(x=20, y=160)

buttonForEncrypt = Button(text="Encrypt", command=EnCrypt, bg="#26ff2f")
buttonForEncrypt.place(x=20, y=250)

checkbox3 = tk.IntVar()
selectKeyFile = tk.Checkbutton(window, text="Select key file", variable=checkbox3, command=selectKeyFileExplorer, bg="#26242f",activebackground="#26242f",fg="#F1D4E5",font=18,activeforeground="#F1D4E5")
selectKeyFile.select()
selectKeyFile.config(fg="#FFF200")


buttonToSelectKeyFile = Button(text="Select File", command=openKeyFile, bg="#26ff2f",width=10)


checkbox4 = tk.IntVar()
enterKeyManually = tk.Checkbutton(window, text="Enter key manually", variable=checkbox4, command=selectKeyManually, bg="#26242f",activebackground="#26242f",fg="#F1D4E5",font=18,activeforeground="#F1D4E5")

keybox = Text(window,height=1,width=28)



buttonForDecrypt = Button(text="Decrypt", command=DeCrypt, bg="#26ff2f")


window.mainloop()
