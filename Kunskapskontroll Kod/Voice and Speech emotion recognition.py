import numpy as np
import tensorflow as tf
import librosa
import librosa.display
import sounddevice as sd

def spela_in():
    ## Spela in ljud och omvandla till MFCC för att använda i modellen

    duration = 3  # Längd på inspelningen i sekunder
    fs = 44100  # Samplingsfrekvens, standard för mikrofoner

    # Starta inspelningen
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Vänta tills inspelningen är klar

    # Beräkna MFCC (Melspektrogram-baserad frekvensanalys)
    mfcc = np.mean(librosa.feature.mfcc(y=recording[:, 0], sr=fs, n_mfcc=40).T, axis=0)
    X = np.array(mfcc)
    X = np.expand_dims(X, -1)
    X = np.expand_dims(X, axis=0)

    return X

from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import keras

### Ladda modellen för röst- och ansiktsigenkänning

face_classifier = cv2.CascadeClassifier(r'C:\Users\leona\EC-Data science\Deep learning\Emotion_Detection_CNN-main\haarcascade_frontalface_default.xml')
classifier = load_model(r'C:\Users\leona\EC-Data science\Deep learning\Deep-Learning-master\Deep-Learning-master\fn.tf')  # Modellens sökväg
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad']

cap = cv2.VideoCapture(0)  # Starta webbkamera

while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konvertera till gråskala för ansiktsdetektion
    faces = face_classifier.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)  # Rita rektangel runt detekterat ansikte
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            audio = spela_in()  # Spela in ljud och omvandla till MFCC
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # Förutsäg emotion baserat på ansikte och ljud
            prediction = classifier.predict([roi, audio])[0]
            label = emotion_labels[prediction.argmax()]
            label_position = (x, y-10)
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Emotion Detector', frame)  # Visa resultat
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Avsluta om 'q' trycks
        break

cap.release()
cv2.destroyAllWindows()
