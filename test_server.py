import server

def test_server_on_uniq():
    assert str(server.on('1')) == "{'status': 'success'}"

def test_server_off_uniq():
    assert str(server.off('1')) == "{'status': 'success'}"

def test_server_on_many():
    assert str(server.on('1,2,3')) == "{'status': 'success'}"

def test_server_off_many():
    assert str(server.off('1,2,3')) == "{'status': 'success'}"

def test_server_on_uniq_error():
    assert str(server.on('a')) == "{'status': 'error'}"

def test_server_off_uniq_error():
    assert str(server.off('a')) == "{'status': 'error'}"

def test_server_on_many_error():
    assert str(server.on('a,2,3')) == "{'status': 'error'}"

def test_server_off_many_error():
    assert str(server.off('b,2,3')) == "{'status': 'error'}"

