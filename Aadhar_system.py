from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Aadhar_system:
    def __init__(self):
        self.root=Tk()
        self.root.title("Aadhaar Management System")
        self.root.geometry("1920x1080+0+0")
        
        style = ttk.Style()
        style.theme_use("clam")
        style = ttk.Style()
        
        
        
        title=Label(self.root,text="Aadhaar Management System",font=("times new roman",40,"bold"),bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        
        #Variables
        self.uid_var=StringVar()
        self.name_var=StringVar()
        self.dob_var=StringVar()        
        self.gender_var=StringVar()
        self.email_var=StringVar()
        self.phno_var=StringVar()
        self.biometric_var=StringVar()
        self.poi_var=StringVar()
        self.cid_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
               
        
        #Manage Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,width=500,height=680)
        
        m_title=Label(Manage_Frame,text="Manage Aadhaar Data",bg="light blue",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15)
        
        m_uid=Label(Manage_Frame,text="UID",bg="light blue",font=("times new roman",15,"bold"))
        m_uid.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        txt_uid=Entry(Manage_Frame,textvariable=self.uid_var,font=("times new roman",12),bd=5,relief=GROOVE)
        txt_uid.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        m_name=Label(Manage_Frame,text="Name",bg="light blue",font=("times new roman",15,"bold"))
        m_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",13),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        m_dob=Label(Manage_Frame,text="Date Of Birth",bg="light blue",font=("times new roman",15,"bold"))
        m_dob.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",12),bd=5,relief=GROOVE)
        txt_dob.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        m_gender=Label(Manage_Frame,text="Gender",bg="light blue",font=("times new roman",15,"bold"))
        m_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)
        
        
        m_address=Label(Manage_Frame,text="Address",bg="light blue",font=("times new roman",15,"bold"))
        m_address.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        self.txt_address=Text(Manage_Frame,width=30,height=3,font=("",10))
        self.txt_address.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        m_email=Label(Manage_Frame,text="Email Id",bg="light blue",font=("times new roman",15,"bold"))
        m_email.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",13),bd=5,relief=GROOVE)
        txt_email.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        m_phno=Label(Manage_Frame,text="Phone No.",bg="light blue",font=("times new roman",15,"bold"))
        m_phno.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        txt_phno=Entry(Manage_Frame,textvariable=self.phno_var,font=("times new roman",12),bd=5,relief=GROOVE)
        txt_phno.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        
        
        m_bdata=Label(Manage_Frame,text="Biometric Data",bg="light blue",font=("times new roman",15,"bold"))
        m_bdata.grid(row=8,column=0,pady=10,padx=20,sticky="w")
        
        combo_bdata=ttk.Combobox(Manage_Frame,textvariable=self.biometric_var,font=("times new roman",14,"bold"),state="readonly")
        combo_bdata['values']=("Successful")
        combo_bdata.grid(row=8,column=1,padx=20,pady=10)
        
        m_poi=Label(Manage_Frame,text="POI No",bg="light blue",font=("times new roman",15,"bold"))
        m_poi.grid(row=9,column=0,pady=10,padx=20,sticky="w")
        
        txt_poi=Entry(Manage_Frame,textvariable=self.poi_var,font=("times new roman",12),bd=5,relief=GROOVE)
        txt_poi.grid(row=9,column=1,pady=10,padx=20,sticky="w")
        
        m_cid=Label(Manage_Frame,text="Centre Id",bg="light blue",font=("times new roman",15,"bold"))
        m_cid.grid(row=10,column=0,pady=10,padx=20,sticky="w")
        
        txt_cid=Entry(Manage_Frame,textvariable=self.cid_var,font=("times new roman",12),bd=5,relief=GROOVE)
        txt_cid.grid(row=10,column=1,pady=10,padx=20,sticky="w")
        
        
        #Button frame
        Btn_Frame=Frame(Manage_Frame,bd=2,relief=RIDGE,bg="light blue")
        Btn_Frame.place(x=15,y=590,width=450)
        
        Add_Btn=Button(Btn_Frame,text="Add",width=10,command=self.add_data).grid(row=0,column=0,padx=15,pady=6)
        Update_Btn=Button(Btn_Frame,text="Update",command=self.update_data,width=10).grid(row=0,column=1,padx=15,pady=6)
        Delete_Btn=Button(Btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=15,pady=6)
        Clear_Btn=Button(Btn_Frame,text="Clear",command=self.clear,width=10).grid(row=0,column=3,padx=15,pady=6)
        Back_Btn=Button(Btn_Frame,text="Go Back To Main Menu",command=self.back,width=20).grid(row=1,columnspan=4,pady=6)
    
             
        
        
        
        #Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Detail_Frame.place(x=550,y=100,width=950,height=680)
        
        
        lbl_search=Label(Detail_Frame,text="Search_By",bg="light blue",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=20,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("UID","Name","Phno","POI_No","Centre_Id","DOB","Gender","Address","Email")
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=25,font=("times new roman",13),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        Search_Btn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=15,pady=10)
        Showall_Btn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=15,pady=10)
        
        
       #Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="light blue")
        Table_Frame.place(x=10,y=70,width=910,height=600)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Aadhar_system_table=ttk.Treeview(Table_Frame,columns=("UID","Name","DOB","Address","Gender","Email","Phno","Biometric_data","POI_No","Centre_Id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Aadhar_system_table.xview)
        scroll_y.config(command=self.Aadhar_system_table.yview)
        self.Aadhar_system_table.heading("UID",text="UID")
        self.Aadhar_system_table.heading("Name",text="Name")
        self.Aadhar_system_table.heading("DOB",text="D.O.B.")
        self.Aadhar_system_table.heading("Address",text="Address")
        self.Aadhar_system_table.heading("Gender",text="Gender")
        self.Aadhar_system_table.heading("Email",text="Email")
        self.Aadhar_system_table.heading("Phno",text="Phone No.")        
        self.Aadhar_system_table.heading("Biometric_data",text="Biometric")
        self.Aadhar_system_table.heading("POI_No",text="POI No")
        self.Aadhar_system_table.heading("Centre_Id",text="Centre Id")
        self.Aadhar_system_table['show']='headings'
        self.Aadhar_system_table.column("UID",width=120,anchor=CENTER)
        self.Aadhar_system_table.column("Name",width=120,anchor=CENTER)
        self.Aadhar_system_table.column("DOB",width=100,anchor=CENTER)
        self.Aadhar_system_table.column("Address",width=180,anchor=CENTER)
        self.Aadhar_system_table.column("Gender",width=80,anchor=CENTER)
        self.Aadhar_system_table.column("Email",width=130,anchor=CENTER)        
        self.Aadhar_system_table.column("Phno",width=100,anchor=CENTER)        
        self.Aadhar_system_table.column("Biometric_data",width=90,anchor=CENTER)  
        self.Aadhar_system_table.column("POI_No",width=110,anchor=CENTER)  
        self.Aadhar_system_table.column("Centre_Id",width=90,anchor=CENTER)  
        self.Aadhar_system_table.pack(fill=BOTH,expand=1)
        self.Aadhar_system_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.root.mainloop()
        
        
    def add_data(self):
        if(self.uid_var.get()=="" or self.name_var.get()=="" or self.dob_var.get()=="" or self.gender_var.get()=="" or self.email_var.get()=="" or self.phno_var.get()=="" or self.biometric_var.get()=="" or self.poi_var.get()=="" or self.cid_var.get()==""):
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
            cur=con.cursor()
            cur.execute("insert into aadhar_card values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.uid_var.get(),self.name_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.gender_var.get(),self.email_var.get(),self.phno_var.get(),self.biometric_var.get(),self.poi_var.get(),self.cid_var.get()))                        
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()     
            messagebox.showinfo("Success","Record has been inserted")
            
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from aadhar_card")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Aadhar_system_table.delete(*self.Aadhar_system_table.get_children())
            for row in rows:
                self.Aadhar_system_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.uid_var.set("")
        self.name_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
        self.gender_var.set("")
        self.email_var.set("")
        self.phno_var.set("")       
        self.biometric_var.set("")
        self.poi_var.set("")
        self.cid_var.set("")
        
    def get_cursor(self,ev):
        cursor_row=self.Aadhar_system_table.focus()
        contents=self.Aadhar_system_table.item(cursor_row)
        row=contents['values']
        self.uid_var.set(row[0])
        self.name_var.set(row[1])
        self.dob_var.set(row[2])        
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[3])
        self.gender_var.set(row[4])
        self.email_var.set(row[5])
        self.phno_var.set(row[6])        
        self.biometric_var.set(row[7])
        self.poi_var.set(row[8])
        self.cid_var.set(row[9])
        
    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("update aadhar_card set name=%s,dob=%s,address=%s,gender=%s,email=%s,phno=%s,biometric_data=%s,poi_no=%s,centre_id=%s where uid=%s",(self.name_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.gender_var.get(),self.email_var.get(),self.phno_var.get(),self.biometric_var.get(),self.poi_var.get(),self.cid_var.get(),self.uid_var.get()))                        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been updated")
        
    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("delete from aadhar_card where uid=%s",(self.uid_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted")
        
    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="sumit",database="aadhaar")
        cur=con.cursor()
        cur.execute("select * from aadhar_card where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Aadhar_system_table.delete(*self.Aadhar_system_table.get_children())
            for row in rows:
                self.Aadhar_system_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def back(self):
        self.root.destroy()
        import PageTwo
        PageTwo.PageTwo()    
        
        
#root=Tk() 
#obj=Aadhar_system(root)
#root.mainloop()   