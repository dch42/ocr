# ocr
CLI script to convert images and pdf files into text for easier processing.

Uses [pytesseract](https://github.com/madmaze/pytesseract) and [pdf2image](https://github.com/Belval/pdf2image) for OCR and image conversion respectively. 

Users running MacOS may also need to install [poppler](https://formulae.brew.sh/formula/poppler) (for `pdftoppm`).

## Setup 🔧
clone the repo and change to directory:
~~~
git clone https://github.com/dch42/ocr.git && cd ocr
~~~

Run `setup.sh` to install the script: 
~~~
chmod +x setup.sh && ./setup.sh
~~~

This will install dependencies and install the script as `ocr` in /Users/$USER/bin, adding it to bash or zsh $PATH. 

## Usage

Invoke specifying desired input and output files with `-i` and `-o`, respectively:

~~~
ocr -i MyFile.pdf -o myfile.txt
~~~

The parsed text will be written/appended to the specified output file.

Multiple input files can be passed in one go, separated by spaces or globbed. 

~~~
ocr -i MyFile.png MyFile2.jpg -o myfiles.txt
ocr -i MyFile* -o myfiles.txt
~~~

### Options
- `-h, --help`
    - show this help message and exit
- `-i, --input [INPUT...]`
    - input file(s) to operate on
- `-o, --output`
    - output file for converted text
- `-p, --print`
    - prints converted text result to terminal