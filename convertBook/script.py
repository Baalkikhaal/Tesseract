'''Convert PDF into png using poppler library's pdftocairo Each page is converted to separate png file
References:
- [Poppler-Utils](https://packages.ubuntu.com/xenial/poppler-utils)
- [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
'''
import os
filename = 'book.pdf'
imgFolder = 'images'
if not os.path.isdir(imgFolder): os.mkdir(imgFolder)
convertToPngCommand = 'wsl pdftocairo -png ' + filename + ' images/page'
os.system(convertToPngCommand)
