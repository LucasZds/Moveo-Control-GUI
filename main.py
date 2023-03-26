import sys
import os
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import QPropertyAnimation
from ui_form import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Widgete()
        self.ui.setupUi(self)  
        
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.setWindowIcon(QtGui.QIcon(":/icons/github.svg"))
        self.setWindowTitle("Moveo Control Software")
        QSizeGrip(self.ui.size_grip)

        
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.GITbtn.clicked.connect(self.Git)
        
        def Git(self):
               

        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:  
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.show()

    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()
        if width == 0:
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/align-left.svg"))
            
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    





    
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/minimize-2.svg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
