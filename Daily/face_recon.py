"""
Uhh made by 5quirre1

Use it ig I don't give a fuck LMFAO

3/6/25 6:22 PM
"""


import os
try:
    import cv2
    import tkinter as tk
    from tkinter import messagebox
    from PIL import Image, ImageTk
    import numpy as np
    from sklearn.preprocessing import LabelEncoder
except ImportError:
    os.system("pip install opencv-python pillow numpy scikit-learn")
    import cv2
    import tkinter as tk
    from tkinter import messagebox
    from PIL import Image, ImageTk
    import numpy as np
    from sklearn.preprocessing import LabelEncoder

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face or smth")
        self.root.geometry("1200x900")
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            messagebox.showerror("Error", "could no camera..")
            self.root.quit()
            return

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame)
        self.label.grid(row=0, column=0, sticky="nsew")

        self.name_label = tk.Label(self.root, text="Enter name to associate with face:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.capture_button = tk.Button(self.root, text="Capture Face", command=self.capture_face)
        self.capture_button.pack()

        self.train_button = tk.Button(self.root, text="Train Recognizer", command=self.train_recognizer)
        self.train_button.pack()

        self.faces_data = []
        self.face_names = []
        self.face_counter = 0
        self.recognizer_trained = False

        self.detect_faces()

    def capture_face(self):
        name = self.name_entry.get()
        if name == "":
            messagebox.showwarning("Input Error", "have a name")
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            self.faces_data.append(face)
            self.face_names.append(name)
            self.face_counter += 1

            messagebox.showinfo("Success", f"Face captured for {name}. Total faces captured: {self.face_counter}")

        if self.face_counter >= 20:
            self.train_recognizer()

    def train_recognizer(self):
        if len(self.faces_data) == 0:
            messagebox.showwarning("Training Error", "no faces captured")
            return
        
        label_encoder = LabelEncoder()
        labels = label_encoder.fit_transform(self.face_names)

        self.face_recognizer.train(self.faces_data, np.array(labels))
        self.recognizer_trained = True
        messagebox.showinfo("Training Complete", "training complete, yay")

    def detect_faces(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if self.recognizer_trained:
                    face = gray[y:y+h, x:x+w]
                    label, confidence = self.face_recognizer.predict(face)

                    if confidence > 100:
                        name = "Unknown"
                    else:
                        name = self.face_names[label]

                    cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img = ImageTk.PhotoImage(img)

            self.label.config(image=img)
            self.label.image = img

            self.root.update_idletasks()
            self.root.update()

        self.cap.release()

    def close_window(self):
        if self.cap is not None:
            self.cap.release()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_window)
    root.mainloop()
    
