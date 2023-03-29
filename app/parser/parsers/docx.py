from parser.interface import ParserInterface
import docx


class DocxParser(ParserInterface):
    def parse(file_path) -> str:
        document = docx.Document(file_path)
        return " ".join([paragraph.text for paragraph in document.paragraphs])
