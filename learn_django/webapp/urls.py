from django.conf.urls import url
from . import views

urlpatterns = [
    url('^customerform$', views.customerView),
]
