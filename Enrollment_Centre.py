# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:31:54 2020

@author: Sumit
"""

from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Enrollment_Centre:
    def __init__(self):
        self.root=Tk()
        self.root.title("Enrollment Centre System")
        self.root.geometry("1920x1080+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        
        title=Label(self.root,text="Enrollment Centre System",font=("times new roman",40,"bold"),bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #Variables
        self.cid_var=StringVar()
        self.cname_var=StringVar()
        self.type_var=StringVar()        
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
               
        
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,width=500,height=680)
        
        m_title=Label(Manage_Frame,text="Manage Centres",bg="light blue",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        m_cid=Label(Manage_Frame,text="Centre ID",bg="light blue",font=("times new roman",20,"bold"))
        m_cid.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        txt_cid=Entry(Manage_Frame,textvariable=self.cid_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_cid.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        m_cname=Label(Manage_Frame,text="Centre Name",bg="light blue",font=("times new roman",20,"bold"))
        m_cname.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_cname=Entry(Manage_Frame,textvariable=self.cname_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_cname.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        m_address=Label(Manage_Frame,text="Centre Address",bg="light blue",font=("times new roman",20,"bold"))
        m_address.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        
        m_type=Label(Manage_Frame,text="Type Of Centre",bg="light blue",font=("times new roman",20,"bold"))
        m_type.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        txt_type=Entry(Manage_Frame,textvariable=self.type_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_type.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        
        
       
       
        #Button frame
        Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light blue")
        Btn_Frame.place(x=15,y=550,width=450)
        
        Add_Btn=Button(Btn_Frame,text="Add",width=10,command=self.add_data).grid(row=0,column=0,padx=15,pady=10)
        Update_Btn=Button(Btn_Frame,text="Update",command=self.update_data,width=10).grid(row=0,column=1,padx=15,pady=10)
        Delete_Btn=Button(Btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=15,pady=10)
        Clear_Btn=Button(Btn_Frame,text="Clear",command=self.clear,width=10).grid(row=0,column=3,padx=15,pady=10)
        Back_Btn=Button(Btn_Frame,text="Go Back To Main Menu",command=self.back,width=20).grid(row=1,column=0,columnspan=2,pady=10)
        Enroll_Btn=Button(Btn_Frame,text="Enroll In A Centre",command=self.goenroll,width=18).grid(row=1,column=2,columnspan=2,pady=10)
    
             
    
             
        
        
        
        #Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Detail_Frame.place(x=550,y=100,width=950,height=680)
        
        
        lbl_search=Label(Detail_Frame,text="Search_By",bg="light blue",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=20,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Centre_Id","Centre_Name","Centre_Address","Type")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=25,font=("times new roman",14),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        Search_Btn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=15,pady=10)
        Showall_Btn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=15,pady=10)
        
        
       #Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="light blue")
        Table_Frame.place(x=10,y=70,width=910,height=600)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Enrollment_Centre_table=ttk.Treeview(Table_Frame,columns=("Center_Id","Center_Name","Center_Address","Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Enrollment_Centre_table.xview)
        scroll_y.config(command=self.Enrollment_Centre_table.yview)
        self.Enrollment_Centre_table.heading("Center_Id",text="Centre ID")
        self.Enrollment_Centre_table.heading("Center_Name",text=" Centre Name")
        self.Enrollment_Centre_table.heading("Center_Address",text="Centre Address")
        self.Enrollment_Centre_table.heading("Type",text="Type Of Centre")
        self.Enrollment_Centre_table['show']='headings'
        self.Enrollment_Centre_table.column("Center_Id",width=10,anchor=CENTER)
        self.Enrollment_Centre_table.column("Center_Name",width=60,anchor=CENTER)
        self.Enrollment_Centre_table.column("Center_Address",width=460,anchor=CENTER)
        self.Enrollment_Centre_table.column("Type",width=20,anchor=CENTER)
        self.Enrollment_Centre_table.pack(fill=BOTH,expand=1)
        self.Enrollment_Centre_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.mainloop()
        
        
    def add_data(self):
        if(self.cid_var.get()=="" or self.cname_var.get()=="" or self.type_var.get()==""):
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
            cur=con.cursor()
            cur.execute("insert into enrollment_centre values(%s,%s,%s,%s)",(self.cid_var.get(),self.cname_var.get(),self.txt_address.get('1.0',END),self.type_var.get()))                        
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()     
            messagebox.showinfo("Success","Record has been inserted")
            
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from enrollment_centre")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Enrollment_Centre_table.delete(*self.Enrollment_Centre_table.get_children())
            for row in rows:
                self.Enrollment_Centre_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.cid_var.set("")
        self.cname_var.set("")
        self.txt_address.delete("1.0",END)
        self.type_var.set("")
        
        
    def get_cursor(self,ev):
        cursor_row=self.Enrollment_Centre_table.focus()
        contents=self.Enrollment_Centre_table.item(cursor_row)
        row=contents['values']
        self.cid_var.set(row[0])
        self.cname_var.set(row[1])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[2])
        self.type_var.set(row[3])
        
        
    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("update enrollment_centre set centre_name=%s,centre_address=%s,type=%s where centre_id=%s",(self.cname_var.get(),self.txt_address.get('1.0',END),self.type_var.get(),self.cid_var.get()))                        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been updated")
        
    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("delete from enrollment_centre where centre_id=%s",(self.cid_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted")
        
    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from enrollment_centre where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Enrollment_Centre_table.delete(*self.Enrollment_Centre_table.get_children())
            for row in rows:
                self.Enrollment_Centre_table.insert('',END,values=row)
            con.commit()
        con.close() 
        
        
    def back(self):
        self.root.destroy()
        import PageTwo
        PageTwo.PageTwo()
        
    def goenroll(self):
        self.root.destroy()
        import Enroll
        Enroll.Enroll()    

    
        
#root=Tk() 
#obj=Enrollment_Centre(root)
#root.mainloop()   