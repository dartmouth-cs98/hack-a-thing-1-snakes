import base64

with open("letter.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    image_64_decode = base64.decodestring(encoded_string) 
    image_result = open('deer_decode.jpg', 'wb') 
    # create a writable image and write the decoding result
    text_file = open("testencode2.txt", "w")
    text_file.write(encoded_string)
    text_file.close()
    image_result.write(image_64_decode)
