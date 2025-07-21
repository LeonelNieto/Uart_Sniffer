# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uart_sniffer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTextBrowser, QWidget)
from resources import resourcer_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1017, 490)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: #f0f0f0;\n"
"}\n"
"")
        self.tab_uart = QTabWidget(self.centralwidget)
        self.tab_uart.setObjectName(u"tab_uart")
        self.tab_uart.setGeometry(QRect(280, 80, 711, 391))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.tab_uart.setFont(font)
        self.tab_uart.setStyleSheet(u"\n"
"QTabBar::tab {\n"
"    background: #2d2d2d;\n"
"    color: #cccccc;\n"
"    padding: 4px 7px;\n"
"    border: 1px solid #3c3c3c;\n"
"    border-bottom: none;\n"
"    border-top-left-radius: 1px;\n"
"    border-top-right-radius: 1px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #007acc; \n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #007acc;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #3c3c3c;\n"
"    top: -1px; \n"
"}\n"
"")
        self.tab_tx = QWidget()
        self.tab_tx.setObjectName(u"tab_tx")
        self.display_tx = QTextBrowser(self.tab_tx)
        self.display_tx.setObjectName(u"display_tx")
        self.display_tx.setGeometry(QRect(20, 20, 661, 331))
        self.tab_uart.addTab(self.tab_tx, "")
        self.tab_rx = QWidget()
        self.tab_rx.setObjectName(u"tab_rx")
        self.display_rx = QTextBrowser(self.tab_rx)
        self.display_rx.setObjectName(u"display_rx")
        self.display_rx.setGeometry(QRect(20, 20, 661, 331))
        self.tab_uart.addTab(self.tab_rx, "")
        self.tab_tx_and_rx = QWidget()
        self.tab_tx_and_rx.setObjectName(u"tab_tx_and_rx")
        self.display_tx_and_rx = QTextBrowser(self.tab_tx_and_rx)
        self.display_tx_and_rx.setObjectName(u"display_tx_and_rx")
        self.display_tx_and_rx.setGeometry(QRect(20, 20, 661, 331))
        self.tab_uart.addTab(self.tab_tx_and_rx, "")
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(30, 30, 36, 36))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_start.setFont(font1)
        self.btn_start.setAutoFillBackground(False)
        self.btn_start.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-image: url(:/icons/play-button.svg);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(100, 30, 38, 38))
        self.btn_stop.setFont(font1)
        self.btn_stop.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/icons/stop-button.svg);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.cmb_baudrate_tx = QComboBox(self.centralwidget)
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.addItem("")
        self.cmb_baudrate_tx.setObjectName(u"cmb_baudrate_tx")
        self.cmb_baudrate_tx.setGeometry(QRect(150, 150, 111, 31))
        self.cmb_baudrate_tx.setFont(font1)
        self.cmb_baudrate_rx = QComboBox(self.centralwidget)
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.addItem("")
        self.cmb_baudrate_rx.setObjectName(u"cmb_baudrate_rx")
        self.cmb_baudrate_rx.setGeometry(QRect(150, 330, 111, 31))
        self.cmb_baudrate_rx.setFont(font1)
        self.lb_com_port_tx = QLabel(self.centralwidget)
        self.lb_com_port_tx.setObjectName(u"lb_com_port_tx")
        self.lb_com_port_tx.setGeometry(QRect(30, 200, 71, 16))
        self.lb_com_port_tx.setFont(font1)
        self.lb_com_port_rx = QLabel(self.centralwidget)
        self.lb_com_port_rx.setObjectName(u"lb_com_port_rx")
        self.lb_com_port_rx.setGeometry(QRect(30, 380, 71, 16))
        self.lb_com_port_rx.setFont(font1)
        self.lb_baudrate_tx = QLabel(self.centralwidget)
        self.lb_baudrate_tx.setObjectName(u"lb_baudrate_tx")
        self.lb_baudrate_tx.setGeometry(QRect(30, 160, 71, 20))
        self.lb_baudrate_tx.setFont(font1)
        self.lb_baudrate_tx_2 = QLabel(self.centralwidget)
        self.lb_baudrate_tx_2.setObjectName(u"lb_baudrate_tx_2")
        self.lb_baudrate_tx_2.setGeometry(QRect(30, 340, 71, 20))
        self.lb_baudrate_tx_2.setFont(font1)
        self.lb_baudrate_tx_3 = QLabel(self.centralwidget)
        self.lb_baudrate_tx_3.setObjectName(u"lb_baudrate_tx_3")
        self.lb_baudrate_tx_3.setGeometry(QRect(30, 280, 101, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(True)
        self.lb_baudrate_tx_3.setFont(font2)
        self.lb_setup_tx = QLabel(self.centralwidget)
        self.lb_setup_tx.setObjectName(u"lb_setup_tx")
        self.lb_setup_tx.setGeometry(QRect(30, 100, 101, 31))
        self.lb_setup_tx.setFont(font2)
        self.sb_com_port_rx = QSpinBox(self.centralwidget)
        self.sb_com_port_rx.setObjectName(u"sb_com_port_rx")
        self.sb_com_port_rx.setGeometry(QRect(150, 380, 111, 23))
        self.sb_com_port_rx.setFont(font1)
        self.sb_com_port_tx = QSpinBox(self.centralwidget)
        self.sb_com_port_tx.setObjectName(u"sb_com_port_tx")
        self.sb_com_port_tx.setGeometry(QRect(150, 200, 111, 23))
        self.sb_com_port_tx.setFont(font1)
        self.chk_use_rx = QCheckBox(self.centralwidget)
        self.chk_use_rx.setObjectName(u"chk_use_rx")
        self.chk_use_rx.setGeometry(QRect(150, 290, 101, 20))
        self.chk_use_rx.setFont(font1)
        self.chk_use_tx = QCheckBox(self.centralwidget)
        self.chk_use_tx.setObjectName(u"chk_use_tx")
        self.chk_use_tx.setGeometry(QRect(150, 110, 101, 20))
        self.chk_use_tx.setFont(font1)
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(170, 30, 35, 35))
        self.btn_save.setFont(font1)
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/icons/download_2.svg);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.led_runnig = QLabel(self.centralwidget)
        self.led_runnig.setObjectName(u"led_runnig")
        self.led_runnig.setGeometry(QRect(280, 40, 12, 12))
        self.led_runnig.setStyleSheet(u"\n"
"QLabel {\n"
"    background-color: #00ff00;\n"
"    border-radius: 6px;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"")
        self.led_stopped = QLabel(self.centralwidget)
        self.led_stopped.setObjectName(u"led_stopped")
        self.led_stopped.setGeometry(QRect(400, 40, 12, 12))
        self.led_stopped.setStyleSheet(u"\n"
"QLabel {\n"
"    background-color: #fedb00;\n"
"    border-radius: 6px;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"")
        self.led_error = QLabel(self.centralwidget)
        self.led_error.setObjectName(u"led_error")
        self.led_error.setGeometry(QRect(530, 40, 12, 12))
        self.led_error.setStyleSheet(u"\n"
"QLabel {\n"
"    background-color: #fe0000;\n"
"    border-radius: 6px;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"")
        self.lb_runnig = QLabel(self.centralwidget)
        self.lb_runnig.setObjectName(u"lb_runnig")
        self.lb_runnig.setGeometry(QRect(300, 30, 61, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.lb_runnig.setFont(font3)
        self.lb_runnig.setStyleSheet(u"color: #f0f0f0;\n"
"font-family: 'Segoe UI', sans-serif;\n"
"font-size: 12pt\n"
"")
        self.lb_stopped = QLabel(self.centralwidget)
        self.lb_stopped.setObjectName(u"lb_stopped")
        self.lb_stopped.setGeometry(QRect(420, 30, 71, 31))
        self.lb_stopped.setFont(font3)
        self.lb_stopped.setStyleSheet(u"color: #f0f0f0;\n"
"font-family: 'Segoe UI', sans-serif;\n"
"font-size: 12pt\n"
"")
        self.lb_stopped_2 = QLabel(self.centralwidget)
        self.lb_stopped_2.setObjectName(u"lb_stopped_2")
        self.lb_stopped_2.setGeometry(QRect(550, 30, 121, 31))
        self.lb_stopped_2.setFont(font3)
        self.lb_stopped_2.setStyleSheet(u"color: #f0f0f0;\n"
"font-family: 'Segoe UI', sans-serif;\n"
"font-size: 12pt\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_uart.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tab_uart.setTabText(self.tab_uart.indexOf(self.tab_tx), QCoreApplication.translate("MainWindow", u"TX", None))
        self.tab_uart.setTabText(self.tab_uart.indexOf(self.tab_rx), QCoreApplication.translate("MainWindow", u"RX", None))
        self.tab_uart.setTabText(self.tab_uart.indexOf(self.tab_tx_and_rx), QCoreApplication.translate("MainWindow", u"TX and RX", None))
        self.btn_start.setText("")
        self.btn_stop.setText("")
        self.cmb_baudrate_tx.setItemText(0, QCoreApplication.translate("MainWindow", u"4800", None))
        self.cmb_baudrate_tx.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cmb_baudrate_tx.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.cmb_baudrate_tx.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.cmb_baudrate_tx.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.cmb_baudrate_tx.setItemText(5, QCoreApplication.translate("MainWindow", u"115200", None))
        self.cmb_baudrate_tx.setItemText(6, QCoreApplication.translate("MainWindow", u"230400", None))
        self.cmb_baudrate_tx.setItemText(7, QCoreApplication.translate("MainWindow", u"460800", None))
        self.cmb_baudrate_tx.setItemText(8, QCoreApplication.translate("MainWindow", u"921600", None))

        self.cmb_baudrate_rx.setItemText(0, QCoreApplication.translate("MainWindow", u"4800", None))
        self.cmb_baudrate_rx.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.cmb_baudrate_rx.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.cmb_baudrate_rx.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.cmb_baudrate_rx.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.cmb_baudrate_rx.setItemText(5, QCoreApplication.translate("MainWindow", u"115200", None))
        self.cmb_baudrate_rx.setItemText(6, QCoreApplication.translate("MainWindow", u"230400", None))
        self.cmb_baudrate_rx.setItemText(7, QCoreApplication.translate("MainWindow", u"460800", None))
        self.cmb_baudrate_rx.setItemText(8, QCoreApplication.translate("MainWindow", u"921600", None))

        self.lb_com_port_tx.setText(QCoreApplication.translate("MainWindow", u"COM PORT", None))
        self.lb_com_port_rx.setText(QCoreApplication.translate("MainWindow", u"COM PORT", None))
        self.lb_baudrate_tx.setText(QCoreApplication.translate("MainWindow", u"BAUDRATE", None))
        self.lb_baudrate_tx_2.setText(QCoreApplication.translate("MainWindow", u"BAUDRATE", None))
        self.lb_baudrate_tx_3.setText(QCoreApplication.translate("MainWindow", u"RX SETUP", None))
        self.lb_setup_tx.setText(QCoreApplication.translate("MainWindow", u"TX SETUP", None))
        self.chk_use_rx.setText(QCoreApplication.translate("MainWindow", u"Enable RX", None))
        self.chk_use_tx.setText(QCoreApplication.translate("MainWindow", u"Enable TX", None))
        self.btn_save.setText("")
        self.led_runnig.setText("")
        self.led_stopped.setText("")
        self.led_error.setText("")
        self.lb_runnig.setText(QCoreApplication.translate("MainWindow", u"Runnig", None))
        self.lb_stopped.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.lb_stopped_2.setText(QCoreApplication.translate("MainWindow", u"COM Port Error", None))
    # retranslateUi

