import customtkinter as ctk
import cv2
from deepface import DeepFace
from PIL import Image, ImageTk
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class EmotionApp:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Emotion Detector")
        self.root.geometry("900x650")

        self.cap = None
        self.running = False

        # Title
        self.title = ctk.CTkLabel(root, text="Real-Time Emotion Detection", 
                                  font=("Arial", 26, "bold"))
        self.title.pack(pady=15)

        # Video Frame
        self.video_label = ctk.CTkLabel(root, text="")
        self.video_label.pack(pady=10)

        # Status Label
        self.status = ctk.CTkLabel(root, text="Status: Camera Off",
                                   font=("Arial", 16))
        self.status.pack(pady=10)

        # Buttons
        self.btn_frame = ctk.CTkFrame(root)
        self.btn_frame.pack(pady=20)

        self.start_btn = ctk.CTkButton(self.btn_frame,
                                       text="Start Camera",
                                       command=self.start_camera,
                                       width=150)
        self.start_btn.grid(row=0, column=0, padx=20)

        self.stop_btn = ctk.CTkButton(self.btn_frame,
                                      text="Stop Camera",
                                      command=self.stop_camera,
                                      width=150)
        self.stop_btn.grid(row=0, column=1, padx=20)

        # Face detector
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def start_camera(self):
        if not self.running:
            self.cap = cv2.VideoCapture(0)
            self.running = True
            self.status.configure(text="Status: Camera Running")
            threading.Thread(target=self.update_frame).start()

    def stop_camera(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.status.configure(text="Status: Camera Off")

    def update_frame(self):

        while self.running:

            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:

                face_img = frame[y:y+h, x:x+w]

                try:
                    result = DeepFace.analyze(
                        face_img,
                        actions=['emotion'],
                        enforce_detection=False
                    )

                    emotion = result[0]['dominant_emotion']
                    confidence = result[0]['emotion'][emotion]

                except:
                    emotion = "neutral"
                    confidence = 0

                # Color + emoji
                if emotion == "happy":
                    color = (0,255,0)
                    emoji = "😄"
                elif emotion == "sad":
                    color = (255,0,0)
                    emoji = "😢"
                elif emotion == "angry":
                    color = (0,0,255)
                    emoji = "😠"
                else:
                    color = (0,255,255)
                    emoji = "😐"

                cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)

                label = f"{emotion.upper()} {confidence:.1f}% {emoji}"

                cv2.putText(frame,
                            label,
                            (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            color,
                            2)

            # Convert image for Tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        if self.cap:
            self.cap.release()

# Run App
root = ctk.CTk()
app = EmotionApp(root)
root.mainloop()