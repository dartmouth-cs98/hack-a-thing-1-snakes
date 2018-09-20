# Agastya Gupta & Kevin Tan - Text Recognition App
## Components: Django OCR Server & iOS CoreML App

We attempted to build an app that would allow one to recognize text in images.
Workflow is as follows:
1) photo taken and processed via iOS app
2) photo encoded to base64 and sent to django server
3) photo decoded on django server and processed with tesseract ocr api
4) text in photo returned to iOS app

What works:
- the Django server
- the iOS app's photo and CoreML functionality

Next steps:
- host Django server on Heroku
- configure iOS app to send http requests to Heroku server & integrate
