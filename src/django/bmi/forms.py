from django import forms

class BmiFormClass(forms.Form):
    user = forms.CharField()
    age = forms.IntegerField()
    weight = forms.IntegerField()
    height = forms.IntegerField()