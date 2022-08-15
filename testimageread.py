import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('media/stat_cards/M3E_Exs_Apex_LordCooper1024_2.jpg')
text = pytesseract.image_to_string(img)
print(text)