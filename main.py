import sys
import time
import os
import serial
import cv2
import math
import pygame
import pybullet as p
import mediapipe as mp
from math import atan2, degrees
import webbrowser # Importar para abrir links
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_form import * # Importar la interfaz gráfica creada en Qt Designer
    
# Ventana principal
class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Widget()  # Crear una instancia de la interfaz gráfica
        self.ui.setupUi(self)  

        # Pagina inicial, index = 0
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainPage)
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
        self.ui.close_window_button.clicked.connect(lambda: self.closeapp())
        self.ui.exit_button.clicked.connect(lambda: self.closeapp())
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
        self.ui.pushButton_7.clicked.connect(lambda:self.set_index(1)) #joystick
        self.ui.pushButton_8.clicked.connect(lambda:self.set_index(2)) #manual
        self.ui.pushButton_12.clicked.connect(lambda:self.set_index(3)) #webcam
        self.ui.pushButton_11.clicked.connect(lambda:self.set_index(4))
        self.ui.pushButton_10.clicked.connect(lambda:self.set_index(5)) 
        self.ui.pushButton_9.clicked.connect(lambda:self.set_index(6))
        self.ui.pushButton_13.clicked.connect(lambda:self.set_index(7))
    
        # Configurar la lógica del botón para abrir un enlace de GitHub
        self.ui.GITbtn.clicked.connect(self.Gitbtn)

        # Establecemos Comunicacion SERIAL
        try:
            self.ser = serial.Serial("COM4", baudrate=9600) #Puerto por defecto
        except Exception as e:
            print(e)
        
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
        
        pygame.init()
        pygame.joystick.init()
        self.control = pygame.joystick.Joystick(0)
        self.control.init()
        self.ejes = [0] * self.control.get_numaxes()
        self.ui.timer2 = QTimer(self)
        self.ui.timer2.start(60)
        self.ui.timer2.timeout.connect(self.leer_entrada)
         
        #pendiente comunicacion con arduino
        #--------------------------------Joystick--------------------------------
        
        #--------------------------------Parametros--------------------------------
        self.ui.horizontalSlider_3.valueChanged.connect(lambda valor: self.actualizar_articulacion(1, valor))
        self.ui.horizontalSlider_6.valueChanged.connect(lambda valor: self.actualizar_articulacion(2, valor))
        self.ui.horizontalSlider_5.valueChanged.connect(lambda valor: self.actualizar_articulacion(3, valor))
        self.ui.horizontalSlider_4.valueChanged.connect(lambda valor: self.actualizar_articulacion(4, valor))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda valor: self.actualizar_articulacion(5, valor))
        self.ui.horizontalSlider.valueChanged.connect(lambda valor: self.actualizar_articulacion(6, valor))
        self.ui.pushButtonpara.clicked.connect(self.enviodedatosparametros)
        self.ui.pushButtonres.clicked.connect(self.enviodedatosparametrosres)
        #inicialmente se necesia comunicacion con arduino
        #--------------------------------Parametros--------------------------------

        #--------------------------------Camara--------------------------------
        self.capture = cv2.VideoCapture(0)
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.angulo = 0
        self.angulocuerpo = 0
        self.ui.timer = QTimer(self)
        self.ui.timer.start(60)
        self.ui.timer.timeout.connect(self.update_image)
        self.anguloanterior = 0
        #queda comunicacion a arduino
        
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
        se deja un index como 1 para optimizar, luego se pasa a muestrear las posiciones de los 
        botones del joystick mediante pygame para sacarlos a una lista. en caso de tener popsicion 4 o 5 
        seteamos valores a 0 ya que esas posiciones por defalt estan en -1. luego se envian cada una de las posiciones
        de la lista para arduino mediante comunicacion se actualiza para las labels y se deja un indice en pantalla
        
        '''
    def enviodedatosparametrosres(self):
        self.ui.horizontalSlider.setValue(255)
        self.ui.horizontalSlider_2.setValue(255)
        self.ui.horizontalSlider_3.setValue(255)
        self.ui.horizontalSlider_4.setValue(255)
        self.ui.horizontalSlider_5.setValue(255)
        self.ui.horizontalSlider_6.setValue(255)
        
        self.enviar_datos((self.ui.horizontalSlider_3.value()-255), #MOTOR 1
                        (self.ui.horizontalSlider_6.value()-255), #MOTOR 3
                        (self.ui.horizontalSlider_6.value()-255), #MOTOR 2
                        (self.ui.horizontalSlider_4.value()-255), #MOTOR 4
                        (self.ui.horizontalSlider_5.value()-255), #MOTOR 5
                        (self.ui.horizontalSlider_2.value()-255), #MOTOR 6
                        (self.ui.horizontalSlider.value()-255)) #PINZA
    def enviodedatosparametros(self):
        self.enviar_datos((self.ui.horizontalSlider_3.value()-255), #MOTOR 1
                        ((self.ui.horizontalSlider_6.value()-255)*-1), #MOTOR 3
                        (self.ui.horizontalSlider_6.value()-255), #MOTOR 2
                        ((self.ui.horizontalSlider_4.value()-255)*-1), #MOTOR 4
                        (self.ui.horizontalSlider_5.value()-255), #MOTOR 5
                        ((self.ui.horizontalSlider_2.value()-255)*-1), #MOTOR 6
                        (self.ui.horizontalSlider.value()-255)) #PINZA
        
    def leer_entrada(self):
        # Actualizacion de variables del joystick
        if self.index == 1:
            num_ejes = 0
            if self.index == 1: # Optimizacion de codigo por index
                pygame.event.pump()
                num_ejes = self.control.get_numaxes()
                
                # Actualizar los valores de los ejes
                for i in range(num_ejes):
                    axis_value = round(self.control.get_axis(i), 2)
                    if abs(axis_value) > 0.6:
                        if i < 4 :
                            self.ejes[i] += axis_value + self.ejes[i]
                        if i == 4 or i == 5:
                            if axis_value > 0.5:
                                self.ejes[i] += axis_value
                # Obtener los valores de los ejes x e y
                x = self.ejes[0]
                y = self.ejes[1]

                # Calcular el ángulo a partir de los valores de los ejes x e y
                angle = degrees(atan2(y, x)) % 360

                # Comprobar si el ángulo se encuentra dentro de los rangos permitidos
                if angle >= 30 and angle <= 330 or angle >= 150 and angle <= 330:
                    self.ejes[0] = x

                if 60 <= angle <= 120 or 240 <= angle <= 300:
                    self.ejes[1] = y

                
                self.enviar_datos(int(self.ejes[0]),int(self.ejes[1]),0,int(self.ejes[3]),
                                int(self.ejes[2]),int(self.ejes[4]),int(self.ejes[5]))
                time.sleep(0.5)

                    # Crear una lista con los Labels y textos correspondientes
                labels = [(self.ui.label_26, "Joystick ix"), (self.ui.label_27, "Joystick iy"),
                        (self.ui.label_28, "Joystick dx"), (self.ui.label_29, "Joystick dy"),
                        (self.ui.label_30, "Gatillo izquierdo"), (self.ui.label_31, "Gatillo derecho")]

                # Actualizar el texto para cada Label usando un bucle for
                for i, (label, text) in enumerate(labels):
                    label.setText(f"{text} {int(self.ejes[i])}")
                    self.actualizar_articulacion(i,450+int(self.ejes[i]))
                

    '''             # Envio de datos para movimientos
                     Botones y ejes a utilizar en formato de array [i]
                        joystick izuierda     joystick derecha     boton "A"      boron "B"
                        Eje 0=0  Eje 1=-0     Eje 2=0 Eje 3=-0     Eje 4 = -1     Eje 5 = -1
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
    def closeapp(self):
        self.ser.close()
        self.close()
        
    def actualizar_articulacion(self, num_articulacion, valor_slider):
        # Convierte el valor del slider al rango de valores aceptable para la articulación
        valor_articulacion = (valor_slider-255)/255
    
        # Actualiza la posición de la articulación en PyBullet según el número de articulación
        if num_articulacion == 1:
            p.setJointMotorControl2(p.objeto, 1, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        elif num_articulacion == 2:
            p.setJointMotorControl2(p.objeto, 2, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        elif num_articulacion == 3:
            p.setJointMotorControl2(p.objeto, 3, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        elif num_articulacion == 4:
            p.setJointMotorControl2(p.objeto, 4, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        elif num_articulacion == 5:
            p.setJointMotorControl2(p.objeto, 5, p.POSITION_CONTROL, targetPosition=valor_articulacion)
        elif num_articulacion == 6:
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
        if self.index==1:
            self.ui.labelrob_2.setPixmap(pixmap)
        if self.index==2 :
            self.ui.labelrobparam.setPixmap(pixmap)
        if self.index==3 :
            self.ui.label_14.setPixmap(pixmap)
        
    
    '''Detecta los puntos de referencia del cuerpo y calcula los ángulos del brazo y la rotación 
    del cuerpo en tiempo real a partir de una webcam y muestra los resultados en un QPixmap.
    Además, actualiza los valores de "self.angulo" y "self.angulocuerpo" si los ángulos detectados
    están dentro de un rango específico.'''      
    def update_image(self):
        # Index para optimizacion de recursos
        if self.index == 3:
            # Leer el frame actual de la captura de video
            success, img = self.capture.read()
            
            # Procesar el frame actual y obtener los landmarks de la pose
            results = self.pose.process(img)
            landmarks = results.pose_landmarks.landmark
            
            # Obtener los puntos de referencia de la muñeca, el codo y el hombro del brazo derecho y nariz
            wrist = landmarks[self.mpPose.PoseLandmark.RIGHT_WRIST]
            elbow = landmarks[self.mpPose.PoseLandmark.RIGHT_ELBOW]
            shoulder = landmarks[self.mpPose.PoseLandmark.RIGHT_SHOULDER]
            nose = landmarks[self.mpPose.PoseLandmark.NOSE]

            # Calcular el ángulo del codo utilizando funciones trigonométricas
            angle = math.degrees(math.atan2(wrist.y - elbow.y, wrist.x - elbow.x) -
                                math.atan2(shoulder.y - elbow.y, shoulder.x - elbow.x))
            angle = round(angle, 2)
            
             # Calcular el ángulo entre la línea que une el hombro y la nariz y la línea que une el codo y la nariz
            angle_body = math.degrees(math.atan2(nose.y - shoulder.y, nose.x - shoulder.x) -
                                  math.atan2(nose.y - elbow.y, nose.x - elbow.x))
            angle_body = round(angle_body, 2)
        
            # Mostrar los ángulos en la imagen
            cv2.putText(img, f"Angulo rotacion: {int(angle_body*-1)}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(img, f"Angulo brazo: {int(angle*-1)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  
            
            '''# Si el ángulo del cuerpo es adecuado, actualizamos variable
            if int(angle_body*-1) < 90 and int(angle_body*-1) > -50:
                self.angulocuerpo=angle_body*-1
                self.enviar_datos(int(self.angulocuerpo),
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,)
                p.setJointMotorControl2(p.objeto, 1, p.POSITION_CONTROL, targetPosition=self.angulocuerpo)'''

            
            
            # Si el ángulo del cuerpo es adecuado, actualizamos variable
            
            if int(angle) < 190 and int(angle) > -20:
                if (angle*-1) > (self.anguloanterior + 5) or (angle*-1) < (self.anguloanterior - 5 ):
                    self.angulo = int(angle*-1)
                    self.anguloanterior = int(angle*-1) 
                    valor_articulacion = (self.angulo-90)/255
                    valor_articulacion1 = (self.angulo-40)/255
                    # Actualiza la posición de la articulación en PyBullet
                    p.setJointMotorControl2(p.objeto, 2, p.POSITION_CONTROL, targetPosition=valor_articulacion)
                    p.setJointMotorControl2(p.objeto, 3, p.POSITION_CONTROL, targetPosition=valor_articulacion1)
                    self.enviar_datos(0,int(self.angulo),0,0,0,0,0)
                    time.sleep(0.05)
                    

            # Mostrar los puntos de los brazos y la línea del brazo derecho
            x1, y1 = int(wrist.x * img.shape[1]), int(wrist.y * img.shape[0])
            x2, y2 = int(elbow.x * img.shape[1]), int(elbow.y * img.shape[0])
            x3, y3 = int(shoulder.x * img.shape[1]), int(shoulder.y * img.shape[0])
            cv2.circle(img, (x1, y1), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 5, (0, 255, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.line(img, (x2, y2), (x3, y3), (255, 0, 0), 2)

            # Mostrar el QImage en el QLabel
            image = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
            self.ui.label_13.setPixmap(QPixmap.fromImage(image))
        
    def set_index(self,valor):
        self.index = valor
        
          
    # Función para la comunicacion del Arduino 
    def ComunicacionARD(self):
        try:
            puerto = self.ui.Puertocom.text()
            self.ser = serial.Serial(puerto, baudrate=9600) #Puerto por defecto            

        except Exception as e:
            print(e) 
       
        
    # Función para abrir el enlace de GitHub en el navegador predeterminado    
    def Gitbtn(self):
        webbrowser.open("https://github.com/LucasZds/Moveo-Control-GUI")
        
    '''  
                        pasos del motor
                motor 1 ---> motor 2 ---> ..... ---> pinza 
    Metodo envio de datos "255,255,255,255,255,255,255"
       datos = string concatenado  # Datos a enviar (en formato bytes)
        ser.write(datos.encode()) # Enviar string codificado en bits                                            '''   
        
    def enviar_datos(self,pasos_motor1,
                pasos_motor2,
                pasos_motor3,
                pasos_motor4,
                pasos_motor5,
                pasos_motor6,
                pasos_pinza):
        datos = f"{pasos_motor1},\
                {pasos_motor2},\
                {pasos_motor3},\
                {pasos_motor4},\
                {pasos_motor5},\
                {pasos_motor6},\
                {pasos_pinza},\n"
        self.ser.write(datos.encode("UTF-8")) # envía los datos al Arduino en formato de bytes
        print("Serial " + datos)
        
    
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