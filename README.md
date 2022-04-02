# ocr
CLI script to convert images and pdf files into text for easier processing.

Uses [pytesseract](https://github.com/madmaze/pytesseract) and [pdf2image](https://github.com/Belval/pdf2image) for OCR and image conversion respectively. 

Users running MacOS may also need to install [poppler](https://formulae.brew.sh/formula/poppler) (for `pdftoppm`).

### Options
- `-h, --help`
    - show this help message and exit
- `-i, --input [INPUT...]`
    - input file(s) to operate on
- `-o, --output`
    - output file for converted text
- `-p, --print`
    - prints converted text result to terminal