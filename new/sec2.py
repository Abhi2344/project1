from  tkinter import *
from tkinter import ttk
import mysql.connector
import os
from PIL import Image,ImageTk
from admin_home import HotelManagementSystem

from tkinter import messagebox





class login_window:
    # def validatepass():
    #     uname =username.get()
    #     passw = password.get()
    #     if uname=='' or passw=='':
    #         messagebox.showinfo("fill the empty field!!!")
    #     else:
    #         if uname=="admin" and passw=="admin":
    #          messagebox.showinfo("Login success")



    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")       

        
        global username
        global password
       
        # self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
        lbl_bg=Label(self.root,bg="#95B9C7")
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white",bd=2)
        frame.place(x=510,y=130,width=340,height=450)

        img1=Image.open(r"E:\hotel_images\hotel_images\login1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=620,y=130,width=120,height=100)

        get_str=Label(frame,text="Admin login",font=("consolas",20,"bold"),fg="black",bg="white",justify=CENTER)
        get_str.place(x=80,y=100)

        username=lbl=Label(frame,text="User name",font=("consolas",15,"bold"),fg="black",bg="white")
        username.config(font=1)
        username.place(x=40,y=155)

       
        username=StringVar()
        self.txtuser=Entry(frame,border=0,font=("consolas",15,"bold"),fg="#F433FF",textvariable=username)
        self.txtuser.config(font=1)
        self.txtuser.place(x=40,y=180)

        frame1=Frame(frame,width=200,height=2,bg="black").place(x=40,y=205)
        password=lbl=Label(frame,text="Password",font=("consolas",15,"bold"),fg="black",bg="white")
        password.config(font=1)
        password.place(x=40,y=230)

        password=StringVar()
        self.txtpass=Entry(frame,font=("consolas",15,"bold"),fg="#F433FF",border=0,textvariable=password,show="*")
        self.txtpass.config(font=1)
        self.txtpass.place(x=40,y=260)

        frame2=Frame(frame,width=200,height=2,bg="black").place(x=40,y=285)
        # img2=Image.open(r"images\loginlogo.png")
        # img2=img2.resize((20,20),Image.ANTIALIAS)
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        # lblimg1.place(x=560,y=338,width=20,height=20)

        # img3=Image.open(r"images\password1.png")
        # img3=img3.resize((20,20),Image.ANTIALIAS)
        # self.photoimage3=ImageTk.PhotoImage(img3)
        # lblimg2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        # lblimg2.place(x=560,y=413,width=20,height=20)


        loginbutton=Button(frame,text="login",command=self.admin_details,font=("consolas",15,"bold"),border=0,fg="gold",bg="orange",activeforeground="white",activebackground="red")
        loginbutton.place(x=95,y=300,width=120,height=35)


       
   
    


    def admin_details(self):
        uname =username.get()
        passw = password.get()
        if uname=='' or passw=='':
            messagebox.showwarning("Warning","All Fields are compulsory")
        else:
           if uname=="admin" and passw=="admin":
            # messagebox.showinfo("Login success","You have logged in successfully")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)

           else:
                messagebox.showwarning("Warning","Enter valid username and password")

    







if __name__ == "__main__":
    root = Tk()
    app=login_window(root)
    root.mainloop()