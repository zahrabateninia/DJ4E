from django import forms
from datetime import datetime

class UniversityForm(forms.Form):
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
