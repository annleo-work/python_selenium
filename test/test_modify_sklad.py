from model.group import Group

def test_modify_sklad(app):
  app.direction.modify_first_sklad(Group(name_sklad="test2"))
