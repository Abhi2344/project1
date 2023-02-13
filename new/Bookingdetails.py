from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk


class Roombooking:
  def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+230+220")


       
        lbl_title=Label(self.root,text="BOOKING DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        img2=Image.open(r"E:\hotel_images\hotel_images\logohotel.png")
        img2=img2.resize((110,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

      
        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",font=("time new roman",12,"bold"),padx=2)
        lableframeleft.place(x=5,y=50,width=425,height=490)

 

        
        lab_cust_contact =Label(lableframeleft,text="Customer contact",font=("arial",12,"bold"),padx=2,pady=6)
        lab_cust_contact.grid(row=0,column=0)


        enty_contact=ttk.Entry(lableframeleft,width=20,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)
        
        btnFetchData=Button(lableframeleft,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

          
        lab_Checkindetails =Label(lableframeleft,text="Check_in Details",font=("arial",12,"bold"),padx=2,pady=6)
        lab_Checkindetails.grid(row=2,column=0)


        enty_Checkindetails=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_Checkindetails.grid(row=2,column=1)

 
        lab_checkoutdetails=Label(lableframeleft,text="check_outd etails",font=("arial",12,"bold"),padx=2,pady=6)
        lab_checkoutdetails.grid(row=3,column=0)


        enty_checkoutdetails=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_checkoutdetails.grid(row=3,column=1)


        
        lab_Room_Type=Label(lableframeleft,text="Room_Type",font=("arial",12,"bold"),padx=2,pady=6)
        lab_Room_Type.grid(row=4,column=0)


        enty_Room_Type=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_Room_Type.grid(row=4,column=1)


        lab_AvalibleRoom=Label(lableframeleft,text="Avalible Room",font=("arial",12,"bold"),padx=2,pady=6)
        lab_AvalibleRoom.grid(row=5,column=0)


        enty_AvalibleRoom=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_AvalibleRoom.grid(row=5,column=1)

         
        lab_NoofDays=Label(lableframeleft,text="No of Days",font=("arial",12,"bold"),padx=2,pady=6)
        lab_NoofDays.grid(row=6,column=0)


        enty_NoofDays=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_NoofDays.grid(row=6,column=1)
     

        lab_Paidtax=Label(lableframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lab_Paidtax.grid(row=7,column=0)


        enty_Paidtax=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_Paidtax.grid(row=7,column=1)

        
        
        lab_SubTotal=Label(lableframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lab_SubTotal.grid(row=8,column=0)


        enty_SubTotal=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_SubTotal.grid(row=8,column=1)


        lab_TotalCost=Label(lableframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lab_TotalCost.grid(row=9,column=0)


        enty_TotalCost=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_TotalCost.grid(row=9,column=1)


        btnBill=Button(lableframeleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

       
          
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)


        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


        
        img3=Image.open(r"E:\hotel_images\hotel_images\bed.jpg")
        img3=img3.resize((530,350),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        
        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=530,height=280)


         
           
        

if __name__ == "__main__":
    root = Tk()
    obj= Roombooking(root)
    root.mainloop()