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