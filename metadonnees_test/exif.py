print("coucou")

from PIL import Image
from PIL.ExifTags import TAGS
# path to the image or video
imagename = "NANCY_JUMEAUX_Jade_02.tif.tif"

# extract EXIF data

import piexif
exif_dict = piexif.load(imagename)
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])
