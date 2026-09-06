import pytest
import serial


@pytest.fixture(scope="session")
def serial_connection():
    device_serial = serial.Serial(port="/dev/ttyUSB0", baudrate=115200)
    yield device_serial
    device_serial.close()