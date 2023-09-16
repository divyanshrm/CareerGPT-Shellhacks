from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize the placeholders for the fields
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your desired username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your primary email address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['password1'].help_text = ''  # Remove default help text
        self.fields['password2'].help_text = ''
        
        
        for field_name, field in self.fields.items():
            # Add class for input fields
            field.widget.attrs['class'] = 'text-input-form'
            
            # Change label class. Labels don't have a class attribute by default in Django forms,
            # so we need to render them manually in the template to add a class.
            
            # For help texts, we also need to modify our template.
            # If the field has help text, we can style it by wrapping the field's help_text attribute in a span or div
            if field.help_text:
                field.help_text = f'<span class="help-text">{field.help_text}</span>'