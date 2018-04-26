from django import forms

class SelectResponse(forms.Form):
    new_status = forms.CharField(label='New Status', max_length=1)
