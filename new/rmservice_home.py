from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
# from Room_details import rm_details
# from Booking_detail import bok_details

# from dinin import dinin_details
# from customer_details import cust_view
from roomservice_view import rms_view
class rsHotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")

        img1=Image.open("E:\hotel_images\hotel_images\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)



        img2=Image.open("E:\hotel_images\hotel_images\logohotel.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=230,height=140)
        
        lbl_title = Label(self.root,text="Welcome ",font=("times new roman",25,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=140,width=1600,height=30)

        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=172,width=1550,height=620)

        lbl_menu = Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_menu.place(x=0,y=0,width=230)

        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=240)

        cust_btn=Button(btn_frame,text="  logout   ",width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)


        cust_btn4=Button(btn_frame,text="  Service requests    ",command=self.rm_details,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn4.grid(row=0,column=0)

       
        img3=Image.open("E:\hotel_images\hotel_images\hotel1.png")
        img3=img3.resize((1310,630),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=225,y=0,width=1310,height=630)


        img4=Image.open("E:\hotel_images\hotel_images\hotel3.jpg")
        img4=img4.resize((230,280),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=113,width=230,height=280)

        img5=Image.open("E:\hotel_images\hotel_images\hotel4.jpg")
        img5=img5.resize((230,260),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=370,width=230,height=260)

    def rm_details(self):
       self.new_window=Toplevel(self.root)
       self.app=rms_view(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj= rsHotelManagementSystem(root)
    root.mainloop()