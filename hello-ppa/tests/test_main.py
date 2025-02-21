from hello_ppa.main import greet

def test_greet():
    assert greet() == "Hello from PPA Package!"