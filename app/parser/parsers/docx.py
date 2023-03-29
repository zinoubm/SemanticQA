from parser.interface import ParserInterface
import pdfplumber


class PdfParser(ParserInterface):
    def parse(file_path) -> str:
        pdf = pdfplumber.open(file_path)
        return " ".join([page.extract_text() for page in pdf.pages])
