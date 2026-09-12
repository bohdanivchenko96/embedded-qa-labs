import serial
import logging

class ESP32Controller:
    def __init__(self, port:str, baudrate:int, timeout:int, **kwargs):
        self._ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._ser and self._ser.is_open:
            self._ser.close()

    def send_command(self, cmd: str) -> str:
        logging.debug(f'Tx: {cmd}')
        self._ser.write(f'{cmd}\n'.encode('utf-8'))

        response = self._ser.readline().decode('utf-8').strip()
        logging.debug(f'Rx: {response}')

        return response