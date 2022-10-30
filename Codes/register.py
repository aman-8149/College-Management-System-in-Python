from tkinter import *
#from cv2 import *
from PIL import Image, ImageTk


class register:

    def __init__(self, main_window):
        self.main_window = main_window
        # college logo

        self.logoimg = ImageTk.PhotoImage(Image.open("logo.png"))
        self.logoimg = self.logoimg._PhotoImage__photo.subsample(3, 3)
        self.logo_img_label = Label(self.main_window, image=self.logoimg, bg="white")
        self.logo_img_label.place(x=10, y=0, height="120", width="120")

        # college name
        Label(self.main_window, text="JAI HIND COLLEGE", font=("Times bold", 50), bg="white", fg="#1f4b99").place(x=160,
                                                                                                                  y=20)

        # frame
        frame = Frame(self.main_window, highlightthickness=2,bd=5)
        frame.place(x=100, y=100, height="400", width="800")
        frame.config(bg="WHITE", highlightbackground="#1f4b99")

        # image
        self.img = ImageTk.PhotoImage(Image.open("login1.jpg"))
        self.panel = Label(self.main_window, image=self.img, bg="white")
        self.panel.place(x=150, y=170, height="300", width="200")

        # entries
        Label(frame, text="USERNAME ", font=("Times", 15, "bold"), bg="white").place(x=290, y=10)
        e1 = Entry(frame, highlightthickness=1)
        e1.config(highlightcolor="black", highlightbackground="black")
        e1.place(x=290, y=50, width="200")

        Label(frame, text="Password ", font=("Times", 15, "bold"), bg="white").place(x=290, y=140)
        e2 = Entry(frame, show="*", highlightthickness=1)
        e2.config(highlightcolor="black", highlightbackground="black")
        e2.place(x=290, y=180, width="200")

        Label(frame, text="Mobile No. ", font=("Times", 15, "bold"), bg="white").place(x=550, y=10)
        e3 = Entry(frame, highlightthickness=1)
        e3.config(highlightcolor="black", highlightbackground="black")
        e3.place(x=550, y=50, width="200")

        Label(frame, text="Confirm Password ", font=("Times", 15, "bold"), bg="white").place(x=550, y=140)
        e4 = Entry(frame, highlightthickness=1,show="*")
        e4.config(highlightcolor="black", highlightbackground="black")
        e4.place(x=550, y=180, width="200")

        Label(frame, text="Email ID. ", font=("Times", 15, "bold"), bg="white").place(x=410, y=240)
        e5 = Entry(frame, highlightthickness=1)
        e5.config(highlightcolor="black", highlightbackground="black")
        e5.place(x=410, y=280, width="200")

        # button

        self.image1 = PhotoImage(file=r"button2.png")
        self.image1 = self.image1.subsample(5, 5)
        self.btn1 = Button(frame, image=self.image1, text="Login", bd=0, bg="white")
        self.btn1.place(x=430, y=340, width=180, height="40")


main_window = Tk()
main_window.geometry("1000x600+150+20")
main_window.resizable(False, False)
main_window.config(bg="white")
obj=register(main_window)
main_window.mainloop()
