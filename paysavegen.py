from PIL import Image, ImageFont, ImageDraw, ImageOps
import os

DATE           = ["06.09.2069", (80, 83), 11]
TERM_NUMBER    = ["101010", (102, 97), 11]
TIME           = ["00:00:00", (253, 83), 11]
TRACE_NUMBER   = ["420420", (253, 97), 11]
TXN            = ["888888888888888888", (65, 125), 11]
INVOICE_NUMBER = ["696969", (131, 139), 11]
AMOUNT         = ["420.00 EUR", (156, 177), 20]
SERIAL_NUMBER  = ["6969696969", (139, 215), 11]
CODE           = ["1010 1010 1010 1010", (27, 280), 23]

try:
    template = Image.open("template.jpg")
except OSError:
    print('Template file not found!')
    exit()

edit = ImageDraw.Draw(template)

for element in [DATE, TERM_NUMBER, TIME, TRACE_NUMBER, TXN, INVOICE_NUMBER, AMOUNT, SERIAL_NUMBER, CODE]:
    try:
        font = ImageFont.truetype("RobotoMono-SemiBold.ttf", element[2])
    except OSError:
        print('Font file nout found!')
        exit()
    
    edit.text(element[1], element[0], 76, font = font)

template = ImageOps.grayscale(template)

template.save('generated.png')