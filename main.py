import base64
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk

def removeScreen(thisScreen):
    thisScreen.withdraw()

def backToHome(thisScreen):
    for widget in thisScreen.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()
    thisScreen.withdraw()
    initialScreen.deiconify()

def encryptText():
    passcode = security_code.get()
    width = 400
    height = 275
    x = (wswidth // 2) - (width // 2)
    y = (wsheight // 2) - (height // 2)
    if passcode == "":
        messagebox.showerror("Encryption", "Input your secret key")
    elif passcode != "asdf":
        messagebox.showerror("Encryption", "Wrong secret key entered")
    else:
        screen = Toplevel(encryptionScreen)
        screen.title("Encryption")
        screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
        screen.configure(bg="#DF0A27")
        screen.iconphoto(False, icon)
        
        # Encrypting Text
        message = text.get(1.0, END)
        encoded_text = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_text)
        encrypt = base64_bytes.decode("ascii")

        Label(screen, text="Encrypted Message Here", bg="#DF0A27", fg="#fff", font="arial 15 bold").place(x = 10, y = 10)
        thisText = Text(screen, font=("times new roman", 12), bg="#fff", fg="#000", relief=GROOVE, bd=5, wrap=WORD)
        thisText.place(x=10, y=50, width=width-20, height=200)
        thisText.insert(END, encrypt)
def decryptText():
    passcode = security_code2.get()
    width = 400
    height = 275
    x = (wswidth // 2) - (width // 2)
    y = (wsheight // 2) - (height // 2)
    if passcode == "":
        messagebox.showerror("Decryption", "Input your secret key")
    elif passcode != "asdf":
        messagebox.showerror("Decryption", "Wrong secret key entered")
    else:
        screen = Toplevel(decryptionScreen)
        screen.title("Decryption")
        screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
        screen.configure(bg="#10C42B")
        screen.iconphoto(False, icon)
        
        # Decrypting Text
        message = text2.get(1.0, END)
        decoded_text = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded_text)
        decrypt = base64_bytes.decode("ascii")

        Label(screen, text="Decrypted Message Here", bg="#10C42B", fg="#fff", font="arial 15 bold").place(x=10, y=10)
        thisText = Text(screen, font=("times new roman", 12), bg="#fff", fg="#000", relief=GROOVE, bd=5, wrap=WORD)
        thisText.place(x=10, y=50, width=width - 20, height=200)
        thisText.insert(END, decrypt)

####################
# This 'on_closing' function is an important part for this app. Because, I wanted to close all windows when one of my three main windows
# (such as initialScreen, encryptionScreen and decryptionScreen) is closed.
###################
def on_closing():
    for widget in initialScreen.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()
    initialScreen.destroy()

def showEncryption():
    global text, security_code, encryptionScreen
    current = 1
    removeScreen(initialScreen)

    width = 350
    height = 375
    x = (wswidth // 2) - (width // 2)
    y = (wsheight // 2) - (height // 2)
    encryptionScreen = Toplevel(initialScreen)
    encryptionScreen.title("Text Encryption")
    encryptionScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    encryptionScreen.iconphoto(False, icon)
    encryptionScreen.configure(bg="#894EF1")
    # encryptionScreen.attributes("-topmost", "true")
    encryptionScreen.wm_transient()

    def reset():
        text.delete(1.0, END)
        security_code.set("")

    Label(encryptionScreen, text="Enter Text For Encryption", fg="white", bg="#894EF1", font="serif 13 bold").place(
        x=10, y=10)
    text = Text(encryptionScreen, font="calibri 16", bg="white", relief=GROOVE, wrap=WORD, bd=10)
    text.place(x=10, y=40, width=330, height=120)

    Label(encryptionScreen, text="Enter The Secret Key", fg="white", bg="#894EF1", font="serif 13").place(x=10, y=170)
    security_code = StringVar()
    Entry(encryptionScreen, textvariable=security_code, width=25, bd=2, font=("arial", 18), show="*").place(x=10, y=200)
    pixelVirtual = PhotoImage(width=1, height=1)
    Button(encryptionScreen, text="ENCRYPT", image=pixelVirtual, compound="c", bg="#DF0A27", fg="white", height=30,
           width=width - 30, bd=0, font="serif 12 bold", cursor="hand2", command=encryptText).place(x=15, y=245)
    Button(encryptionScreen, text="RESET", image=pixelVirtual, compound="c", bg="#FF8B00", fg="white", height=30,
           width=width - 30, bd=0, font="serif 12 bold", cursor="hand2", command=reset).place(x=15, y=285)
    Button(encryptionScreen, text="BACK", image=pixelVirtual, compound="c", bg="#4F1B61", fg="white", height=30,
           width=width - 30, bd=0, font="serif 12 bold", cursor="hand2",
           command=lambda: backToHome(encryptionScreen)).place(x=15, y=325)

    encryptionScreen.protocol("WM_DELETE_WINDOW", on_closing)
    encryptionScreen.mainloop()

def showDecryption():
    global text2, security_code2, decryptionScreen
    current = 1
    removeScreen(initialScreen)

    width = 350
    height = 375
    x = (wswidth // 2) - (width // 2)
    y = (wsheight // 2) - (height // 2)
    decryptionScreen = Toplevel(initialScreen)
    decryptionScreen.title("Text Decryption")
    decryptionScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    decryptionScreen.iconphoto(False, icon)
    decryptionScreen.configure(bg="#894EF1")
    # decryptionScreen.attributes("-topmost", "true")
    decryptionScreen.wm_transient()

    def reset():
        text2.delete(1.0, END)
        security_code2.set("")

    Label(decryptionScreen, text="Enter Text For Decryption", fg="white", bg="#894EF1", font="serif 13 bold").place(
        x=10, y=10)
    text2 = Text(decryptionScreen, font="calibri 16", bg="white", relief=GROOVE, wrap=WORD, bd=10)
    text2.place(x=10, y=40, width=330, height=120)

    Label(decryptionScreen, text="Enter The Secret Key", fg="white", bg="#894EF1", font="serif 13").place(x=10, y=170)
    security_code2 = StringVar()
    Entry(decryptionScreen, textvariable=security_code2, width=25, bd=2, font=("arial", 18), show="*").place(x=10,
                                                                                                             y=200)
    pixelVirtual = PhotoImage(width=1, height=1)
    Button(decryptionScreen, text="DECRYPT", image=pixelVirtual, compound="c", bg="#00B00D", fg="white", height=30,
           width=width - 30, bd=0, font="serif 12 bold", cursor="hand2", command=decryptText).place(x=15, y=245)
    Button(decryptionScreen, text="RESET", image=pixelVirtual, compound="c", bg="#FF8B00", fg="white", height=30,
           width=width - 30, bd=0, font="serif 12 bold", cursor="hand2", command=reset).place(x=15, y=285)
    Button(decryptionScreen, text="BACK", image=pixelVirtual, compound="c", bg="#4F1B61", fg="white", height=30,
           width=width - 30, bd=0, font="serif 12 bold", cursor="hand2",
           command=lambda: backToHome(decryptionScreen)).place(x=15, y=325)

    decryptionScreen.protocol("WM_DELETE_WINDOW", on_closing)
    decryptionScreen.mainloop()

def startInitialScreen():
    global initialScreen, icon, wswidth, wsheight, current

    current = 0
    initialScreen = Tk()
    # Window screen size
    wswidth = initialScreen.winfo_screenwidth()
    wsheight = initialScreen.winfo_screenheight()
    # App screen size
    width = 400
    height = 300

    x = (wswidth // 2) - (width // 2)
    y = (wsheight // 2) - (height // 2)
    initialScreen.geometry("%dx%d+%d+%d" % (width, height, x, y))

    icon = ImageTk.PhotoImage(Image.open("security_high.png"))
    initialScreen.iconphoto(False, icon)

    initialScreen.title("Text Encryption App - Python")
    initialScreen.configure(bg="#BD9BDF")

    pixelVirtual = PhotoImage(width=1, height=1)
    btnX = 20
    btnY = (height // 2)
    Button(text=" Text Encryption", image=pixelVirtual, compound="c", height=30, width=(width - 40), bg="#DF0A27",
           fg="white", bd=0, font=("sans 14 bold"), cursor="hand2", command=showEncryption).place(x=btnX, y=btnY - 40)
    Button(text=" Text Decryption", image=pixelVirtual, compound="c", height=30, width=(width - 40), bg="#08C108",
           fg="white", bd=0, font=("sans 14 bold"), cursor="hand2", command=showDecryption).place(x=btnX, y=btnY)

    initialScreen.protocol("WM_DELETE_WINDOW", on_closing)
    initialScreen.mainloop()


startInitialScreen()
