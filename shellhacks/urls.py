"""shellhacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from accounts import views
from django.urls import include
from django.conf.urls.static import static
from accounts import views as acc_views
from django.views.generic.base import RedirectView

app_name='myreddit'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='accounts:login'), name='home'),
    re_path('^accounts/',include('accounts.urls',namespace='accounts')),
    re_path('^accounts/',include('django.contrib.auth.urls')),
    re_path('^test/$',views.TestPage.as_view(),name='test'),
    re_path('^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    path('resume/', include('resume.urls')),
    path('dashboard/', include('dashboard.urls',namespace='dashboard')),
    path('about/',acc_views.About.as_view(),name='about')
]
