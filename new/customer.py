from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk


class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",10,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        img2=Image.open(r"E:\hotel_images\hotel_images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)


        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("time new roman",12,"bold"),padx=2)
        lableframeleft.place(x=5,y=50,width=425,height=490)


        lab_cust_ref=Label(lableframeleft,text="Customer_Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lab_cust_ref.grid(row=0,column=0)


        enty_ref=Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        enty_ref.grid(row=0,column=1)

       
        cname=Label(lableframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0)


        txtcname=Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        

        labmname=Label(lableframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        labmname.grid(row=2,column=0)


        txtmname=Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)


        lab_gender=Label(lableframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lab_gender.grid(row=3,column=0)

        combo_gender=ttk.Combobox(lableframeleft,text="Gender",font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

 

         
         
        labPostCode=Label(lableframeleft,text="PostCode",font=("arial",12,"bold"),padx=2,pady=6)
        labPostCode.grid(row=4,column=0)


        txtPostCode=Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)


           
         
        labMobile=Label(lableframeleft,text="Mobile number",font=("arial",12,"bold"),padx=2,pady=6)
        labMobile.grid(row=5,column=0)


        txtMobile=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)


           
        labEmail=Label(lableframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        labEmail.grid(row=6,column=0)


        txtEmail=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)


     
        labNationality=Label(lableframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        labNationality.grid(row=7,column=0)

        combo_Nationality=ttk.Combobox(lableframeleft,text="Nationality",font=("arial",12,"bold"),width=27,)
        combo_Nationality["value"]=("Indian","American","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
        

      




      
        labIdProof=Label(lableframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        labIdProof.grid(row=8,column=0)

        combo_Id=ttk.Combobox(lableframeleft,text="Id proof Type",font=("arial",12,"bold"),width=27,)
        combo_Id["value"]=("AadharCard","DrivingLicence","Passport")
        combo_Id.current(0)
        combo_Id.grid(row=8,column=1)
        






        labIdNumber=Label(lableframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        labIdNumber.grid(row=9,column=0)


        txtIdNumber=Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)


    
        labAddress=Label(lableframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        labAddress.grid(row=10,column=0)


        txtAddress=Entry(lableframeleft,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)

    
        
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


        
       

       
        





if __name__ == "__main__":
    root = Tk()
    obj=cust_win(root)
    root.mainloop()