import pytesseract
from PIL import Image

print(pytesseract.image_to_string(Image.open('letter.jpg')))
print(pytesseract.image_to_string(Image.open('font_size.png')))
print(pytesseract.image_to_string(Image.open('img.jpg')))