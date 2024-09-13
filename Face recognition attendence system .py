import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
import os

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face icon.ico")

        # Load and resize images
        self.load_and_place_images()

        # Title name
        title_lbl = tk.Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM PROGRAM", font=("times new roman", 30, "bold"), bg="black", fg="white")
        title_lbl.place(x=20, y=130, width=1200, height=40)

        # Buttons
        self.create_buttons()

    def load_and_place_images(self):
        images = [
            ("Images of interface page\\images (1).jpeg", 0, 0, 500, 130),
            ("Images of interface page\\images (12).jpeg", 400, 0, 500, 130),
            ("Images of interface page\\images (8).jpeg", 900, 0, 500, 130),
            ("Images of interface page\\images (13).jpeg", 0, 130, 1300, 570)
        ]
        for img_path, x, y, w, h in images:
            img = Image.open(img_path)
            img = img.resize((w, h), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=photoimg).place(x=x, y=y, width=w, height=h)
            # Keep a reference to avoid garbage collection
            self.__dict__[f"photoimg_{x}_{y}"] = photoimg

    def create_buttons(self):
        buttons = [
            ("Images of interface page\\images (15).jpeg", "Student details", self.student_details, 150, 200),
            ("Images of interface page\\images (6).jpeg", "Face Detection", self.face_data, 400, 200),
            ("Images of interface page\\images (14).jpeg", "Attendance", self.attendance_data, 650, 200),
            ("Images of interface page\\images (4).jpeg", "Train Data", self.train_data, 150, 400),
            ("Images of interface page\\images (0).png", "Photos", self.open_img, 400, 400),
            ("Images of interface page\\images (3).jpeg", "About Developer", self.developer_data, 650, 400),
            ("Images of interface page\\images (16).jpeg", "Exit", self.iexit, 900, 400)
        ]
        for img_path, text, command, x, y in buttons:
            img = Image.open(img_path)
            img = img.resize((150, 150), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)
            tk.Button(self.root, image=photoimg, command=command, cursor="hand2").place(x=x, y=y, width=150, height=150)
            if text:
                tk.Button(self.root, text=text, command=command, font="Forte", bg="dark blue", fg="white", cursor="hand2").place(x=x, y=y + 150, width=150, height=35)
            # Keep a reference to avoid garbage collection
            self.__dict__[f"photoimg_button_{x}_{y}"] = photoimg

    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.open_new_window(Student)

    def train_data(self):
        self.open_new_window(Train)

    def face_data(self):
        self.open_new_window(Face_Recognition)

    def attendance_data(self):
        self.open_new_window(Attendance)
        
    def developer_data(self):
        self.open_new_window(Developer)

    def open_new_window(self, class_ref):
        new_window = tk.Toplevel(self.root)
        class_ref(new_window)

    def iexit(self):
        # Ask the user if they really want to exit
        confirm_exit = messagebox.askyesno("Exit", "Do you really want to exit?", parent=self.root)
        if confirm_exit:  # If the user clicked "Yes"
          self.root.destroy()  # Close the window

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
