# from _typeshed import Self
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import Image, ImageTk
from Room_details import rm_details
from Booking_detail import bok_details
from addstaff import sta_details
from dinin import dinin_details
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
# from pract import example2
conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")

class Roombooking:
    
  def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+225+205")

        my_cursor1=conn.cursor()
        query1=("select select_room from room_details")
        my_cursor1.execute(query1)
        my_data=my_cursor1.fetchall()
        
        
        my_list = [r for r,in my_data]
        global cust_cont
        global checidt
        global checodt
        global nofeld
        global nofchld
        global nofday
        global sel_roomno
      
        global sel_room
        global cust_reg

        single_room=["301",
        "302",
        "201",
        "102"
        ]
        Double_Room=["302",
        "203",
        "206",
        "104"
        ]
        Deluxe_Room=["306",
        "103",
        "202",
        ]
        DoubleDouble_Room=["305",
        "204",
        "106"
        ]
        Twin_Room=["304",
        "105",
        "101"
        ]
        Duplex_Room=["303",
        "205"
        ]



        today=date.today()
        def pickroomno(e):
            if self.security_c.get() == "Single Room":
                self.security_r.config(value=single_room)
                self.security_r.current(0)
            if self.security_c.get() == "Double Room":
                self.security_r.config(value=Double_Room)
                self.security_r.current(0)
            if self.security_c.get() == "Deluxe Room":
               self.security_r.config(value=Deluxe_Room)
               self.security_r.current(0)
            if self.security_c.get() == "Double-Double (Twin Double) Room":
               self.security_r.config(value=DoubleDouble_Room)
               self.security_r.current(0)
            if self.security_c.get() == "Twin Room":
               self.security_r.config(value=Twin_Room)
               self.security_r.current(0)
            if self.security_c.get() == "Duplex Room":
               self.security_r.config(value=Duplex_Room)
               self.security_r.current(0)
            
      
        lableframeleft=Frame(self.root,bd=10,bg="white",relief=RAISED)
        lableframeleft.place(x=380,y=20,width=500,height=400)

        lab_cust_contact =Label(lableframeleft,text="Customer contact",font=("consolas",12,"bold"),bg="white",padx=2,pady=6)
        lab_cust_contact.grid(row=0,column=0)

        cust_cont = StringVar()
        enty_contact=Entry(lableframeleft,width=29,font=("consolas",13,"bold"),border=0,fg="black",bg="white",textvariable=cust_cont)
        enty_contact.config(font=1)
        enty_contact.place(x=150,y=10)
        frame1=Frame(lableframeleft,width=268,height=2,bg="violet").place(x=150,y=32)

        lab_cust_reg =Label(lableframeleft,text="Customer email",font=("consolas",12,"bold"),bg="white",padx=2,pady=6)
        lab_cust_reg.grid(row=1,column=0)

        cust_reg = StringVar()
        enty_reg=Entry(lableframeleft,width=29,font=("consolas",13,"bold"),border=0,fg="black",bg="white",textvariable=cust_reg)
        enty_reg.config(font=1)
        enty_reg.place(x=150,y=40)
        frame9=Frame(lableframeleft,width=268,height=2,bg="violet").place(x=150,y=62)



        
        
        

        lab_Checkindetails =Label(lableframeleft,text="Check_in Date",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_Checkindetails.grid(row=2,column=0)

        # btnAdd=Button(lableframeleft,text="Date",font=("arial",12,"bold"),command=self.datefield,bg="black",fg="gold",width=9)
        # btnAdd.grid(row=2,column=1)
        checidt = StringVar()
        # enty_Checkindetails=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"),textvariable=checidt)
        # enty_Checkindetails.grid(row=2,column=1)
        enty_Checkindetails = DateEntry(lableframeleft,width=40,mindate=today,date_pattern='dd/mm/Y',padx=2,pady=6,textvariable=checidt)
        enty_Checkindetails.grid(row=2,column=1)
 
        lab_checkoutdetails=Label(lableframeleft,text="check_out date",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_checkoutdetails.grid(row=3,column=0)

        checodt = StringVar()
        # enty_checkoutdetails=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"),textvariable=checodt)
        # enty_checkoutdetails.grid(row=3,column=1)
        enty_checkoutdetails = DateEntry(lableframeleft,width=40,mindate=today,date_pattern='dd/mm/Y',padx=2,pady=6,textvariable=checodt)
        enty_checkoutdetails.grid(row=3,column=1)

        lab_Room_Type=Label(lableframeleft,text="Room_Type",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_Room_Type.grid(row=4,column=0)


        # enty_Room_Type=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        # enty_Room_Type.grid(row=4,column=1)
        sel_room = StringVar()
        self.security_c=ttk.Combobox(lableframeleft,values=my_list,font=("consolas",10,"bold"),textvariable=sel_room,width=35)
        # self.security_q["values"]=("select","Single Room","Double Room","Deluxe Room","Double-Double (Twin Double) Room","Twin Room","Duplex Room","Studio")
        self.security_c.grid(row=4,column=1)
        self.security_c.current(0)
        self.security_c.bind("<<ComboboxSelected>>",pickroomno)


        lab_AvalibleRoom=Label(lableframeleft,text="Room number",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_AvalibleRoom.grid(row=5,column=0)


        # enty_AvalibleRoom=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        # enty_AvalibleRoom.grid(row=5,column=1)
        sel_roomno = StringVar()
        # sel_roomno=book.return1
        # self.security_q=Entry(lableframeleft,width=29,Text=sel_roomno,font=("consolas",9,"bold"),border=0,fg="black",bg="white",textvariable=sel_roomno)
        
        self.security_r=ttk.Combobox(lableframeleft,values=[" "],font=("consolas",10,"bold"),text=sel_roomno,width=35,textvariable=sel_roomno)
        # self.security_r["values"]=("select","101","102","103","104","105","106","201","202","203","204","205","206","301","302","303","304","305","306")
        self.security_r.current(0)
        self.security_r.grid(row=5,column=1)


        lab_NoofDays=Label(lableframeleft,text="No of Days",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_NoofDays.grid(row=6,column=0)

        nofday = StringVar()
        enty_NoofDays=Entry(lableframeleft,width=29,font=("consolas",13,"bold"),border=0,fg="black",bg="white",textvariable=nofday)
        enty_NoofDays.config(font=1)
        enty_NoofDays.place(x=150,y=210)
        frame2=Frame(lableframeleft,width=268,height=2,bg="violet").place(x=150,y=232)
     

        lab_NoofDays=Label(lableframeleft,text="No of elders",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_NoofDays.grid(row=7,column=0)

        nofeld = StringVar()
        enty_NoofDays=Entry(lableframeleft,width=29,font=("consolas",13,"bold"),border=0,fg="black",bg="white",textvariable=nofeld)
        enty_NoofDays.config(font=1)
        enty_NoofDays.place(x=150,y=240)
        frame3=Frame(lableframeleft,width=268,height=2,bg="violet").place(x=150,y=265)

        lab_NoofDays=Label(lableframeleft,text="No of childrens",bg="white",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_NoofDays.grid(row=8,column=0)

        nofchld = StringVar()
        enty_NoofDays=Entry(lableframeleft,width=29,font=("consolas",13,"bold"),border=0,fg="black",bg="white",textvariable=nofchld)
        enty_NoofDays.config(font=1)
        enty_NoofDays.place(x=150,y=280)
        frame4=Frame(lableframeleft,width=268,height=2,bg="violet").place(x=150,y=302)

        


        # # lab_TotalCost=Label(lableframeleft,text="No of rooms",font=("arial",12,"bold"),padx=2,pady=6)
        # # lab_TotalCost.grid(row=9,column=0)

        # # nofrm = StringVar()
        # # enty_TotalCost=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"),textvariable=nofrm)
        # enty_TotalCost.grid(row=9,column=1)
        


      

       
          
        # btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        # btn_frame.place(x=140,y=330,width=100,height=35)


        btnAdd=Button(lableframeleft,text="Book",font=("consolas",12,"bold"),bg="blue",fg="gold",bd=5,width=9,command=self.admin_details)
        btnAdd.place(x=180,y=340,width=100,height=35)



  def admin_details(self):
            
            
           
            if nofchld=='' or nofday=='' or nofeld=='' or sel_room=='' or sel_roomno=='':
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
                        
                        query=("select * from cust_booking where av_room=%s && status='booking confirm'")
                        
                        value =(sel_roomno.get(),)
                        my_cursor.execute(query,value)
                        row = my_cursor.fetchone()
                        if row!=None:
                            messagebox.showwarning("warning","Room Not avialable please choose another room",parent=self.root)
                        
                        else:
                            my_cursor1=conn.cursor()
                            query1="select * from cust_reg where email=%s"
                            value1=(cust_reg.get(),)                                               
                            my_cursor1.execute(query1,value1)
                            rs=my_cursor1.fetchone()
                            
                            if rs==None:
                                messagebox.showwarning("warning","You email id is not regestred please check your email id",parent=self.root)
                            else:
                                conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into cust_booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        '',
                                                                        cust_cont.get(),
                                                                        cust_reg.get(),
                                                                        checidt.get(),
                                                                        checodt.get(),
                                                                        sel_room.get(),
                                                                        sel_roomno.get(),
                                                                        nofday.get(),
                                                                        nofeld.get(),
                                                                        nofchld.get(),
                                                                        'booking pending'

                                                                        
                                                                

                    ))

                                conn.commit()
                                conn.close()
                                messagebox.showinfo('confirmation', 'Room booked for booking confirmation check booking status',parent=self.root)
                 

                 
                        
       
                   

                    except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

 
    
  # def datefield(self):
  #     self.new_window=Toplevel(self.root)
  #     self.app=example2(self.new_window)
from PIL import Image, ImageTk
class book:
    def _init_(self,root):
        global lblimg
        global rm_no
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x425+232+205")

        frame1=Frame(self.root,bd=10,bg="white")
        frame1.place(x=5,y=5,width=800,height=350)

        scroll_x=ttk.Scrollbar(frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame1,orient=VERTICAL)

        frame2=Frame(frame1,bd=10,bg="white")
        frame2.place(x=10,y=10,width=750,height=330)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        # scroll_x.config(command=self.root.xview)
        # scroll_y.config(command=self.root.yview)
        img1=Image.open("images\hotel1.png")
        img1=img1.resize((200,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        rm_no=StringVar()
        lblimg=Label(frame2,text="Room No-:",bg="white")
        lblimg.place(x=0,y=0,width=60,height=10)
        lblimg=Label(frame2,text="101",bg="white",textvariable=rm_no)
        lblimg.place(x=80,y=0,width=60,height=10)

        lblimg=Label(frame2,image=self.photoimg1)
        lblimg.place(x=0,y=20,width=200,height=140)
        btnAdd=Button(frame2,text="Book",font=("consolas",12,"bold"),command=self.bok1_details,bg="blue",fg="gold")
        btnAdd.place(x=40,y=180,width=70,height=35)
    def return1(self):
        self.rm=rm_no.get()
        return self.rm
        
        

    def bok1_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
     


if __name__ == "__main__":
    root = Tk()
    obj= Roombooking(root)
    root.mainloop()

# from tkinter import *
# from tkinter.font import BOLD
# from PIL import Image, ImageTk
# from Room_details import rm_details
# from Booking_detail import bok_details
# from addstaff import sta_details
# from dinin import dinin_details

# class HotelManagementSystem:
#     def _init_(self,root):
#         self.root=root
#         self.root.title("Hotel Management System")
#         self.root.geometry("1500x800+0+0")