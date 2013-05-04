__author__ = 'abhi'

from django import forms


class createUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    fname = forms.CharField()
    lname = forms.CharField()

    def clean_email(self):
        cd = self.cleaned_data

        email = cd.get('email')

        if len(email) < 3:
            raise forms.ValidationError("Please Title more then two word..")

        return email

    def clean_password(self):
        cd = self.cleaned_data

        password = cd.get('password')

        if len(password) < 5:
            raise forms.ValidationError("Password length must be at least 5")

        return password

    def clean_fname(self):
        cd = self.cleaned_data

        fname = cd.get('fname')

        if len(fname) == 0:
            raise forms.ValidationError("First name cannot be null")

        return fname

    def clean_lname(self):
        cd = self.cleaned_data

        lname = cd.get('lname')

        if len(lname) == 0:
            raise forms.ValidationError("Last name cannot be null")

        return lname

    def clean(self):
        cd = self.cleaned_data

        email = cd.get('email')
        password = cd.get('password')

        if email == password:
            raise forms.ValidationError("password should not be an email")

        return cd

