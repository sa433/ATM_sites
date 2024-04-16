from django import forms

class inputfile(forms.Form):
    file = forms.FileField()