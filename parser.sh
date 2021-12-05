#!/bin/bash

for city in ~/Desktop/nuovi_itinerari/*; do
  cd ~/Desktop/nuovi_itinerari_parsati/ && mkdir "${city##*/}"
  for subcategory in "$city"/*; do
    cd ~/Desktop/nuovi_itinerari_parsati/"${city##*/}" && mkdir "${subcategory##*/}"
    for journey in "$subcategory"/*.gpx; do

      cd ~/Desktop/nuovi_itinerari_parsati/"${city##*/}"/"${subcategory##*/}" && python3 ~/Documents/projects/journey-parser/journey-parser.py "$journey"

    done

  done
done