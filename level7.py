from PIL import Image

img = Image.open("oxygen.png")
S = ''

for i in [(x-7)*7 for x in range(7,img.size[1])]:
  for data in img.getpixel( ( i , 43 ) )[0:1]:
    S += chr(data)

print S

answer = [105,110,116,101,103,114,105,116,121]
print ''.join([chr(x) for x in answer])