from django import forms

from courses.models import Course


# fmt: off
class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)
# fmt: on
