import sys
import os
import serial
import cv2
import pybullet as p
import mediapipe as mp
import webbrowser # Importar para abrir links
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_form import * # Importar la interfaz gráfica creada en Qt Designer}

try:
    ser = serial.Serial('COM4', baudrate=9600) #Puerto por defecto
except Exception as e:
    print(e)
    
# Ventana principal
class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Widget()  # Crear una instancia de la interfaz gráfica
        self.ui.setupUi(self)  
        
        self.index = 0
        
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

        # Index para optimizacion de ambiente
        self.ui.pushButton_7.clicked.connect(self.set_index_1)
        self.ui.pushButton_8.clicked.connect(self.set_index_2) #parametros manual
        self.ui.pushButton_12.clicked.connect(self.set_index_3) #webcam
        self.ui.pushButton_11.clicked.connect(self.set_index_4)
        self.ui.pushButton_10.clicked.connect(self.set_index_5) 
        self.ui.pushButton_9.clicked.connect(self.set_index_6)
        self.ui.pushButton_13.clicked.connect(self.set_index_7)
    
        # Configurar la lógica del botón para abrir un enlace de GitHub
        self.ui.GITbtn.clicked.connect(self.Gitbtn)

        # Establecemos Comunicacion SERIAL
        self.ui.pushButton_14.clicked.connect(self.ComunicacionARD)
        
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
        
        # Cargamos Diseño para pybullet
        p.connect(p.GUI)
        p.objeto = p.loadURDF("archivos_moveo/moveo_urdf/urdf/moveo_urdf.urdf", [0, 0, 0], globalScaling=2, useFixedBase=True)
        p.setGravity(0, 0, -10)
        self.ui.timer1 = QTimer(self)
        self.ui.timer1.start(50)
        self.ui.timer1.timeout.connect(self.update_robot)
        
        #--------------------------------Manuales--------------------------------
        
        #--------------------------------Joystick--------------------------------
        
        #--------------------------------Joystick--------------------------------
        
        #--------------------------------Parametros--------------------------------
        self.ui.horizontalSlider_3.valueChanged.connect(self.actualizar_articulacion_1)
        self.ui.horizontalSlider_6.valueChanged.connect(self.actualizar_articulacion_2)
        self.ui.horizontalSlider_5.valueChanged.connect(self.actualizar_articulacion_3)
        self.ui.horizontalSlider_4.valueChanged.connect(self.actualizar_articulacion_4)
        self.ui.horizontalSlider_2.valueChanged.connect(self.actualizar_articulacion_5)
        self.ui.horizontalSlider.valueChanged.connect(self.actualizar_articulacion_6)
        #--------------------------------Parametros--------------------------------

        #--------------------------------Camara--------------------------------
        self.capture = cv2.VideoCapture(1)
        self.ui.timer = QTimer(self)
        self.ui.timer.start(60)
        self.ui.timer.timeout.connect(self.update_image)
        
        #queda sacar angulos de movimiento para pasar a simulacion y comunicacion a ardduino
        
        #--------------------------------Camara--------------------------------
        
        #--------------------------------Manuales--------------------------------
        #--------------------------------Automaticos--------------------------------
        #--------------------------------Ajedrez--------------------------------
        
        #proximamente
        
        #--------------------------------Ajedrez--------------------------------
        #--------------------------------Joystick--------------------------------
        
        
        #--------------------------------Joystick--------------------------------
        #--------------------------------Parametros--------------------------------
        
        
        #--------------------------------Parametros--------------------------------
        #--------------------------------Predeterminados--------------------------------
        
        
        #--------------------------------Predeterminados--------------------------------
        #--------------------------------Automaticos--------------------------------
        self.show()
        '''
        base_link
        odom_joint
        Joint_1
        Joint_2
        Joint_3
        Joint_4
        Joint_5
        Gripper_Servo_Gear_Joint
        Tip_Gripper_Servo_Joint
        Gripper_Idol_Gear_Joint
        Tip_Gripper_Idol_Joint
        Pivot_Arm_Gripper_Servo_Joint
        Pivot_Arm_Gripper_Idol_Joint'''
        
    def actualizar_articulacion_1(self, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
        # Actualiza la posición de la articulación en PyBullet
        p.setJointMotorControl2(p.objeto, 1, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        
    def actualizar_articulacion_2(self, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
        # Actualiza la posición de la articulación en PyBullet
        p.setJointMotorControl2(p.objeto, 2, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        
    def actualizar_articulacion_3(self, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
        # Actualiza la posición de la articulación en PyBullet
        p.setJointMotorControl2(p.objeto, 3, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        
    def actualizar_articulacion_4(self, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
        # Actualiza la posición de la articulación en PyBullet
        p.setJointMotorControl2(p.objeto, 4, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        
    def actualizar_articulacion_5(self, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
        # Actualiza la posición de la articulación en PyBullet
        p.setJointMotorControl2(p.objeto, 5, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        
    def actualizar_articulacion_6(self, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
        # Actualiza la posición de la articulación en PyBullet
        p.setJointMotorControl2(p.objeto, 6, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        
    def update_robot(self):
        # Configura la cámara
        p.resetDebugVisualizerCamera(cameraDistance=1, cameraYaw=200, cameraPitch=-30, cameraTargetPosition=[0,0,1])
        p.stepSimulation()
        # Captura la imagen de la ventana de visualización
        width, height, rgba, depth, seg = p.getCameraImage(640, 480, renderer=p.ER_BULLET_HARDWARE_OPENGL)
        # Convierte los datos RGBA en un objeto de imagen de OpenCV
        bgr = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGR)
        imagen = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        # Convierte la imagen en un QPixmap
        qimage = QImage(imagen, width, height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        # Muestra el QPixmap en una etiqueta
        if self.index==2 :
            self.ui.labelrobparam.setPixmap(pixmap)
        if self.index==3 :
            self.ui.label_14.setPixmap(pixmap)
        
        
    def update_image(self):
        if self.index == 3:
            mpDraw = mp.solutions.drawing_utils
            mpPose = mp.solutions.pose
            pose = mpPose.Pose()
            success, img = self.capture.read()
            results = pose.process(img)
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    print(id, lm)
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED) 
            image = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
            # Mostrar el QImage en el QLabel
            self.ui.label_13.setPixmap(QPixmap.fromImage(image))
        
    def set_index_1(self):
        self.index = 1
        
    def set_index_2(self):
        self.index = 2

    def set_index_3(self):
        self.index = 3

    def set_index_4(self):
        self.index = 4

    def set_index_5(self):
        self.index = 5

    def set_index_6(self):
        self.index = 6
        
    def set_index_7(self):
        self.index = 7
          
    # Función para la comunicacion del Arduino 
    def ComunicacionARD(self):
        ser = serial.Serial(str(self.ui.lineEdit.text), baudrate=9600)  
       
        
    # Función para abrir el enlace de GitHub en el navegador predeterminado    
    def Gitbtn(self):
        webbrowser.open("https://github.com/LucasZds/Moveo-Control-GUI")
        
    '''  
            pasos del motor ---> sentido del motor ---> estado del motor
                motor 1 ---> motor 2 ---> ..... ---> pinza 
    Metodo envio de datos "255,0,0,255,0,0,255,0,0,255,0,0,255,0,0,255,0,0,255,0,0"
       datos = string concatenado  # Datos a enviar (en formato bytes)
        ser.write(datos.encode()) # Enviar string codificado en bits                                            '''   
        
    def enviar_datos(pasos_motor1, sentido_motor1, enable_motor1,
                pasos_motor2, sentido_motor2, enable_motor2,
                pasos_motor3, sentido_motor3, enable_motor3,
                pasos_motor4, sentido_motor4, enable_motor4,
                pasos_motor5, sentido_motor5, enable_motor5,
                pasos_motor6, sentido_motor6, enable_motor6,
                pasos_pinza, sentido_pinza, enable_pinza):
        datos = f"{pasos_motor1},{sentido_motor1},{enable_motor1},\
                {pasos_motor2},{sentido_motor2},{enable_motor2},\
                {pasos_motor3},{sentido_motor3},{enable_motor3},\
                {pasos_motor4},{sentido_motor4},{enable_motor4},\
                {pasos_motor5},{sentido_motor5},{enable_motor5},\
                {pasos_motor6},{sentido_motor6},{enable_motor6},\
                {pasos_pinza},{sentido_pinza},{enable_pinza},\n"
        ser.write(datos.encode()) # envía los datos al Arduino en formato de bytes
    
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