from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtCore import QCoreApplication
from core.chatbot import get_response, llenarJson, guardarJson
from core.pdf import ConversacionPDFGenerator

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setGeometry(200, 200, 600, 400)

        self.conversation_text = QTextEdit()
        self.conversation_text.setReadOnly(True)
        self.conversation_text.setStyleSheet("font-size: 18px; color: black;")

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Escribe un mensaje...")
        self.user_input.setStyleSheet("font-size: 14px; ")
        self.user_input.returnPressed.connect(self.send_message)

        # Botón para enviar mensaje
        send_button = QPushButton("Enviar")
        send_button.setStyleSheet("font-size: 14px; background-color: #2196F3; color: white;")
        send_button.clicked.connect(self.send_message)

        # Botón para generar PDF
        pdf_button = QPushButton("Salir y guardar la conversación en un PDF")
        pdf_button.setStyleSheet("font-size: 14px; background-color: red; color: white;")
        pdf_button.clicked.connect(self.generate_pdf)

        # Diseño de la ventana
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.conversation_text)
        central_layout.addWidget(self.user_input)
        central_layout.addWidget(send_button)
        central_layout.addWidget(pdf_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def send_message(self):
        user_message = self.user_input.text()

        user_format = QTextCharFormat()
        user_format.setForeground(QColor("#2196F3"))
        self.conversation_text.setCurrentCharFormat(user_format)
        self.conversation_text.append("Tú: " + user_message)

        bot_format = QTextCharFormat()
        bot_format.setForeground(QColor("black"))
        self.conversation_text.setCurrentCharFormat(bot_format)

        # Obtener la respuesta del chatbot
        chatbot_response = get_response(user_message)
        self.conversation_text.append("SairaBot: " + chatbot_response)

        # Llenar el JSON con la conversación
        llenarJson(user_message)

        self.user_input.clear()

    def generate_pdf(self):
        guardarJson()
        json_file_path = 'data/conversacion/conversacion.json'
        pdf_file_path = 'data/conversacion/conversacion.pdf'
        conversacion_generator = ConversacionPDFGenerator(json_file_path, pdf_file_path)
        conversacion_generator.load_conversacion_from_json()
        conversacion_generator.generate_pdf()

        QMessageBox.information(self, "Conversación guardada", 
                                "Fue un placer atenderte. Tu conversación se guardó en un PDF.")
        
        # Cerrar la aplicación
        QCoreApplication.quit()

