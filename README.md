English | [繁體中文](README_TCH.md)
# DetectWordFromImage
A simple method to get word from image. Using pytesseract.

# Usage
You can using this script to get word from your image.

# Before start
## tesseract
You need to install [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) before using the script.

In default it will be english detect only. So if you want get more language to detect it can be download in here: [traineddata](https://github.com/tesseract-ocr/tessdata/tree/main).

And you can put these data set in the ```path_you_install\Tesseract-OCR\tessdata\``` folder.

I highly recommend you to put ```path_you_install\Tesseract-OCR\``` this folder to your system path to easily using the script. Or you will need to add a line in the code:
```py
pytesseract.pytesseract.tesseract_cmd = r'path:\Tesseract-OCR\tesseract.exe'
```

## python modules
You will need to install these python module:

```cmd
pip install pillow
pip install pytesseract
```

And I recommend to install opencv for image editing to get better effect:

```cmd
pip install opencv-python
```
