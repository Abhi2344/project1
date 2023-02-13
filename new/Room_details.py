from os import path

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from PIL import Image,ImageTk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import mysql.connector 
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import io

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")

class rm_details:
    # def upload_file(self):
    #      # Image upload and display
    #     global filename,img
        
    #     filename = filedialog.askopenfilename()
    #     img = ImageTk.PhotoImage(file=filename)
        
    



    def __init__(self,root) :

    

       
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+225+205")

        global floorno
        global sel_room
        global desc
        global imbt
        global mystr
        mystr = StringVar()
      

        self.var_floorno=StringVar()
        self.var_sel_room=StringVar()
        self.var_desc=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        lbl_title = Label(self.root,text="Room details",font=("consolas",20,"bold"),bg="blue",fg="grey")
        lbl_title.place(x=430,y=30,width=200,height=30)

        frame=Frame(self.root,bg="white",bd=10,relief=RAISED)
        frame.place(x=270,y=70,width=500,height=250)

        floorno=lbl=Label(frame,text="price",font=("consolas",10,"bold"),fg="black",bg="white")
        floorno.place(x=80,y=40,width=50)

        floorno=StringVar()
        self.flno=Entry(frame,font=("consolas",10,"bold"),border=0,textvariable=floorno)
        self.flno.config(font=1)
        self.flno.place(x=150,y=40)
        frame1=Frame(frame,width=270,height=2,bg="violet").place(x=150,y=62)

        security_q = Label(frame,text="Select room type",font=("consolas",10,"bold"),bg="white")
        security_q.place(x=20,y=80,width=120)
        
        sel_room = StringVar()
        self.security_q=ttk.Combobox(frame,font=("consolas",10,"bold"),textvariable=sel_room)
        self.security_q["values"]=("select","Single Room","Double Room","Deluxe Room","Double-Double (Twin Double) Room","Twin Room","Duplex Room")
        self.security_q.place(x=150,y=80,width=270)
        self.security_q.current(0)

        detail= Label(frame,text="Description",font=("consolas",10,"bold"),bg="white")
        detail.place(x=60,y=120,width=75)

        desc=StringVar()
        self.detail=Entry(frame,font=("consolas",10,"bold"),border=0,textvariable=desc)
        self.detail.config(font=1)
        self.detail.place(x=150,y=120)
        frame1=Frame(frame,width=270,height=2,bg="violet").place(x=150,y=142)

        # img= Label(frame,text="Image",font=("times new roman",10,"bold"),bg="white")
        # img.place(x=100,y=220,width=300)

        
    
        
        #   my_image_label = Label(image=my_image).pack()
        #  img= Image.open(path)
        #  img=ImageTk.PhotoImage(img)


        # path = StringVar()
        # path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','.jpg'),('all files','.*')))

        # my_image = ImageTk.PhotoImage(Image.open(path))
    
        # def UploadAction():
        #     global filename
        #     filename = filedialog.askopenfilename()
        #     filename = StringVar()
        #     if(filename):
                 
        #          resize_image = Image.resize((100,100))
        #          show_img = ImageTk.PhotoImage(resize_image) 
        #          mystr = Label(frame,image=show_img)
        #          mystr.image = show_img
        #          mystr.pack()
        #     else:
        #         print("error")
        
       
        # img_butn=Button(frame,text="  select image    ",width=22,font=("times new roman",15,"bold"),command=self.upload_file,bg="red",fg="gold",bd=0,cursor="hand1")
        # img_butn.place(x=170,y=250,width=150,height=30)
        
    
        
       
# #the variable 'var1' mentioned here holds Integer Value, by default 0
#         var1=IntVar()
# #this creates Checkbutton widget and uses place() method.
#         Checkbutton(frame,text="Lunch",bg="white", variable=var1).place(x=40,y=240)


# #the variable 'var2' mentioned here holds Integer Value, by default 0
#         var2=IntVar()
#         Checkbutton(frame,text="Dinner",bg="white", variable=var2).place(x=100,y=240)

#         var3=IntVar()
#         Checkbutton(frame,text="Breakfast",bg="white", variable=var3).place(x=160,y=240)
        cust_btn2=Button(frame,text="   Add Detail    ",width=22,font=("consolas",15,"bold"),command=self.add_data,bg="blue",fg="gold",bd=5,cursor="hand1")
        cust_btn2.place(x=170,y=180,width=150,height=30)
   
    def add_data(self):

            global img 
            global filename 
            # fob=open(root.filename,'rb').read() # filename from upload_file()
        
            if floorno.get()=="":
                messagebox.showerror("Required","Please fill this field",parent=self.root)
            else:
                
                try:
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
                    my_cursor=conn.cursor()
                    
                    my_cursor.execute("insert into room_details values(%s,%s,%s,%s)",(
                                                                        '',
                                                                        floorno.get(),
                                                                        sel_room.get(),
                                                                        desc.get()
                                                                        

                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo('confirmation', 'Record Saved',parent=self.root)
                    
        
                    

                except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
            


        
                    
        
            
    # def select_file():

    #     global my_image
    #     path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','.jpg'),('all files','.*')))
    #     my_label = Label(text=path).pack()
    #     my_image = ImageTk.PhotoImage(Image.open(path))
        
    





if __name__ == "__main__":
    root=Tk()
    obj1=rm_details(root)
    root.mainloop()
'''
if _name_ == "_main_":
    root = Tk()
    app=login_window(root)
    root.mainloop()'''