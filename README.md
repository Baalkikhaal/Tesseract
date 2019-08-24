> Following uses [GitHub Markdown](https://guides.github.com/features/mastering-markdown/)

# Testing Tesseract for Optical Character recognition

- Setting up the Project on Windows
- HOWTO use the Python scripts

## Setting up the Project on Windows

- Install Google's [Tesseract](https://github.com/madmaze/pytesseract) library
- Install Popper Utils
- Create a project directory
- Set up [Python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Install Google's [Tesseract](https://github.com/madmaze/pytesseract) library

Download from the link and install it. After installation, add the path to the binary `tesseract.exe` to environment variable `PATH`

Image1
![Tesseract Install](/Tutorial/Screenshots/TesseractOCRhowTo.png)

#### Testing Tesseract

Text Recognition from scan with only text

`tesseract testScanOfText.png stdout`

Image2
![convertScanCrop](/Tutorial/Screenshots/TesseractOCRhowTo2.png)

Text Recognition from scan with Structured text

`tesseract testScanStructuredText.png stdout`

Tesseract is intelligent enought to neglect borders and non-text objects (Image3).

When the text is distorted it fails sometimes (Image4).

Image3
![convertScanCrop](/Tutorial/Screenshots/TesseractOCRhowTo3.png)

Image4
![convertScanCrop](/Tutorial/Screenshots/TesseractOCRhowTo4.png)

### Install Popper Utils

Poppler is a linux library to convert pdf documents into image formats. [Poppler for windows](http://blog.alivate.com.au/poppler-windows/) provides windows builds for Poppler.

However, an alternative solution is to use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) where poppler can be installed in linux and can be called in windows shell via `wsl` redirection. Even the installation of poppler in linux subsystem can be performed from a windows shell as follows

`wsl sudo apt install poppler-utils`

Image5
![Poppler for Windows](/Tutorial/Screenshots/TesseractOCRhowTo5.png)

### Create a project directory

`PythonProjects\Tesseract`

### Set up [Python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
Enter the project

`..\PythonProjects> cd Tesseract`

Create a virtual environment inside project folder (assuming Python3 all throughout)

`..\PythonProjects\Tesseract> python -m venv mypy3envtesseract`

Activate the environment

`..\Tesseract> .\mypy3envtesseract\Scripts\activate`

>After finishing work, dont forget to deactivate the environment
>
>`..\Tesseract> deactivate`

Install the required packages. `Ipython` is useful for preliminary codetesting

`> pip install ipython pytesseract`

## HOWTO use the Python scripts

1. convert the pdf into png images
  - `pdftopng.py book.pdf`
  - Will create png images in `images` sub directory

1. convert the png images into text
  - `pngtotxt.py output.txt`
  - Will loop over the images in `images` subdirectory, convert to txt and stitch the text streams into output.txt.
  - Rerunning with same output file will overwrite the text!.
