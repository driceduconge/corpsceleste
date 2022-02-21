# path to the image or video
from bs4 import BeautifulSoup
import xmltodict
import json
import re
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import os
# assign directory
directory = 'versiontravail'

f=open("output.json","w")
evv=open("test.csv","w")
evv.write("Fichier,nom,prenomn,mots_clefs,ecole,date,heure,ouv.,vitesse"+"\n")
for fname in os.listdir(directory):
    f = os.path.join(directory, fname)
    # checking if it is a file
    if os.path.isfile(f):
        imagename = "versiontravail/"+fname
        print(imagename+"\n")
        exif_dict = piexif.load(imagename)
        try:
            ouverture_t = exif_dict["Exif"][piexif.ExifIFD.FocalLength]
        except:
            ouverture = " "
        else:
            ouverture = str(ouverture_t[0])

        try:
            vitesse_t = exif_dict["Exif"][piexif.ExifIFD.ExposureTime]
        except:
            vitesse = " "
        else:
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
            #print(reg)

        filedata = json.loads(file)
        filename = imagename
        try:
            title = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["photoshop:authorsposition"]
        except:
            title = "Sans Titre"
        #filename = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:title"]["rdf:alt"]["rdf:li"]["#text"]
        try:
            infos_aseparer = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:creator"]["rdf:seq"]["rdf:li"]
        except:
            prenom = " "
            nom = " "
        else:
            prenom = infos_aseparer[0]
            nom = infos_aseparer[1]

        try:
            date_heure = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["xmp:createdate"]
        except:
            date = "Inconnu"
            heure = "Inconnu"
        else:
            d_h = re.split("T",date_heure)
            date = d_h[0]
            heure = d_h[1]
        try:
            mots_clefs_bef = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:subject"]["rdf:bag"]["rdf:li"]
        except:
            mots_clefs = "Inconnu"
        else:
            mots_clefs = ""
            for mot in mots_clefs_bef:
                mots_clefs += mot+"|"
        try:
            ecole = filedata["html"]["body"]["x:xmpmeta"]["rdf:rdf"]["rdf:description"]["dc:rights"]["rdf:alt"]["rdf:li"]["#text"]
        except:
            ecole = "PLOUP"
        print(filename+","+prenom+","+nom+","+mots_clefs+","+ecole+","+date+","+heure+","+ouverture+","+vitesse+"\n")
        evv.write(filename+","+prenom+","+nom+","+mots_clefs+","+ecole+","+date+","+heure+","+ouverture+","+vitesse+"\n")
