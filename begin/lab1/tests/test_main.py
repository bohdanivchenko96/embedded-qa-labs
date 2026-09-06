def test_ping_message(serial_connection):
    serial_connection.write(b'PING\n')
    response = serial_connection.readline()
    assert response.strip() == b'PONG'

def test_invalid_message(serial_connection):
    serial_connection.write(b'invalid\n')
    response = serial_connection.readline()
    assert response.strip() == b'ERR unknown_command'