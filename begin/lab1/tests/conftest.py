import pytest
import serial
from ESP32Controller import ESP32Controller

PORT = "/dev/ttyUSB0"
BAUDRATE = 115200
TIMEOUT = 1

@pytest.fixture(scope="session")
def esp32():
    try:
        with ESP32Controller(PORT,BAUDRATE,TIMEOUT) as esp32:
            yield esp32
    except serial.SerialException as e:
        pytest.fail(f"ESP32 is unavailable on {PORT}, error is {e}")