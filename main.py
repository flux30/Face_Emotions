from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'C:\Users\bijay\Documents\face_emotions\haarcascade_frontalface_default.xml') #object-detection in images
classifier = load_model(r'C:\Users\bijay\Documents\face_emotions\model.h5') #pre-trained model for emotion detection

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise'] #default camera

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #loop to continuously capture the frame
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #grayscale
    faces = face_classifier.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2) #rectangle around the detected face
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA) #captures roi and resizes into 48*48

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            prediction = classifier.predict(roi)[0]
            label = emotion_labels[prediction.argmax()]
            label_position = (x, y)
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) #makes prediction using pre trained model

    cv2.imshow('Emotion Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
