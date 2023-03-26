# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QToolBox, QVBoxLayout, QWidget)
import rc_img

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(710, 421)
        Widget.setMinimumSize(QSize(500, 300))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 174, 239, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        Widget.setPalette(palette)
        Widget.setStyleSheet(u"*{border:none;\n"
"background-color:rgb(0,174,239);\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(Widget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        self.slide_menu_container.setMinimumSize(QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QSize(0, 16777215))
        self.slide_menu_container.setStyleSheet(u"*{background-color:rgb(0,26,39);}\n"
"QPushButton{\n"
"background-color:rgb(0,26,39);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0,174,239);\n"
"}")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(196, 0))
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_9 = QFrame(self.slide_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.slide_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.toolBox = QToolBox(self.frame_5)
        self.toolBox.setObjectName(u"toolBox")
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        self.toolBox.setFont(font1)
        self.toolBox.setStyleSheet(u"QToolBox::tab{\n"
"border-radius:5px;\n"
"background-color:rgb(0,174,239);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 160, 244))
        self.horizontalLayout_6 = QHBoxLayout(self.page)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton_7.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)

        self.verticalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon1)

        self.verticalLayout_11.addWidget(self.pushButton_8)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.verticalLayout_11.addWidget(self.pushButton_12)


        self.horizontalLayout_6.addWidget(self.frame_10)

        icon3 = QIcon()
        icon3.addFile(u":/icons/move.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon3, u"Control Manual")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 160, 244))
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icons/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon4)

        self.verticalLayout_9.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_11)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setIcon(icon)

        self.verticalLayout_9.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setIcon(icon1)

        self.verticalLayout_9.addWidget(self.pushButton_9)

        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/icons/star.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon5)

        self.verticalLayout_9.addWidget(self.pushButton_13)


        self.verticalLayout_10.addWidget(self.frame_11)

        icon6 = QIcon()
        icon6.addFile(u":/icons/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon6, u"Control Automatico")

        self.verticalLayout_8.addWidget(self.toolBox)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.exit_button = QPushButton(self.frame_8)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon7)
        self.exit_button.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.exit_button, 0, Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main_body = QFrame(Widget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color:rgb(0,26,39);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(30, 30))
        self.frame.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,26,39);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0,174,239);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.open_close_side_bar_btn = QPushButton(self.frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon8)
        self.open_close_side_bar_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.header_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setFont(font2)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setStyleSheet(u"border-bottom:3px solid rgb(230,5,64);")
        self.lineEdit.setDragEnabled(False)

        self.horizontalLayout_7.addWidget(self.lineEdit, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton_14 = QPushButton(self.frame_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,26,39);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0,174,239);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.pushButton_14, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,26,39);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(166, 175, 179);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.minimize_window_button = QPushButton(self.frame_2)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_2)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon11 = QIcon()
        icon11.addFile(u":/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_2)
        self.close_window_button.setObjectName(u"close_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_content = QFrame(self.main_body)
        self.main_body_content.setObjectName(u"main_body_content")
        sizePolicy.setHeightForWidth(self.main_body_content.sizePolicy().hasHeightForWidth())
        self.main_body_content.setSizePolicy(sizePolicy)
        self.main_body_content.setFrameShape(QFrame.StyledPanel)
        self.main_body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.main_body_content)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.manualpar = QWidget()
        self.manualpar.setObjectName(u"manualpar")
        self.pushButton_2 = QPushButton(self.manualpar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 160, 80, 24))
        self.stackedWidget.addWidget(self.manualpar)
        self.manualwebcam = QWidget()
        self.manualwebcam.setObjectName(u"manualwebcam")
        self.pushButton_3 = QPushButton(self.manualwebcam)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 170, 80, 24))
        self.stackedWidget.addWidget(self.manualwebcam)
        self.manualjoy = QWidget()
        self.manualjoy.setObjectName(u"manualjoy")
        self.pushButton = QPushButton(self.manualjoy)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 130, 80, 24))
        self.stackedWidget.addWidget(self.manualjoy)
        self.autaje = QWidget()
        self.autaje.setObjectName(u"autaje")
        self.pushButton_4 = QPushButton(self.autaje)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(290, 140, 80, 24))
        self.stackedWidget.addWidget(self.autaje)
        self.autoJoy = QWidget()
        self.autoJoy.setObjectName(u"autoJoy")
        self.pushButton_5 = QPushButton(self.autoJoy)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(300, 140, 80, 24))
        self.stackedWidget.addWidget(self.autoJoy)
        self.autopara = QWidget()
        self.autopara.setObjectName(u"autopara")
        self.pushButton_6 = QPushButton(self.autopara)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(340, 140, 80, 24))
        self.stackedWidget.addWidget(self.autopara)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.horizontalLayout_8 = QHBoxLayout(self.mainPage)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_12 = QFrame(self.mainPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icons/chevron-down.svg"))

        self.verticalLayout_13.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_3.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_13.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icons/arrow-left.svg"))

        self.verticalLayout_13.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.mainPage)
        self.autopred = QWidget()
        self.autopred.setObjectName(u"autopred")
        self.pushButton_15 = QPushButton(self.autopred)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(310, 150, 80, 24))
        self.stackedWidget.addWidget(self.autopred)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_content)

        self.footen = QFrame(self.main_body)
        self.footen.setObjectName(u"footen")
        self.footen.setMinimumSize(QSize(0, 40))
        self.footen.setFrameShape(QFrame.StyledPanel)
        self.footen.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footen)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.footen)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.footen)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.GITbtn = QPushButton(self.frame_7)
        self.GITbtn.setObjectName(u"GITbtn")
        self.GITbtn.setMinimumSize(QSize(30, 30))
        self.GITbtn.setMaximumSize(QSize(70, 70))
        self.GITbtn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,174,239);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0,26,39);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.GITbtn.setIcon(icon13)
        self.GITbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.GITbtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.size_grip = QFrame(self.footen)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footen, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)


        self.retranslateUi(Widget)

        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Moveo Contol Panel", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"Joystick", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"Parametros", None))
        self.pushButton_12.setText(QCoreApplication.translate("Widget", u"WebCam", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Widget", u"Control Manual", None))
        self.pushButton_11.setText(QCoreApplication.translate("Widget", u"Ajedrez", None))
        self.pushButton_10.setText(QCoreApplication.translate("Widget", u"Joystick", None))
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"Parametros", None))
        self.pushButton_13.setText(QCoreApplication.translate("Widget", u"Predeterminados", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Widget", u"Control Automatico", None))
        self.exit_button.setText(QCoreApplication.translate("Widget", u"EXIT", None))
        self.open_close_side_bar_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Puerto COM", None))
        self.pushButton_14.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"pagina2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"webcam", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"pagina1", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"Moveo Software Control", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Software Libre creado para controlar brazo robotico moveo", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Seleciona el puerto conectado a tu controlador y luego pasa a la seccion del menu", None))
        self.label_4.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Widget", u"GUI - Moveo 2023", None))
        self.GITbtn.setText("")
    # retranslateUi

