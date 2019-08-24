import os
filename = 'book.pdf'
imgFolder = 'images'
if not os.path.isdir(imgFolder): os.mkdir(imgFolder)
convertToPngCommand = 'wsl pdftocairo -png ' + filename + ' images/page'
os.system(convertToPngCommand)