import pygame
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.etiqueta = QLabel("Presiona un botón del control", self)
        self.setCentralWidget(self.etiqueta)

        pygame.init()
        pygame.joystick.init()
        self.control = pygame.joystick.Joystick(0)
        self.control.init()

        # Inicializar la lista de botones y ejes
        self.ejes = [0] * self.control.get_numaxes()

    def leer_entrada(self):
        pygame.event.pump()
   
        num_ejes = self.control.get_numaxes()


        # Actualizar los valores de los ejes
        for i in range(num_ejes):
            self.ejes[i] = round(self.control.get_axis(i), 2)

        texto_ejes = ", ".join([f"Eje {i}: {self.ejes[i]}" for i in range(num_ejes)])
        self.etiqueta.setText(texto_ejes)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    timer = QTimer()
    timer.timeout.connect(ventana.leer_entrada)
    timer.start(100) # Actualizar la entrada cada 100 milisegundos
    app.exec_()
