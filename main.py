import sys
import os
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import QPropertyAnimation
from ui_form import * # Importar la interfaz gráfica creada en Qt Designer
import webbrowser # Importar para abrir links

# Ventana principal
class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Widget()  # Crear una instancia de la interfaz gráfica
        self.ui.setupUi(self)  
        
        # Configuracion general de la ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.setWindowIcon(QtGui.QIcon(":/icons/github.svg"))
        self.setWindowTitle("Moveo Control Software")
        
        # Configurar la lógica de los botones de la ventana
        QSizeGrip(self.ui.size_grip)
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        
        # Configurar la lógica de los botones para cambiar entre los modos manual y automático
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.manualjoy))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.manualpar))
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.manualwebcam))
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.autaje))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.autoJoy)) 
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.autopara))
        self.ui.pushButton_13.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.autopred))

        # Configurar la lógica del botón para abrir un enlace de GitHub
        self.ui.GITbtn.clicked.connect(self.Gitbtn)

        # Configurar la lógica de los eventos de movimiento del ratón para la ventana
        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:  
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow
        
        # Configurar la lógica del botón para abrir o cerrar el menú lateral
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
        
        #--------------------------------Ventana 1--------------------------------
        self.ui.pushButton_19.clicked.connect(self.sumavalor)
        self.ui.pushButton_18.clicked.connect(self.restavalor)
        self.ui.checkBox.clicked.connect(self.updateButtons)   
        
        #--------------------------------Ventana 1--------------------------------
        self.show()
        
    # Función para abrir el enlace de GitHub en el navegador predeterminado    
    def Gitbtn(self):
        webbrowser.open("https://github.com/LucasZds/Moveo-Control-GUI")
        
    def limites(self):
        x = self.ui.lineEdit_2.text()
        if x == "":
            x=0
        if int(x) > 179 :
            x = "179"
        if int(x) < -179 :
            x = "-179"
        return x
        
    def sumavalor(self):
        x = self.limites()
        self.ui.lineEdit_2.setText(str(int(x)+1)) 
            
    def restavalor(self):
        x = self.limites()
        self.ui.lineEdit_2.setText(str(int(x)-1)) 
        
    
        
    
    # Función para animar y mostrar u ocultar el menú lateral
    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()
        if width == 0:
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/align-left.svg"))

        # Se crea una animación que cambia el ancho máximo del menú lateral de su ancho actual a un nuevo ancho
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        
    def updateButtons(self):
        if self.ui.checkBox.isChecked():
            self.ui.pushButton_18.setEnabled(True)
            self.ui.pushButton_19.setEnabled(True)
            self.ui.lineEdit_2.setEnabled(True)
        else:
            self.ui.pushButton_18.setEnabled(False)
            self.ui.pushButton_19.setEnabled(False)
            self.ui.lineEdit_2.setEnabled(False)
        
    # Función para guardar la posición global del mouse en la ventana al hacer clic
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    # Función para restaurar o maximizar la ventana
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/minimize-2.svg"))

# Código para iniciar la aplicación y mostrar la ventana principal
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        sys.exit(1)