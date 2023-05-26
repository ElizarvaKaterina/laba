from PIL import Image, ImageFilter

f = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
count = 0
for file in f:
    if file.endswith('.jpg') or file.endswith('.png'):
        count += 1
        img = Image.open(file)
        new_img = img.filter(ImageFilter.EMBOSS)
        new_img.show()
        try:
            os.mkdir("F:/алгоритмы/питон/9")
        except:
            pass
        new_img.save(f"F:/алгоритмы/питон/9/new_img{count}.png")
