#!/usr/bin/bash

# Script pour tester l'algorithme de detection

# Pre-requis : Avoir lancer successivement le script generate_negatives.sh
#              et le script traincascade.sh 

python3 facedetect.py --cascade out.xml  0
