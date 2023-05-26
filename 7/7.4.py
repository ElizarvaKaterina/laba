from PIL import Image

watermark = "watermark.png"
with Image.open(watermark) as img_watermark:
    img_watermark.load()

img_watermark = Image.open(watermark)
img_watermark = img_watermark.resize((img_watermark.width // 2, img_watermark.height // 2))

filename = "3.jpg"
with Image.open(filename) as img:
    img.load()
    img.paste(img_watermark, (50, 50), img_watermark)
    img.save("watermark_3.jpg")
