# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:07:22 2020

@author: Sumit
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:31:54 2020

@author: Sumit
"""

from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Enroll:
    def __init__(self):
        self.root=Tk()
        self.root.title("Enrollment Management System")
        self.root.geometry("1920x1080+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        title=Label(self.root,text="Enrollment Management System",font=("times new roman",40,"bold"),bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #Variables
        self.cid_var=StringVar()
        self.poi_var=StringVar()
                
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
               
        
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,width=500,height=680)
        
        m_title=Label(Manage_Frame,text="Manage Enrollments",bg="light blue",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        m_poi=Label(Manage_Frame,text="POI No",bg="light blue",font=("times new roman",20,"bold"))
        m_poi.grid(row=1,column=0,pady=10,padx=25,sticky="w")
        
        txt_poi=Entry(Manage_Frame,textvariable=self.poi_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_poi.grid(row=1,column=1,pady=10,padx=25,sticky="w")
        
        
        m_cid=Label(Manage_Frame,text="Centre ID",bg="light blue",font=("times new roman",20,"bold"))
        m_cid.grid(row=2,column=0,pady=10,padx=25,sticky="w")
        
        txt_cid=Entry(Manage_Frame,textvariable=self.cid_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_cid.grid(row=2,column=1,pady=10,padx=25,sticky="w")
        
       
        
       
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
        Detail_Frame.place(x=550,y=100,width=950,height=480)
        
        
        lbl_search=Label(Detail_Frame,text="Search_By",bg="light blue",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=20,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("POI_No","Centre_Id")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=25,font=("times new roman",14),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        Search_Btn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=15,pady=10)
        Showall_Btn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=15,pady=10)
        
        #INFO Frame
        Info_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="light blue")
        Info_Frame.place(x=700,y=590,width=450,height=190)
        
        m_title=Label(Info_Frame,text="Enrollment Centre Timings",bg="light blue",font=("times new roman",25,"bold"))
        m_title.grid(row=0,column=3,pady=10)
        
        m_title1=Label(Info_Frame,text="9:00 to 18:00 (Monday to Friday) ",bg="light blue",font=("times new roman",15))
        m_title1.grid(row=1,column=3,pady=8)
        
        m_title2=Label(Info_Frame,text="12:00 to 16:00 (Saturaday and Sunday)",bg="light blue",font=("times new roman",15))
        m_title2.grid(row=2,column=3,pady=8)
        
        
       #Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="light blue")
        Table_Frame.place(x=10,y=70,width=910,height=400)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Enroll_table=ttk.Treeview(Table_Frame,columns=("POI_No","Center_Id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Enroll_table.xview)
        scroll_y.config(command=self.Enroll_table.yview)
        self.Enroll_table.heading("POI_No",text="POI No")
        self.Enroll_table.heading("Center_Id",text="Centre ID")        
        self.Enroll_table['show']='headings'
        self.Enroll_table.column("POI_No",width=180,anchor=CENTER)
        self.Enroll_table.column("Center_Id",width=180,anchor=CENTER)        
        self.Enroll_table.pack(fill=BOTH,expand=1)
        self.Enroll_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.mainloop()
        
        
    def add_data(self):
        if(self.poi_var.get()=="" or self.cid_var.get()==""):
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
            cur=con.cursor()
            cur.execute("insert into enrolls values(%s,%s)",(self.poi_var.get(),self.cid_var.get()))                        
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()     
            messagebox.showinfo("Success","Record has been inserted")
            
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from enrolls")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Enroll_table.delete(*self.Enroll_table.get_children())
            for row in rows:
                self.Enroll_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.poi_var.set("")
        self.cid_var.set("")     
        
        
        
    def get_cursor(self,ev):
        cursor_row=self.Enroll_table.focus()
        contents=self.Enroll_table.item(cursor_row)
        row=contents['values']      
        self.poi_var.set(row[0])
        self.cid_var.set(row[1])
        
        
        
    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("update enrolls set centre_id=%s where poi_no=%s",(self.cid_var.get(),self.poi_var.get()))                        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been updated")
        
        
    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("delete from enrolls where poi_no=%s",(self.poi_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted")
        
    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from enrolls where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Enroll_table.delete(*self.Enroll_table.get_children())
            for row in rows:
                self.Enroll_table.insert('',END,values=row)
            con.commit()
        con.close() 
        
        
    def back(self):
        self.root.destroy()
        import PageTwo
        PageTwo.PageTwo()
        
    

    
        
#root=Tk() 
#obj=Enroll(root)
#root.mainloop()   