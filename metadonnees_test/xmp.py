# path to the image or video
from bs4 import BeautifulSoup
import xmltodict
import json
import re
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

f=open("output.json","w")
e=open("test.csv","w")
e.write("Fichier,nom,prenomn,mots_clefs,ecole,date,heure,ouv.,vitesse"+"\n")

imagename = "NANCY_JUMEAUX_Jade_02.tif.tif"

exif_dict = piexif.load(imagename)

ouverture_t = exif_dict["Exif"][piexif.ExifIFD.FocalLength]
vitesse_t = exif_dict["Exif"][piexif.ExifIFD.ExposureTime]
print(ouverture_t)
print(vitesse_t)
ouverture = str(ouverture_t[0])
vitesse = str(vitesse_t[0]) + "/" + str(vitesse_t[1])
# read the image data using PIL
with open( imagename, "rb") as fin:
    img = fin.read()
    imgAsString=str(img)
    xmp_start = imgAsString.find('<x:xmpmeta')
    xmp_end = imgAsString.find('</x:xmpmeta')
    if xmp_start != xmp_end:
        xmpString = imgAsString[xmp_start:xmp_end+12]

    xmpAsXML = BeautifulSoup( xmpString, features="lxml" )
    file = json.dumps(xmltodict.parse(xmpAsXML.prettify()), indent = 4)
    f.write(file)
    #print(reg)

filedata = json.loads(file)
filename = imagename
title = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["photoshop:authorsposition"]
#filename = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:title"]["rdf:alt"]["rdf:li"]["#text"]
infos_aseparer = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:creator"]["rdf:seq"]["rdf:li"]
prenom = infos_aseparer[0]
nom = infos_aseparer[1]
date_heure = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["xmp:createdate"]
d_h = re.split("T",date_heure)

date = d_h[0]
heure = d_h[1]
mots_clefs_bef = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:subject"]["rdf:bag"]["rdf:li"]
mots_clefs = mots_clefs_bef[0]+"|"+mots_clefs_bef[1]+"|"+mots_clefs_bef[2]
ecole = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:rights"]["rdf:alt"]["rdf:li"]["#text"]


e.write(filename+","+prenom+","+nom+","+mots_clefs+","+ecole+","+date+","+heure+","+ouverture+","+vitesse+"\n")
