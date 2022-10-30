import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime


#taking images from a directory and storing in array
path='D:/AMAN/college practicals sem3/advanced python/code/login/images'
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)

#Storing name from the filename
for cl in mylist:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)

#encoding the images from the file
def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('attendance.csv','r+') as f:
        mydatalist=f.readlines()
        nameList=[]
        for line in mydatalist:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtstring=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')

encodeListKnown=findEncodings(images)
print("Encoding complete")

#capturing video
cap=cv2.VideoCapture(0)

while True:
    #reading the webcam image
    success,img=cap.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25) #resizing the file image
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    facesCurFrame=face_recognition.face_locations(imgs) #finding face location
    encodesCurFrame=face_recognition.face_encodings(imgs,facesCurFrame) #encoding the webcam images
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace) #comparing file image and webcam imagesss
        facedis=face_recognition.face_distance(encodeListKnown,encodeFace) #finding the distance between both the images
    
        #print(facedis)
        #finfing minimum distance of images
        matchIndex=np.argmin(facedis)
        #print(matchIndex)
        #we get multiple faces sometimes so we need to find the minimum distance between the images if it matches it will show the name
        if matches[matchIndex]:
            #print(matches[matchIndex])
            name=classnames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        else:
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
            cv2.putText(img,"Failed",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
    
# #opening image and converting it into rbg
# imgelon=face_recognition.load_image_file("D:/AMAN/college practicals sem3/advanced python/code/login/images/aman.jpeg")
# imgelon=cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
# imgtest=face_recognition.load_image_file("D:/AMAN/college practicals sem3/advanced python/code/login/images/isha.jpeg")
# imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)


# #finding face and draw rectangle around it
# faceloc=face_recognition.face_locations(imgelon)[0]
# encodeElon=face_recognition.face_encodings(imgelon)[0]
# cv2.rectangle(imgelon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),6)

# facelocTest=face_recognition.face_locations(imgtest)[0]
# encodeTest=face_recognition.face_encodings(imgtest)[0]
# cv2.rectangle(imgtest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)
# #print(facelocTest)

# #comparing both image is it match or not
# results=face_recognition.compare_faces([encodeElon],encodeTest)
# #finding the distance of both image
# facedis=face_recognition.face_distance([encodeElon],encodeTest)
# print(results,facedis)
# #putting the 
# cv2.putText(imgtest,f'{results}{round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


# #displaying image
# cv2.imshow("aman maurya",imgelon)
# cv2.imshow("aman maurya test",imgtest)

