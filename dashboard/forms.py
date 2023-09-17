from django import forms

class JobRoleForm(forms.Form):
    role_name = forms.CharField(label='Job Role Name', max_length=255)
    

class TextInputForm(forms.Form):
    text = forms.CharField(max_length=128)
    role_company=forms.CharField(max_length=128, required=False)