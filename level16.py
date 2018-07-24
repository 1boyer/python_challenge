from PIL import Image

old_im = Image.open("mozart.gif")
if old_im.mode != 'RGB':
    old_im = old_im.convert('RGB')
pixels = old_im.load()
width, height = old_im.size[0], old_im.size[1]
new_im = Image.new('RGB', (old_im.size[0], old_im.size[1]))
pixels_new = new_im.load()

rows_removed = 0
for y in xrange(old_im.size[1]):
    if y not in rows_to_remove:
        columns_removed = 0;
        for x in xrange(old_im.size[0]):
            if x not in columns_to_remove:
                pixels_new[x - columns_removed, y - rows_removed] = pixels[x, y]
            else:
			    columns_removed += 1;
    else:
        rows_removed += 1
		
new_im.save("cave0.png")