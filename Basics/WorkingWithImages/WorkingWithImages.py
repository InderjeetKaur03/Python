# install pillow library
# Different methods avaialble are resize, rotate, putalpha, sixe, paste
#pip install pillow

from PIL import Image
photo = Image.open('MyPhoto.jpg')
photo.show()

