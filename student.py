from msilib import add_data
from tkinter import END, W, Button, Entry, Frame, Grid, Label, LabelFrame, Place, StringVar, Tk, messagebox, ttk
import tkinter
from PIL import Image, ImageTk
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Student")
        self.root.wm_iconbitmap("face icon.ico")

        
        
         
        #variables
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_dep=StringVar()
       
    
    
    
    

       



         #first image
        img = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\images (2).jpeg")
        img = img.resize((500, 130), Image.LANCZOS)    
        self.photoimg = ImageTk.PhotoImage(img)  

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)  # Corrected height parameter


        #second image
        img1 = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\images 1.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)    
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=500, height=130)
        
        
        #third image
        img2 = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page/images (7).jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)    
        self.photoimg2 = ImageTk.PhotoImage(img2)  

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=500, height=130)


         #background image
        img3 = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\images (13).jpeg")
        img3 = img3.resize((1300, 700), Image.LANCZOS)    
        self.photoimg3 = ImageTk.PhotoImage(img3)  


        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1300, height=570)


         #title name
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=20,y=0,width= 1200,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1300,height=600)

        #left rabel frame

        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief="ridge",text="Student Details",font=("times new roman",10,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=470)

        #image
        img_left = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\image 3.webp")
        img_left = img_left.resize((550, 90), Image.LANCZOS)    
        self.photoimg_left = ImageTk.PhotoImage(img_left)  

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=20, y=0, width=550, height=90)


        #Current course

        current_course_frame=LabelFrame(Left_frame,bg="white",bd=2,relief="ridge",text="Current Course Information",font=("times new roman",10,"bold"))
        current_course_frame.place(x=20,y=90,width=550,height=120)


        

        
        # department
        dep_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=8,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=12,state="readonly")
        dep_combo["values"]=("Select Department","Tech","Bussiness","Education","Law")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=2,padx=2,pady=8,sticky=W)

          # course
        course_label=Label(current_course_frame,text="COURSE",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=3,padx=8,sticky=W)


        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=12,state="readonly")
        course_combo["values"]=("Select Course","BCA","B-TECH","BE","LLB","BBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=4,padx=2,pady=8,sticky=W)

         # YEAR
        year_label=Label(current_course_frame,text="YEAR",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=8,sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=12,state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=2,padx=2,pady=8,sticky=W)

          # SEMESTER
        semester_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=3,padx=8,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",10,"bold"),width=12,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=4,padx=2,pady=8,sticky=W)



        #class student information
        class_student_frame=LabelFrame(Left_frame,bg="white",bd=2,relief="ridge",text="Class Student Information",font=("times new roman",10,"bold"))
        class_student_frame.place(x=20,y=220,width=550,height=230)


         
        #student name
        studentName_label=Label(class_student_frame,text="Name",font=("times new roman",10,"bold"),bg="white")
        studentName_label.grid(row=0,column=0,padx=8,pady=3,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=15,font=("times new roman",10,"bold"))
        studentName_entry.grid(row=0,column=1,padx=8,pady=3,sticky=W)

        #student id
        studentId_label=Label(class_student_frame,text="Student Id",font=("times new roman",10,"bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=8,pady=3,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",10,"bold"))
        studentId_entry.grid(row=0,column=3,padx=8,pady=3,sticky=W)



        #Class division
        Class_Div_label=Label(class_student_frame,text="Class Division",font=("times new roman",10,"bold"),bg="white")
        Class_Div_label.grid(row=1,column=0,padx=8,pady=3,sticky=W)

        # Class_Div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div_name,width=15,font=("times new roman",10,"bold"))
        # Class_Div_entry.grid(row=1,column=1,padx=8,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),width=12,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=8,pady=3,sticky=W)


        #Roll number
        Roll_NO_label=Label(class_student_frame,text="Roll No.",font=("times new roman",10,"bold"),bg="white")
        Roll_NO_label.grid(row=1,column=2,padx=8,pady=3,sticky=W)

        Roll_NO_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("times new roman",10,"bold"))
        Roll_NO_entry.grid(row=1,column=3,padx=8,sticky=W)

        #Gender
        Gender_label=Label(class_student_frame,text="Gender",font=("times new roman",10,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=8,pady=3,sticky=W)

        # Gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=15,font=("times new roman",10,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=8,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=12,state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=8,pady=3,sticky=W)


         #Date Of Birth
        dob_label=Label(class_student_frame,text="Date Of Birth",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=8,pady=3,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=15,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=8,sticky=W)

         #Email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=8,pady=3,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=8,sticky=W)


        #phone number
        phone_label=Label(class_student_frame,text="Phone Number",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=8,pady=3,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=8,sticky=W)

         #address
        address_label=Label(class_student_frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=8,pady=3,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=8,sticky=W)

         #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=8,pady=3,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=4,column=3,padx=8,sticky=W)

        #Radio Buttons
        
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0,)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="no")
        radiobtn2.grid(row=6,column=1)


        #button frame
        btn_frame=Frame(class_student_frame,bg="white",bd=2,relief="ridge")
        btn_frame.place(x=3,y=160,width=540,height=52)

        #save button
        save_button=Button(btn_frame,command=self.add_data,text="Save",width=15,height=1,font=("times new roman",10,"bold"),bg="black",fg="white")
        save_button.grid(row=0,column=0,padx=4)

        #update button
        update_button=Button(btn_frame,command=self.update_data,text="Update",width=15,height=1,font=("times new roman",10,"bold"),bg="dark green",fg="white")
        update_button.grid(row=0,column=1,padx=4)

        #delete button
        delete_button=Button(btn_frame,command=self.delete_data,text="Delete",width=15,height=1,font=("times new roman",10,"bold"),bg="red",fg="white")
        delete_button.grid(row=0,column=2,padx=4)

        #reset button
        reset_button=Button(btn_frame,command=self.reset_data,text="Reset",width=15,height=1,font=("times new roman",10,"bold"),bg="dark blue",fg="white")
        reset_button.grid(row=0,column=3,padx=4)

         #button frame
        btn_frame=Frame(class_student_frame,bg="white",bd=2,relief="ridge")
        btn_frame.place(x=3,y=188,width=540,height=25)

        #take photo sample
        takePhoto_button=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",10,"bold"),bg="orange",fg="white")
        takePhoto_button.grid(row=1,column=0,padx=10)

        #update photo sample
        update_button=Button(btn_frame,text="Update Photo Sample",width=30,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_button.grid(row=1,column=1,padx=10)


        

        #right rabel frame

        right_frame=LabelFrame(main_frame,bg="white",bd=2,relief="ridge",text="Student Details",font=("times new roman",10,"bold"))
        right_frame.place(x=650,y=10,width=600,height=470)

        #image
        img_right = Image.open(r"C:\Users\lenovo\Desktop\face Recognization System\Images of interface page\images (3).jpeg")
        img_right = img_right.resize((580, 90), Image.LANCZOS)    
        self.photoimg_right = ImageTk.PhotoImage(img_right)  

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=580, height=90)

        # =======search system=========
        Search_frame=LabelFrame(right_frame,bg="white",bd=2,relief="ridge",text="Serch System",font=("times new roman",10,"bold"))
        Search_frame.place(x=20,y=90,width=550,height=60)

         #search label
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=8,pady=1,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",10,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=12,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=8,sticky=W)



       #search button
        search_button=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=3)

        #show all button
        showAll_button=Button(Search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_button.grid(row=0,column=4,padx=3)

        #=======Table frame==========
       

        # Create the table frame
        table_frame = Frame(right_frame, bg="white", bd=2, relief="ridge")
        table_frame.place(x=20, y=160, width=550, height=290)

        # Create the scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

        # Create the Treeiew

        self.student_table=ttk.Treeview(table_frame,columns=(
                "Department", "Course", "Year", "Semester", "Student Id", "Name", "Division", "Roll No.",
                "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "PhotoSample"
            ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)


                  # Configure the scrollbars
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

                  # Define the column headings
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student Id", text="Student Id")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Roll No.", text="Roll No.")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("PhotoSample", text="PhotoSample")

                  # Set the display mode
        self.student_table["show"] = "headings"
        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Student Id", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("Roll No.", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("PhotoSample", width=120)

                  # Pack the Treeview into the frame
        self.student_table.pack(fill="both",expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
     # save button   
    #function declration
    def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_id.get()== "" or self.var_name.get()== "" or self.var_course=="" or self.var_roll=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
       

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="sumit@12345",
                database="face_recognization_student"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO student  "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()  # Assuming `var_radio1` represents the `photosample` field
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
          

            messagebox.showinfo("Success","Student details added successfully",parent=self.root)  
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
     #fetch data
    def fetch_data(self): 
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="sumit@12345",
                database="face_recognization_student"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            
            if len(data) !=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                  self.student_table.insert("",END,values=i)
                  
                  conn.commit()
              conn.close()
              #get cursor
    def get_cursor(self,event=""):
              cursor_focus=self.student_table.focus()
              content=self.student_table.item(cursor_focus)
              data=content["values"]
              
              self.var_dep.set(data[0])
              self.var_course.set(data[1])
              self.var_year.set(data[2])
              self.var_sem.set(data[3])
              self.var_std_id.set(data[4])
              self.var_name.set(data[5])
              self.var_div.set(data[6])
              self.var_roll.set(data[7])
              self.var_gender.set(data[8])
              self.var_dob.set(data[9])
              self.var_email.set(data[10])
              self.var_phone.set(data[11])
              self.var_address.set(data[12])
              self.var_teacher.set(data[13])
              self.var_radio1.set(data[14])
              
            #update function
    def update_data(self):
      # Check if required fields are filled
      if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_name.get() == "":
          messagebox.showerror("Error", "All fields are required", parent=self.root)
          return
      
      # Ask for confirmation before updating
      Update = messagebox.askyesno("Update", "Do you really want to update student details?", parent=self.root)
      
      if Update:
          try:
              # Connect to the MySQL database
              conn = mysql.connector.connect(
                  host="localhost",
                  user="root",  # Use 'user' instead of 'username'
                  password="sumit@12345",
                  database="face_recognization_student"
              )
              my_cursor = conn.cursor()

              # Correct SQL UPDATE statement with backticks around column names
              sql_update_query = """
              UPDATE student
              SET `Department` = %s, `Course` = %s, `Year` = %s, `Semester` = %s, `Name` = %s, `Division` = %s,
                  `Roll No` = %s, `Gender` = %s, `DOB` = %s, `Email` = %s, `Phone` = %s, `Address` = %s,
                  `Teacher` = %s, `PhotoSample` = %s
              WHERE `Student Id` = %s
              """

              # Execute the query with the actual values
              my_cursor.execute(sql_update_query, (
                  self.var_dep.get(),
                  self.var_course.get(),
                  self.var_year.get(),
                  self.var_sem.get(),
                  self.var_name.get(),
                  self.var_div.get(),
                  self.var_roll.get(),
                  self.var_gender.get(),
                  self.var_dob.get(),
                  self.var_email.get(),
                  self.var_phone.get(),
                  self.var_address.get(),
                  self.var_teacher.get(),
                  self.var_radio1.get(), 
                  self.var_std_id.get()   # This is the condition to specify which row to update
              ))

              # Commit changes and close the connection
              conn.commit()
              conn.close()
              
              # Show success message and fetch updated data
              messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
              self.fetch_data()
          except Exception as es:
              # Show error message with detailed exception
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
    #delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)  
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you realy want to delete student details",parent=self.root)
                if delete>0: 
                  conn = mysql.connector.connect(
                  host="localhost",
                  user="root",  # Use 'user' instead of 'username'
                  password="sumit@12345",
                  database="face_recognization_student"
              )
                  my_cursor = conn.cursor()
                  sql="delete FROM student  WHERE `Student Id` = %s"
                  val=(self.var_std_id.get(),)   
                  my_cursor.execute(sql,val) 
                else:
                  if not delete:
                    return
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Delete","Student Id successfully deleted from system",parent=self.root)    
            except Exception as es:
             
              messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)      
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
   # generate data set take photo samples
   
   
    def generate_dataset(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
            return
        
        student_id = self.var_std_id.get()

        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sumit@12345",
                database="face_recognization_student"
            )
            my_cursor = conn.cursor()
            
            # Update student data
            sql_update_query = """
                UPDATE student
                SET `Department` = %s, `Course` = %s, `Year` = %s, `Semester` = %s, `Name` = %s, `Division` = %s,
                    `Roll No` = %s, `Gender` = %s, `DOB` = %s, `Email` = %s, `Phone` = %s, `Address` = %s,
                    `Teacher` = %s, `PhotoSample` = %s
                WHERE `Student Id` = %s
            """
            
            # Execute the update query
            my_cursor.execute(sql_update_query, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                student_id  # Use the student ID to specify which row to update
            ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Load predefined data on face frontal from OpenCV
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def _face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y+h, x:x+w]
                    return face_cropped
                return None  # Return None if no face is detected

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if _face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(_face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Fixed typo here
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                
                if cv2.waitKey(1) == 13 or img_id >= 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data sets completed!!")

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    
        


                    
                  
              
           
                 
                


      




if __name__ == "__main__":
     root = Tk()
     app = Student(root)  # 'app' is a better name than 'object' which is a reserved word
     root.mainloop()



