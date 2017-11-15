from PIL import Image
import re


img = Image.open("/home/milosz/pycharmProjects/python_challenge/resources/oxygen.png")
height = img.height
width = img.width
pix = img.load()
img.close()

coded_m = []
for i in range(0,width,7):
    coded_m.append(pix[i,height/2][0])

message  = "".join(map(chr,coded_m))[:-3]

s_numbers = re.findall("[0-9]{3}",message)
i_numbers = map(int,s_numbers)
answer = "".join((map(chr,i_numbers)))

print(answer)




