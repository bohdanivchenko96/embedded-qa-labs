def test_ping_message(esp32):
    response = esp32.send_command('PING')
    assert response == 'PONG'

def test_invalid_message(esp32):
    response = esp32.send_command('invalid')
    assert response == 'ERR unknown_command'

