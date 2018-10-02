import pytest
from pytest_bdd import scenario, given, when, then

import webapp.hello
from webapp.hello import create_app

import subprocess
import time
import os

@pytest.fixture(autouse=True, scope='session')
def webapp():
    new_env = os.environ.copy()
    new_env['FLASK_APP'] = 'webapp.hello'
    server = subprocess.Popen(['flask', 'run'], env=new_env)
    time.sleep(1)
    yield server
    server.terminate()

@scenario('hello.feature', 'Say hello')
def test_say_hello():
    pass

@when('I visit hello page')
def visit_hello_page(browser):
    browser.visit('http://localhost:5000/')

@then('I shoud see Hello World')
def see_hello_world(browser):
    assert browser.is_text_present('Hello World')

