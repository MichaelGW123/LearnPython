# Michael Williamson
# Python Program to launch Webpages
# 7/29/2020

import webbrowser
import tkinter

root = tkinter.Tk()

root.title("Web Browser")
root.geometry("300x200")


def google():
    webbrowser.open("www.google.com")


#opengoogle = tkinter.Button(root, text = "hello", command = google).pack(pady=20)

root.mainloop()