import cv2
import sys, os


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        ret_val, frame = cam.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        if mirror: 
            img = cv2.flip(img, 1)

            # on charge le modèle de détection des visages
            face_model = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
             
             
            # détection du ou des visages
            faces = face_model.detectMultiScale(img)
             
            # on place un cadre autour des visages
            #print ("nombre de visages", len(faces), "dimension de l'image", img.shape, "image", image)
            for face in faces:
                cv2.rectangle(img, (face[0], face[1]), (face[0] + face[2], face[0] + face[3]), (255, 0, 0), 3)

            
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
