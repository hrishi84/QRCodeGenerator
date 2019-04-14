import pyqrcode
from pyqrcode import QRCode
from PIL import Image


def file_format(i):
    switcher={
            1:'png',
            2:'svg',
            3:'jpg' 
            }
    return switcher.get(i)

#input of the link or text
text = input("\nEnter the link/ string to be encoded : ")

#encoding of link into url
#do not change the variable name from url as url specifies link
#you can use number instead of url
url = pyqrcode.create(text)

#selection of file extension
file_type = input("\nSelect the type of file format \n1 png\n2 svg\n3 jpg \n")

#conversion of input into integer of base 10
opt = int(file_type,10)

#calling the switch case for file extension
fileformat = file_format(opt)

# print(file_type, " ", file_format, " ", fileformat)

#defining the filename of the qrcode
filename = text +"_QRCODE_"+"."+fileformat

#generating the QR code
url.png(filename, scale =8)

#loading the image 
image = Image.open(filename)

#displaying the image
image.show()

print("\nQR code is generated with a file name :" + filename)



