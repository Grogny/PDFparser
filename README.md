<h1 align="center">PDF Parser Tools</h1>

<p align="center">
  <img src="https://github.com/Grogny/PDFparser/blob/main/PDFParserimages/pdfparserstyle.png">
</p>

<p align="center">
  :mag: PDFparser is a basic Python script that allow you to <strong>Download</strong>, <strong>Find</strong> and <strong>Parse</strong> PDF files! :wrench:
</p>

---
## USAGE:

Clone the repository:
```bash
git clone https://github.com/Grogny/PDFparser
```


#
Open the repository:
```bash
cd PDFparser
```

#
Install the requirements:
```bash
pip install -r requirements.txt
```

#
Run the script:

*To download PDF file*:
```bash
python3 pdfparser.py -d [PDF_URL]
```
*or*
```bash
python3 pdfparser.py --download [PDF_URL]
```

#
*To find if a website contain PDF files*:
```bash
python3 pdfparser.py -f [WEBSITE_URL]
```
*or*
```bash
python3 pdfparser.py --find [WEBSITE_URL]
```

#
*To extract the PDF informations*:
```bash
python3 pdfparser.py -e [PDF_NAME]
```
*or*
```bash
python3 pdfparser.py --extract [PDF_NAME]
```

#
:exclamation: I only tried the script on a Debian terminal, I don't know if it work on Windows. :exclamation:

---
## EXAMPLES AND SCREENSHOTS:

<img src="https://github.com/Grogny/PDFparser/blob/main/PDFParserimages/pdfparsermenu.png">

#
Downloader example:
<p align="left">
  <img src="https://github.com/Grogny/PDFparser/assets/87657107/f83a7dd3-6cd7-4c4b-a5e3-7d37d56e60f6">
</p>

#
Finder example:
<p align="left">
  <img src="https://github.com/Grogny/PDFparser/blob/main/PDFParserimages/findsample.png">
</p>

#
Extractor example:
<p align="left">
  <img src="https://github.com/Grogny/PDFparser/assets/87657107/19492ff5-f6e5-4298-bb08-23749d4babad">
</p>

#
**Note:**

All the unamed PDF files will be rename "Untitled.pdf".\
:warning: I do not own the PDF and the Website used for the example. :warning:

- ©[PDF](https://pdfobject.com/pdf/sample.pdf)
- ©[Website](https://www.princexml.com/samples/)

---
## MODULES I USED:

- [urllib](https://docs.python.org/3/library/urllib.html)
- [PyPDF](https://pypdf.readthedocs.io/en/stable/)
- [BeautifulSoup](https://omz-software.com/pythonista/docs/ios/beautifulsoup.html)
- [colorama](https://super-devops.readthedocs.io/en/latest/misc.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [requests](https://requests.readthedocs.io/en/latest/)
- [os](https://docs.python.org/3/library/os.html)

---
## DISCLAIMER:

I am not responsible for what you do and the information you retrieve with <strong>PDFparser</strong>.
