from tkinter import *
#from cv2 import *
from PIL import Image, ImageTk
from pymysql import *


class login:

    def __init__(self,root):
        self.main_window = root
        self.main_window.title("login")
        self.main_window.geometry("1000x600+150+20")
        self.main_window.resizable(False, False)
        self.main_window.config(bg="white")
        # college logo

        self.logoimg = ImageTk.PhotoImage(Image.open("logo.png"))
        self.logoimg = self.logoimg._PhotoImage__photo.subsample(3, 3)
        self.logo_img_label = Label(self.main_window, image=self.logoimg, bg="white")
        self.logo_img_label.place(x=10, y=0, height="120", width="120")

        # college name
        Label(self.main_window, text="JAI HIND COLLEGE", font=("Times bold", 50), bg="white", fg="#1f4b99").place(x=160,
                                                                                                                  y=20)

        # frame
        frame = Frame(self.main_window, highlightthickness=2, bd=5)
        frame.place(x=100, y=100, height="400", width="800")
        frame.config(bg="WHITE", highlightbackground="#1f4b99")

        # image
        self.img = ImageTk.PhotoImage(Image.open("login1.jpg"))
        self.panel = Label(self.main_window, image=self.img, bg="white")
        self.panel.place(x=150, y=170, height="300", width="200")

        # entries
        Label(frame, text="USERNAME ", font=("Times", 15, "bold"), bg="white").place(x=320, y=110)
        e1 = Entry(frame, highlightthickness=2)
        e1.config(highlightcolor="black", highlightbackground="black")
        e1.place(x=500, y=114, width="200")

        Label(frame, text="Password ", font=("Times", 15, "bold"), bg="white").place(x=325, y=210)
        e2 = Entry(frame, show="*", highlightthickness=2)
        e2.config(highlightcolor="black", highlightbackground="black")
        e2.place(x=500, y=210, width="200")

        # button

        self.image1 = PhotoImage(file=r"button.png")
        self.image1 = self.image1.subsample(5, 5)
        self.btn1 = Button(frame, image=self.image1, text="Login", bd=0, bg="white")
        self.btn1.place(x=380, y=300, width=180, height="40")
    def connection(self):
        connecting=connect(host='localhost',user='root',password='');
        if connecting:
            print("connected")

root=Tk()
obj = login(root)
obj.connection()
root.mainloop()
