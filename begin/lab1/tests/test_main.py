def test_ping_message(serial_connection):
    serial_connection.write(b'PING\n')
    response = serial_connection.readline()
    assert b'PONG' in response

def test_invalid_message(serial_connection):
    serial_connection.write(b'invalid\n')
    response = serial_connection.readline()
    assert b'ERR unknown_command' in response