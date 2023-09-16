from django import forms

class UploadResumeForm(forms.Form):
    resume_file = forms.FileField()