#!/bin/bash - 

for fcase in fiveSpot{02..10}; do
    cd $fcase;
    pwd;
    cp ../fiveSpot01/time.pvsm .;
    cp ../fiveSpot01/generatePics.py .;
    sed -i "s/fiveSpot01/$fcase/g" time.pvsm generatePics.py;
    paraview --state=time.pvsm --script=generatePics.py;
    cd ..;
done
