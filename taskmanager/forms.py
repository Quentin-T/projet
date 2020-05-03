from django import forms
from .models import Journal, Task


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['entry']
