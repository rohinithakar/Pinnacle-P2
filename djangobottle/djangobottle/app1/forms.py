from django import forms
from models import MoocInstance

class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        cd = self.cleaned_data

        title = cd.get('title')

        if len(title) < 3:
            raise forms.ValidationError("Please Title more then two word..")

        return title

    def clean_text(self):
        cd = self.cleaned_data

        text = cd.get('text')

        if len(text) < 10:
            raise forms.ValidationError("More text Plaese..")

        return text

    def clean(self):
        cd = self.cleaned_data

        email = cd.get('email')
        title = cd.get('title')

        if email == title:
            raise forms.ValidationError("Title should not be an email")

        return cd


class MoocForm(forms.Form):
    def __init__(self, default=None, *args, **kwargs):
        super(MoocForm, self).__init__(*args, **kwargs)
        self.fields['moocs'] = forms.ChoiceField(widget = forms.Select(),
                     choices = ([(o.team_name, str(o.team_name)) for o in MoocInstance.objects.all()]), initial=default,)