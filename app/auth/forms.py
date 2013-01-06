from django import forms

ROLES = [("user","user"),("admin","admin")]

class AuthorizationForm(forms.Form):
    login = forms.CharField(
        max_length=30,
        label="Enter your login",
        error_messages={"code":"login error","message":"Wrong login!"}
    )
    email = forms.EmailField(
        max_length=75,
        label="Enter your email",
        error_messages={"code":"email error","message":"Wrong email!"}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        label="Password")
    first_name = forms.CharField(
        max_length=30,
        label="Enter your first name",
        error_messages={"code":"email name","message":"Wrong name!"}
    )
    last_name = forms.CharField(
        max_length=30,
        label="Enter your last name",
        error_messages={"code":"email name","message":"Wrong name!"}
    )
    role = forms.ChoiceField(
        label="Choose your role",
        choices=ROLES
    )