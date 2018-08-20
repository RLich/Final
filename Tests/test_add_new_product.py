import pytest
from Config.cfg_att import Config
from application import Application
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_product(app):
    app.login(Config.username, Config.password)
    time.sleep(1)





