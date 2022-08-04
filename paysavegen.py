from PIL import Image, ImageFont, ImageDraw, ImageOps
import os

DATE           = ["03.08.2023", (80, 83), 11]
TERM_NUMBER    = ["189431", (102, 97), 11]
TIME           = ["23:27:13", (253, 83), 11]
TRACE_NUMBER   = ["269337", (253, 97), 11]
TXN            = ["339495890444148443", (65, 125), 11]
INVOICE_NUMBER = ["284715", (131, 139), 11]
AMOUNT         = ["100.00 EUR", (156, 177), 20]
SERIAL_NUMBER  = ["3162213136", (139, 215), 11]
CODE           = ["9016 0877 2466 1371", (27, 280), 23]

try:
    template = Image.open("template.jpg")
except OSError:
    print('Template file nout found!')

edit = ImageDraw.Draw(template)

for element in [DATE, TERM_NUMBER, TIME, TRACE_NUMBER, TXN, INVOICE_NUMBER, AMOUNT, SERIAL_NUMBER, CODE]:
    font = ImageFont.truetype("RobotoMono-SemiBold.ttf", element[2])
    edit.text(element[1], element[0], 76, font = font)

template = ImageOps.grayscale(template)

template.save('generated.png')