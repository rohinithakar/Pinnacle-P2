__author__ = 'rohini'

from django import forms


class courseForm(forms.Form):
    course_title = forms.CharField()
    section = forms.CharField()
    department = forms.CharField()
    year = forms.DateField()
    instructor_name = forms.CharField()
    instructor_email = forms.EmailField()
    days = forms.CharField()
    hours = forms.CharField()
    description = forms.CharField()

    class Meta:
        fieldsets = (
            (None, {
                'fields': ('course_title', 'section', 'department', 'year'),
            }),
            ("Instructor", {
                'fields': ('instructor_name', 'instructor_email'),
            }),
            ("Details", {
                'fields': ('days', 'hours','description'),
            }),
        )

