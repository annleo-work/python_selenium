# by Annleo
from model.group import Group

def test_add_sklad(app):
  app.direction.add_new_sklad(Group(num_sklad="3", name_sklad="test1"))

