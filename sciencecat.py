from PIL import Image
im = Image.open("cat.jpg")

r,g,b = im.split()

count = 0
total = 0
pixelCount = 0
for pixel in r.getdata():
    pixelCount = pixelCount + 1
    if pixel >= 100:
        count = count + 1
        total = total + pixel


print("hot pixels " + str(total/count/256*100) + "%")
print("ratio " + str(count/pixelCount*100) + "%")
r.show()
