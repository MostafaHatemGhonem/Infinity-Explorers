
from PIL import Image

myImage = Image.open("D:\Projects_Learning\Infinity-Explorers\Infinity-Explorers\Programing\Python-Tasks\Mostafa-Hatem\Tasks_From_086_To_089\image\elzero-pillow.png")



myBox = (400, 0, 800, 400)
myCroppedImage = myImage.crop(myBox)
myCroppedImage = myCroppedImage.convert("L")
myCroppedImage.show()

myCroppedImage.save("D:\Projects_Learning\Infinity-Explorers\Infinity-Explorers\Programing\Python-Tasks\Mostafa-Hatem\Tasks_From_086_To_089\image\Lcropped.png")

myLine = (0, 400, 1200, 800)
myRotateLine = myImage.crop(myLine)
myRotateLine = myRotateLine.convert("L")
myRotateLine = myRotateLine.rotate(180)
myRotateLine.show()
myRotateLine.save("D:\Projects_Learning\Infinity-Explorers\Infinity-Explorers\Programing\Python-Tasks\Mostafa-Hatem\Tasks_From_086_To_089\image\ImageRotate.png")