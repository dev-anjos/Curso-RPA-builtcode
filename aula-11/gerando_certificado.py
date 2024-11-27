from docx import Document
from docx.shared import Pt

arquivoWord = Document("Certificado1.docx")

estilo = arquivoWord.styles["Normal"]

for paragrafo in arquivoWord.paragraphs:
    if "@nome" in paragrafo.text:
        paragrafo.text = "Juan Pedro Anjos da silva"
        font = estilo.font
        font.name = "Calibri (Corpo)"
        font.size = Pt(24)

arquivoWord.save('Certifcado.docx')

