Emotion Detection System 👁️😊😠😲
==================================

A real-time emotion detection system that identifies facial expressions using your webcam and classifies them into 7 basic emotions.

✨ Features
----------

*   Real-time face detection using Haar Cascade
*   Emotion classification (7 categories)
*   Clean visualization with bounding boxes and labels
*   Lightweight and easy to use
*   Cross-platform compatibility

🛠️ Installation
----------------

### Prerequisites

*   Python 3.7 or higher
*   pip package manager

### Steps

1.  **Clone the repository**  
    
        git clone https://github.com/yourusername/face-emotion-detection.git
        cd face-emotion-detection
    
2.  **Install dependencies**  
    
        pip install -r requirements.txt
    
3.  **Download model files**  
    Ensure `model.h5` and `haarcascade_frontalface_default.xml` are in the project directory.

🚀 Usage
--------

Run the emotion detection system:

    python main.py

### Controls

*   Press **Q** key to quit the application
*   Ensure proper lighting conditions
*   Face the camera directly for best results  

🧠 Technical Details
--------------------

### Model Specifications

*   **Input:** 48×48 pixel grayscale images
*   **Output:** 7 emotion classes
*   **Architecture:** Convolutional Neural Network (CNN)

⚠️ Requirements
---------------

*   Python 3.7+
*   OpenCV 4.x (`opencv-python`)
*   TensorFlow 2.x
*   Keras 2.x
*   NumPy

📝 Notes
--------

*   For best results, ensure good lighting conditions
*   The system works best with frontal faces
*   Performance depends on your hardware capabilities
*   Model accuracy may vary with different facial orientations

🤝 Contributing
---------------

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
