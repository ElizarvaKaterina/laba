from PIL import Image, ImageFilter

x = ["1.png", "2.jpg", "3.png", "4.jpg", "5.png"]
count = 0
for file in x:
    if file.endswith('.jpg') or file.endswith('.png'):
        count += 1
        img = Image.open(file)
        new_img = img.filter(ImageFilter.EMBOSS)
        new_img.show()
        try:
            os.mkdir("")
        except:
            pass
        new_img.save(f"new_img{count}.png")
