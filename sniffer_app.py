from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMainWindow
from ui_sniffer_uart import Ui_MainWindow
from PySide6 import QtWidgets
from datetime import datetime
import serial
import sys
import threading

class UserInterface( QMainWindow, Ui_MainWindow ):
    def __init__( self ):
        super( ).__init__( )
        self.setupUi( self )
        self.setWindowTitle( "UART SNIFFER" )
        self.uart_tx = None
        self.uart_rx = None
        self.com_port_tx = 1
        self.com_port_rx = 1
        self.baudrate_tx = 912600
        self.baudrate_rx = 921600
        self.com_port_tx_error = False
        self.com_port_rx_error = False
        self.captured_mix_data = []
        self.captured_tx_data  = [] 
        self.captured_rx_data  = []
        self.lock = threading.Lock()
        self.stop_event_read_tx = threading.Event( )
        self.stop_event_read_rx = threading.Event( )
        self.clear_screens( )
        self.btn_start.clicked.connect( self.start_loggin )
        self.btn_stop.clicked.connect( self.stop_loggin )
    
    # def show( self ):
    #     self.show( )
    
    def start_loggin( self ):
        self.clear_screens( )
        self.current_date_and_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.configure_uart( )
        if not ( self.com_port_tx_error or self.com_port_tx_error ):
            if self.chk_use_tx.isChecked( ):
                self.thread_read_tx = threading.Thread(target=self.read_uart, args=( self.uart_tx, "TX", self.stop_event_read_tx ), daemon=True)
                self.thread_read_tx.start( )
            if self.chk_use_rx.isChecked( ):
                self.thread_read_rx = threading.Thread(target=self.read_uart, args=( self.uart_rx, "RX", self.stop_event_read_tx ), daemon=True)
                self.thread_read_rx.start( )
    
    def stop_loggin( self ):
        self.stop_event_read_tx.set( )
        self.stop_event_read_rx.set( )
        self.thread_read_tx.join( )
        self.thread_read_rx.join( )

    def configure_uart( self ):
        if self.chk_use_tx.isChecked():
            try:
                self.get_serial_config( "Tx" )
                self.uart_tx = serial.Serial(f'COM{self.com_port_tx}', self.baudrate_tx, timeout=0.01 )
                self.com_port_tx_error = False
            except Exception:
                self.com_port_tx_error = True
                print(f"Verifica el puerto TX: COM{self.com_port_tx}")

        if self.chk_use_rx.isChecked():
            try:
                self.get_serial_config( "Rx" )
                self.uart_rx = serial.Serial(f'COM{self.com_port_rx}', self.baudrate_rx, timeout=0.01 )
                self.com_port_rx_error = False
            except Exception:
                self.com_port_rx_error = True
                print(f"Verifica el puerto RX: COM{self.com_port_rx}")

    def get_serial_config( self, rx_or_tx:str ):
        if rx_or_tx.upper() == "TX":
            self.com_port_tx = self.sb_com_port_tx.value( )
            self.baudrate_tx = int( self.cmb_baudrate_tx.currentText( ) )
        else:
            self.com_port_rx = self.sb_com_port_rx.value( )
            self.baudrate_rx = int( self.cmb_baudrate_rx.currentText( ) )

    def read_uart(self, uart, label, stop_event):
        while not stop_event.is_set( ):
            try:
                byte = uart.read( 1 )
                if byte:
                    hex_byte = byte.hex( )
                    with self.lock:
                        self.hex_byte_to_print = f"{label}:{hex_byte} "
                        if label.upper( ) == "TX":
                            self.display_tx.insertPlainText( self.hex_byte_to_print )
                            self.captured_tx_data.append( self.hex_byte_to_print )
                        if label.upper( ) == "RX":
                            self.display_rx.insertPlainText( self.hex_byte_to_print )
                            self.captured_rx_data.append( self.hex_byte_to_print )

                        self.display_tx_and_rx.insertPlainText( self.hex_byte_to_print )
                        self.captured_mix_data.append( self.hex_byte_to_print )
            except Exception:
                break

    def clear_screens( self ):
        self.display_tx.clear( )
        self.display_rx.clear( )
        self.display_tx_and_rx.clear( )

app = QtWidgets.QApplication( sys.argv )
window = UserInterface( )
window.show( )
app.exec( )