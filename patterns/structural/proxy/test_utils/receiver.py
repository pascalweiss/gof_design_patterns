def test_response(data):
    if data.encryped:
        return "received encrypted data"
    return "received unencrypted data"
