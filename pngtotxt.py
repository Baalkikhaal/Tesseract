'''Convert png to txt using pytesseract module, a python wrapper for Google's Tesseract-OCR library
References:
- [Pytesseract](https://github.com/madmaze/pytesseract)
- [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- [Tesseract HOWTO](https://www.learnopencv.com/deep-learning-based-text-recognition-ocr-using-tesseract-and-opencv/)
'''
import sys
import os
import pytesseract

if len(sys.argv) < 2:
    print('Usage: pdftotext.py output.txt')
    sys.exit(1)
# Read output file path from command line
outputFile = sys.argv[1]
projectFolder = os.path.abspath(os.curdir)
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
