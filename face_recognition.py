import cv2
import mysql.connector
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
import tkinter as tk
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face icon.ico")

        
        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="black", fg="white")
        title_lbl.place(x=25, y=0, width=1200, height=50)
        
        # Image
        img2 = Image.open(r"Images of interface page\iron-man-inside-2.webp")
        img2 = img2.resize((1300, 640), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=55, width=1300, height=640)
        
        # Button
        img4 = Image.open(r"Images of interface page\images (3).jpeg")
        img4 = img4.resize((150, 150), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(self.root, image=self.photoimg4, cursor="hand2", command=self.face_recog)
        b1.place(x=600, y=240, width=150, height=150)

        b1_1 = Button(self.root, text="Face Recognition", font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.face_recog)
        b1_1.place(x=600, y=370, width=150, height=35)
        
    # Attendance 
    def mark_attendance(self, i, r, n, c):
        with open(r"Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",") 
                name_list.append(entry[0])
          
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S") 
                f.writelines(f"\n{i},{r},{n},{c},{dtstring},{d1},Present")  
    
    # Face recognition    
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="sumit@12345",
                    database="face_recognization_student"
                )
                my_cursor = conn.cursor()
                
                try:
                    # Correct SQL Query with parameterized inputs
                    my_cursor.execute("SELECT `Name` FROM `student` WHERE `Student Id` = %s", (id,))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n else "Unknown"
                    
                    my_cursor.execute("SELECT `Roll No` FROM `student` WHERE `Student Id` = %s", (id,))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r else "Unknown"
                    
                    my_cursor.execute("SELECT `Course` FROM `student` WHERE `Student Id` = %s", (id,))
                    c = my_cursor.fetchone()
                    c = "+".join(c) if c else "Unknown"
                    
                    my_cursor.execute("SELECT `Student Id` FROM `student` WHERE `Student Id` = %s", (id,))
                    i = my_cursor.fetchone()
                    i = "+".join(i) if i else "Unknown"
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                finally:
                    conn.close()
                
                if confidence > 60:
                    cv2.putText(img, f"Student Id:{i}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 3)
                    cv2.putText(img, f"Roll No:{r}", (x, y - 49), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 3)
                    cv2.putText(img, f"Course:{c}", (x, y ), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0,), 3)
                    self.mark_attendance(i, r, n, c)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                coord = [x, y, w, h]
                
            return coord
        
        def recognize(img, clf, faceCascade):
            # Resize the frame to a desired width and height
            desired_width = 800  # Adjust as needed
            desired_height = 600  # Adjust as needed
            img = cv2.resize(img, (desired_width, desired_height))
            
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()  # Correct method
        try:
            clf.read("classifier.xml")
        except cv2.error as e:
            print(f"Error loading classifier: {e}")
        
        video_cap = cv2.VideoCapture(1)
        
        if not video_cap.isOpened():
            print("Error: Could not open video capture.")
            return
        
        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1) == 13:  # Enter key
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
