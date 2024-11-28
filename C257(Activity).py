from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title('My Crypto Bank')
root.geometry('600x600')
root.configure(background='white')

image_1= ImageTk.PhotoImage(Image.open('image1.jpeg'))

image_2= ImageTk.PhotoImage(Image.open('image2.jpeg'))



f1=Frame(root, padx=5,pady=5,bg='white')
Label(f1, image=image_1,bg='white').grid(row=0,column=0,padx=5)
Label(f1, image=image_2,bg='white').grid(row=0,column=1,padx=5)
f1.pack()
root.mainloop()