def hello(name):
    return "Hello, " + name + "!"


def test_hello():
    greeting = hello('Yattom')
    # 確認
    assert greeting == 'Hello, Yattom!'
