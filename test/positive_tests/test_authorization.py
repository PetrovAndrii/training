





def test_authorization(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")


"""
def test_authorization_google(app):
    app.session.login_google(username="uz.all.test@gmail.com", password="P@ssw0rd!@#")
    app.session.logout()
"""