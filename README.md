# Agastya Gupta & Kevin Tan - Image Text Recognition App
## Components: Django OCR Server & iOS CoreML App

We attempted to build an app that would allow one to recognize text in images.
Workflow is as follows:
1) photo taken and processed via iOS app
2) photo encoded to base64 and sent to django server
3) photo decoded on django server and processed with tesseract ocr api
4) text in photo returned to iOS app

What works:
- the Django server (Agastya)
- the iOS app's photo and CoreML functionality to some extent (Kevin)

What didn't work:
- Django version issues
- Swift version issues caused certain functionalities of the app to be pretty buggy. For instance, image recognition output appears only sometimes in Xcode. Photo taking and saving functionality is not working properly, primarily because we believe the tutorial we followed was in Swift 3 while the current Swift is version 4.

What we learned:
- iOS development for camera apps (storyboard and Swift)
- coreML for iOS
- No cheap computer vision labelling API

Next steps:
- host Django server on Heroku
- configure iOS app to send http requests to Heroku server & integrate

## Guides referenced:  

Django/Tesseract:  
https://docs.djangoproject.com/en/2.1/intro/tutorial01/  
https://www.bogotobogo.com/python/Django/Python_Django_Image_Files_Uploading_Example.php  
https://pypi.org/project/pytesseract/  
 
iOS:  
https://www.youtube.com/watch?v=Zv4cJf5qdu0  
https://www.youtube.com/watch?v=p6GA8ODlnX0  
 
Resolving CSRF issues:  
https://www.fir3net.com/Web-Development/Django/csrf-verification-failed-request-aborted.html  
https://stackoverflow.com/questions/38305269/when-tested-http-post-with-chrome-postman-it-doesnt-work-in-django  
