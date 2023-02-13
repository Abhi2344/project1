from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
class rms_details:

    def __init__(self,root) :
       
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+225+205")

        global sel_roomno
        global des
        global sel_rmno
        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        lbl_title = Label(self.root,text="Service details",font=("consolas",15,"bold"),fg="grey")
        lbl_title.place(x=430,y=10,width=200,height=30)

        frame=Frame(self.root,bg="white")
        frame.place(x=250,y=50,width=600,height=200)

        floorno=lbl=Label(frame,text="Roomno",font=("consolas",10,"bold"),fg="black",bg="white")
       
        floorno.place(x=150,y=15)

        # self.flno=ttk.Entry(frame,font=("times new roman",10,"bold"))
        # self.flno.place(x=150,y=70,width=230)
        sel_roomno = StringVar()
        self.security_q=ttk.Combobox(frame,font=("consolas",10,"bold"),textvariable=sel_roomno,width=35)
        self.security_q["values"]=("select","101","102","103","104","105","106","201","202","203","204","205","206","301","302","303","304","305","306")
        self.security_q.place(x=150,y=40,width=230)
        self.security_q.current(0)

        floorno=lbl=Label(frame,text="Description",font=("consolas",10,"bold"),fg="black",bg="white")
      
        
        floorno.place(x=150,y=65)
        des=StringVar()
        self.flno=Entry(frame,font=("consolas",10,"bold"),fg="black",bg="white",textvariable=des,border=0)
        self.flno.config(font=1)
        self.flno.place(x=150,y=90)
        frame1=Frame(frame,width=230,height=2,bg="violet").place(x=150,y=112)

        regbutton=Button(frame,text="Order",font=("consolas",15,"bold"),command=self.ser_details,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=200,y=120,width=120,height=35)

        frame1=Frame(self.root,bg="white",bd=10,relief=RAISED)
        frame1.place(x=250,y=270,width=600,height=160)

        lbl_title = Label(frame1,text="check status",font=("consolas",15,"bold"),fg="grey")
        lbl_title.place(x=180,y=10,width=200,height=30)

        floorno=Label(frame1,text="Roomno",font=("consolas",10,"bold"),fg="black",bg="white")
        floorno.place(x=80,y=50)
        sel_rmno=StringVar()
        self.security_q=ttk.Combobox(frame1,font=("consolas",10,"bold"),textvariable=sel_rmno,width=35)
        self.security_q["values"]=("select","101","102","103","104","105","106","201","202","203","204","205","206","301","302","303","304","305","306")
        self.security_q.place(x=150,y=50,width=230)
        self.security_q.current(0)
        # floorno=Label(frame1,text="status",font=("times new roman",10,"bold"),fg="black",bg="white")
        # floorno.place(x=500,y=50,width=60)
        self.status=Label(frame1,text="",font=("consolas",10,"bold"),fg="black",bg="white")
        self.status.place(x=200,y=125)
        regbutton=Button(frame1,text="check status",font=("consolas",15,"bold"),borderwidth=1,command=self.sta,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=200,y=80,width=140,height=35)
        
        # self.sta()
    def ser_details(self):
            
            
           
            if des=='' or sel_roomno=='':
                    messagebox.showwarning("Warning","All Fields are compulsory",parent=self.root)
            else:
               
                    

                    try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                        
                        my_cursor1=conn.cursor()
                        
                        
                        my_cursor1.execute("select * from cust_booking where status=%s and av_room=%s",(
                                                                                        'booking confirm',
                                                                                        sel_roomno.get()
                        ))
                        
                        rs=my_cursor1.fetchone()

                        #  if gen==1:
                        #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"male",add.get(),nation.get(),idpr.get())
                        #  elif gen==2:
                        #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"female",add.get(),nation.get(),idpr.get())
                        #  else:
                        #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"other",add.get(),nation.get(),idpr.get())

                        if rs==None:
                             messagebox.showwarning("warning","You have not booked a room",parent=self.root)
                        else:

                            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                            my_cursor=conn.cursor()
                            
                            my_cursor.execute("insert into room_service values(%s,%s,%s,%s)",(
                                                                        '',
                                                                        sel_roomno.get(),
                                                                        des.get(),
                                                                        'request pending'
                                                                        
                                                                        
                                                                

                    ))

                            conn.commit()
                            conn.close()
                            messagebox.showinfo('confirmation', 'Request placed',parent=self.root)
                 

                 
                        
       
                   

                    except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
 
        # security_q = Label(frame,text="Menu",font=("times new roman",10,"bold"),bg="white")
        # security_q.place(x=100,y=110)

        # self.security_q=ttk.Combobox(frame,font=("times new roman",10,"bold"),textvariable=self.var_sel_room)
        # self.security_q["values"]=("select","Pav bhaji","Paneer kofta","Malai kofta","vada pav","dosa","idli sambar","misal pav","")
        # self.security_q.place(x=100,y=140,width=350)
        # self.security_q.current(0)


        
    def sta(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select status from room_service where rm_no LIKE '%{sel_rmno.get()}%'")
       
        rows=my_cursor.fetchone()
        if len(rows)!=0:
                self.status.config(text=f"status-:{str(rows)}")
                self.status.after(200,self.sta)
                for i in rows:
                    self.status.insert("",END,values=i)
        conn.commit
        conn.close()
        

        
'''
class login_window:
    def _init_(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0") ''' 

if __name__ == "__main__":
    root=Tk()
    obj1=rms_details(root)
    root.mainloop()