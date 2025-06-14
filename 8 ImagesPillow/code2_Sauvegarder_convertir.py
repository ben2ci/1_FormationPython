from PIL import Image

# 1er CAS
# im = Image.open('_images/rose.jpg')
# im.save('_images/rose.png')

# 2ème CAS
# im = Image.open('_images/homme.png')
# im.convert("RGB").save('_images/homme.jpg')

# 3ème CAS création de notre propre image
im = Image.open('_images/homme.png')
im_png = Image.new("RGB", im.size, (255, 0, 0))
im_png.paste(im, im)
im_png.show()
# im.split()[3].show()
