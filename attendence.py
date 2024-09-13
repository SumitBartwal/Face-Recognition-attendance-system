from msilib import add_data
import os
from tkinter import END, W, Button, Entry, Frame, Grid, Label, LabelFrame, Place, StringVar, Tk, messagebox, ttk
import tkinter
from PIL import Image, ImageTk
import mysql.connector
import cv2
import csv
import os
from tkinter import filedialog
from tkinter import Tk
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Attandence")
        self.root.wm_iconbitmap("face icon.ico")

        
        
        
        #variables
        self.var_atten_std_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_course=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
          #first image
        img = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\images (2).jpeg")
        img = img.resize((500, 160), Image.LANCZOS)    
        self.photoimg = ImageTk.PhotoImage(img)  

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=160)  # Corrected height parameter


        #second image
        img1 = Image.open(r"Images of interface page\images 1.jpeg")
        img1 = img1.resize((500, 160), Image.LANCZOS)    
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=500, height=160)
        
        
        #third image
        img2 = Image.open(r"Images of interface page\images (7).jpeg")
        img2 = img2.resize((500, 160), Image.LANCZOS)    
        self.photoimg2 = ImageTk.PhotoImage(img2)  

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=500, height=160)
        
        
         #title name
        title_lbl=Label(self.root,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=20,y=170,width= 1200,height=40)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=220,width=1290,height=600)
        
         #left rabel frame

        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief="ridge",text="Student Attendence Details",font=("times new roman",15,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=450)
        
        #image
        img_left = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\image 3.webp")
        img_left = img_left.resize((550, 90), Image.LANCZOS)    
        self.photoimg_left = ImageTk.PhotoImage(img_left)  

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=20, y=0, width=550, height=90)
        
        

        left_inside_frame=LabelFrame(Left_frame,bg="white",bd=2,relief="ridge")
        left_inside_frame.place(x=20,y=90,width=550,height=300)
        
         #std id
        attendance_label=Label(left_inside_frame,text="Student Id",font=("times new roman",10,"bold"),bg="white")
        attendance_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)
        
        attendance_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_std_id,width=20,font=("times new roman",10,"bold"))
        attendance_entry.grid(row=0,column=1,padx=8,pady=5,sticky=W)
 
        
        #Roll
        roll_label=Label(left_inside_frame,text="Roll No",font=("times new roman",10,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=8,pady=5,sticky=W)
        
        
        #Name
        Name_label=Label(left_inside_frame,text="Name",font=("times new roman",10,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=8,pady=5,sticky=W)
        
        Name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",10,"bold"))
        Name_entry.grid(row=1,column=1,padx=8,pady=5,sticky=W)
        
        #course
        
        course_label=Label(left_inside_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=1,column=2,padx=8,pady=5,sticky=W)
        
        course_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_course,width=20,font=("times new roman",10,"bold"))
        course_entry.grid(row=1,column=3,padx=8,pady=5,sticky=W)
        
        #Time
        
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",10,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=8,pady=5,sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",10,"bold"))
        time_entry.grid(row=2,column=1,padx=8,pady=5,sticky=W)
        
        #date
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",10,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=8,pady=5,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",10,"bold"))
        date_entry.grid(row=2,column=3,padx=8,pady=5,sticky=W)
        
        #Attendence Status
        attndence_status_label=Label(left_inside_frame,text="SEMESTER",font=("times new roman",10,"bold"),bg="white")
        attndence_status_label.grid(row=3,column=0,padx=8,sticky=W)

        attndence_status_combo=ttk.Combobox(left_inside_frame,font=("times new roman",10,"bold"),width=20,state="readonly")
        attndence_status_combo["values"]=("Status","Present","Absent")
        attndence_status_combo.current(0)
        attndence_status_combo.grid(row=3,column=1,padx=2,pady=8,sticky=W)
        
         #button frame
        btn_frame=Frame(left_inside_frame,bg="white",bd=2,relief="ridge")
        btn_frame.place(x=3,y=160,width=540,height=28)

        #import csv
        save_button=Button(btn_frame,text="Import Csv",command=self.importCsv,width=16,height=1,font=("times new roman",10,"bold"),bg="black",fg="white")
        save_button.grid(row=0,column=0,padx=4)

        #export csv
        update_button=Button(btn_frame,command=self.exportCsv,text="Export Csv",width=16,height=1,font=("times new roman",10,"bold"),bg="dark green",fg="white")
        update_button.grid(row=0,column=1,padx=4)

        #update
        delete_button=Button(btn_frame,text="Update",width=16,height=1,font=("times new roman",10,"bold"),bg="red",fg="white")
        delete_button.grid(row=0,column=2,padx=4)

        #reset button
        reset_button=Button(btn_frame,command=self.reset_data,text="Reset",width=16,height=1,font=("times new roman",10,"bold"),bg="dark blue",fg="white")
        reset_button.grid(row=0,column=3,padx=4)

         
        
        
        
        
         
        
        
        #right rabel frame

        right_frame=LabelFrame(main_frame,bg="white",bd=2,relief="ridge",text="Attendence Details",font=("times new roman",15,"bold"))
        right_frame.place(x=650,y=10,width=600,height=470)
        
          # Create the table frame
 
  
        table_frame = Frame(right_frame, bg="white", bd=2, relief="ridge")
        table_frame.place(x=5, y=5, width=590, height=400)
        
        # Create the scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

        # Create the Treeview
        self.Attendance_table = ttk.Treeview(
            table_frame,
            columns=("Student Id", "Roll No", "Name", "Course", "Time", "Date", "Attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        
        # Configure the scrollbars
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)
        
        # Define the column headings
        self.Attendance_table.heading("Student Id", text="Student Id")
        self.Attendance_table.heading("Roll No", text="Roll No")
        self.Attendance_table.heading("Name", text="Name")
        self.Attendance_table.heading("Course", text="Course")
        self.Attendance_table.heading("Time", text="Time")
        self.Attendance_table.heading("Date", text="Date")
        self.Attendance_table.heading("Attendance", text="Attendance")
    
        self.Attendance_table.column("Student Id", width=100)
        self.Attendance_table.column("Roll No", width=100)
        self.Attendance_table.column("Name", width=100)
        self.Attendance_table.column("Course", width=100)
        self.Attendance_table.column("Time", width=100)
        self.Attendance_table.column("Date", width=100)
        self.Attendance_table.column("Attendance", width=100)
        
        self.Attendance_table["show"] = "headings"
        
        self.Attendance_table.pack(fill="both", expand=1)
        
        self.Attendance_table.bind("<ButtonRelease-1>", self.get_cursor)

    def fetchData(self, rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("", "end", values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        
        if not fln:
            return  # User canceled the file dialog
        
        with open(fln, newline='') as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            mydata = list(csvread)  # Read all data into mydata
            
        self.fetchData(mydata)
    
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to export", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                defaultextension=".csv",
                filetypes=(("CSV", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            
            if not fln:
                return  # User canceled the save dialog
            
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                
            messagebox.showinfo("Data Export", f"Your data has been exported to {os.path.basename(fln)} successfully.",parent=self.root)
        
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    def get_cursor(self, event):
        cursor_row = self.Attendance_table.focus()
        if not cursor_row:
            print("No item selected")
            return
        
        content = self.Attendance_table.item(cursor_row)
        if "values" not in content:
            print("No values found in the selected item")
            return
        
        row = content["values"]
        if len(row) >= 7:
            self.var_atten_std_id.set(row[0])
            self.var_atten_name.set(row[1])
            self.var_atten_roll.set(row[2])
            self.var_atten_course.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_attendance.set(row[6])
        else:
            print("Row data does not contain enough elements")
            
            
    #reset
    def reset_data(self):
         self.var_atten_std_id.set("")
         self.var_atten_name.set("")
         self.var_atten_roll.set("")
         self.var_atten_course.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance.set("")
        

        
       
        
if __name__ == "__main__":
     root = Tk()
     app = Attendance(root)  # 'app' is a better name than 'object' which is a reserved word
     root.mainloop()
        
        