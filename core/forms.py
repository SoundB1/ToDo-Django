from django import forms

class ToDoForm(forms.Form):
    task_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)

class EditToDoForm(forms.Form):
    task_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)