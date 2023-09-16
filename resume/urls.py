from django.urls import path
from . import views
app_name='resume'
urlpatterns = [
    # ... your other URLs ...
    path('upload_resume/', views.upload_resume, name='upload_resume'),
]