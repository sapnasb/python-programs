from PIL import Image
from PIL.ExifTags import TAGS
import os

image = Image.open(os.path.join(r'C:\PATH\IMG_20180924_162938.jpg'))

info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label,value in info_dict.items():
    print(f"{label:25}: {value}")

exifdata = image._getexif()

for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")

    
"""

Filename                 : C:\PATH\IMG_20180924_162938.jpg
Image Size               : (4000, 3000)
Image Height             : 3000
Image Width              : 4000
Image Format             : JPEG
Image Mode               : RGB
Image is Animated        : False
Frames in Image          : 1
GPSInfo                  : {29: '2018:09:24', 5: 2.2, 7: (10.0, 59.0, 37.0)}
ResolutionUnit           : 2
ExifOffset               : 174
Make                     : Xiaomi
Model                    : Redmi 5
DateTime                 : 2018:09:24 16:29:38
YCbCrPositioning         : 1
XResolution              : 72.0
YResolution              : 72.0
ExifVersion              : 0220
ComponentsConfiguration  : ☺☻♥
ShutterSpeedValue        : 4.321
DateTimeOriginal         : 2018:09:24 16:29:38
DateTimeDigitized        : 2018:09:24 16:29:38
ApertureValue            : 2.27
BrightnessValue          : -2.25
MeteringMode             : 2
FlashPixVersion          : 0100
Flash                    : 16
FocalLength              : 3.81
ColorSpace               : 1
ExifImageWidth           : 4000
ExifInteroperabilityOffset: 627
FocalLengthIn35mmFilm    : 26
SceneCaptureType         : 64
SubsecTime               : 469059
SubsecTimeOriginal       : 469059
SubsecTimeDigitized      : 469059
ExifImageHeight          : 3000
SensingMethod            : 2
ExposureTime             : 0.05
FNumber                  : 2.2
SceneType                : ☺
ExposureProgram          : 0
ISOSpeedRatings          : 1600
ExposureMode             : 0
WhiteBalance             : 0

"""

        