from django import forms

class ToDoForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
