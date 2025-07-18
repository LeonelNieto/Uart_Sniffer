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
        self.tab_uart = QTabWidget(self.centralwidget)
        self.tab_uart.setObjectName(u"tab_uart")
        self.tab_uart.setGeometry(QRect(30, 10, 701, 461))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.tab_uart.setFont(font)
        self.tab_tx = QWidget()
        self.tab_tx.setObjectName(u"tab_tx")
        self.display_tx = QTextBrowser(self.tab_tx)
        self.display_tx.setObjectName(u"display_tx")
        self.display_tx.setGeometry(QRect(20, 20, 651, 391))
        self.tab_uart.addTab(self.tab_tx, "")
        self.tab_rx = QWidget()
        self.tab_rx.setObjectName(u"tab_rx")
        self.display_rx = QTextBrowser(self.tab_rx)
        self.display_rx.setObjectName(u"display_rx")
        self.display_rx.setGeometry(QRect(20, 20, 651, 391))
        self.tab_uart.addTab(self.tab_rx, "")
        self.tab_tx_and_rx = QWidget()
        self.tab_tx_and_rx.setObjectName(u"tab_tx_and_rx")
        self.display_tx_and_rx = QTextBrowser(self.tab_tx_and_rx)
        self.display_tx_and_rx.setObjectName(u"display_tx_and_rx")
        self.display_tx_and_rx.setGeometry(QRect(20, 20, 651, 391))
        self.tab_uart.addTab(self.tab_tx_and_rx, "")
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(760, 380, 51, 51))
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
        self.btn_stop.setGeometry(QRect(840, 380, 60, 55))
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
        self.cmb_baudrate_tx.setGeometry(QRect(870, 100, 111, 31))
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
        self.cmb_baudrate_rx.setGeometry(QRect(870, 270, 111, 31))
        self.cmb_baudrate_rx.setFont(font1)
        self.lb_com_port_tx = QLabel(self.centralwidget)
        self.lb_com_port_tx.setObjectName(u"lb_com_port_tx")
        self.lb_com_port_tx.setGeometry(QRect(750, 150, 71, 16))
        self.lb_com_port_tx.setFont(font1)
        self.lb_com_port_rx = QLabel(self.centralwidget)
        self.lb_com_port_rx.setObjectName(u"lb_com_port_rx")
        self.lb_com_port_rx.setGeometry(QRect(750, 320, 71, 16))
        self.lb_com_port_rx.setFont(font1)
        self.lb_baudrate_tx = QLabel(self.centralwidget)
        self.lb_baudrate_tx.setObjectName(u"lb_baudrate_tx")
        self.lb_baudrate_tx.setGeometry(QRect(750, 110, 71, 20))
        self.lb_baudrate_tx.setFont(font1)
        self.lb_baudrate_tx_2 = QLabel(self.centralwidget)
        self.lb_baudrate_tx_2.setObjectName(u"lb_baudrate_tx_2")
        self.lb_baudrate_tx_2.setGeometry(QRect(750, 280, 71, 20))
        self.lb_baudrate_tx_2.setFont(font1)
        self.lb_baudrate_tx_3 = QLabel(self.centralwidget)
        self.lb_baudrate_tx_3.setObjectName(u"lb_baudrate_tx_3")
        self.lb_baudrate_tx_3.setGeometry(QRect(750, 220, 101, 31))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(True)
        self.lb_baudrate_tx_3.setFont(font2)
        self.lb_setup_tx = QLabel(self.centralwidget)
        self.lb_setup_tx.setObjectName(u"lb_setup_tx")
        self.lb_setup_tx.setGeometry(QRect(750, 50, 101, 31))
        self.lb_setup_tx.setFont(font2)
        self.sb_com_port_rx = QSpinBox(self.centralwidget)
        self.sb_com_port_rx.setObjectName(u"sb_com_port_rx")
        self.sb_com_port_rx.setGeometry(QRect(870, 320, 111, 23))
        self.sb_com_port_rx.setFont(font1)
        self.sb_com_port_tx = QSpinBox(self.centralwidget)
        self.sb_com_port_tx.setObjectName(u"sb_com_port_tx")
        self.sb_com_port_tx.setGeometry(QRect(870, 150, 111, 23))
        self.sb_com_port_tx.setFont(font1)
        self.chk_use_rx = QCheckBox(self.centralwidget)
        self.chk_use_rx.setObjectName(u"chk_use_rx")
        self.chk_use_rx.setGeometry(QRect(870, 230, 101, 20))
        self.chk_use_rx.setFont(font1)
        self.chk_use_tx = QCheckBox(self.centralwidget)
        self.chk_use_tx.setObjectName(u"chk_use_tx")
        self.chk_use_tx.setGeometry(QRect(870, 60, 101, 20))
        self.chk_use_tx.setFont(font1)
        self.btn_stop_2 = QPushButton(self.centralwidget)
        self.btn_stop_2.setObjectName(u"btn_stop_2")
        self.btn_stop_2.setGeometry(QRect(920, 384, 61, 51))
        self.btn_stop_2.setFont(font1)
        self.btn_stop_2.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/icons/download_2.svg);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
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
        self.btn_stop_2.setText("")
    # retranslateUi

