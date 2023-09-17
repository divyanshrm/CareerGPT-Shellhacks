from django import forms

class JobRoleForm(forms.Form):
    role_name = forms.CharField(label='Job Role Name', max_length=255)
    

