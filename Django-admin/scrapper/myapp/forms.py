# myapp/forms.py

from django import forms

class JobSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search Jobs')
