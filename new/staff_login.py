from  tkinter import * 
from tkinter import ttk
import mysql.connector

from tkinter import messagebox
from PIL import Image,ImageTk
from customerhome import cHotelManagementSystem
from custreg import cust_regs
from staff_home import sHotelManagementSystem
from rmservice_home import rsHotelManagementSystem
from kitechens_home import ksHotelManagementSystem
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
        global pos
       
        lbl_bg=Label(self.root,bg="#95B9C7")
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white",bd=2)
        frame.place(x=510,y=120,width=360,height=500)

        img1=Image.open(r"E:\hotel_images\hotel_images\login1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=620,y=130,width=120,height=100)

        get_str=Label(frame,text="Staff login",font=("consolas",20,"bold"),fg="black",bg="white",justify=CENTER)
        get_str.place(x=88,y=100)


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

        pos = StringVar()
        gender = Label(frame,text="Position",font=("consolas",15,"bold"),fg="black",bg="white")
        gender.config(font=1)
        
        gender.place(x=40,y=300)
        radiobutton_1 = ttk.Radiobutton(frame, text='Recieptionist',variable=pos, value="Recieptionist")
        radiobutton_1.pack()
        
        radiobutton_1.place(x=40,y=330)
        radiobutton_2 = ttk.Radiobutton(frame, text='Room service', variable=pos, value="Room service")
        radiobutton_2.pack()
        radiobutton_2.place(x=140,y=330)
        radiobutton_3 = ttk.Radiobutton(frame, text='Kitchen staff', variable=pos, value="Kitchen staff")
        radiobutton_3.pack()
        radiobutton_3.place(x=260,y=330)

        # img2=Image.open(r"images\loginlogo.png")
        # img2=img2.resize((20,20),Image.ANTIALIAS)
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        # lblimg1.place(x=560,y=268,width=20,height=20)

        # img3=Image.open(r"images\password1.png")
        # img3=img3.resize((20,20),Image.ANTIALIAS)
        # self.photoimage3=ImageTk.PhotoImage(img3)
        # lblimg2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        # lblimg2.place(x=560,y=346,width=20,height=20)


        loginbutton=Button(frame,text="login",font=("consolas",15,"bold"),command=self.clogin_details,border=0,fg="gold",bg="orange",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=360,width=120,height=35)


        

        forpassbutton=Button(frame,text="forgot password",font=("consolas",10,"bold"),border=0,fg="black",bg="white",activeforeground="white",activebackground="black")
        forpassbutton.place(x=10,y=420,width=160)

    def clogin_details(self):
            usname =uname.get()
            passw = passwo.get()
           
               
               

                
            if usname=='' or passw=='':
                    messagebox.showwarning("Warning","All Fields are compulsory")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from staff_details where username=%s and password=%s and position=%s",(
                                                                                        usname,
                                                                                        passw,
                                                                                        pos.get()
                                                                                        



                ))
                row = my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("error","Invalid username and password")
                # elif pos.get=="Recieptionist":
                #     messagebox.showinfo("","Receptionist")
                #     self.new_window=Toplevel(self.root)
                #     self.app=sHotelManagementSystem(self.new_window)
                # elif pos.get()=="Room service":
                #     messagebox.showinfo("","room service")
                # elif pos.get()=="Kitchen staff":
                #     messagebox.showinfo("","Kitchen staff")
                else:
                    if pos.get()=="Recieptionist":
                    #    messagebox.showinfo("","Receptionist")
                       self.new_window=Toplevel(self.root)
                       self.app=sHotelManagementSystem(self.new_window)
                    elif pos.get()=="Room service":
                        # messagebox.showinfo("","room service")
                        self.new_window=Toplevel(self.root)
                        self.app=rsHotelManagementSystem(self.new_window)
                    elif pos.get()=="Kitchen staff":
                        # messagebox.showinfo("","Kitchen staff")
                        self.new_window=Toplevel(self.root)
                        self.app=ksHotelManagementSystem(self.new_window)

                    else:

                        # messagebox.showinfo("success","you have logged in successfully",parent=self.root)
                        self.root.destroy()
                        os.system("python staff_home.py")
                conn.commit()
                conn.close()

