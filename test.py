import pybullet as p
import cv2

# Carga el archivo URDF y crea el objeto
p.connect(p.GUI)
objeto = p.loadURDF("ruta/al/archivo.urdf")
# Configura la cámara
p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=45, cameraPitch=-30, cameraTargetPosition=[0,0,0])

# Captura la imagen de la ventana de visualización
width, height, rgba, depth, seg = p.getCameraImage(640, 480, renderer=p.ER_BULLET_HARDWARE_OPENGL)

# Convierte los datos RGBA en un objeto de imagen de OpenCV
bgr = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGR)
imagen = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

# Convierte la imagen en un QPixmap
qimage = QImage(imagen, width, height, QImage.Format_RGB888)
pixmap = QPixmap.fromImage(qimage)

# Muestra el QPixmap en una etiqueta
self.ui.label.setPixmap(pixmap)