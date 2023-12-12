from django import forms

class CLiente(forms.Form):
    nome = forms.CharField(max_length=20, required=False)
    idade = forms.IntegerField()