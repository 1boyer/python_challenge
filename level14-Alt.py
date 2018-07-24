from PIL import Image
img = Image.open('wire.png','r')
imgB = Image.new('RGB',(100,100),(0,0,0))

def grabImgLine(src,dest,start,end,loc,across,inc,pos):
    for c in range(start,end,inc):
        if across: dest.putpixel((c,loc),src.getpixel((pos,0)))
        else: dest.putpixel((loc,c),src.getpixel((pos,0)))
        pos += 1
    if across: loc += inc
    else: loc -= inc
    return pos,loc

i,xmin,ymin,xmax,ymax= 0,0,0,99,99
while(xmax >=0 and ymax >= 0):
    i,ymin = grabImgLine(img,imgB,xmin,xmax+1,ymin,True,1,i)
    i,xmax = grabImgLine(img,imgB,ymin,ymax+1,xmax,False,1,i)
    i,ymax = grabImgLine(img,imgB,xmax,xmin-1,ymax,True,-1,i)
    i,xmin = grabImgLine(img,imgB,ymax,ymin-1,xmin,False,-1,i)

imgB.save('spiral.png')