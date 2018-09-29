from foo.target import hello

def test_hello_world():
    actual = hello()
    assert "Hello, World!" == actual
