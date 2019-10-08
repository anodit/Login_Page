from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("800x600+300+50")
        # All Images
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon = PhotoImage(file="images/man-user.png")
        self.pass_icon = PhotoImage(file="images/password.png")
        self.logo_icon = PhotoImage(file="images/logo.png")

        # =====variables======
        self.uname = StringVar()
        self.pass_ = StringVar()

        bg_lb1 = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="#0f73c4", fg="#deefed",
                      bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=170, y=150)
        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15))
        txtuser.grid(row=1, column=1, padx=20)
        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white")
        lblpass.grid(row=2, column=0, padx=20, pady=20)
        txtpass = Entry(Login_Frame, bd=5, relief=GROOVE, textvariable=self.pass_, font=("", 15))
        txtpass.grid(row=2, column=1,
                     padx=20)
        btn_log = Button(Login_Frame, text="Login", width=15, command=self.login, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green")
        btn_log.grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.uname.get() == "Mohit" and self.pass_.get() == "12345":
            messagebox.showinfo("Successfull", f"Welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


root = Tk()
obj = Login_System(root)
root.mainloop()
