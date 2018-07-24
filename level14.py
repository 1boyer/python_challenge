from PIL import Image

old_im = Image.open("wire.png")
if old_im.mode != 'RGB':
    old_im = old_im.convert('RGB')
pixels = old_im.load()
new_im = Image.new('RGB',(100,100))
pixels_new = new_im.load()

length = 100
depth = 0
i = 0
for x in xrange(old_im.size[0]):
  if i == 4*(length-1):
    length -= 1;
    depth += 1 
    i = 0
  elif i < length:
    pixels_new[depth+i,depth] = pixels[x,0]
  elif i < 2*length-1:
    pixels_new[depth+length-1,depth+(i%length)] = pixels[x,0]
  elif i < 3*length-2:
    pixels_new[depth+length-1-(i%(2*length-1)),depth+length-1] = pixels[x,0]
  elif i < 4*length-4:
    pixels_new[depth,depth+length-1-(i%(3*length-2))] = pixels[x,0]
  i += 1
  
new_im.save("bun.png")