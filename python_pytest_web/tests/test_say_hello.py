from pytest_bdd import scenario, given, when, then

@scenario('hello.feature', 'Say hello')
def test_say_hello():
    pass

@when('I visit hello page')
def visit_hello_page():
    pass

@then('I shoud see Hello World')
def see_hello_world():
    pass

