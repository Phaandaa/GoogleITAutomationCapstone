from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate(file_path, title, content):
    doc = SimpleDocTemplate(file_path, pagesize=landscape(letter))
    styles = getSampleStyleSheet()

    elements = []

    title_text = Paragraph(title, styles["Title"])
    elements.append(title_text)
    elements.append(Spacer(1, 12))

    content_text = Paragraph(content, styles["Normal"])
    elements.append(content_text)

    doc.build(elements)