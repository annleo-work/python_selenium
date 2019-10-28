# by Annleo
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture

def test_login(app):
  app.session.login(Group(user_name="user101", password="123456"))
  app.session.logout()
def test_login_empty(app):
  app.session.login(Group(user_name="", password=""))

