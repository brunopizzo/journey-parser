import os
import sys
from xml.etree import ElementTree as ET


if __name__ == '__main__':
    filepath = sys.argv[1]
    print(filepath)
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Parsing points
    gpsPoints = []
    for child in root.findall(".//{http://www.topografix.com/GPX/1/1}trkpt"):
        gpsPoints.append([float(child.attrib['lat']), float(child.attrib['lon']), float(child[0].text)])

    # writing file
    name = os.path.splitext(root.find(".//{http://www.topografix.com/GPX/1/1}name").text)[0]
    f = open(name + ".txt", "w+")
    f.write(name + "\n")
    f.write(str(gpsPoints))
