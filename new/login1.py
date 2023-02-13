from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x1000+0+0")        
       
        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open(r"E:\hotel_images\hotel_images\loginlogo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=635,y=175,width=100,height=100)

        get_str=Label(frame,text=" welcome admin ",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        username=lbl=Label(frame,text="user name",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)

        img2=Image.open(r"E:\hotel_images\hotel_images\loginlogo.png")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=560,y=328,width=20,height=20)


        loginbutton=Button(frame,text="login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=300,width=120,height=35)


        regbutton=Button(frame,text="New user registration",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbutton.place(x=20,y=350,width=180)


        forpassbutton=Button(frame,text="forgot password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forpassbutton.place(x=10,y=390,width=160)

if __name__ == "__main__":
    root = Tk()
    app=login_window(root)
    root.mainloop()