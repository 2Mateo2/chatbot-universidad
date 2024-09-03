from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import json


class ConversacionPDFGenerator:
    def __init__(self, json_file_path, pdf_file_path):
        self.json_file_path = json_file_path
        self.pdf_file_path = pdf_file_path
        self.conversacion = []

    def load_conversacion_from_json(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
            self.conversacion = json.load(json_file)

    def generate_pdf(self):
        doc = SimpleDocTemplate(self.pdf_file_path, pagesize=letter)

        styles = getSampleStyleSheet()
        user_style = ParagraphStyle(name="UserStyle", parent=styles["Normal"])
        user_style.alignment = 0
        user_style.textColor = colors.HexColor("#000202")

        chatbot_style = ParagraphStyle(name="ChatbotStyle", parent=styles["Normal"])
        chatbot_style.alignment = 0
        chatbot_style.textColor = colors.HexColor("#DE1333")

        story = []

        for mensaje in self.conversacion:

            if "user" in mensaje.keys():
                story.append(Paragraph(
                    f" Estudiante: {mensaje['user']}",
                    user_style,
                    encoding="UTF-8"
                ))

            if "bot" in mensaje.keys():
                story.append(Paragraph(
                    f" SairaBot: {mensaje['bot']}",
                    chatbot_style,
                    encoding="UTF-8"
                ))

            story.append(Spacer(1, 12))

        doc.build(story)

        print(f'El archivo PDF "{self.pdf_file_path}" ha sido creado con éxito.')