class sta_details:

    def _init_(self,root) :
       
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x425+232+205")

        global fname
        global ag
        global add
        global gen
        global pos
        global id_no
        global mbno
        global uname
        global pas

        self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        lbl_title = Label(self.root,text="Staff details",font=("times new roman",25,"bold"),bg="blue",fg="grey")
        lbl_title.place(x=430,y=30,width=200,height=30)

        frame=Frame(self.root,bg="white")
        frame.place(x=250,y=70,width=700,height=400)

        floorno=lbl=Label(frame,text="Full name",font=("times new roman",10,"bold"),fg="black",bg="white")
        floorno.place(x=40,y=40)

        fname = StringVar()
        self.flno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fname)
        self.flno.place(x=40,y=70,width=230)

        idno=lbl=Label(frame,text="Idno",font=("times new roman",10,"bold"),fg="black",bg="white")
        idno.place(x=40,y=100)

        id_no = StringVar()
        self.ino=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=id_no)
        self.ino.place(x=40,y=130,width=230)

        mobno=lbl=Label(frame,text="Mobile No",font=("times new roman",10,"bold"),fg="black",bg="white")
        mobno.place(x=40,y=160)

        mbno = StringVar()
        self.mno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=mbno)
        self.mno.place(x=40,y=190,width=230)

        addr=lbl=Label(frame,text="Address",font=("times new roman",10,"bold"),fg="black",bg="white")
        addr.place(x=40,y=220)

        add = StringVar()
        self.ad=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
        self.ad.place(x=40,y=250,width=230)

        age=lbl=Label(frame,text="Age",font=("times new roman",10,"bold"),fg="black",bg="white")
        age.place(x=350,y=40)

        ag = StringVar()
        self.ag=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=ag)
        self.ag.place(x=350,y=70,width=230)

        gen = StringVar()
        gender = Label(frame,text="Gender",font=("times new roman",10,"bold"),bg="white")
        gender.place(x=350,y=100)
        radiobutton_1 = ttk.Radiobutton(frame, text='Male', variable=gen, value="Male")
        radiobutton_1.pack()
        radiobutton_1.place(x=370,y=130)
        radiobutton_2 = ttk.Radiobutton(frame, text='Female', variable=gen, value="Female")
        radiobutton_2.pack()
        radiobutton_2.place(x=370,y=160)
        radiobutton_3 = ttk.Radiobutton(frame, text='Other', variable=gen, value="Other")
        radiobutton_3.pack()
        radiobutton_3.place(x=370,y=190)

        pos = StringVar()
        gender = Label(frame,text="position",font=("times new roman",10,"bold"),bg="white")
        gender.place(x=350,y=220)
        radiobutton_1 = ttk.Radiobutton(frame, text='Recieptionist', variable=pos, value="Recieptionist")
        radiobutton_1.pack()
        radiobutton_1.place(x=370,y=250)
        radiobutton_2 = ttk.Radiobutton(frame, text='Room service', variable=pos, value="Room service")
        radiobutton_2.pack()
        radiobutton_2.place(x=470,y=250)
        radiobutton_3 = ttk.Radiobutton(frame, text='Kitchen staff', variable=pos, value="Kitchen staff")
        radiobutton_3.pack()
        radiobutton_3.place(x=590,y=250)

        age=lbl=Label(frame,text="username",font=("times new roman",10,"bold"),fg="black",bg="white")
        age.place(x=40,y=275)

        uname = StringVar()
        self.ag=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=uname)
        self.ag.place(x=40,y=300,width=230)

        age=lbl=Label(frame,text="password",font=("times new roman",10,"bold"),fg="black",bg="white")
        age.place(x=350,y=270)

        pas = StringVar()
        self.ag=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=pas)
        self.ag.place(x=350,y=300,width=230)


        regbutton=Button(frame,text="Add",font=("times new roman",15,"bold"),command=self.admin_details,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        regbutton.place(x=250,y=325,width=120,height=35)

    def admin_details(self):
            
            
           
            if fname=='' or mbno=='' or ag==''or add=='' or gen=='' or pos=='':
                    messagebox.showwarning("Warning","All Fields are compulsory")
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
                        # query=("select * from cust_bo where av_room=%s")
                        # value =(sel_roomno.get(),)
                        # my_cursor.execute(query,value)
                        # row = my_cursor.fetchone()
                        # if row!=None:
                        #     messagebox.showwarning("warning","Room already booked please choose another room no")
                        # else:
                        my_cursor.execute("insert into staff_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                      '',
                                                                      fname.get(),
                                                                      id_no.get(),
                                                                      mbno.get(),
                                                                      add.get(),
                                                                      ag.get(),
                                                                      gen.get(),
                                                                      pos.get(),
                                                                      uname.get(),
                                                                      pas.get()
                                                                      
                                                                      
                                                            

                 ))

                        conn.commit()
                        conn.close()
                        messagebox.showinfo('confirmation', 'Record Saved',parent=self.root)
                 

                 
                        
       
                   

                    except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
        
if __name__ == "__main__":
    main()