from logging import root, setLoggerClass
from  tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import tkinter as tk
from tkcalendar import DateEntry


conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class staff_view:
    def __init__(self,root):
        self.root=root
        self.root.title("view staff details")
        self.root.geometry("1295x570+225+205")  
        global se

        details_table=Frame(self.root,bd=5,relief=RIDGE,bg="red")
        details_table.place(x=10,y=50,width=1000,height=300) 

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.staff_details_table=ttk.Treeview(details_table,column=("staff_id","fname","idno","mobileno","address","age","gender","position","username","password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_details_table.xview)
        scroll_y.config(command=self.staff_details_table.yview)

        self.staff_details_table.heading("staff_id",text="staff_id")
        self.staff_details_table.heading("fname",text="first name")
        self.staff_details_table.heading("idno",text="idno")
        self.staff_details_table.heading("mobileno",text="mobileno")
        self.staff_details_table.heading("address",text="address")
        self.staff_details_table.heading("age",text="Dob")
        self.staff_details_table.heading("gender",text="gender")
        self.staff_details_table.heading("position",text="postion")
        self.staff_details_table.heading("username",text="username")
        self.staff_details_table.heading("password",text="password")

        self.staff_details_table["show"]="headings"
        self.staff_details_table.column("staff_id",width=60)
        self.staff_details_table.column("fname",width=60)
        self.staff_details_table.column("idno",width=60)
        self.staff_details_table.column("mobileno",width=60)
        self.staff_details_table.column("address",width=60)
        self.staff_details_table.column("age",width=60)
        self.staff_details_table.column("gender",width=60)
        self.staff_details_table.column("position",width=60)
        self.staff_details_table.column("username",width=60)
        self.staff_details_table.column("password",width=60)
        
        self.staff_details_table.pack(fill=BOTH,expand=1)
        self.staff_details_table.bind("<ButtonRelease-1>",self.cursor)
        self.fetch_data()

        regbutton=Button(self.root,text="search",font=("times new roman",15,"bold"),command=self.show,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=10,y=370,width=120,height=35)

        se=StringVar()
        self.flno=ttk.Entry(self.root,font=("times new roman",10,"bold"),textvariable=se)
        self.flno.place(x=140,y=380,width=200)
        regbutton=Button(self.root,text="Delete",font=("times new roman",15,"bold"),command=self.mDelete,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=480,y=370,width=120,height=35)
        # upbutton=Button(self.root,text="Update",font=("times new roman",15,"bold"),command=self.cursor,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        # upbutton.place(x=650,y=370,width=120,height=35)

    def fetch_data(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
             my_cursor=conn.cursor()
             my_cursor.execute("select*from staff_details")
             rows=my_cursor.fetchall()
             if len(rows)!=0:
                 self.staff_details_table.delete(*self.staff_details_table.get_children())
                 for i in rows:
                     self.staff_details_table.insert("",END,values=i)
                 conn.commit
             conn.close()
        
    def mDelete(self):
       
        selected_item = self.staff_details_table.selection()[0]
        # print(self.cust_details_table.item(selected_item)['values'])
        sid = self.staff_details_table.item(selected_item)['values'][0]
        
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            query = "DELETE FROM staff_details WHERE staff_id =%s"
            value = (sid,)
            rs = my_cursor.execute(query,value)
           
            
            conn.commit()
            self.staff_details_table.delete(selected_item)
            conn.close()
            messagebox.showinfo("success","Data deleted successfully",parent=self.root)

            
        except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}")

    def show(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select * from staff_details where position LIKE '%{se.get()}%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.staff_details_table.delete(*self.staff_details_table.get_children())
                for i in rows:
                    self.staff_details_table.insert("",END,values=i)
        conn.commit
        conn.close()
    def cursor(self):
        cursor_row=self.staff_details_table.focus()
        content = self.staff_details_table.item(cursor_row,"values")
        print(content)
        cursor = tk.Toplevel(root)
        register_lbl=Label(cursor,text="UPDATE HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=600,y=40)
        frame=Frame(cursor,bg="white",bd=5,relief=RIDGE)
        frame.place(x=380,y=85,width=690,height=430)
        floorno=Label(frame,text="Full name",font=("times new roman",10,"bold"),fg="black",bg="white")
        floorno.place(x=40,y=40)

        fname = StringVar()
        flno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fname)
        flno.place(x=40,y=70,width=230)

        idno=Label(frame,text="Idno",font=("times new roman",10,"bold"),fg="black",bg="white")
        idno.place(x=40,y=100)

        id_no = StringVar()
        ino=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=id_no)
        ino.place(x=40,y=130,width=230)

        mobno=Label(frame,text="Mobile No",font=("times new roman",10,"bold"),fg="black",bg="white")
        mobno.place(x=40,y=160)

        mbno = StringVar()
        mno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=mbno)
        mno.place(x=40,y=190,width=230)

        addr=Label(frame,text="Address",font=("times new roman",10,"bold"),fg="black",bg="white")
        addr.place(x=40,y=220)

        add = StringVar()
        ad=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
        ad.place(x=40,y=250,width=230)

        age=Label(frame,text="Age",font=("times new roman",10,"bold"),fg="black",bg="white")
        age.place(x=350,y=40)

        ag = StringVar()
        enty_Checkindetails = DateEntry(frame,date_pattern='dd/mm/Y',padx=2,pady=6,textvariable=ag)
        enty_Checkindetails.place(x=350,y=70,width=230)

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
        radiobutton_1_p = ttk.Radiobutton(frame, text='Recieptionist', variable=pos, value="Recieptionist")
        radiobutton_1_p.pack()
        radiobutton_1_p.place(x=370,y=250)
        radiobutton_2_p = ttk.Radiobutton(frame, text='Room service', variable=pos, value="Room service")
        radiobutton_2_p.pack()
        radiobutton_2_p.place(x=470,y=250)
        radiobutton_3_p = ttk.Radiobutton(frame, text='Kitchen staff', variable=pos, value="Kitchen staff")
        radiobutton_3_p.pack()
        radiobutton_3_p.place(x=590,y=250)

        age=Label(frame,text="username",font=("times new roman",10,"bold"),fg="black",bg="white")
        age.place(x=40,y=275)

        uname = StringVar()
        ag=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=uname)
        ag.place(x=40,y=300,width=230)

        age=Label(frame,text="password",font=("times new roman",10,"bold"),fg="black",bg="white")
        age.place(x=350,y=270)

        pas = StringVar()
        ag_pas=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=pas)
        ag_pas.place(x=350,y=300,width=230)

        flno.insert(0,content[1]),
        ino.insert(0,content[2]),
        mno.insert(0,content[3]),
        ad.insert(0,content[4]),
        enty_Checkindetails.insert(0,content[5]),
        
        # radiobutton_1._getitem_(0,content[6]),
        # radiobutton_2._getitem_(0,content[6]),        
        # radiobutton_3._getitem_(0,content[6]),
        # radiobutton_1._getitem_(0,content[7]),
        # radiobutton_2._getitem_(0,content[7]),
        # radiobutton_3._getitem_(0,content[7]),
        ag.insert(0,content[8]),
        ag_pas.insert(0,content[9])

        def update():
            nonlocal content,enty_Checkindetails,ag,flno,ino,ad,ag,ag_pas,radiobutton_1,radiobutton_2,radiobutton_3,radiobutton_1_p,radiobutton_2_p,radiobutton_3_p
            fname.get()
            id_no.get()
            mbno.get()
            add.get()
            ag.get()
            gen.get()
            pos.get()
            uname.get()
            pas.get()
            self.staff_details_table.item(cursor_row,values=(content[0],fname,id_no,mbno,add,ag,gen,pos,uname,pas))
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE staff_details SET fl_name=%s, idno=%s, mob_no=%s, address=%s, age=%s, gender=%s, position=%s, username=%s, password=%s WHERE staff_id=%s",
                                                                                        (fname,id_no,mbno,add,ag,gen,pos,uname,pas,content[0])
            
            )
            
            conn.commit()
            conn.close()
            messagebox.showinfo("sucess","Data updated successfully")
            
            
           
            # radiobutton_1.delete(0,END)
            # radiobutton_2.delete(0,END)
            # radiobutton_3.delete(0,END)
            flno.delete(0,END)
           
            ino.delete(0,END)
            mno.delete(0,END)
            ad.delete(0,END)
            enty_Checkindetails.delete(0,END)
            ag.delete(0,END)
            ag_pas.delete(0,END)
           
            frame.destroy()
            cursor.destroy()
            self.new_window=Toplevel(self.root)
            self.app=staff_view(self.new_window)

        regbutton=Button(frame,text="Update data",font=("times new roman",15,"bold"),command=update,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        regbutton.place(x=250,y=350,width=120,height=35)

if __name__ == "__main__":
    root = Tk()
    app=staff_view(root)
    root.mainloop()