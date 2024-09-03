import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from view.view_principal import ChatbotWindow

class IntroMessageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Introducción")
        self.setGeometry(200, 200, 600, 400)

        # Crear un widget central y un diseño vertical
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Crear una etiqueta para mostrar el mensaje informativo
        info_label = QLabel("¡Hola y bienvenido al Chatbot de la Universidad Barranquilla!\n\n"
                            "Soy SairaBot, tu asistente virtual para todo lo relacionado con la universidad. "
                            "Estoy aquí para ayudarte con información sobre nuestros programas, requisitos de matrícula, "
                            "horarios, precios y cualquier otra duda que puedas tener.\n\n"
                            "Para comenzar, simplemente haz clic en el botón 'Continuar' y estaré encantada de asistirte.")
        info_label.setStyleSheet("font-size: 16px; padding: 20px;")
        info_label.setWordWrap(True)

        # Crear un botón para continuar
        continue_button = QPushButton("Continuar")
        continue_button.setStyleSheet("font-size: 14px; background-color: #2196F3; color: white;")
        continue_button.clicked.connect(self.open_chatbot)

        # Agregar la etiqueta y el botón al diseño
        layout.addWidget(info_label)
        layout.addWidget(continue_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_chatbot(self):
        self.close()
        self.chatbot_window = ChatbotWindow()
        self.chatbot_window.show()

