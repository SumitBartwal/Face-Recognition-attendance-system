import cv2
import mysql.connector
from PIL import Image, ImageTk
from tkinter import LabelFrame, Tk, Label, Button
import tkinter as tk
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("About Developer")
        self.root.wm_iconbitmap("face icon.ico")

       
       
        
        
        title_lbl = Label( text="FACE RECOGNITION ATTENDENCE SYSTEM PROGRAM", font=("times new roman", 30, "bold"), bg="black", fg="white")
        title_lbl.place(x=20, y=0, width=1200, height=40)
        
        right_frame=LabelFrame(self.root,bg="light blue",fg="dark green",bd=2,relief="ridge",text="About Developer",font=("times new roman",20,"bold"))
        right_frame.place(x=20,y=40,width=1200,height=660)
        
        info_frame=Label(self.root,bg="indigo",fg="white",text="Program made by\n\nSumit Bartwal\nBca 1st year\n and \nJeevan Rana \nBca 1st year",font=("times new roman",20,"bold"))
        info_frame.place(x=300,y=100,width=600,height=500)
        
        
        
         
        
        

if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()        