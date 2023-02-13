# from _typeshed import Self
#from _typeshed import Self
from logging import root, setLoggerClass
from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import tkinter as tk
from custreg import cust_regs
# import pdfkit
import os
import tempfile

# def main():
#     win = Tk()
#     app = cust_view(win)
   
#     win.mainloop()

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class cust_view:
    
    def __init__(self,root):
        global cust_details_table
        
        # self.cust_details_table.bind("<Control-b>",pdf)
        # def pdf(txt):
        #         temp_file=tempfile.mktemp('.pdf')
        #         open(temp_file,'w').write(str(txt))
        #         os.startfile(temp_file,'print')  
        
        self.root=root
        self.root.title("Customer details")
        self.root.geometry("1295x570+225+205")  

        global selected_items
        global se
        
        details_table=Frame(self.root,bd=5,relief=RIDGE,bg="red")
        details_table.place(x=10,y=50,width=1000,height=300) 
        


        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("cust_id","fname","lname","email","contact_no","security_q","security_ans","password","confirm password","gender","address","nationality","idpf"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        selected_items = self.cust_details_table.selection()
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("cust_id",text="customer id")
        self.cust_details_table.heading("fname",text="first name")
        self.cust_details_table.heading("lname",text="last name")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("contact_no",text="mobile no")
        self.cust_details_table.heading("security_q",text="security question")
        self.cust_details_table.heading("security_ans",text="security answer")
        self.cust_details_table.heading("password",text="password")
        self.cust_details_table.heading("confirm password",text="confirm password")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("address",text="address")
        self.cust_details_table.heading("nationality",text="nationality")
        self.cust_details_table.heading("idpf",text="idpf")
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("cust_id",width=60)
        self.cust_details_table.column("fname",width=60)
        self.cust_details_table.column("email",width=60)
        self.cust_details_table.column("contact_no",width=60)
        self.cust_details_table.column("security_q",width=60)
        self.cust_details_table.column("security_ans",width=60)
        self.cust_details_table.column("password",width=60)
        self.cust_details_table.column("confirm password",width=60)
        self.cust_details_table.column("gender",width=60)
        self.cust_details_table.column("address",width=60)
        self.cust_details_table.column("nationality",width=60)
        self.cust_details_table.column("idpf",width=60)
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.cursor)
        self.fetch_data()
        regbutton=Button(self.root,text="search",font=("times new roman",15,"bold"),command=self.showct,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
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
             my_cursor.execute("select*from cust_reg")
             rows=my_cursor.fetchall()

             if len(rows)!=0:
                 self.cust_details_table.delete(*self.cust_details_table.get_children())
                 for i in rows:
                    self.cust_details_table.insert("",END,values=i)
                    # def pdf():
                

                    #     x="my.pdf"
                    #     content = rows.get("0.0", tk.END)
                    #     pdfkit.from_string(content, x)
                    #     print("pdf created")
                    #     os.startfile("my.pdf")


                    


                 conn.commit
             conn.close()
       
       
       
                # regbutton=Button(self.root,text="print",font=("times new roman",15,"bold"),command=pdf(rows.get('1.0',END)),bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        # regbutton=Button(self.root,text="print",font=("times new roman",15,"bold"),command=pdf(),bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        # regbutton.place(x=620,y=370,width=120,height=35)       # regbutton.place(x=620,y=370,width=120,height=35)
        
    def mDelete(self):
       
        selected_item = self.cust_details_table.selection()[0]
        # print(self.cust_details_table.item(selected_item)['values'])
        cid = self.cust_details_table.item(selected_item)['values'][0]
        
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            query = "DELETE FROM cust_reg WHERE cust_id =%s"
            value = (cid,)
            rs = my_cursor.execute(query,value)
           
            
            conn.commit()
            self.cust_details_table.delete(selected_item)
            conn.close()
            messagebox.showinfo("success","Data deleted successfully",parent=self.root)

            
        except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
    def showct(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select * from cust_reg where email LIKE '%{se.get()}%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
                    
        conn.commit
        conn.close()


    def cursor(self):
        cursor_row=self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row,"values")
        print(content)
        cursor = tk.Toplevel(root)
        register_lbl=Label(cursor,text="UPDATE HERE",font=("times new roman",20,"bold"),fg="green")
        register_lbl.place(x=600,y=40)
        frame=Frame(cursor,bg="white",bd=10,relief=RAISED)
        frame.place(x=380,y=85,width=650,height=430)


       

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
        combo_Nationality["value"]=("select","Indian","American","russian","german","Other")
        combo_Nationality.current(0)
        combo_Nationality.place(x=370,y=280,width=230)
        
        labIdProof=Label(frame,text="Id Proof Type",font=("arial",10,"bold"),padx=2,pady=2)
        labIdProof.place(x=50,y=305)

        idpr=StringVar()
        combo_Id=ttk.Combobox(frame,text="Id proof Type",font=("arial",10,"bold"),textvariable=idpr)
        combo_Id["value"]=("select","AadharCard","DrivingLicence","Passport")
        combo_Id.current(0)
        combo_Id.place(x=50,y=330,width=230)

        address = Label(frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        address.place(x=50,y=255)

        add=StringVar()
        address_en=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
        address_en.place(x=50,y=280,width=230)

             

        fname_entry.insert(0,content[1]),
        lname_entry.insert(0,content[2]),
        self.txt_email.insert(0,content[3]),
        contactno.insert(0,content[4]),
        combo_security_q.insert(0,content[5]),
        security_q_answer.insert(0,content[6]),
        password.insert(0,content[7]),
        confi_password.insert(0,content[8]),
        # gen.get(0,content[9]),
        # radiobutton_1.insert("male",content[9]),
        # radiobutton_2.insert("female",content[9])
        # radiobutton_3.insert("others",content[9])
        combo_Nationality.insert(0,content[10]),
        combo_Id.insert(0,content[11]),
        address_en.insert(0,content[12])

        def upddate():
            nonlocal content,cursor_row,address_en,combo_Id,combo_Nationality,radiobutton_1,radiobutton_2,radiobutton_3,fname_entry,lname_entry,contactno,security_q_answer,combo_security_q,password,confi_password
            fn = fname.get()
            ln= lname.get()
            ea =email.get()
            ct= cont.get()
            ps= passw.get()
            cps= cpassw.get()
            sq= secuq.get()
            sa= secua.get()
            
            self.txt_email
        # global gender
            

            ge=gen.get()
            id= idpr.get()
            nt= nation.get()
            ad= add.get()
            self.cust_details_table.item(cursor_row,values=(content[0],fn,ln,ea,ct,sq,sa,ps,cps,ge,nt,id,ad))
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE cust_reg SET fname=%s, lname=%s, email=%s, mobile_no=%s, security_question=%s, security_answer=%s, password=%s, confirm_password=%s, gender=%s, nationality=%s, idpf=%s, Address=%s WHERE cust_id=%s",
                                                                                            (fn,ln,ea,ct,sq,sa,ps,cps,ge,nt,id,ad,content[0])
            
            )
           
            conn.commit()
            conn.close()
            messagebox.showinfo("sucess","Data updated successfully")
            
            
           
            # radiobutton_1.delete(0,END)
            # radiobutton_2.delete(0,END)
            # radiobutton_3.delete(0,END)
            fname_entry.delete(0,END)
            lname_entry.delete(0,END)
            self.txt_email.delete(0,END)
            contactno.delete(0,END)
            security_q_answer.delete(0,END)
            combo_security_q.delete(0,END)
            password.delete(0,END)
            confi_password.delete(0,END)
            combo_Nationality.delete(0,END)
            combo_Id.delete(0,END)
            address_en.delete(0,END)
            frame.destroy()
            cursor.destroy()
            self.new_window=Toplevel(self.root)
            self.app=cust_view(self.new_window)


        regbutton=Button(frame,text="Update Data",font=("consolas",15,"bold"),command=upddate,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=250,y=375,width=120,height=35)  
            
        

        # def pdf(event):
                

        #         x="my.pdf"
        #         content = self.cust_details_table.get("0.0", tk.END)
        #         pdfkit.from_string(content, x)
        #         print("pdf created")
        #         os.startfile("my.pdf")

        # cust_regs.admin_details.set(row[1]),
        # lname.set(row[2]),
        # email.set(row[3]),
        # cont.set(row[4]),
        # secuq.set(row[5]),
        # secua.set(row[6]),
        # passw.set(row[7]),
        # cpassw.set(row[8]),
        # gen.set(row[9]),
        # nation.set(row[10]),
        # idpr.set(row[11]),
        # add.set(row[12]),
    
        

    # def update(self):
        
        # newWindow = tk.Toplevel(self.root)
        # # update = Toplevel(main)
        # newWindow.title("Login")
        # newWindow.geometry("1500x800+0+0") 
        # # global fname
        # # global lname
        # # global email
        # # global cont
        # # global passw
        # # global cpassw
        # # global secuq
        # # global secua
        # # global add
        # # # global gender
        # # global em

        # # global gen
        # # global idpr
        # # global nation
       
        # # self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
        # # lbl_bg=Label(self.root,image=self.bg)
        # # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # register_lbl=Label(newWindow,text="Update HERE",font=("times new roman",20,"bold"),fg="green")
        # register_lbl.place(x=600,y=40)

        # self.bg1=ImageTk.PhotoImage(file=r"images\bed.jpg")
        # lbl_bg1=Label(newWindow,image=self.bg1)
        # lbl_bg1.place(x=50,y=-300,width=450,height=1200)


        # frame=Frame(newWindow,bg="white")
        # frame.place(x=500,y=85,width=650,height=430)


       

        # fname = Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        # fname.place(x=50,y=5)

        # fname = StringVar()
        # fname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fname)
        # fname_entry.place(x=50,y=30,width=230)

        # lname = Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
        # lname.place(x=50,y=55)

        # lname = StringVar()
        # lname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=lname)
        # lname_entry.place(x=50,y=80,width=230)

        # email = Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        # email.place(x=50,y=105)

        # email=StringVar()
        # self.txt_email=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=email)
        # self.txt_email.place(x=50,y=130,width=230)

        # contactno = Label(frame,text="MobileNo",font=("times new roman",10,"bold"),bg="white")
        # contactno.place(x=50,y=155)

        # cont = StringVar()
        # contactno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cont)
        # contactno.place(x=50,y=180,width=230)

        # security_q = Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
        # security_q.place(x=50,y=205)

        # secuq=StringVar()
        # combo_security_q=ttk.Combobox(frame,font=("times new roman",10,"bold"),textvariable=secuq,state="readonly")
        # combo_security_q["values"]=("select","your birth place","your favourite game","Your pet name")
        # combo_security_q.place(x=50,y=230,width=230)
        # combo_security_q.current(0)

        # security_q_answer = Label(frame,text="Security answer",font=("times new roman",10,"bold"),bg="white")
        # security_q_answer.place(x=370,y=205)

        # secua=StringVar()
        # security_q_answer=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=secua)
        # security_q_answer.place(x=370,y=230,width=230)


        # password = Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
        # password.place(x=370,y=5)

        # passw =StringVar()
        # password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=passw)
        # password.place(x=370,y=30,width=230)

        # confi_password = Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
        # confi_password.place(x=370,y=55)

        # cpassw = StringVar()
        # confi_password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cpassw)
        # confi_password.place(x=370,y=80,width=230)

        # gen = StringVar()
        # gender = Label(frame ,text="Gender",font=("times new roman",10,"bold"))
        # gender.place(x=370,y=105)
        # # gender = Label(frame,text="Gender",font=("times new roman",10,"bold"),textvariable=gen,bg="white")
        # # gender.place(x=370,y=105)
        # radiobutton_1 = ttk.Radiobutton(frame, text='Male', variable=gen, value="male")
        # radiobutton_1.pack()
        # radiobutton_1.place(x=370,y=130)
        # radiobutton_2 = ttk.Radiobutton(frame, text='Female', variable=gen, value="female")
        # radiobutton_2.pack()
        # radiobutton_2.place(x=370,y=155)
        # radiobutton_3 = ttk.Radiobutton(frame, text='Other', variable=gen, value="other")
        # radiobutton_3.pack()
        # radiobutton_3.place(x=370,y=180)

        # labNationality=Label(frame,text="Nationality",font=("arial",10,"bold"),padx=2,pady=2)
        # labNationality.place(x=370,y=255)

        # nation=StringVar()
        # combo_Nationality=ttk.Combobox(frame,text="Nationality",font=("arial",10,"bold"),textvariable=nation)
        # combo_Nationality["value"]=("Indian","American","russian","german","Other")
        # combo_Nationality.current(0)
        # combo_Nationality.place(x=370,y=280,width=230)
        
        # labIdProof=Label(frame,text="Id Proof Type",font=("arial",10,"bold"),padx=2,pady=2)
        # labIdProof.place(x=50,y=305)

        # idpr=StringVar()
        # combo_Id=ttk.Combobox(frame,text="Id proof Type",font=("arial",10,"bold"),textvariable=idpr)
        # combo_Id["value"]=("AadharCard","DrivingLicence","Passport")
        # combo_Id.current(0)
        # combo_Id.place(x=50,y=330,width=230)

        # address = Label(frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        # address.place(x=50,y=255)

        # add=StringVar()
        # address=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
        # address.place(x=50,y=280,width=230)

        # regbutton=Button(frame,text="Update Data",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        # regbutton.place(x=250,y=375,width=120,height=35)       

        # global fname
        # global lname
        # global email
        # global cont
        # global passw
        # global cpassw
        # global secuq
        # global secua
        # global add
        # # global gender
        # global em

        # global gen
        # global idpr
        # global nation
       
        # # self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
        # # lbl_bg=Label(self.root,image=self.bg)
        # # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # register_lbl=Label(update,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
        # register_lbl.place(x=600,y=40)

        # self.bg1=ImageTk.PhotoImage(file=r"images\bed.jpg")
        # lbl_bg1=Label(self.root,image=self.bg1)
        # lbl_bg1.place(x=50,y=-300,width=450,height=1200)


        # frame=Frame(self.root,bg="white")
        # frame.place(x=500,y=85,width=650,height=430)


       

        # fname = Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        # fname.place(x=50,y=5)

        # fname = StringVar()
        # fname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fname)
        # fname_entry.place(x=50,y=30,width=230)

        # lname = Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
        # lname.place(x=50,y=55)

        # lname = StringVar()
        # lname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=lname)
        # lname_entry.place(x=50,y=80,width=230)

        # email = Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        # email.place(x=50,y=105)

        # email=StringVar()
        # self.txt_email=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=email)
        # self.txt_email.place(x=50,y=130,width=230)

        # contactno = Label(frame,text="MobileNo",font=("times new roman",10,"bold"),bg="white")
        # contactno.place(x=50,y=155)

        # cont = StringVar()
        # contactno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cont)
        # contactno.place(x=50,y=180,width=230)

        # security_q = Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
        # security_q.place(x=50,y=205)

        # secuq=StringVar()
        # combo_security_q=ttk.Combobox(frame,font=("times new roman",10,"bold"),textvariable=secuq,state="readonly")
        # combo_security_q["values"]=("select","your birth place","your favourite game","Your pet name")
        # combo_security_q.place(x=50,y=230,width=230)
        # combo_security_q.current(0)

        # security_q_answer = Label(frame,text="Security answer",font=("times new roman",10,"bold"),bg="white")
        # security_q_answer.place(x=370,y=205)

        # secua=StringVar()
        # security_q_answer=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=secua)
        # security_q_answer.place(x=370,y=230,width=230)


        # password = Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
        # password.place(x=370,y=5)

        # passw =StringVar()
        # password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=passw)
        # password.place(x=370,y=30,width=230)

        # confi_password = Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
        # confi_password.place(x=370,y=55)

        # cpassw = StringVar()
        # confi_password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cpassw)
        # confi_password.place(x=370,y=80,width=230)

        # gen = StringVar()
        # gender = Label(frame ,text="Gender",font=("times new roman",10,"bold"))
        # gender.place(x=370,y=105)
        # # gender = Label(frame,text="Gender",font=("times new roman",10,"bold"),textvariable=gen,bg="white")
        # # gender.place(x=370,y=105)
        # radiobutton_1 = ttk.Radiobutton(frame, text='Male', variable=gen, value="male")
        # radiobutton_1.pack()
        # radiobutton_1.place(x=370,y=130)
        # radiobutton_2 = ttk.Radiobutton(frame, text='Female', variable=gen, value="female")
        # radiobutton_2.pack()
        # radiobutton_2.place(x=370,y=155)
        # radiobutton_3 = ttk.Radiobutton(frame, text='Other', variable=gen, value="other")
        # radiobutton_3.pack()
        # radiobutton_3.place(x=370,y=180)

        # labNationality=Label(frame,text="Nationality",font=("arial",10,"bold"),padx=2,pady=2)
        # labNationality.place(x=370,y=255)

        # nation=StringVar()
        # combo_Nationality=ttk.Combobox(frame,text="Nationality",font=("arial",10,"bold"),textvariable=nation)
        # combo_Nationality["value"]=("Indian","American","russian","german","Other")
        # combo_Nationality.current(0)
        # combo_Nationality.place(x=370,y=280,width=230)
        
        # labIdProof=Label(frame,text="Id Proof Type",font=("arial",10,"bold"),padx=2,pady=2)
        # labIdProof.place(x=50,y=305)

        # idpr=StringVar()
        # combo_Id=ttk.Combobox(frame,text="Id proof Type",font=("arial",10,"bold"),textvariable=idpr)
        # combo_Id["value"]=("AadharCard","DrivingLicence","Passport")
        # combo_Id.current(0)
        # combo_Id.place(x=50,y=330,width=230)

        # address = Label(frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        # address.place(x=50,y=255)

        # add=StringVar()
        # address=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
        # address.place(x=50,y=280,width=230)

        # regbutton=Button(frame,text="Update",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        # regbutton.place(x=250,y=375,width=120,height=35)
    #     # mDelete = messagebox.askyesno("Delete","Do you want to delete this record")
    #     # if mDelete>0:
    #     #     conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
    #     #     my_cursor=conn.cursor()
    #     #     query = "delete from cust_reg email=%s"
    #     #     value = (self.em)



# class cust_regs:
#     def _init_(self,root):
#         self.root=root
#         self.root.title("Login")
#         self.root.geometry("1500x800+0+0")        

#         global fname
#         global lname
#         global email
#         global cont
#         global passw
#         global cpassw
#         global secuq
#         global secua
#         global add
#         # global gender

#         global gen
#         global idpr
#         global nation
       
#         # self.bg=ImageTk.PhotoImage(file=r"images\hotel1.png")
#         # lbl_bg=Label(self.root,image=self.bg)
#         # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#         register_lbl=Label(root,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green")
#         register_lbl.place(x=600,y=40)

#         self.bg1=ImageTk.PhotoImage(file=r"images\bed.jpg")
#         lbl_bg1=Label(self.root,image=self.bg1)
#         lbl_bg1.place(x=50,y=-300,width=450,height=1200)


#         frame=Frame(self.root,bg="white")
#         frame.place(x=500,y=85,width=650,height=430)


       

#         fname = Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
#         fname.place(x=50,y=5)

#         fname = StringVar()
#         fname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=fname)
#         fname_entry.place(x=50,y=30,width=230)

#         lname = Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
#         lname.place(x=50,y=55)

#         lname = StringVar()
#         lname_entry=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=lname)
#         lname_entry.place(x=50,y=80,width=230)

#         email = Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
#         email.place(x=50,y=105)

#         email=StringVar()
#         self.txt_email=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=email)
#         self.txt_email.place(x=50,y=130,width=230)

#         contactno = Label(frame,text="MobileNo",font=("times new roman",10,"bold"),bg="white")
#         contactno.place(x=50,y=155)

#         cont = StringVar()
#         contactno=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cont)
#         contactno.place(x=50,y=180,width=230)

#         security_q = Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
#         security_q.place(x=50,y=205)

#         secuq=StringVar()
#         combo_security_q=ttk.Combobox(frame,font=("times new roman",10,"bold"),textvariable=secuq,state="readonly")
#         combo_security_q["values"]=("select","your birth place","your favourite game","Your pet name")
#         combo_security_q.place(x=50,y=230,width=230)
#         combo_security_q.current(0)

#         security_q_answer = Label(frame,text="Security answer",font=("times new roman",10,"bold"),bg="white")
#         security_q_answer.place(x=370,y=205)

#         secua=StringVar()
#         security_q_answer=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=secua)
#         security_q_answer.place(x=370,y=230,width=230)


#         password = Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
#         password.place(x=370,y=5)

#         passw =StringVar()
#         password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=passw)
#         password.place(x=370,y=30,width=230)

#         confi_password = Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
#         confi_password.place(x=370,y=55)

#         cpassw = StringVar()
#         confi_password=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=cpassw)
#         confi_password.place(x=370,y=80,width=230)

#         gen = StringVar()
#         gender = Label(frame ,text="Gender",font=("times new roman",10,"bold"))
#         gender.place(x=370,y=105)
#         # gender = Label(frame,text="Gender",font=("times new roman",10,"bold"),textvariable=gen,bg="white")
#         # gender.place(x=370,y=105)
#         radiobutton_1 = ttk.Radiobutton(frame, text='Male', variable=gen, value="male")
#         radiobutton_1.pack()
#         radiobutton_1.place(x=370,y=130)
#         radiobutton_2 = ttk.Radiobutton(frame, text='Female', variable=gen, value="female")
#         radiobutton_2.pack()
#         radiobutton_2.place(x=370,y=155)
#         radiobutton_3 = ttk.Radiobutton(frame, text='Other', variable=gen, value="other")
#         radiobutton_3.pack()
#         radiobutton_3.place(x=370,y=180)

#         labNationality=Label(frame,text="Nationality",font=("arial",10,"bold"),padx=2,pady=2)
#         labNationality.place(x=370,y=255)

#         nation=StringVar()
#         combo_Nationality=ttk.Combobox(frame,text="Nationality",font=("arial",10,"bold"),textvariable=nation)
#         combo_Nationality["value"]=("Indian","American","russian","german","Other")
#         combo_Nationality.current(0)
#         combo_Nationality.place(x=370,y=280,width=230)
        
#         labIdProof=Label(frame,text="Id Proof Type",font=("arial",10,"bold"),padx=2,pady=2)
#         labIdProof.place(x=50,y=305)

#         idpr=StringVar()
#         combo_Id=ttk.Combobox(frame,text="Id proof Type",font=("arial",10,"bold"),textvariable=idpr)
#         combo_Id["value"]=("AadharCard","DrivingLicence","Passport")
#         combo_Id.current(0)
#         combo_Id.place(x=50,y=330,width=230)

#         address = Label(frame,text="Address",font=("times new roman",10,"bold"),bg="white")
#         address.place(x=50,y=255)

#         add=StringVar()
#         address=ttk.Entry(frame,font=("times new roman",10,"bold"),textvariable=add)
#         address.place(x=50,y=280,width=230)

#         regbutton=Button(frame,text="Register",font=("times new roman",15,"bold"),command=self.admin_details,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
#         regbutton.place(x=250,y=375,width=120,height=35)

       

#     def admin_details(self):
#             un =fname.get()
#             ln = lname.get()
#             em = email.get()
#             con = cont.get()
#             passwo = passw.get()
            
#             cpasswo = cpassw.get()
#             if un=='' or passw=='' or em==''or con=='' or passwo=='' or cpasswo=='':
#                     messagebox.showwarning("Warning","All Fields are compulsory")
#             else:
#                 if passwo!=cpasswo:
#                     messagebox.showwarning("Warning","password and confirm password should be equal")
#                 else:
                    

#                     try:
#                         #  if gen==1:
#                         #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"male",add.get(),nation.get(),idpr.get())
#                         #  elif gen==2:
#                         #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"female",add.get(),nation.get(),idpr.get())
#                         #  else:
#                         #     data = (un,ln,em,con,secuq.get(),secua.get(),passwo,cpasswo,"other",add.get(),nation.get(),idpr.get())

#                         conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
#                         my_cursor=conn.cursor()
#                         query=("select * from cust_reg where email=%s")
#                         value =(em,)
#                         my_cursor.execute(query,value)
#                         row = my_cursor.fetchone()
#                         if row!=None:
#                             messagebox.showwarning("warning","Email alredy registered use different email")
#                         else:
#                             my_cursor.execute("insert into cust_reg values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
#                                                                       '',
#                                                                       un,
#                                                                       ln,
#                                                                       em,
#                                                                       con,
#                                                                       secuq.get(),
#                                                                       secua.get(),
#                                                                       passwo,
#                                                                       cpasswo,
#                                                                       gen.get(),
#                                                                       add.get(),
#                                                                       nation.get(),
#                                                                       idpr.get()
                                                            

#                  ))

#                         conn.commit()
#                         conn.close()
#                         messagebox.showinfo('confirmation', 'Record Saved',parent=self.root)
                 

                 
                        
       
                   

#                     except Exception as e  :
#                         messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
       
#     def mDelete(self):
        
#         selected_item = self.cust_details_table.selection()[0]
        
#         try:
#             conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
#             my_cursor=conn.cursor()
#             query = "delete from cust_reg where email=%s"
#             value = (email.get(),)
            
#             rs = my_cursor.execute(query,value)
#             if(rs.rowcount==1):
#                self.cust_details_table.delete(selected_item)
#             conn.commit()
#             conn.close()

            
#         except Exception as e  :
#                         messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
#         # mDelete = messagebox.askyesno("Delete","Do you want to delete this record")
#         # if mDelete>0:
#         #     conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
#         #     my_cursor=conn.cursor()
#         #     query = "delete from cust_reg email=%s"
#         #     value = (self.em)

if __name__ == "__main__":
    root = Tk()
    obj= cust_view(root)
    root.mainloop()