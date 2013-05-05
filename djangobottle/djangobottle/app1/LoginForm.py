__author__ = 'abhi'

from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        cd = self.cleaned_data

        username = cd.get('username')

        if len(username) < 3:
            raise forms.ValidationError("Please Title more then two word..")

        return username

    def clean_password(self):
        cd = self.cleaned_data

        password = cd.get('password')

        if len(password) == 0:
            raise forms.ValidationError("Password cannot be null")

        return password

    def clean(self):
        cd = self.cleaned_data

        username = cd.get('username')
        password = cd.get('password')

        if username == password:
            raise forms.ValidationError("password should not be an username")

        return cd

