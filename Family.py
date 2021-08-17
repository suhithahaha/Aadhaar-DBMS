# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:31:42 2020

@author: Sumit
"""

from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Family:
    def __init__(self):
        self.root=Tk()
        self.root.title("Family Information")
        self.root.geometry("1920x1080+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        
        title=Label(self.root,text="Family Information",font=("times new roman",40,"bold"),bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #Variables
        self.por_var=StringVar()
        self.poi_var=StringVar()   
        self.uidmem_var=StringVar()             
        self.relation_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
               
        
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,width=500,height=680)
        
        m_title=Label(Manage_Frame,text="Manage Family",bg="light blue",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        m_por=Label(Manage_Frame,text="POR No",bg="light blue",font=("times new roman",20,"bold"))
        m_por.grid(row=1,column=0,pady=10,padx=13,sticky="w")
        
        txt_por=Entry(Manage_Frame,textvariable=self.por_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_por.grid(row=1,column=1,pady=10,padx=13,sticky="w")
        
        m_poi=Label(Manage_Frame,text="POI No",bg="light blue",font=("times new roman",20,"bold"))
        m_poi.grid(row=2,column=0,pady=10,padx=13,sticky="w")
        
        txt_poi=Entry(Manage_Frame,textvariable=self.poi_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_poi.grid(row=2,column=1,pady=10,padx=13,sticky="w")
        
        m_uidmem=Label(Manage_Frame,text="UID Of Member",bg="light blue",font=("times new roman",20,"bold"))
        m_uidmem.grid(row=4,column=0,pady=10,padx=13,sticky="w")
        
        txt_uidmem=Entry(Manage_Frame,textvariable=self.uidmem_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_uidmem.grid(row=4,column=1,pady=10,padx=13,sticky="w")
        
               
        m_relation=Label(Manage_Frame,text="Relation",bg="light blue",font=("times new roman",20,"bold"))
        m_relation.grid(row=3,column=0,pady=10,padx=13,sticky="w")
        
        txt_relation=Entry(Manage_Frame,textvariable=self.relation_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_relation.grid(row=3,column=1,pady=10,padx=13,sticky="w")
        
       
        
        #Button frame
        Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="light blue")
        Btn_Frame.place(x=15,y=550,width=450)
        
        Add_Btn=Button(Btn_Frame,text="Add",width=10,command=self.add_data).grid(row=0,column=0,padx=15,pady=10)
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
        combo_search['values']=("POR_Id","POI_No","UID_Of_Member")
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
        self.Family_table=ttk.Treeview(Table_Frame,columns=("POR_Id","POI_No","Relation","UID_Of_Member"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Family_table.xview)
        scroll_y.config(command=self.Family_table.yview)
        self.Family_table.heading("POR_Id",text="POR ID")
        self.Family_table.heading("POI_No",text="POI No")
        self.Family_table.heading("UID_Of_Member",text="UID OF MEMBER")        
        self.Family_table.heading("Relation",text="Relation")
        self.Family_table['show']='headings'
        self.Family_table.column("POR_Id",width=180,anchor=CENTER)
        self.Family_table.column("POI_No",width=180,anchor=CENTER)
        self.Family_table.column("UID_Of_Member",width=180,anchor=CENTER)        
        self.Family_table.column("Relation",width=100,anchor=CENTER)
        self.Family_table.pack(fill=BOTH,expand=1)
        self.Family_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.mainloop()
        
        
    def add_data(self):
        if(self.por_var.get()=="" or self.poi_var.get()==""):
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
            cur=con.cursor()
            cur.execute("insert into family values(%s,%s,%s,%s)",(self.por_var.get(),self.poi_var.get(),self.relation_var.get(),self.uidmem_var.get()))                        
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()     
            messagebox.showinfo("Success","Record has been inserted")
            
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from family")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Family_table.delete(*self.Family_table.get_children())
            for row in rows:
                self.Family_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.por_var.set("")
        self.poi_var.set("")
        self.uidmem_var.set("")
        self.relation_var.set("")
                
    def get_cursor(self,ev):
        cursor_row=self.Family_table.focus()
        contents=self.Family_table.item(cursor_row)
        row=contents['values']
        self.por_var.set(row[0])
        self.poi_var.set(row[1])
        self.uidmem_var.set(row[3])
        self.relation_var.set(row[2])
       
        
    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("update family set uid_of_member=%s,relation=%s where por_id=%s and poi_no=%s",(self.uidmem_var.get(),self.relation_var.get(),self.por_var.get(),self.poi_var.get()))                        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close() 
        messagebox.showinfo("Success","Record has been updated")
        
    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("delete from family where por_id=%s",(self.por_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted")
        
    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhar")
        cur=con.cursor()
        cur.execute("select * from family where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Family_table.delete(*self.Family_table.get_children())
            for row in rows:
                self.Family_table.insert('',END,values=row)
            con.commit()
        con.close() 
        
    def back(self):
        self.root.destroy()
        import PageTwo
        PageTwo.PageTwo()
        
        
#root=Tk() 
#obj=Family(root)
#root.mainloop()   