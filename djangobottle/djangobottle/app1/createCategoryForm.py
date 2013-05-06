__author__ = 'swetapatel'


from django import forms


class createCategoryForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    createDate = forms.CharField()
    status = forms.IntegerField()

    def clean_name(self):
        cd = self.cleaned_data

        name = cd.get('name')


        if len(name) == 0:
           raise forms.ValidationError("Name cannot be null")

        return name

    def clean_description(self):
        cd = self.cleaned_data

        description = cd.get('description')

        if len(description) == 0:
           raise forms.ValidationError("Description cannot be null")

        return description

    def clean_createDate(self):
        cd = self.cleaned_data

        createDate = cd.get('createDate')

        #if len(fname) == 0:
           # raise forms.ValidationError("First name cannot be null")

        return createDate

    def clean_status(self):
        cd = self.cleaned_data

        status = cd.get('status')

        #if len(lname) == 0:
            #raise forms.ValidationError("Last name cannot be null")

        return status



