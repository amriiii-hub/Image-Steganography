from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
#import stepic

root = Tk()
root.title("IMG STENO GREAPHY")
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

s=StringVar()

#img=images()

def openf():
    fname=filedialog.askopenfilename(title='open')
    print(fname)
    img=Image.open(fname)
    img=img.resize((250,250),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    btn2 = Button(root, text='message',command=openf1).pack()
def openf1():
    newwin = Toplevel(root)
    L=Label(newwin,text="Enter Message:")
    L.pack()
    e=Entry(newwin,width=30,textvariable=s)
    e.pack()
    btn2 = Button(newwin, text='Encrypt', command=open2).pack()
def open2():
    win1 = Toplevel(root)
    btn1 = Button(win1, text='decoder', command=open3,bg="red",fg='blue')
    btn1.pack()
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\Wallpaper\\bg1.jpg"))
    panel = Label(win1, image = img)
    panel.pack()
    root.mainloop()

def open4():
    win2 = Toplevel(root)
    label=Label(win2,text="IMAGE ENCODER VALUES",bg="blue")
    label.pack()
    d=s.get()
    lab2=Label(win2,text=d,font=20).pack()
    root.mainloop()

   
    #imgs=img.get()
    #labe6=Lable(win1,image=imgs,width=100,height=200).pack()
   
   
def open3():
    win1 = Toplevel(root)
    d=s.get()
    lab2=Label(win1,text=d,font=20).pack()
    #im2 = Image.open(im1)
    #stegoImage = stepic.decode(im2)
    #stegoImage.show()

    
btn1 = Button(root, text='open image', command=openf).pack()
root.mainloop()
