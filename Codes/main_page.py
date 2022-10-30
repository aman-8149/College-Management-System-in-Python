from tkinter import *


def log():
    root.destroy()
    import login
def reg():
    root.destroy()
    import register
def face():
    root.destroy()
    import attendance

root = Tk()
root.title("main page")
btn2 = Button(root, text="Login",command=log)
btn2.place(x=10, y=10)
btn3 = Button(root, text="Register",command=reg)
btn3.place(x=10, y=50)
btn4 = Button(root, text="Attendance",command=face)
btn4.place(x=10, y=100)

# btn4=Button(root,text="Register")
# btn4.place(x=10,y=10)

root.mainloop()
