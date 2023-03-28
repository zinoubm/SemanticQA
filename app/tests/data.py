from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph


def dummy_pdf(text: str):
    # debug
    print("raw text")
    print(text)

    temp_file_path = "/tmp/temp_file"

    # Set up the PDF canvas and page size
    c = canvas.Canvas(temp_file_path, pagesize=letter)

    # Create a style for the paragraph
    style = ParagraphStyle(
        name="Normal", alignment=TA_CENTER, fontName="Helvetica", fontSize=12
    )

    # Add Lorem text to the PDF
    p = Paragraph(text, style=style)
    p.wrapOn(c, inch * 6, inch * 4)
    p.drawOn(c, inch * 2, inch * 5)

    # Save the PDF file
    c.save()

    return temp_file_path


def dummy_txt(text: str):
    temp_file_path = "/tmp/temp_file"

    with open(temp_file_path, "w") as file:
        file.write(text)

    return temp_file_path
