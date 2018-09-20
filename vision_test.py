import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.oauth2 import service_account
#credentials = service_account.Credentials.from_service_account_file('apikey.json')

#client = vision.ImageAnnotatorClient(credentials=credentials)
#client = vision.ImageAnnotatorClient('apikey.json')   

# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
file_name = os.path.join(
    os.path.dirname(__file__),
    'img.png') # Your image path from current directory 

client = vision.ImageAnnotatorClient()

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations
print('Labels:')

for label in labels:
    print(label.description)