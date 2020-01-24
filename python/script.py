import cv2
import matplotlib.pyplot as plt

img=cv2.imread("Poster-sized_portrait_of_Barack_Obama.jpg")
img_LBP=cv2.imread("Poster-sized_portrait_of_Barack_Obama.jpg")

hauteur=img.shape[0]
largeur=img.shape[1]

print("hauteur :",hauteur)
print("largeur :",largeur)

h=0
l=0
n=0
i=0
conversion_binaire_décimal=[128,64,32,16,8,4,2,1]
LBP_valeurs=list()
LBP_signe=[0,0,0,0,0,0,0,0]
pixel_rouge=0
pixel_bleu=0
pixel_vert=0

while h<hauteur-1: ### détection des bords
	while l<largeur-1:
		if(h!=0 or h!=hauteur-1 or l!=0 or l!=largeur-1):		
			LBP_valeurs=[img[h-1,l-1],img[h-1,l],img[h-1,l+1],img[h,l+1],img[h+1,l+1],img[h+1,l],img[h+1,l-1],img[h,l-1]]
			while n<8: ### binarisation
				if(LBP_valeurs[n][2]>img[h,l][2]):
					LBP_signe[n]=1
				else:
					LBP_signe[n]=0	
				n=n+1	 
			while i<8: ### pondération
				pixel_rouge=pixel_rouge + LBP_signe[i]*conversion_binaire_décimal[i]	
				i=i+1
			img_LBP[h,l][2]=pixel_rouge
			n=0
			i=0

			while n<8: ### binarisation
				if(LBP_valeurs[n][1]>img[h,l][1]):
					LBP_signe[n]=1
				else:
					LBP_signe[n]=0	
				n=n+1	 
			while i<8: ### pondération
				pixel_vert=pixel_vert + LBP_signe[i]*conversion_binaire_décimal[i]	
				i=i+1
			img_LBP[h,l][1]=pixel_vert	
			n=0
			i=0

			while n<8: ### binarisation
				if(LBP_valeurs[n][0]>img[h,l][0]):
					LBP_signe[n]=1
				else:
					LBP_signe[n]=0	
				n=n+1	 
			while i<8: ### pondération
				pixel_bleu=pixel_bleu + LBP_signe[i]*conversion_binaire_décimal[i]	
				i=i+1
			img_LBP[h,l][0]=pixel_bleu
		l=l+1
		n=0
		i=0
		pixel_rouge=0
		pixel_bleu=0
		pixel_vert=0	
	h=h+1
	l=0

h=0
l=0
histogramme_rouge=list()
histogramme_vert=list()
histogramme_bleu=list()

while h<hauteur-1:
	while l<largeur-1:
		if(h!=0 or h!=hauteur-1 or l!=0 or l!=largeur-1):
			histogramme_rouge.append(img_LBP[h,l][2])
			l=l+1
	h=h+1
	l=0

h=0
l=0

while h<hauteur-1:
	while l<largeur-1:
		if(h!=0 or h!=hauteur-1 or l!=0 or l!=largeur-1):
			histogramme_vert.append(img_LBP[h,l][1])
			l=l+1
	h=h+1
	l=0

h=0
l=0
while h<hauteur-1:
	while l<largeur-1:
		if(h!=0 or h!=hauteur-1 or l!=0 or l!=largeur-1):
			histogramme_bleu.append(img_LBP[h,l][0])
			l=l+1
	h=h+1
	l=0		

#matplotlib.hist(histogramme_rouge, range = (0, 5), bins = 5, color = 'yellow',edgecolor = 'red')

if histogramme_bleu==histogramme_rouge:
	print("ntm")

#histogramme rouge
plt.hist(histogramme_rouge)

plt.title('Histogramme rouge', fontsize=10)

plt.savefig("Histogramme rouge.png")



#histogramme bleu
plt.hist(histogramme_bleu)

plt.title('Histogramme bleu', fontsize=10)

plt.savefig("Histogramme bleu.png")


#histogramme vert
plt.hist(histogramme_vert)

plt.title('Histogramme vert', fontsize=10)

plt.savefig("Histogramme vert.png")


cv2.imwrite('pogbacountours.jpg', img_LBP)


