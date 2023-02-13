from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import random
class sta_details:

    def __init__(self,root) :
       
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+225+205")

        global fname
        global ag
        global add
        global gen
        global pos
        global id_no
        global mbno
        global uname
        global pas

        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        lbl_title = Label(self.root,text="Staff details",font=("consolas",20,"bold"),bd=5,bg="blue",fg="red")
        lbl_title.place(x=490,y=0,width=200,height=25)

        frame=Frame(self.root,background="white",bd=10,relief=RAISED)
        frame.place(x=250,y=35,width=700,height=390)

        floorno=lbl=Label(frame,text="Full name",font=("consolas",10,"bold"),fg="black",bg="white")
        floorno.place(x=40,y=40)

        fname = StringVar()
        self.flno=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=fname)
        self.flno.config(font=1)
        self.flno.place(x=40,y=70,width=230)
        frame1=Frame(frame,width=230,height=2,bg="violet").place(x=40,y=95)

        idno=lbl=Label(frame,text="Idno",font=("consolas",10,"bold"),fg="black",bg="white")
        idno.place(x=40,y=100)

        id_no = StringVar()
        q=random.randint(100000,1000000)
        id_no.set(q)
        self.ino=Entry(frame,font=("consolas",10,"bold"),state='readonly',border=0,fg="black",bg="white",textvariable=id_no)
        self.ino.config(font=1)
        
        self.ino.place(x=40,y=130,width=230)
        frame2=Frame(frame,width=230,height=2,bg="violet").place(x=40,y=152)

        mobno=lbl=Label(frame,text="Mobile No",font=("consolas",10,"bold"),fg="black",bg="white")
        mobno.place(x=40,y=160)

        mbno = StringVar()
        self.mno=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=mbno)
        self.mno.config(font=1)
        self.mno.place(x=40,y=190,width=230)

        frame3=Frame(frame,width=230,height=2,bg="violet").place(x=40,y=212)
        addr=lbl=Label(frame,text="Address",font=("consolas",10,"bold"),fg="black",bg="white")
        addr.place(x=40,y=220)

        add = StringVar()
        self.ad=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=add)
        self.ad.config(font=1)
        self.ad.place(x=40,y=250,width=230)
        frame4=Frame(frame,width=230,height=2,bg="violet").place(x=40,y=272)
        age=lbl=Label(frame,text="Dob",font=("consolas",10,"bold"),fg="black",bg="white")
        age.place(x=350,y=40)

        ag = StringVar()
        # self.ag=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=ag)
        # self.ag.place(x=350,y=70,width=230)
        enty_Checkindetails = DateEntry(frame,date_pattern='dd/mm/Y',border=0,fg="violet",bg="violet",padx=2,pady=6,textvariable=ag)
        enty_Checkindetails.config(font=1)
        enty_Checkindetails.place(x=350,y=70,width=230)

        gen = StringVar()
        gender = Label(frame,text="Gender",font=("consolas",10,"bold"),bg="white")
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
        gender = Label(frame,text="position",font=("consolas",10,"bold"),bg="white")
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

        age=lbl=Label(frame,text="username",font=("consolas",10,"bold"),fg="black",bg="white")
        age.place(x=40,y=275)

        uname = StringVar()
        self.ag=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=uname)
        self.ag.config(font=1)
        self.ag.place(x=40,y=300,width=230)
        frame4=Frame(frame,width=230,height=2,bg="violet").place(x=40,y=322)

        age=lbl=Label(frame,text="password",font=("consolas",10,"bold"),fg="black",bg="white")
        age.place(x=350,y=270)

        pas = StringVar()
        self.ag=Entry(frame,font=("consolas",10,"bold"),border=0,fg="black",bg="white",textvariable=pas,show="*")
        self.ag.config(font=1)
        self.ag.place(x=350,y=300,width=230)
        frame5=Frame(frame,width=230,height=2,bg="violet").place(x=352,y=322)


        regbutton=Button(frame,text="Add",font=("consolas",15,"bold"),command=self.admin_details,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=250,y=335,width=120,height=35)

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
                        messagebox.showinfo('confirmation', 'staff added sucessfully',parent=self.root)
                 

                 
                        
       
                   

                    except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
        
'''
class login_window:
    def _init_(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0") ''' 

if __name__ == "__main__":
    root=Tk()
    obj1=sta_details(root)
    root.mainloop()