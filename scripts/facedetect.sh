#!/usr/bin/bash

# Script pour tester l'algorithme de detection

## Pre-requis : Avoir lancer successivement le script traincascade.sh 

#Essayer le cascade.xml en video
python videodetect.py
#Essayer le cascade.xml en image. Vous pouvez changer l'image de reférence dans imagedetect.py
python imagedetect.py