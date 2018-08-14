from app.view.LoginForm import LoginForm

class Login:

    loginForm = LoginForm()

    def get(self):
        self.loginForm.index()
