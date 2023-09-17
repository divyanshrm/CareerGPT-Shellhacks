from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from . import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
User=get_user_model()
class HomePage(TemplateView):
    template_name='index.html'



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Replace with the path to your custom login template

    def form_invalid(self, form):
        error_message = "Please enter a correct username and password."
        return self.render_to_response(self.get_context_data(form=form, error_message=error_message))
class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
    
    def form_valid(self, form):
        # Check if the email already exists
        email = form.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            # Add an error to the form
            form.add_error('email', 'User with this email already exists')
            return self.form_invalid(form)
        
        return super().form_valid(form)

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class About(TemplateView):
    template_name='about.html'