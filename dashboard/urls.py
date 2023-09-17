from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.urls import path


app_name='dashboard'

urlpatterns = [
    re_path('enhance/', views.enhance, name='enhance'),
    re_path('ask/', views.ask, name='ask'),
    path('courses/<str:skill_name>/', views.courses, name='courses'),
    re_path('', views.main_board, name='dashboard'),  # Put this last
]