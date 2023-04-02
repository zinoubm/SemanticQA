from textwrap3 import dedent
from unidecode import unidecode
from parser.parsers.pdf import PdfParser
import re


def chunk_text(text, max_size=4000):
    paragraphs = dedent(text)
    ascii_paragraphs = re.findall(r"[^.?!]+[(\.)?!]", unidecode(paragraphs))

    chuncks = []
    chunck = ""
    for sentence in ascii_paragraphs:
        if len(chunck) + len(sentence) < max_size:
            chunck += sentence
        else:
            chuncks.append(chunck.strip())
            chunck = ""

    return chuncks


if __name__ == "__main__":

    pdf_path = "TheTwitterUserAgreement_1.pdf"

    text = PdfParser.parse(pdf_path)

    chuncks = chunk_text(text, 3500)

    for chunck in chuncks:
        print(chunck)
        print("------------")
