from urllib.request import urlretrieve
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from pypdf import PdfReader
from colorama import Fore

import argparse
import colorama
import requests
import os

def downloader(pdf_url):
    urlretrieve(pdf_url, ".pdf" )
    reader = PdfReader(".pdf")
    meta = reader.metadata
    colorama.init()

    i=0
    try:
        if meta.title:
            files = os.listdir()
            if f"{meta.title}" in files:
                while True:
                    if os.path.isfile(f"{meta.title}{i}.pdf"):
                        i+=1
                    else:
                        os.rename(".pdf", f"{meta.title}{i}.pdf")
                        print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.RED}{meta.title}{i}.pdf {Fore.WHITE}successfully downloaded! \n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}You can extract the informations by using -e | --extract")
                        break                      
            else:
                os.rename(".pdf", f"{meta.title}.pdf")
                print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.RED}{meta.title}.pdf {Fore.WHITE}successfully downloaded! \n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}You can extract the informations by using -e | --extract")
        else:
            files = os.listdir()
            if "Untitled.pdf" in files:
                while True:
                    if os.path.isfile(f"Untitled{i}.pdf"):
                        i+=1
                    else:
                        os.rename(".pdf", f"Untitled{i}.pdf")
                        print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.RED}Untitled{i}.pdf {Fore.WHITE}successfully downloaded! \n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}You can extract the informations by using -e | --extract")
                        break
            else:
                os.rename(".pdf", "Untitled.pdf")
                print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.RED}Untitled.pdf {Fore.WHITE}successfully downloaded! \n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}You can extract the informations by using -e | --extract")      
    except Exception:
        print(f"{Fore.LIGHTGREEN_EX}[!] {Fore.WHITE}An error occured, this {Fore.RED}PDF file {Fore.WHITE}can't be downloaded.")

def finder(website_url):
    colorama.init()
    r = requests.get(website_url)
    page = r.text
    soup = BeautifulSoup(page, "html.parser")
    colorama.init()
    
    if r.status_code == 404:
        print(f"\n{Fore.LIGHTGREEN_EX}[!] {Fore.WHITE}The website address is invalid.")
    else:
        i=0
        for a in soup.find_all("a", href=True):
            pdf_url = a['href']
            if ".pdf" in pdf_url:
                i+=1
                print(f"\n{Fore.LIGHTGREEN_EX}[{i}] {Fore.WHITE}{pdf_url}:")
                if i>0:
                    try:
                        downloader(pdf_url)
                    except Exception:
                        downloader(f"{website_url}{pdf_url}")            
        print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}There is {Fore.RED}{i} PDF files {Fore.WHITE}in this website.")

def extractor(pdf_name):
    reader = PdfReader(pdf_name)
    meta = reader.metadata
    colorama.init()

    stats = f"""\nInformations From {Fore.RED}{pdf_name}{Fore.WHITE}:\n
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Title: {meta.title}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Author: {meta.author}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Creator: {meta.creator}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Producer: {meta.producer}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Creation Date: {meta.creation_date}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Modification Date: {meta.modification_date}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Subject: {meta.subject}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Extensible Metadata Platform: {meta.xmp_metadata}
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Number of pages: {len(reader.pages)}
    """
    print(stats)

    if len(reader.pages) > 1:
        page = reader.pages[0]
        text = page.extract_text()
        print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Text from page {Fore.RED}1{Fore.WHITE}:\n{text}")
        answer = input(f"\n{Fore.LIGHTGREEN_EX}[?] {Fore.WHITE}Do you want to see the other pages? (Y/N): ").lower()
        for i in range(1, len(reader.pages)):
            if answer != "y":
                break
            else:
                page = reader.pages[i]
                text = page.extract_text()
                print(f"\n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Text from page {Fore.RED}{i+1}{Fore.WHITE}:\n{text}\n")
    else:
        print(f"""\n{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Text from the page:\n{text}""")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--download', help="Put the URL of the PDF file you want to download.", dest='pdf_url')
    parser.add_argument('-f', '--find', help="Find all the PDF in a website with his URL.", dest='website_url' )
    parser.add_argument('-e', '--extract', help="Put the name of the PDF previously downloaded to download it and extract all the informations.", dest='pdf_name' )
    args = parser.parse_args()

    if args.pdf_url:
        downloader(args.pdf_url)
    elif args.website_url:
        finder(args.website_url)
    elif args.pdf_name:
        extractor(args.pdf_name)
    else:
        colorama.init()
        print(F"""
    {Fore.RED}__________________                           
    {Fore.RED}| ___ \  _  \  ___|                      
    {Fore.RED}| |_/ / | | | |_{Fore.WHITE} _ __   __ _ _ __ ___  ___ _ __ 
    {Fore.RED}|  __/| | | |  _{Fore.WHITE}| '_ \ / _` | '__/ __|/ _ \ '__|
    {Fore.RED}| |   | |/ /| | {Fore.WHITE}| |_) | (_| | |  \__ \  __/ |   
    {Fore.RED}\_|   |___/ \_| {Fore.WHITE}| .__/ \__,_|_|  |___/\___|_|   
    {Fore.RED}                {Fore.WHITE}| |                             
    {Fore.RED}                {Fore.WHITE}|_|                                                                                 

    {Fore.LIGHTGREEN_EX}USAGE:
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}python3 pdfparser.py -d | --download [PDF LINK] : Download a PDF by using his web link.
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}python3 pdfparser.py -f | --find [WEB PAGES] : Find all the PDF inside a web pages.
    {Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}python3 pdfparser.py -e | --extract [PDF NAME] : Extract all the MetaData from the PDF.
    """)

if __name__ == "__main__":
  main()
