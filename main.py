from keras.models import model_from_json
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

import cv2 as cv
import serial
import time
import numpy

#port ='COM9'
#ser = serial.Serial(port, 9600)

ca = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX

loaded_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

def __draw_label(img, text, pos, bg_color):
    font_face = cv.FONT_HERSHEY_SIMPLEX
    scale = 3
    color = (0, 0, 0)
    thickness = cv.FILLED
    margin = 2

    txt_size = cv.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    #cv.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv.putText(img, text, pos, font_face, scale, bg_color, 1, cv.LINE_AA)


while(1):
    re, img = ca.read()
    
    fram = cv.resize(img, (240, 240))
    
    fram = cv.cvtColor(fram, cv.COLOR_BGR2GRAY)
    
    cv.imshow('Preprocessing',fram)
    
    fram = numpy.reshape(fram,[1,240,240,1])

    classes = loaded_model.predict_classes(fram)
    
    if(classes==[0]):
        #ser.write(b'0')
        #cv.putText(img,'Forward',(120,120), font, 18,(220,20,60),2,cv.LINE_AA)
        __draw_label(img, 'Forward', (20,80), (0,0,255))
        cv.imshow('Classification',img)
        print('forward')
        
    if(classes==[1]):
        #ser.write(b'1')
        print('hold')
        #cv.putText(img,'Hold',(120,120), font, 18,(220,20,60),2,cv.LINE_AA)
        __draw_label(img, 'Hold', (20,80), (0,0,255))
        cv.imshow('Classification',img)
    
    if(classes==[2]):
        #ser.write(b'2')
        print('left')
        #cv.putText(img,'Left',(120,120), font, 18,(220,20,60),2,cv.LINE_AA)
        __draw_label(img, 'Left', (20,80), (0,0,255))
        cv.imshow('Classification',img)
        
    if(classes==[3]):
        #ser.write(b'3')
        print('right')
        #cv.putText(img,'Right',(120,120), font, 18,(220,20,60),2,cv.LINE_AA)
        __draw_label(img, 'Right', (20,80), (0,0,255))
        cv.imshow('Classification',img)
    
    print(classes)
    
    time.sleep(0.1)
    
    k = cv.waitKey(60) & 0xff
    if k == 27:
        break
    
ca.release()
cv.destroyAllWindows()