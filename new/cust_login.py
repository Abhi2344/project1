from  tkinter import *
from tkinter import ttk
import mysql.connector

from tkinter import messagebox
from PIL import Image,ImageTk
from customerhome import cHotelManagementSystem
from custreg import cust_regs
import os
def main():
    win = Tk()
    app = clogin_window(win)
    win.mainloop()

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class clogin_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")     

        global uname 
        global passwo  
       
        lbl_bg=Label(self.root,bg="#95B9C7")
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white",bd=2)
        frame.place(x=510,y=120,width=340,height=450)

        img1=Image.open(r"E:\hotel_images\hotel_images\login1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=620,y=130,width=120,height=100)

        get_str=Label(frame,text="Customer login",font=("consolas",20,"bold"),fg="black",bg="white",justify=CENTER)
        get_str.place(x=70,y=100)


        username=lbl=Label(frame,text="Username",font=("consolas",15,"bold"),fg="black",bg="white")
        username.config(font=1)
        username.place(x=40,y=155)


        uname = StringVar()
        self.txtuser=Entry(frame,font=("consolas",15,"bold"),fg="#F433FF",border=0,textvariable=uname)
        self.txtuser.config(font=1)
        self.txtuser.place(x=40,y=180)
        frame1=Frame(frame,width=200,height=2,bg="black").place(x=40,y=205)

        password=lbl=Label(frame,text="Password",font=("consolas",15,"bold"),fg="black",bg="white")
        password.config(font=1)
        password.place(x=40,y=230)

        passwo = StringVar()
        self.txtpass=Entry(frame,font=("consolas",15,"bold"),fg="#F433FF",border=0,textvariable=passwo,show="*")
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


        
        loginbutton=Button(frame,text="login",command=self.clogin_details,font=("consolas",15,"bold"),border=0,fg="gold",bg="orange",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=300,width=120,height=35)


        regbutton=Button(frame,text="New user registration",font=("consolas",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="black",command=self.cust_reg)
        regbutton.place(x=20,y=350,width=180)

       
        forpassbutton=Button(frame,text="forgot password",font=("consolas",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="black")
        forpassbutton.place(x=10,y=390,width=160)

    def clogin_details(self):
            usname =uname.get()
            passw = passwo.get()
           
               
               

                
            if usname=='' or passw=='':
                    messagebox.showwarning("Warning","All Fields are compulsory")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from cust_reg where email=%s and password=%s",(
                                                                                        usname,
                                                                                        passw
                                                                                        



                ))
                row = my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("error","Invalid username and password")
                else:
                    # messagebox.showinfo("success","you have logged in successfully",parent=self.root)
                    # self.new_window=Toplevel(self.root)
                    # self.app=cHotelManagementSystem(self.new_window)
                    self.root.destroy()
                    os.system("python customerhome.py")
                conn.commit()
                conn.close()
                

    def cust_reg(self):
        self.root.destroy()
        os.system("python custreg.py")

class cust_regs:
    def _init_(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")        

        global fname
        global lname
        global email
        global cont
        global passw
        global cpassw
        global secuq
        global secua
        global add
        # global gender

        global gen
        global idpr
        global nation
       
        # self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        register_lbl=Label(root,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=600,y=40)

        self.bg1=ImageTk.PhotoImage(file=r"images\bed.jpg")
        lbl_bg1=Label(self.root,image=self.bg1)
        lbl_bg1.place(x=50,y=-300,width=450,height=1200)


        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=85,width=650,height=430)


       

        fname = Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        fname.place(x=50,y=5)

        fname = StringVar()
        fname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fname)
        fname_entry.place(x=50,y=30,width=230)

        lname = Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
        lname.place(x=50,y=55)

        lname = StringVar()
        lname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=lname)
        lname_entry.place(x=50,y=80,width=230)

        email = Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email.place(x=50,y=105)

        email=StringVar()
        self.txt_email=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=email)
        self.txt_email.place(x=50,y=130,width=230)

        contactno = Label(frame,text="MobileNo",font=("times new roman",10,"bold"),bg="white")
        contactno.place(x=50,y=155)

        cont = StringVar()
        contactno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cont)
        contactno.place(x=50,y=180,width=230)

        security_q = Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
        security_q.place(x=50,y=205)

        secuq=StringVar()
        combo_security_q=ttk.Combobox(frame,font=("times new roman",10,"bold"),textvariable=secuq,state="readonly")
        combo_security_q["values"]=("select","your birth place","your favourite game","Your pet name")
        combo_security_q.place(x=50,y=230,width=230)
        combo_security_q.current(0)

        security_q_answer = Label(frame,text="Security answer",font=("times new roman",10,"bold"),bg="white")
        security_q_answer.place(x=370,y=205)

        secua=StringVar()
        security_q_answer=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=secua)
        security_q_answer.place(x=370,y=230,width=230)


        password = Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
        password.place(x=370,y=5)

        passw =StringVar()
        password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=passw)
        password.place(x=370,y=30,width=230)

        confi_password = Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
        confi_password.place(x=370,y=55)

        cpassw = StringVar()
        confi_password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cpassw)
        confi_password.place(x=370,y=80,width=230)

        gen = StringVar()
        gender = Label(frame ,text="Gender",font=("times new roman",10,"bold"))
        gender.place(x=370,y=105)
        # gender = Label(frame,text="Gender",font=("times new roman",10,"bold"),textvariable=gen,bg="white")
        # gender.place(x=370,y=105)
        radiobutton_1 = ttk.Radiobutton(frame, text='Male', variable=gen, value="male")
        radiobutton_1.pack()
        radiobutton_1.place(x=370,y=130)
        radiobutton_2 = ttk.Radiobutton(frame, text='Female', variable=gen, value="female")
        radiobutton_2.pack()
        radiobutton_2.place(x=370,y=155)
        radiobutton_3 = ttk.Radiobutton(frame, text='Other', variable=gen, value="other")
        radiobutton_3.pack()
        radiobutton_3.place(x=370,y=180)

        labNationality=Label(frame,text="Nationality",font=("arial",10,"bold"),padx=2,pady=2)
        labNationality.place(x=370,y=255)

        nation=StringVar()
        combo_Nationality=ttk.Combobox(frame,text="Nationality",font=("arial",10,"bold"),textvariable=nation)
        combo_Nationality["value"]=("Indian","American","russian","german","Other")
        combo_Nationality.current(0)
        combo_Nationality.place(x=370,y=280,width=230)
        
        labIdProof=Label(frame,text="Id Proof Type",font=("arial",10,"bold"),padx=2,pady=2)
        labIdProof.place(x=50,y=305)

        idpr=StringVar()
        combo_Id=ttk.Combobox(frame,text="Id proof Type",font=("arial",10,"bold"),textvariable=idpr)
        combo_Id["value"]=("AadharCard","DrivingLicence","Passport")
        combo_Id.current(0)
        combo_Id.place(x=50,y=330,width=230)

        address = Label(frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        address.place(x=50,y=255)

        add=StringVar()
        address=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
        address.place(x=50,y=280,width=230)

        regbutton=Button(frame,text="Register",font=("times new roman",15,"bold"),command=self.admin_details,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        regbutton.place(x=250,y=375,width=120,height=35)

        


    def admin_details(self):
            un =fname.get()
            ln = lname.get()
            em = email.get()
            con = cont.get()
            passwo = passw.get()
            
            cpasswo = cpassw.get()
            if un=='' or passw=='' or em==''or con=='' or passwo=='' or cpasswo=='':
                    messagebox.showwarning("Warning","All Fields are compulsory")
            else:
                if passwo!=cpasswo:
                    messagebox.showwarning("Warning","password and confirm password should be equal")
                else:
                    

                    try:
                        #  if gen==1:
                        #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"male",add.get(),nation.get(),idpr.get())
                        #  elif gen==2:
                        #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"female",add.get(),nation.get(),idpr.get())
                        #  else:
                        #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"other",add.get(),nation.get(),idpr.get())

                        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                        my_cursor=conn.cursor()
                        query=("select * from cust_reg where email=%s")
                        value =(em,)
                        my_cursor.execute(query,value)
                        row = my_cursor.fetchone()
                        if row!=None:
                            messagebox.showwarning("warning","Email alredy registered use different email")
                        else:
                            my_cursor.execute("insert into cust_reg values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                      '',
                                                                      un,
                                                                      ln,
                                                                      em,
                                                                      con,
                                                                      secuq.get(),
                                                                      secua.get(),
                                                                      passwo,
                                                                      cpasswo,
                                                                      gen.get(),
                                                                      add.get(),
                                                                      nation.get(),
                                                                      idpr.get()
                                                            

                 ))

                        conn.commit()
                        conn.close()
                        messagebox.showinfo('confirmation', 'Record Saved',parent=self.root)
                 

                 
                        
       
                   

                    except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

if __name__ == "__main__":
    main()