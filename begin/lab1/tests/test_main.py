def test_device_connection(serial_connection):
    serial_connection.write(b'PING')
    response = serial_connection.readline()
    assert b'PONG' in response