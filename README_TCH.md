[English](README.md) | 繁體中文
# 從圖像中偵測文字
這是一個使用 pytesseract 從圖像中獲取文字的簡易腳本。

# 使用方法
你可以使用這個腳本從圖像中獲取文字。

# 開始之前
## Tesseract OCR
在使用這個腳本之前，你需要先安裝 [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)。

默認情況下，它只能偵測英文。如果你想要偵測更多語言，可以從這裡下載：[traineddata](https://github.com/tesseract-ocr/tessdata/tree/main)。

然後，你可以將這些數據集放在 ```安裝路徑\Tesseract-OCR\tessdata\``` 文件夾中。

我強烈建議將 ```安裝路徑\Tesseract-OCR\``` 這個文件夾添加到系統的環境變量中，這樣可以更方便地使用腳本。否則，你需要在代碼中添加一行：
```py
pytesseract.pytesseract.tesseract_cmd = r'路徑:\Tesseract-OCR\tesseract.exe'
```

## Python 模組
你需要安裝以下 Python 模組：

```cmd
pip install pillow
pip install pytesseract
```

我推薦你安裝 OpenCV 進行圖像編輯，以獲得更好的效果：

```cmd
pip install opencv-python
```
