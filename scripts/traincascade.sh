#!/usr/bin/bash

# Script pour generer automatiquement des images negatives a partir des positives
# puis pour entrainer le classifieur cascade

# Pre-requis : Avoir compiler OpenCV 3.4 et avoir plusieurs photos positives et plusieurs
# photos negatives (si possible un miller de negatives)

find  "$(cd ../negatives; pwd)" -name '*.jpg' > ../negatives/negatives.txt
find  "$(cd ../positives; pwd)" -name '*.jpg' > ../positives/positives.txt
mkdir ../samples

perl createsamples.pl ../positives/positives.txt ../negatives/negatives.txt ../samples 7800 "opencv_createsamples -bgcolor 235 -bgthresh 20 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0 -maxidev 20 -w 20 -h 20"
python3 mergevec.py -v ../samples -o out.vec

mkdir data

opencv_traincascade -data data -vec out.vec -bg ../negatives/negatives.txt -numPos 780 -numNeg 500 -numStages 20 -w 20 -h 20
