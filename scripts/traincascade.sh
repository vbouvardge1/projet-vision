#!/usr/bin/bash

# Script pour generer automatiquement des images negatives a partir des positives
# puis pour entrainer le classifieur cascade

# Pre-requis : Avoir compiler OpenCV 3.4 et avoir plusieurs photos positives et plusieurs
# photos negatives (si possible un miller de negatives) et les mettres dans les fichiers correspondant.

#Créer 2 fichiers .txt avec les chemin des images
find  ../negatives/ -name '*.jpg' > ../negatives/negatives.txt
find  ../positives/ -name '*.jpg' > ../positives/positives.txt
#créer un dossier samples
 mkdir ../samples

#Créer un .vec par image positives
perl createsamples.pl ../positives/positives.txt ../negatives/negatives.txt ../samples 1000 "opencv_createsamples -bgcolor 235 -bgthresh 20 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0 -maxidev 20 -w 20 -h 20"

#Regrouper les .vec en un out.vec
 python mergevec.py -v ../samples -o out.vec

#créer un dossier data
mkdir data

#Faire l'entrainement cascade
opencv_traincascade -data data -vec out.vec -bg ../negatives/negatives.txt -numPos 780 -numNeg 500 -numStages 20 -w 20 -h 20
#L'entrainement terminer sera dans ./data/cascade.xml