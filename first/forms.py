from django import forms
from django.utils.safestring import mark_safe

class SelectionForm(forms.Form):

    search = forms.CharField(required=False,
                             widget=forms.TextInput(
                                 attrs={'size': 20,
                                        'class': 'form-control',
                                        'placeholder': 'search'}))


