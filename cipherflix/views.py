from allauth.account.views import SignupView, LoginView


class AccountSignupView(SignupView):
    # Signup View extended

    # change template's name and path
    template_name = "users/custom_signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_signup_view = AccountSignupView.as_view()

class AccountLoginView(LoginView):
    # Signup View extended

    # change template's name and path
    template_name = "users/custom_login.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_login_view = AccountLoginView.as_view()

