from PIL import Image

img = Image.open('нг.jpg')
area = (0, 0, 150, 150)
cropped_img = img.crop(area)

cropped_img.save('new_нг.jpg')
