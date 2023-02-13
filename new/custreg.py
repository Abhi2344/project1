from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import os

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class cust_regs:
    def __init__(self,root):
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
        global em

        global gen
        global idpr
        global nation
       
        # self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        register_lbl=Label(root,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=600,y=40)

        self.bg1=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\bed.jpg")
        lbl_bg1=Label(self.root,image=self.bg1)
        lbl_bg1.place(x=50,y=-300,width=450,height=1200)


        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=85,width=650,height=430)


       

        fname = Label(frame,text="First Name",font=("consolas",10,"bold"),bg="white")
        fname.place(x=50,y=5)

        fname = StringVar()
        fname_entry=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=fname)
        fname_entry.config(font=1)
        fname_entry.place(x=50,y=30,width=230)
        frame1=Frame(frame,width=230,height=2,bg="violet").place(x=50,y=52)

        lname = Label(frame,text="Last Name",font=("consolas",10,"bold"),bg="white")
        lname.place(x=50,y=55)

        lname = StringVar()
        lname_entry=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=lname)
        lname_entry.config(font=1)
        lname_entry.place(x=50,y=80,width=230)
        frame2=Frame(frame,width=230,height=2,bg="violet").place(x=50,y=104)

        email = Label(frame,text="Email",font=("consolas",10,"bold"),bg="white")
        email.place(x=50,y=107)

        email=StringVar()
        self.txt_email=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=email)
        self.txt_email.config(font=1)
        self.txt_email.place(x=50,y=130,width=230)
        frame3=Frame(frame,width=230,height=2,bg="violet").place(x=50,y=152)
        contactno = Label(frame,text="MobileNo",font=("consolas",10,"bold"),bg="white")
        contactno.place(x=50,y=155)

        cont = StringVar()
        contactno=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=cont)
        contactno.config(font=1)
        contactno.place(x=50,y=180,width=230)
        frame4=Frame(frame,width=230,height=2,bg="violet").place(x=50,y=202)
        security_q = Label(frame,text="Select Security Question",font=("consolas",10,"bold"),bg="white")
        security_q.place(x=50,y=205)

        secuq=StringVar()
        combo_security_q=ttk.Combobox(frame,font=("consolas",10,"bold"),background="violet",textvariable=secuq,state="readonly")
        combo_security_q["values"]=("select","your birth place","your favourite game","Your pet name")
        combo_security_q.place(x=50,y=230,width=230)
        combo_security_q.current(0)

        security_q_answer = Label(frame,text="Security answer",font=("consolas",10,"bold"),bg="white")
        security_q_answer.place(x=370,y=205)

        secua=StringVar()
        security_q_answer=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=secua)
        security_q_answer.config(font=1)
        security_q_answer.place(x=370,y=230,width=230)
        frame5=Frame(frame,width=230,height=2,bg="violet").place(x=370,y=252)


        password = Label(frame,text="Password",font=("consolas",10,"bold"),bg="white")
        password.place(x=370,y=5)

        passw =StringVar()
        password=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=passw,show="*")
        password.config(font=1)
        password.place(x=370,y=30,width=230)
        frame6=Frame(frame,width=230,height=2,bg="violet").place(x=370,y=52)


        confi_password = Label(frame,text="Confirm Password",font=("consolas",10,"bold"),bg="white")
        confi_password.place(x=370,y=55)

        cpassw = StringVar()
        confi_password=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=cpassw,show="*")
        confi_password.config(font=1)
        confi_password.place(x=370,y=80,width=230)
        frame7=Frame(frame,width=230,height=2,bg="violet").place(x=370,y=102)

        gen = StringVar()
        gender = Label(frame ,text="Gender",font=("consolas",10,"bold"),bg="white")
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

        labNationality=Label(frame,text="Nationality",font=("consolas",10,"bold"),padx=2,pady=2,bg="white")
        labNationality.place(x=370,y=258)

        nation=StringVar()
        combo_Nationality=ttk.Combobox(frame,text="Nationality",font=("consolas",10,"bold"),textvariable=nation)
        combo_Nationality["value"]=("Indian","American","russian","german","Other")
        combo_Nationality.current(0)
        combo_Nationality.place(x=370,y=280,width=230)
        
        labIdProof=Label(frame,text="Id Proof Type",font=("consolas",10,"bold"),bg="white",padx=2,pady=2)
        labIdProof.place(x=50,y=305)

        idpr=StringVar()
        combo_Id=ttk.Combobox(frame,text="Id proof Type",font=("consolas",10,"bold"),textvariable=idpr)
        combo_Id["value"]=("AadharCard","DrivingLicence","Passport")
        combo_Id.current(0)
        combo_Id.place(x=50,y=330,width=230)

        address = Label(frame,text="Address",font=("consolas",10,"bold"),bg="white")
        address.place(x=50,y=255)

        add=StringVar()
        address=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=add)
        address.config(font=1)
        address.place(x=50,y=280,width=230)
        frame8=Frame(frame,width=230,height=2,bg="violet").place(x=50,y=302)

        regbutton=Button(frame,text="Register",font=("consolas",15,"bold"),command=self.admin_details,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
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
                            messagebox.showinfo('confirmation', 'Registration sucessfull',parent=self.root)
                            self.root.destroy()
                            os.system("python cust_login.py")

                 
                        
       
                   

                    except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

    
        
if __name__ == "__main__":
    root = Tk()
    app=cust_regs(root)
    root.mainloop()