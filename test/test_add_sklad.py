# by Annleo
from model.group import Group

def test_login_empty(app):
  app.session.login(user_name="", password="")

def test_add_sklad(app):
  app.session.login(user_name="user101", password="123456")
  app.direction.add_new_sklad(Group(name_sklad="3", num_sklad="test1"))
  app.session.logout()

