from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UniversityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('index')
        self.helper.form_method = 'GET'

    SUBJECT_CHOICES = (
        (1, 'Web development'),
        (2, 'Systems programming'),
        (3, 'Data analysis')
    )
    name = forms.CharField()
    age = forms.IntegerField()
    subjects = forms.ChoiceField(
        choices= SUBJECT_CHOICES,
        widget=forms.RadioSelect()
        )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}))
