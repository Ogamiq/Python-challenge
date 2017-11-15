from PIL import Image


img = Image.open("/home/milosz/pycharmProjects/python_challenge/resources/oxygen.png")
height = img.height
width = img.width
pix = img.load()


coded_m = []
for i in range(0,width - 3,7):
    coded_m.append(pix[i,height/2][0])

print(coded_m)
