from django import forms

class Result(forms.Form):
    a = forms.CharField(label='Minimum Support', max_length=200)
    b = forms.CharField(label='Minimum Confidence', max_length=200)