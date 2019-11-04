def test_del_sklad(app):
  app.session.login(user_name="user101", password="123456")
  app.direction.del_first_sklad()
  app.session.logout()