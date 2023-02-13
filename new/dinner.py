from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
class din_details:

    def __init__(self,root) :
       
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+225+205")

        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        global fl_no
        global me_ty
        global me
        global qu
        lbl_title = Label(self.root,text="Dinner details",font=("consolas",15,"bold"),bg="light blue",fg="green")
        lbl_title.place(x=430,y=30,width=200,height=30)

        frame=Frame(self.root,bg="white",bd=10,relief=RAISED)
        frame.place(x=250,y=70,width=600,height=350)

        floorno=lbl=Label(frame,text="Roomno",font=("consolas",10,"bold"),fg="black",bg="white")
        floorno.place(x=150,y=40)

        fl_no=StringVar()
        # self.flno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fl_no)
        # self.flno.place(x=150,y=70,width=230)
        self.security_q=ttk.Combobox(frame,font=("consolas",10,"bold"),textvariable=fl_no,width=35)
        self.security_q["values"]=("select","101","102","103","104","105","106","201","202","203","204","205","206","301","302","303","304","305","306")
        self.security_q.place(x=150,y=70,width=230)
        self.security_q.current(0)

        security_q = Label(frame,text="Select Meal type",font=("consolas",10,"bold"),bg="white")
        security_q.place(x=150,y=100)

        me_ty=StringVar()
        combo_security_q=ttk.Combobox(frame,font=("consolas",10,"bold"),state="readonly",textvariable=me_ty)
        combo_security_q["values"]=("select","Dinner","Lunch","breakfast")
        combo_security_q.place(x=150,y=125,width=230)
        combo_security_q.current(0)

        floorno=lbl=Label(frame,text="meal",font=("consolas",10,"bold"),fg="black",bg="white")
        floorno.place(x=150,y=150)

        me = StringVar()
        self.flno=ttk.Combobox(frame,font=("consolas",10,"bold"),state="readonly",textvariable=me)
        self.flno["values"]=("select","pav bhaji","vada pav","misal pav","dosa","idli","chole bhature")
        self.flno.place(x=150,y=180,width=230)
        self.flno.current(0)
        # frame1=Frame(frame,width=230,height=2,bg="violet").place(x=150,y=202)

        self.qul=lbl=Label(frame,text="quantity",font=("consolas",10,"bold"),fg="black",bg="white")
        self.qul.place(x=150,y=210)
        qu=StringVar()
        self.qu=Spinbox(frame,from_=1,to=10,bd=3,textvariable=qu)
        self.qu.place(x=150,y=230,width=230)

        regbutton=Button(frame,text="Order",font=("consolas",15,"bold"),command=self.din_detail,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=200,y=260,width=120,height=35)

        # security_q = Label(frame,text="Menu",font=("times new roman",10,"bold"),bg="white")
        # security_q.place(x=100,y=110)

        # self.security_q=ttk.Combobox(frame,font=("times new roman",10,"bold"),textvariable=self.var_sel_room)
        # self.security_q["values"]=("select","Pav bhaji","Paneer kofta","Malai kofta","vada pav","dosa","idli sambar","misal pav","")
        # self.security_q.place(x=100,y=140,width=350)
        # self.security_q.current(0)

        
    def din_detail(self):
            
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
           
            
            if me_ty=='' or fl_no=='':
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
                        
                        my_cursor1=conn.cursor()
                        
                        
                        my_cursor1.execute("select * from cust_booking where status=%s and av_room=%s",(
                                                                                        'booking confirm',
                                                                                        fl_no.get()
                        ))
                        
                        rs=my_cursor1.fetchone()
                        
                        
                        if rs==None:
                             messagebox.showwarning("warning","You have not booked a room",parent=self.root)
                        
                        else:
                           
                            print("true")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into dinner values(%s,%s,%s,%s,%s,%s)",(
                                                                        '',
                                                                        fl_no.get(),
                                                                        me_ty.get(),
                                                                        me.get(),
                                                                        qu.get(),
                                                                        'pending'
                                                                        
                                                                        
                                                                

                    ))
                            
                            conn.commit()
                            conn.close()
                            messagebox.showinfo('confirmation', 'order placed',parent=self.root)
                    

                        
                        
       
                   

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
    obj1=din_details(root)
    root.mainloop()