from pytest_bdd import scenario, given, when, then

@scenario('hello.feature', 'Say hello')
def test_say_hello():
    pass

@when('I visit hello page')
def visit_hello_page(browser):
    browser.visit('http://localhost:5000/')

@then('I shoud see Hello World')
def see_hello_world(browser):
    assert browser.is_text_present('Hello World')

