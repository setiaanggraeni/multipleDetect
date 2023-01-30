import cv2
from deepface import DeepFace

# importing_haarcascade_classifiers
face_classifier =cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# face_detection_function
def face_detection(image):
    
    # grascaling_image_passed
    if ret is True:
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        # detecting_faces    
        faces=face_classifier.detectMultiScale(gray,1.6,7)
        count = 0
        # drawing_face_rectangle
        for (x,y,w,h) in faces:
            if len(faces) > 1:
                face = frame[y:y + h, x:x + w]  # slice the face from the image
                count = count + 1
                cv2.imwrite(str(count) + '.jpg', face)
                if count == 2:
                    img1 = cv2.imread("1.jpg")
                    img2 = cv2.imread("2.jpg")
                    resulCompare = DeepFace.verify(img1, img2, enforce_detection=False)['verified']
                    if resulCompare:
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        bottomLeftCornerOfText = (10, 500)
                        fontScale = 1
                        fontColor = (60, 179, 113)
                        thickness = 3
                        lineType = 2

                        cv2.putText(image, 'OK Pemilik KTP',
                                    bottomLeftCornerOfText,
                                    font,
                                    fontScale,
                                    fontColor,
                                    thickness,
                                    lineType)
                        cv2.imwrite("Verified" + '.jpg', image)
                    else:
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        bottomLeftCornerOfText = (10, 500)
                        fontScale = 1
                        fontColor = (127,0,255)
                        thickness = 3
                        lineType = 2

                        cv2.putText(image, 'Hati-Hati Bukan Pemilik KTP',
                                    bottomLeftCornerOfText,
                                    font,
                                    fontScale,
                                    fontColor,
                                    thickness,
                                    lineType)
                        cv2.imwrite("Not Verified" + '.jpg', image)
            # draw_rectangle_around_face
            cv2.rectangle(image,(x,y),(x+w,y+h),(60, 179, 113),2)
    
    # returning_image_with_rectangles
    return image
    
# capturing_video_from_webcam
cap=cv2.VideoCapture(1)

while True:

    # reading_from_camera
    ret,frame=cap.read()
    cv2.imshow('face_detection',face_detection(frame))

    # if_enter_pressed_then_exit
    if cv2.waitKey(1)==13:
        break
        
# releasing_camera
cap.release()
# destroying_window
cv2.destroyAllWindows()