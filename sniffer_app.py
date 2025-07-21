from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import QMainWindow, QApplication
from ui_sniffer_uart import Ui_MainWindow
from datetime import datetime
import serial
import sys
import threading
import os

class UartSignals(QObject):
    new_data = Signal(str, str)

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("UART SNIFFER")
        self.set_initial_leds_status( )
        self.green = "#00ff00"
        self.red = "#fe0000"
        self.yellow = "#fedb00"
        self.uart_tx = None
        self.uart_rx = None
        self.com_port_tx = 1
        self.com_port_rx = 1
        self.baudrate_tx = 912600
        self.baudrate_rx = 921600
        self.com_port_tx_error = False
        self.com_port_rx_error = False
        self.captured_mix_data = []
        self.captured_tx_data = []
        self.captured_rx_data = []
        self.lock = threading.Lock()
        self.stop_event_read_tx = threading.Event()
        self.stop_event_read_rx = threading.Event()

        self.signals = UartSignals()
        self.signals.new_data.connect( self.update_display )

        self.clear_screens()
        self.btn_start.clicked.connect( self.start_loggin )
        self.btn_stop.clicked.connect( self.stop_loggin )
        self.btn_save.clicked.connect( self.save_log )

    def start_loggin(self):
        self.set_initial_leds_status()
        self.clear_screens()
        self.configure_uart()
        if not (self.com_port_tx_error or self.com_port_rx_error):
            if self.chk_use_tx.isChecked():
                self.stop_event_read_tx.clear()
                self.thread_read_tx = threading.Thread(
                    target=self.read_uart,
                    args=(self.uart_tx, "TX", self.stop_event_read_tx),
                    daemon=True
                )
                self.thread_read_tx.start()
                self.set_led_state( self.led_runnig, self.green)


            if self.chk_use_rx.isChecked():
                self.stop_event_read_rx.clear()
                self.thread_read_rx = threading.Thread(
                    target=self.read_uart,
                    args=(self.uart_rx, "RX", self.stop_event_read_rx),
                    daemon=True
                )
                self.thread_read_rx.start()
                self.set_led_state( self.led_runnig, self.green)

    def stop_loggin(self):
        self.stop_event_read_tx.set()
        self.stop_event_read_rx.set()
        self.set_initial_leds_status()
        self.set_led_state( self.led_stopped, self.yellow)
        self.uart_rx.close( )
        self.uart_tx.close( )

        if hasattr(self, 'thread_read_tx') and self.thread_read_tx.is_alive():
            self.thread_read_tx.join()

        if hasattr(self, 'thread_read_rx') and self.thread_read_rx.is_alive():
            self.thread_read_rx.join()

    def save_log( self ):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        self.current_date_and_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.log_file_name = "log_" + self.current_date_and_time + ".txt"
        with open( str( f"logs\\{self.log_file_name}" ), "a" ) as file:
            file.write( " ".join( self.captured_mix_data ) )

    def configure_uart(self):
        if self.chk_use_tx.isChecked():
            try:
                self.get_serial_config("TX")
                self.uart_tx = serial.Serial(f'COM{self.com_port_tx}', self.baudrate_tx, timeout=0.01)
                self.com_port_tx_error = False
            except Exception:
                self.com_port_tx_error = True
                self.set_initial_leds_status()
                self.set_led_state( self.led_error, self.red)
                print(f"Verifica el puerto TX: COM{self.com_port_tx}")

        if self.chk_use_rx.isChecked():
            try:
                self.get_serial_config("RX")
                self.uart_rx = serial.Serial(f'COM{self.com_port_rx}', self.baudrate_rx, timeout=0.01)
                self.com_port_rx_error = False
            except Exception:
                self.com_port_rx_error = True
                self.set_initial_leds_status()
                self.set_led_state( self.led_error, self.red)
                print(f"Verifica el puerto RX: COM{self.com_port_rx}")

    def get_serial_config(self, rx_or_tx: str):
        if rx_or_tx.upper() == "TX":
            self.com_port_tx = self.sb_com_port_tx.value()
            self.baudrate_tx = int(self.cmb_baudrate_tx.currentText())
        else:
            self.com_port_rx = self.sb_com_port_rx.value()
            self.baudrate_rx = int(self.cmb_baudrate_rx.currentText())

    def read_uart(self, uart, label, stop_event):
        while not stop_event.is_set():
            try:
                byte = uart.read(1)
                if byte:
                    hex_byte = byte.hex()
                    self.signals.new_data.emit(label, hex_byte)
            except Exception:
                break

    def update_display(self, label, hex_byte):
        text = f"{label}:{hex_byte.upper()} "
        byte_text = hex_byte.upper()

        if label.upper() == "TX":
            self.display_tx.insertPlainText( byte_text )
            self.captured_tx_data.append( byte_text )
        elif label.upper() == "RX":
            self.display_rx.insertPlainText( byte_text )
            self.captured_rx_data.append( byte_text )

        self.display_tx_and_rx.insertPlainText(text)
        self.captured_mix_data.append(text)

    def clear_screens(self):
        self.display_tx.clear()
        self.display_rx.clear()
        self.display_tx_and_rx.clear()

    def set_led_state( self, led_indicator, color ):
        led_indicator.setStyleSheet(f"background-color: {color}; border-radius: 6px;")

    def set_initial_leds_status( self ):
        self.gray_color = "#999999"
        self.set_led_state( self.led_runnig, self.gray_color )
        self.set_led_state( self.led_stopped, self.gray_color )
        self.set_led_state( self.led_error, self.gray_color )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface()
    window.show()
    sys.exit(app.exec())
