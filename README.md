# QRCodeGenerator
QR code generator using pyqrcode

# pyqrcode
The pyqrcode module is a QR code generator that is simple to use and written in pure python. The module can automates most of the building process for creating QR codes. Most codes can be created using only two lines of code!

Unlike other generators, all of the helpers can be controlled manually. You are free to set any or all of the properties of your QR code.

#Installation

Installation is very simple using pip

> pip install pyqrcode

# Usage

You only need pyqrcode import for this  \
Here PIL is used to display the images once they are generated \
You can create directly png type by importing pypng
> pip install pypng

# Encoding Data

This module supports all four encodings for data: numeric, alphanumeric, kanji, and binary.

The numeric type is the most efficient way to encode digits. As the name implies it is designed to encode integers. Some numbers might be two large, the object can use a string containing only digits instead of an actual number.
```
 number = pyqrcode.create(121546654)
```
```
 url = pyqrcode.create('youtube.com')
```
```
 life = pyqrcode.creaate('''Hello world welcome to yhis universe enjoy your stay.''')
```
