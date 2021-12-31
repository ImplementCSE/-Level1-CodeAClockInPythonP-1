#Uploaded by Implement_CSE
# importing the supporting libraries
from tkinter import *
from tkinter.ttk import *
from time import strftime

# Tkinter - window
root = Tk()
root.title("Digital Clock - Implement_CSE Project")

# defining the time function

def time_module():
    s = strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000, time_module)


# declaring the labels
label = Label(root, font=("ds-digital", 80),
              background="black", foreground="orange")
label.pack(anchor='center')

# invoking the functions
time_module()
mainloop()

# Implement CSE
# Watch implementation video on YouTube
#Channel Link: https://www.youtube.com/channel/UC1u7U7AAzBN7aYkS-DoLghA
