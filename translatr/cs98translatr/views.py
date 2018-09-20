# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from django.views.decorators.csrf import csrf_exempt


import pytesseract
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import base64

def index(request):
    return HttpResponse("Hello, world.")

@csrf_exempt
def process(request):
	image_64_decode = base64.decodestring(request.body)
	image_result = open('sample.jpg', 'wb')
	image_result.write(image_64_decode)
	context = {"words": pytesseract.image_to_string(Image.open('sample.jpg'))}
	#return render(request, 'cs98translatr/process.html', {"words":os.getcwd()})
	return render(request, 'cs98translatr/process.html', context)