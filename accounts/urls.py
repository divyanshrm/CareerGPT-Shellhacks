from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static

app_name='accounts'

urlpatterns = [
    re_path('^login/',views.CustomLoginView.as_view(),name='login'),
    re_path('^logout/',auth_views.LogoutView.as_view(),name='logout'),
    re_path('^signup/',views.SignUp.as_view(),name='signup'),
]

