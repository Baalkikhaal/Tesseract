'''Convert PDF into png using poppler library's pdftocairo Each page is converted to separate png file
References:
- [Poppler-Utils](https://packages.ubuntu.com/xenial/poppler-utils)
- [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
- [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about)
'''

import sys
import os

if len(sys.argv) < 2:
    print('Usage: pdftopng.py book.pdf')
    sys.exit(1)
# Read pdf file path from command line
filename = sys.argv[1]
imgFolder = 'images'
if not os.path.isdir(imgFolder): os.mkdir(imgFolder)
convertToPngCommand = 'wsl pdftocairo -png ' + filename + ' images/page'
os.system(convertToPngCommand)
