import cv2
stop_cascade = cv2.CascadeClassifier('./data/cascade.xml')
img = cv2.imread('obamatest.jpg')
bieres = stop_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
for (x,y,w,h) in bieres:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),10)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()