from model.group import Group

def test_modify_sklad(app):
  app.session.login(user_name="user101", password="123456")
  app.direction.modify_first_sklad(Group(name_sklad="3"))
  app.session.logout()
