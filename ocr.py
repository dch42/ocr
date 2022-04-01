#!/usr/bin/env python3
"""Convert images to text for easier processing using OCR"""

import argparse
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

# define and parse args
parser = argparse.ArgumentParser(
    description="Convert images to text for easier processing using OCR")
parser.add_argument(
    "-i", "--input", type=str, nargs='+', required='True', help='input file(s) to operate on')
parser.add_argument(
    "-o", "--output", type=str, nargs='+', help='output file for converted text')
args = parser.parse_args()

def pdf_to_image(pdf):
    """Converts pdf pages to image files"""
    doc = convert_from_path(pdf)
    count = 1
    images = []
    for page in doc:
        image_name = f"{pdf}"+"page_"+str(count)+".jpg"
        page.save(image_name, 'JPEG')
        images.append(image_name)
        count += 1
    print(images)
    return images

def convert_to_text(image):
    """Use OCR to scrape text from image"""
    text = pytesseract.image_to_string(Image.open(image))
    print(text)

for arg in args.input:
    if arg.endswith('.pdf'):
        pdf_images = pdf_to_image(arg)
        for image in pdf_images:
            convert_to_text(image)
    else:
        convert_to_text(arg)





