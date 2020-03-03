https://docs.opencv.org/2.4/modules/contrib/doc/facerec/tutorial/facerec_video_recognition.html

1) prener des photos de votre visage de face.
2) utiliser le pogramme alignement.py pour mettre à l'échelle, faire pivoter et recadrer vos images
   de visages en changeant les paramettres de ses lignes de commande.
86 image =  Image.open("image d'entrée.jpg")
87 CropFace(image, eye_left=(position x, position y), eye_right=(position position x,position y), offset_pct=(0.3,0.3), dest_sz=(200,200)).save("image de sortie.jpg")
3) remplacer le fichier persons.csv avec le chemin vers une image, le séparateur ";" et l'étiquette de l'image (une étiquette par personne).
4) lancer la commande my_exe dans un terminal dans  ./build/bin.

commande my_exe:
./my_exe.exe ../../script/haarcascade_frontalface_alt.xml ../../script/persons.csv 0