import qrcode
from tkinter import *
from PIL import Image, ImageTk

class Qr_Generator:
    def __init__(self, root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator| Python mini project")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="Qr code Generator",font=("times new roman",40),bg="#053246",fg="white")
        title.place(x=0,y=0,relwidth=1)
        
        # employee details window
        # variables
        self.var_emp_code= StringVar()
        self.var_emp_name= StringVar()
        self.var_emp_department= StringVar()
        self.var_emp_designation= StringVar()

        emp_Frame=Frame(self.root,bd= 2,relief=RIDGE,bg="white")
        emp_Frame.place(x=50,y=100,width=500,height=380)                    
        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20),bg="#053246",fg="white")
        emp_title.place(x=0,y=0,relwidth=1)
        
        lbl__emp_code=Label(emp_Frame,text="Employee ID",font=("time new roman",15,"bold"),bg="white")
        lbl__emp_code.place(x=20,y=60)
        
        lbl_emp_code=Label(emp_Frame,text="Name",font=("time new roman",15,"bold"),bg="white")
        lbl_emp_code.place(x=20,y=100)
        
        lbl_emp_code=Label(emp_Frame,text="Department",font=("time new roman",15,"bold"),bg="white")
        lbl_emp_code.place(x=20,y=140)
        
        lbl_emp_code=Label(emp_Frame,text="Designation",font=("time new roman",15,"bold"),bg="white")
        lbl_emp_code.place(x=20,y=180) 
    
        txt__emp_code=Entry(emp_Frame ,font=("time new roman",15),textvariable=self.var_emp_code,bg="lightblue")
        txt__emp_code.place(x=200,y=60)
        
        txt__emp_code=Entry(emp_Frame,text="Name",font=("time new roman",15),textvariable=self.var_emp_name,bg="lightblue")
        txt__emp_code.place(x=200,y=100)
        
        txt__emp_code=Entry(emp_Frame,font=("time new roman",15),textvariable=self.var_emp_department,bg="lightblue")
        txt__emp_code.place(x=200,y=140)
        
        txt__emp_code=Entry(emp_Frame,font=("time new roman",15),textvariable=self.var_emp_designation,bg="lightblue")
        txt__emp_code.place(x=200,y=180)     
        
        # creating button
        btn_generate = Button(emp_Frame,text="QR generate",command=self.generate,font=("times new roman",18,"bold"),bg="#2196f3",fg="white")
        btn_generate.place(x=90,y=250,width=180,height=30)
        
        btn_clear= Button(emp_Frame,text="Clear",font=("times new roman",18,"bold"),command=self.clear,bg="#2196f3",fg="white")
        btn_clear.place(x=280,y=250,width=120,height=30)    
        
        self.msg=""
        self.lb_msg=Label(emp_Frame,text=self.msg,font=("goudy old style",20),bg="white",fg="green")    
        self.lb_msg.place(x=0,y=320,relwidth=1)
        
        # employee Qr window 
        qr_Frame=Frame(self.root,bd= 2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=250,height=380)                    
        emp_title=Label(qr_Frame,text="Employee Qr code",font=("goudy old style",20),bg="#053246",fg="white")
        emp_title.place(x=0,y=0,relwidth=1)
        
        self.qr_code_image = Label(qr_Frame, text="QR code\n Not available", font=("times new roman",15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
        self.qr_code_image.place(x=35,y=100,width=180,height=180)
    
    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')
        self.var_emp_name.set('')
        self.msg= ""
        self.lb_msg.config(text=self.msg)
        self.qr_code_image.config(image="")  # Clearing the QR code image
    
    def generate(self):
        if self.var_emp_designation.get()== '' or self.var_emp_code.get()==''or self.var_emp_department.get() == '' or self.var_emp_name.get() == '':
            self.msg= "All fields are required"
            self.lb_msg.config(text=self.msg,fg="red")
        else:
            # Generating QR code
            qr_data = f"ID: {self.var_emp_code.get()}\nName: {self.var_emp_name.get()}\nDepartment: {self.var_emp_department.get()}\nDesignation: {self.var_emp_designation.get()}"
            qr = qrcode.make(qr_data)
            qr_path = "employee_qr.png"
            qr.save(qr_path)
            
            # Displaying QR code image
            qr_image = Image.open(qr_path)
            qr_image = qr_image.resize((180, 180))
            qr_image = ImageTk.PhotoImage(qr_image)
            self.qr_code_image.config(image=qr_image)
            self.qr_code_image.image = qr_image  # Keeping a reference to avoid garbage collection
            self.msg="QR Generated Successfully!!!!"
            self.lb_msg.config(text=self.msg,fg="green")
            
root = Tk()
obj = Qr_Generator(root)
root.mainloop()
