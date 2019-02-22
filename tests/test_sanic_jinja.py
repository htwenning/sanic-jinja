import pytest
from sanic_jinja import generate_template
from sanic import Sanic

def test_sanic_jinja():
    app = Sanic(__name__)
    template = generate_template('tests')
    response = template('index.html', name='ben')
    assert response.body == b'user:ben'