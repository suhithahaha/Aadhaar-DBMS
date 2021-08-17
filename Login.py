from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk



class Login_System:
    def __init__(self,main):
        self.main=main
        self.main.title("Login System")
        self.main.geometry("1366x768+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        #All images
        self.bg_icon=PhotoImage(file="F:/Aadhar DBMS Project/images/aadhar.png")
        self.user_icon=PhotoImage(file="F:/Aadhar DBMS Project/images/user.png")
        self.pwd_icon=PhotoImage(file="F:/Aadhar DBMS Project/images/pwd.png")
        self.logo_icon=PhotoImage(file="F:/Aadhar DBMS Project/images/logo.png")
        
        #Variables
        self.uname=StringVar()
        self.pwd=StringVar()
        
        bg_label=Label(self.main,image=self.bg_icon).pack()
        
        title=Label(self.main,text="AADHAAR   Login   System",font=("algerian",60),bd=10,relief=GROOVE,bg="light blue")
        title.place(x=0,y=0,relwidth=1)
        
        Login_Frame=Frame(self.main,bg="light blue")
        Login_Frame.place(x=500,y=150)
        
        logo_label=Label(Login_Frame,image=self.logo_icon,bd=5,bg="light blue").grid(row=0,columnspan=2,pady=20)
        
        label_user=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txt_user=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=25)
        
        label_pwd=Label(Login_Frame,text="Password",image=self.pwd_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txt_pwd=Entry(Login_Frame,bd=5,textvariable=self.pwd,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=25)
        
        button_login=Button(Login_Frame,text="Login",command=self.login,width=14,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=3,column=0,pady=10)
        button_exit=Button(Login_Frame,text="Exit",command=self.exit_menu,width=14,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=3,column=1,pady=10)
    
    
    def login(self):
        if self.uname.get()=="" or self.pwd.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.uname.get()=="Suhitha" and self.pwd.get()=="admin":
            messagebox.showinfo("Successfull",f"Welcome {self.uname.get()}")
            main.destroy()
            import PageTwo
            PageTwo.PageTwo()
        else:
            messagebox.showerror("Error","Invalid Username or Password")
    
    
    def exit_menu(self):
        option=messagebox.askyesno("Exit","Do you really want to exit?")
        if option>0:
            self.main.destroy()
        else:
            return
              
        
main=Tk()
obj=Login_System(main)
main.mainloop()