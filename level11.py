from PIL import Image

def find_rows(height):
    rows_found=[]
    for y in xrange(height):
        if y%2:
            rows_found.append(y)
    return rows_found

def find_columns(width):
    columns_found=[]
    for x in xrange(width):
        if x%2:
            columns_found.append(x)
    return columns_found

old_im = Image.open("cave.jpg")
if old_im.mode != 'RGB':
    old_im = old_im.convert('RGB')
pixels = old_im.load()
width, height = old_im.size[0], old_im.size[1]
rows_to_remove = find_rows(height) #Remove every other row
columns_to_remove = find_columns(width)
new_im = Image.new('RGB', (width - len(columns_to_remove), height - len(rows_to_remove)))
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