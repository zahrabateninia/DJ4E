from django import forms

class UniversityForm(forms.Form):
    SUBJECT_CHOICES = (
        (1, 'Web development'),
        (2, 'Systems programming'),
        (3, 'Data analysis')
    )
    name = forms.CharField()
    age = forms.IntegerField()
    subjects = forms.ChoiceField(choices= SUBJECT_CHOICES)
    date_of_birth = forms.DateField()