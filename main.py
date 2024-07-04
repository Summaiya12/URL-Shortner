from tkinter import *
import pyshorteners

#Define main window
window = Tk()
window.title("Link Shorter")
window.geometry("500x500")
window.resizable(False, False)


#deine functions

def shorten():
    if entry2.get():
        entry2.delete(0, END)

    if entry1.get():
        url = pyshorteners.Shortener().tinyurl.short(entry1.get())

        entry2.insert(END, url)

        print(pyshorteners.Shortener().tinyurl.expand(url))


#define frontend
label1 = Label(window, text="Enter Link To Shorten", font=("Helvetica", 34))
label1.pack(pady=20)

entry1 = Entry(window, font=("Helvetica", 24))
entry1.pack(pady=20)

button = Button(window, text="Shorten Link", command=shorten, font=("Helvetica", 24))
button.pack(pady=20)

label2 = Label(window, text="Shortened Link", font=("Helvetica", 14))
label2.pack(pady=50)

entry2 = Entry(window, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="systembuttonface")
entry2.pack(pady=10)

window.mainloop()
