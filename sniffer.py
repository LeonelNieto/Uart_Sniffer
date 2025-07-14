import serial
import threading
import time
from datetime import datetime

current_date_and_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

log_file_name = f"log_{current_date_and_time}.txt"

uart1 = serial.Serial('COM16', 921600, timeout=0.01)  # RX
uart2 = serial.Serial('COM15', 921600, timeout=0.01)  # TX

captured_data = []
lock = threading.Lock()

def read_uart(uart, label):
    while True:
        try:
            byte = uart.read(1)
            if byte:
                hex_byte = byte.hex()
                with lock:
                    byte_to_print = f"{label}:{hex_byte}"
                    print(byte_to_print)
                    captured_data.append(f"{label}:{hex_byte}\n")
        except Exception as e:
            print(f"Error en {label}: {e}")
            break

t1 = threading.Thread(target=read_uart, args=(uart1, "rx"), daemon=True)
t2 = threading.Thread(target=read_uart, args=(uart2, "tx"), daemon=True)

t1.start()
t2.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print(" ".join(captured_data))
    with open(str(f"logs\\{log_file_name}"), "a") as file:
        file.write(" ".join(captured_data))
    