from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trips$', views.index, name='index')
]
