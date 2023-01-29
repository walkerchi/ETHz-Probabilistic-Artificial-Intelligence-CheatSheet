"""
    you may install fitz and PyMuPDF first
    >>> pip install fitz
    >>> pip install PyMuPDF
   
"""

import fitz 
import os 
import argparse

def pdf2png(pdf_path, zoom):
    if not os.path.exists(pdf_path):
        raise FileExistsError(f"{os.path.abspath(pdf_path)} not exits")
    pdf = fitz.open(pdf_path)
 
    for i in range(0, pdf.pageCount):
        page = pdf[i]
        pm = page.getPixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        pm.writePNG(pdf_path[:-4]+f"{i}.png")
    
    pdf.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser("This is a pdf to png converter based on fitz")
    parser.add_argument("-p", "--path", type=str,
                        default="Probabilistic_Artificial_Intelligence_CheatSheet.pdf")
    parser.add_argument("-z","--zoom", type=int, default=3)
    config = parser.parse_args()
    pdf2png(config.path, config.zoom)

