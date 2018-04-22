from django import forms

class SelectResponse(forms.Form):
    new_status = forms.ChoiceField()
