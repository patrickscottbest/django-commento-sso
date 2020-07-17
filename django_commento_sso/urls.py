from django.urls import path
from django.conf.urls import url
from django_commento_sso import views

urlpatterns = [
    path('commento', views.sso, name='django_commento_sso'),
]
