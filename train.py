from tkinter import Button, Label, Tk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import re  # Import regular expression module

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face icon.ico")

        # Title
        title_lbl = Label(self.root, text="TRAIN DATA", font=("times new roman", 30, "bold"), bg="dark green", fg="white")
        title_lbl.place(x=5, y=0, width=1260, height=50)

        # Image top
        img2 = Image.open(r"Images of interface page\face-detection.webp")
        img2 = img2.resize((1300, 290), Image.LANCZOS)    
        self.photoimg2 = ImageTk.PhotoImage(img2)  
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=50, width=1300, height=290)

        # Button
        b1 = Button(self.root, command=self.train_classifier, text="Train Classifier", font=("times new roman", 30, "bold"), bg="red", fg="white", cursor="hand2")
        b1.place(x=0, y=340, width=1290, height=50)

        # Image bottom
        img1 = Image.open(r"Images of interface page\images (12).jpeg")
        img1 = img1.resize((1300, 290), Image.LANCZOS)    
        self.photoimg1 = ImageTk.PhotoImage(img1)  
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=390, width=1300, height=290)
      
    def train_classifier(self):
        data_dir = "data"
        
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"The directory '{data_dir}' does not exist.")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]

        if not path:
            messagebox.showerror("Error", "No image files found in the 'data' directory.")
            return

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert("L")  # Convert to grayscale
                imageNp = np.array(img, 'uint8')

                # Extract numeric ID from the filename using regex
                filename = os.path.split(image)[1]
                match = re.search(r'(\d+)', filename)  # Search for one or more digits anywhere in the filename
                
                if not match:
                    messagebox.showwarning("Warning", f"Filename '{filename}' does not contain a numeric ID. Skipping this file.")
                    continue
                
                id_str = match.group(1)  # Get the first matched group of digits
                id = int(id_str)  # Convert to integer

                faces.append(imageNp)
                ids.append(id)

                # Debug: Display the image being processed
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while processing file '{filename}': {str(e)}")

        if not faces:
            messagebox.showerror("Error", "No valid images to train. Ensure all filenames contain numeric IDs.")
            return

        ids = np.array(ids)

        try:
            # Initialize the LBPH face recognizer
            clf = cv2.face.LBPHFaceRecognizer_create()  # Ensure this method exists in your OpenCV version
            # Train the recognizer
            clf.train(faces, ids)
            # Save the trained model
            clf.write("classifier.xml")
            messagebox.showinfo("Result", "Training datasets completed successfully!", parent=self.root)
        except cv2.error as e:
            messagebox.showerror("Error", f"OpenCV error occurred: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
