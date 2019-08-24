'''Convert png to txt using pytesseract module, a python wrapper for Google's Tesseract-OCR library
References:
- [Pytesseract](https://github.com/madmaze/pytesseract)
- [Tesseract HOWTO](https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/)
'''
import pytesseract
import os
projectFolder = os.path.abspath(os.curdir)
outputFile = 'output.txt'
outputFilePath = os.path.abspath(os.path.join(projectFolder, outputFile))
if os.path.isfile(outputFilePath): os.remove(outputFilePath)
imgFolder = 'images'
os.chdir(imgFolder)
images = os.listdir(os.curdir)
sortedImages = sorted(images, key=os.path.getmtime)
for each in sortedImages:
    textStream = pytesseract.image_to_string(each)
    with open(outputFilePath, 'a') as f:
        f.write(textStream)
os.chdir('..')
