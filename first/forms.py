from django import forms
from django.utils.safestring import mark_safe

SORT_CHOICES = (
    ('newest', 'NEWEST'),
    ('popular', 'POPULAR'),
    ('price_cheap', 'LOW PRICE'),
    ('price_expensive', 'HIGH PRICE'),
)

class SelectionForm(forms.Form):

    selection = forms.ChoiceField(required=False,
                                  choices=SORT_CHOICES,
                                  label=mark_safe("<strong>Display by</strong>&nbsp"),
                                  initial='newest',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    search = forms.CharField(required=False,
                             widget=forms.TextInput(
                                 attrs={'size': 20,
                                        'class': 'form-control',
                                        'placeholder': 'search'}))


