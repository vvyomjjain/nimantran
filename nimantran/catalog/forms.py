from django import forms

class SelectResponse(forms.Form):
    new_status = forms.CharField(help_text = "enter a value")
