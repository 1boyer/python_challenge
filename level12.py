evil = open('evil2.gfx','rb').read()
img1 = open('img1.jpg','wb')
img2 = open('img2.jpg','wb')
img3 = open('img3.jpg','wb')
img4 = open('img4.jpg','wb')
img5 = open('img5.jpg','wb')


for b in range(0,len(evil),5):
    img1.write(evil[b])
    img2.write(evil[b+1])
    img3.write(evil[b+2])
    img4.write(evil[b+3])
    img5.write(evil[b+4])

img1.close()
img2.close()
img3.close()
img4.close()
img5.close()