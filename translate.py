import pytesseract
from PIL import image

print(pytesseract.image_to_string(Image.open('letter.jpg')))
print(pytesseract.image_to_string(Image.open('font_size.png')))
print(pytesseract.image_to_string(Image.open('img.jpg')))