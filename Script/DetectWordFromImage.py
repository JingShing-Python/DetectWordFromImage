import cv2
import pytesseract
# need to add 'path:\programs\Tesseract-OCR' to the system path
# or add this line->
# pytesseract.pytesseract.tesseract_cmd = r'path:\Tesseract-OCR\tesseract.exe'

def detect_text(image_path, lang='eng'):
    # lang can be 'eng', 'chi_sim', 'chi_tra'
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(threshold, lang=lang)
    print(text)

if __name__ == "__main__":
    image_path = input("enter the image path: ")
    detect_text(image_path)
