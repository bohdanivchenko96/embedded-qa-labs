import pytest
import serial

PORT = "/dev/ttyUSB0"
BAUDRATE = 115200
TIMEOUT = 1

@pytest.fixture(scope="session")
def serial_connection():
    try:
        with serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT) as ser:
            yield ser
    except serial.SerialException as e:
        pytest.fail(f"ESP32 is unavailable on {PORT}, error is {e}")