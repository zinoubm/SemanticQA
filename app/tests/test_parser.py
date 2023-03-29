import os
import re
from parser.parsers.pdf import PdfParser
from parser.parsers.txt import TxtParser
from parser.parsers.docx import DocxParser


from tests.data import dummy_pdf, dummy_txt, dummy_docx


def standarize(text):
    return re.sub(r"\s+", " ", text).strip()


def test_pdf_parser():
    text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor"
        "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud"
        "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    )

    temp_file_path = dummy_pdf(text)
    parsed_text = PdfParser.parse(temp_file_path)
    os.remove(temp_file_path)

    assert standarize(parsed_text) == standarize(text)


def test_txt_parser():
    text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor"
        "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud"
        "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    )

    temp_file_path = dummy_txt(text)
    parsed_text = TxtParser.parse(temp_file_path)
    os.remove(temp_file_path)

    assert standarize(parsed_text) == standarize(text)


def test_docx_parser():
    text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor"
        "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud"
        "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    )

    temp_file_path = dummy_docx(text)
    parsed_text = DocxParser.parse(temp_file_path)
    os.remove(temp_file_path)

    assert standarize(parsed_text) == standarize(text)
