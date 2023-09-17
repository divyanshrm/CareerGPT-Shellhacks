from django import forms

class JobRoleForm(forms.Form):
    role_name = forms.CharField(label='Job Role Name', max_length=255)
    

class TextInputForm(forms.Form):
    text = forms.CharField(max_length=128)
    role_company=forms.CharField(max_length=128, required=False)


from django.core.exceptions import ValidationError

def word_limit(value):
    words = value.split()
    if len(words) > 300:
        raise ValidationError(f'The description has {len(words)} words which is more than the allowed 300 words.')

class JobDescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30}), label="Job Description",validators=[word_limit])

