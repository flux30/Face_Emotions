Emotion Detection System
Overview
This project is a real-time emotion detection system that uses a webcam to detect faces and predict emotions. It utilizes a pre-trained deep learning model to classify emotions into one of seven categories: Angry, Disgust, Fear, Happy, Neutral, Sad, or Surprise.

Features
Real-time face detection using Haar Cascade classifier

Emotion prediction using a pre-trained Keras model

Simple and intuitive interface

Displays emotion labels directly on the video feed

Requirements
Python 3.x

OpenCV

TensorFlow

Keras

NumPy

Installation
Clone this repository

Install the required packages:

bash
pip install -r requirements.txt
Usage
Run the main script:

bash
python main.py
The application will open your webcam and start detecting faces and emotions

Press 'q' to quit the application

File Structure
main.py: Main application script

model.h5: Pre-trained emotion detection model

haarcascade_frontalface_default.xml: Haar Cascade classifier for face detection

requirements.txt: List of required Python packages

Notes
Make sure the paths to model.h5 and haarcascade_frontalface_default.xml in the code match their actual locations in your system

The application works best with good lighting conditions and clear frontal face views

Performance may vary depending on your hardware configuration

License
This project is open-source and available for personal and educational use. For commercial use, please contact the author.

Acknowledgments
Uses OpenCV's Haar Cascade classifier for face detection

Emotion detection model trained on FER-2013 dataset
