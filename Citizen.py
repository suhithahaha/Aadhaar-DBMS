# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:31:37 2020

@author: Sumit
"""

from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Citizen:
    def __init__(self):
        self.root=Tk()
        self.root.title("Citizen Management")
        self.root.geometry("1920x1080+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        title=Label(self.root,text="Citizen Management",font=("times new roman",40,"bold"),bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #Variables
        self.poi_var=StringVar()
        self.name_var=StringVar()
       
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
               
        
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,width=500,height=680)
        
        m_title=Label(Manage_Frame,text="Manage Citizens",bg="light blue",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        m_poi=Label(Manage_Frame,text="POI_No",bg="light blue",font=("times new roman",20,"bold"))
        m_poi.grid(row=1,column=0,pady=10,padx=40,sticky="w")
        
        txt_poi=Entry(Manage_Frame,textvariable=self.poi_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_poi.grid(row=1,column=1,pady=10,padx=40,sticky="w")
        
        m_name=Label(Manage_Frame,text="Name",bg="light blue",font=("times new roman",20,"bold"))
        m_name.grid(row=2,column=0,pady=10,padx=40,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=40,sticky="w")         
        
        m_address=Label(Manage_Frame,text="Address",bg="light blue",font=("times new roman",20,"bold"))
        m_address.grid(row=3,column=0,pady=10,padx=40,sticky="w")
        
        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=3,column=1,pady=10,padx=40,sticky="w")       
       
              
        
        #Button frame
        Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light blue")
        Btn_Frame.place(x=15,y=550,width=450)
        
        Add_Btn=Button(Btn_Frame,text="Add",width=10,command=self.add_citizen).grid(row=0,column=0,padx=15,pady=10)
        Update_Btn=Button(Btn_Frame,text="Update",command=self.update_data,width=10).grid(row=0,column=1,padx=15,pady=10)
        Delete_Btn=Button(Btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=15,pady=10)
        Clear_Btn=Button(Btn_Frame,text="Clear",command=self.clear,width=10).grid(row=0,column=3,padx=15,pady=10)
        Back_Btn=Button(Btn_Frame,text="Go Back To Main Menu",command=self.back,width=20).grid(row=1,columnspan=4,pady=10)
    
             
        
        
        
        #Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Detail_Frame.place(x=550,y=100,width=950,height=680)
        
        
        lbl_search=Label(Detail_Frame,text="Search_By",bg="light blue",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=20,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("POI_No","Name","Address")
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
        self.Citizen_table=ttk.Treeview(Table_Frame,columns=("POI_No","Name","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Citizen_table.xview)
        scroll_y.config(command=self.Citizen_table.yview)
        self.Citizen_table.heading("POI_No",text="POI_No")
        self.Citizen_table.heading("Name",text="Name")
        self.Citizen_table.heading("Address",text="Address")
        self.Citizen_table['show']='headings'
        self.Citizen_table.column("POI_No",width=100,anchor=CENTER)
        self.Citizen_table.column("Name",width=120,anchor=CENTER)
        self.Citizen_table.column("Address",width=200,anchor=CENTER)
        self.Citizen_table.pack(fill=BOTH,expand=1)
        self.Citizen_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.mainloop()
        
        
    def add_citizen(self):
        if(self.poi_var.get()=="" or self.name_var.get()==""):
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
            cur=con.cursor()
            cur.execute("insert into citizen values(%s,%s,%s)",(self.poi_var.get(),self.name_var.get(),self.txt_address.get('1.0',END)))                        
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()     
            messagebox.showinfo("Success","Record has been inserted")
            
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from citizen")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Citizen_table.delete(*self.Citizen_table.get_children())
            for row in rows:
                self.Citizen_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.poi_var.set("")
        self.name_var.set("")
        self.txt_address.delete("1.0",END)
               
    def get_cursor(self,ev):
        cursor_row=self.Citizen_table.focus()
        contents=self.Citizen_table.item(cursor_row)
        row=contents['values']
        self.poi_var.set(row[0])
        self.name_var.set(row[1])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[2])
        
        
    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("update citizen set name=%s,address=%s where poi_no=%s",(self.name_var.get(),self.txt_address.get('1.0',END),self.poi_var.get()))                        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been updated")
        
    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("delete from citizen where poi_no=%s",(self.poi_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted")
        
    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from citizen where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Citizen_table.delete(*self.Citizen_table.get_children())
            for row in rows:
                self.Citizen_table.insert('',END,values=row)
            con.commit()
        con.close()   
        
    def back(self):
        self.root.destroy()
        import PageTwo
        PageTwo.PageTwo()
        
        
        
#root=Tk() 
#obj = Citizen(root)
#root.mainloop()   