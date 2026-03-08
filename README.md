AI Emotion Detection System

A real-time emotion detection system built using Python, OpenCV, DeepFace, and CustomTkinter. The application captures live webcam video, detects human faces, and analyzes facial expressions to identify emotions such as happy, sad, angry, and neutral.

The system includes a graphical interface that allows users to start and stop the webcam while displaying emotion predictions with confidence scores.

Features

-Real-time emotion detection using webcam

-Face detection with Haar Cascade classifier

-Emotion recognition using DeepFace

-Graphical user interface built with CustomTkinter

-Display of detected emotion with confidence score

-Start and stop camera controls

Technologies Used

--Python

--OpenCV

--DeepFace

--CustomTkinter

--Pillow (PIL)

--NumPy

Project Structure
AI_Emotion_Detection_System
│
└── main.py
Installation

Clone the repository:

git clone https://github.com/Yashdot2005/AI_Emotion_Detection_System.git

Go to the project folder:

cd AI_Emotion_Detection_System

Install the required libraries:

pip install customtkinter opencv-python pillow deepface numpy
Running the Application

Run the program using:

python main.py

Steps to use the system:

Launch the application.

Click Start Camera to begin emotion detection.

The system detects faces and analyzes emotions in real time.

Click Stop Camera to stop the webcam.

How It Works

The webcam captures live video frames.

OpenCV detects faces using the Haar Cascade classifier.

Each detected face is analyzed using the DeepFace emotion recognition model.

The dominant emotion and confidence score are displayed in the interface.

Author

Yash Ghotekar  
Computer Science Engineering Student  
Interested in Artificial Intelligence and Machine Learning  
GitHub: https://github.com/Yashdot2005
