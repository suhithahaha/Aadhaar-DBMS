# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:41:42 2020

@author: Sumit
"""

from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox



class PageTwo:
    def __init__(self):
        self.main=Tk()
        self.main.title("Welcome Page")
        self.main.geometry("1920x1080+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        #All images
        self.bg_icon=PhotoImage(file="F:/Aadhar DBMS Project/images/aadhar.png")
        self.logo_icon=PhotoImage(file="F:/Aadhar DBMS Project/images/logo.png")
        
        #Variables
        self.uname=StringVar()
        self.pwd=StringVar()
        
        bg_label=Label(self.main,image=self.bg_icon).pack()
        
        title=Label(self.main,text="WELCOME  To  AADHAAR ",font=("algerian",60),bd=10,relief=GROOVE,bg="light blue")
        title.place(x=0,y=0,relwidth=1)
        
        Inner_Frame=Frame(self.main,bg="light blue")
        Inner_Frame.place(x=250,y=250)
        
        logo_label=Label(Inner_Frame,image=self.logo_icon,bd=5,bg="light blue").grid(row=0,columnspan=5,pady=20)
        
        button_citizen=Button(Inner_Frame,text="Citizen",command=self.citizen,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=1,column=0,pady=10,padx=10)
        button_aadharcard=Button(Inner_Frame,text="Aadhar Card",command=self.aadhaar,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=1,column=1,pady=10,padx=10)
        button_family=Button(Inner_Frame,text="Family",command=self.family,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=1,column=2,pady=10,padx=10)
        button_operator=Button(Inner_Frame,text="Operator",command=self.operator,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=1,column=3,pady=10,padx=10)
        button_ecentre=Button(Inner_Frame,text="Enrollment Centre",command=self.ecentre,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=1,column=4,pady=10,padx=10)
        button_logout=Button(Inner_Frame,text="Logout",command=self.logout,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=2,columnspan=5,pady=10)
        
        #Abbrevations Frame
        Abbr_Frame=Frame(self.main,bd=6,relief=RIDGE,bg="light blue")
        Abbr_Frame.place(x=1250,y=120,width=250,height=150)
        
        m_title=Label(Abbr_Frame,text="Abbreviations",bg="light blue",font=("times new roman",20,"bold"))
        m_title.grid(row=0,column=0,padx=2,pady=2)
        
        m_title1=Label(Abbr_Frame,text="POR:- Proof Of Relationship ",bg="light blue",font=("times new roman",14))
        m_title1.grid(row=1,column=0,padx=2,pady=2)
        
        m_title2=Label(Abbr_Frame,text="POI:- Proof Of Identity",bg="light blue",font=("times new roman",14))
        m_title2.grid(row=2,column=0,padx=2,pady=2)
        
        m_title3=Label(Abbr_Frame,text="(Required for Enrollment)",bg="light blue",font=("times new roman",14))
        m_title3.grid(row=3,column=0,padx=2,pady=2)
        
        #Indo Frame
        Info_Frame=Frame(self.main,bd=6,relief=RIDGE,bg="light blue")
        Info_Frame.place(x=10,y=120,width=220,height=200)
        
        m_title=Label(Info_Frame,text="IMP INFO",bg="light blue",font=("times new roman",20,"bold"))
        m_title.grid(row=0,column=0,padx=2,pady=2)
        
        m_title1=Label(Info_Frame,text="FOR NEW USERS ",bg="light blue",font=("times new roman",14))
        m_title1.grid(row=1,column=0,padx=2,pady=2)
        
        m_title2=Label(Info_Frame,text="First make your CITIZEN",bg="light blue",font=("times new roman",14))
        m_title2.grid(row=2,column=0,padx=2,pady=2)
        
        m_title2=Label(Info_Frame,text="profile",bg="light blue",font=("times new roman",14))
        m_title2.grid(row=3,column=0,padx=2,pady=2)
        
        m_title3=Label(Info_Frame,text="(Required for Enrollment)",bg="light blue",font=("times new roman",14))
        m_title3.grid(row=4,column=0,padx=2,pady=2)
        
        #button_login=Button(Login_Frame,text="Login",command=self.login,width=15,font=("times new roman",14,"bold"),bg="light blue",fg="black").grid(row=3,column=1,pady=10)
        self.main.mainloop()
    
    def logout(self):
        option=messagebox.askyesno("Exit","Do you really want to logout?")
        if option>0:
            self.main.destroy()
            import Login_System  
        else:
            return
       
    def citizen(self):
        self.main.destroy()
        import Citizen
        Citizen.Citizen()
        
    def aadhaar(self):
        self.main.destroy()
        import Aadhar_system
        Aadhar_system.Aadhar_system()
        
    def family(self):
        self.main.destroy()
        import Family
        Family.Family()
        
    def operator(self):
        self.main.destroy()
        import Operator
        Operator.Operator()
    
    def ecentre(self):
        self.main.destroy()
        import Enrollment_Centre
        Enrollment_Centre.Enrollment_Centre()
    
#main=Tk()
#obj=PageTwo(main)
#main.mainloop()