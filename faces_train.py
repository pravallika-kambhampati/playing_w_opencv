import os 
import cv2 as cv
import numpy as np

people = []

people = ['Ben Afflek','Elton John', 'Jerry Seinfield', 'Madonna','Mindy Kaling']
DIR = r'/Users/pravallika/Desktop/OpenCV/playing_w_opencv/Resources/Faces/train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []
def create_train_data():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_Rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_Rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train_data()
print('Training data is now available....')

features = np.array(features, dtype=object)
labels = np.array(labels)

# Create an instance of opencv's inbuilt face recognizer model 
face_recognizer = cv.face.LBPHFaceRecognizer_create()

print('Training the model on the training data....')

# train the recognizer on the features list and labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_recognizer_model.yml')

print('Training finished...')
print('Face recognizer model is now available..')
np.save('features.npy', features)
np.save('labels.npy',labels) 

            




