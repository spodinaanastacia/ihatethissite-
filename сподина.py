import os
def f(t,n):
    print(t)
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype ('C:/Users/user/Documents/bahnschrift.ttf', size=18)
    im2 = Image.new ('RGB', (800,600), color=('#FAACAC'))
    draw_text = ImageDraw.Draw(im2)
    draw_text.text(
        (300,300),
        t,
        font=font,
        fill=('#1C0606'))
    #im2.show()
    
    im2.save(f'C:/Users/user/Documents/name{n}.jpg')

t=('Привет',
   'Здраствуйсте',
   '1322435',
   'qwerty')
print(t)
n=0
for i in range (4):
    f(t[i],i)
 
