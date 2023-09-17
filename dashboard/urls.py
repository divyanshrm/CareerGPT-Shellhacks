from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static

app_name='dashboard'

urlpatterns = [
    re_path('$',views.main_board,name='dashboard'),
    re_path('enhance/', views.enhance, name='enhance'),
    re_path('ask/',views.ask,name='ask'),
]
