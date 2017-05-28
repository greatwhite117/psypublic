from django import forms

class MoneyForm(forms.Form):
    minus = forms.IntegerField(label='minus')