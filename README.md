# UART Sniffer

A Python-based UART (Universal Asynchronous Receiver-Transmitter) sniffer application built with PySide6/Qt6. This tool allows you to monitor and capture serial communication data from two separate UART channels simultaneously.

## Features

- **Dual UART Monitoring**: Monitor both TX (transmit) and RX (receive) channels independently
- **Real-time Display**: Live monitoring of UART data with hexadecimal output
- **Multi-tab Interface**: 
  - Separate tabs for TX data, RX data, and combined TX/RX view
  - Clean, organized data presentation
- **Flexible Configuration**: 
  - Configurable COM ports (1-99)
  - Multiple baudrate options (4800 to 921600 bps)
  - Individual enable/disable for TX and RX channels
- **Data Logging**: Save captured data to timestamped log files
- **Threading Support**: Non-blocking UI with threaded UART reading

## Screenshots

For MAC OS
<img width="1014" height="514" alt="Image" src="https://github.com/user-attachments/assets/e5437bf6-b7b0-4a3b-ad12-fa9d3a22fe47" />

For WINDOWS
<img width="1010" height="517" alt="Image" src="https://github.com/user-attachments/assets/4e3d9778-80c2-4536-b90b-8d7e595a40ae" />

The application features a modern Qt interface with:
- Tabbed display for different data views
- Control buttons with custom SVG icons
- Real-time configuration options
- Start/Stop/Save controls

## Requirements

- Python 3.7+
- PySide6
- pyserial

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Uart_Sniffer.git
cd Uart_Sniffer
```

2. Install required dependencies:
```bash
pip install PySide6 pyserial
```

## Usage

### Running the Application

```bash
python sniffer_app.py
```

### Configuration

1. **TX Channel Setup**:
   - Check "Use TX" to enable TX monitoring
   - Select COM port number
   - Choose baudrate from dropdown

2. **RX Channel Setup**:
   - Check "Use RX" to enable RX monitoring  
   - Select COM port number
   - Choose baudrate from dropdown

3. **Start Monitoring**:
   - Click the play button to start capturing
   - Data will appear in real-time in the respective tabs

4. **Stop and Save**:
   - Click the stop button to halt monitoring
   - Click the save button to export captured data to log file

### Data Display

- **TX Tab**: Shows only transmit data
- **RX Tab**: Shows only receive data  
- **TX and RX Tab**: Shows combined data with channel labels (TX: or RX:)

All data is displayed in uppercase hexadecimal format.

### Log Files

- Logs are automatically saved to a `logs/` directory
- Filename format: `log_YYYY_MM_DD_HH_MM_SS.txt`
- Contains combined TX/RX data with channel labels

## Supported Baudrates

- 4800
- 9600
- 19200
- 38400
- 57600
- 115200
- 230400
- 460800
- 921600

## File Structure

```
Uart_Sniffer/
├── sniffer_app.py          # Main application logic
├── ui_sniffer_uart.py      # Qt UI definitions (auto-generated)
├── resources/
│   ├── __init__.py
│   └── resourcer_rc.py     # Qt resource file with icons
├── logs/                   # Generated log files (created automatically)
└── README.md
```

## Technical Details

### Architecture

- **Main Application**: `UserInterface` class inherits from `QMainWindow`
- **Signal System**: Uses Qt signals for thread-safe UI updates
- **Threading**: Separate threads for TX and RX UART reading
- **Error Handling**: Graceful handling of COM port connection errors

### Key Classes

- `UserInterface`: Main application window and logic
- `UartSignals`: Qt signal definitions for data communication
- `Ui_MainWindow`: Auto-generated UI layout (from Qt Designer)

### Threading Model

The application uses daemon threads for UART reading to prevent blocking the UI:
- One thread per active UART channel
- Thread-safe communication via Qt signals
- Proper cleanup on application exit

## Troubleshooting

### Common Issues

1. **COM Port Not Found**:
   - Verify the COM port exists and is not in use by another application
   - Check Windows Device Manager or use `mode` command to list available ports

2. **Permission Denied**:
   - Ensure the application has permission to access serial ports
   - On Linux/Mac, you may need to add your user to the dialout group

3. **No Data Appearing**:
   - Verify correct baudrate settings
   - Check that the device is actually transmitting data
   - Ensure proper wiring connections

---

**Note**: This application is designed for Windows COM ports. For Linux/Mac compatibility, modify the serial port naming convention in `configure_uart()` method.
