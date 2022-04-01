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
    "-o", "--output", type=str, required='True', help='output file for converted text')
args = parser.parse_args()

def pdf_to_image(pdf):
    """Converts pdf pages to image files"""
    doc = convert_from_path(pdf)
    count = 1
    images = []
    for page in doc:
        image_name = f"{pdf}"+"_page_"+str(count)+".jpg"
        page.save(image_name, 'JPEG')
        images.append(image_name)
        count += 1
    return images

def convert_to_text(image):
    """Use OCR to scrape text from image"""
    text = pytesseract.image_to_string(Image.open(image))
    print(text)
    return text

def write_out(text):
    out_file = args.output
    with open(out_file, 'w') as out:
        out.write(text)

for arg in args.input:
    if arg.endswith('.pdf'):
        pdf_images = pdf_to_image(arg)
        for image in pdf_images:
            text = convert_to_text(image)
            write_out(text)
    else:
        text = convert_to_text(arg)
        write_out(text)